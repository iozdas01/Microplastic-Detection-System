"""TED EU (Tenders Electronic Daily) — public EU procurement notices.

CLI:
    python -m scripts.data.ted --keywords "HVAC maintenance,chiller inspection" [--months 24]

Python API:
    from scripts.data.ted import query_ted
    contracts = query_ted(["HVAC maintenance"], months_back=24, slug="my-idea")

Registry gate: ``ted_eu``.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
from typing import Any

import requests

from scripts.data._common import (
    DEFAULT_HEADERS,
    emit_json,
    is_enabled,
    log_manifest,
)


def _pick_multilingual(field: Any) -> str:
    """TED text fields come as either str or `{lang: value}` — prefer 'eng'."""
    if field is None:
        return ""
    if isinstance(field, str):
        return field
    if isinstance(field, dict):
        val = field.get("eng")
        if val is None:
            val = next(iter(field.values()), None)
        if isinstance(val, list):
            return val[0] if val else ""
        return val or ""
    if isinstance(field, list):
        return field[0] if field else ""
    return str(field)


def query_ted(keywords: list[str], months_back: int = 24,
              slug: str | None = None) -> list[dict]:
    """Search TED EU notices by title keywords over the last N months."""
    if not is_enabled("ted_eu"):
        log_manifest(slug, {"phase": "api_call", "api": "ted_eu",
                            "decision": "skip", "reason": "not_enabled"})
        return []

    endpoint = "https://api.ted.europa.eu/v3/notices/search"
    since = (datetime.now(timezone.utc)
             - timedelta(days=months_back * 30)).strftime("%Y%m%d")
    query_parts = " OR ".join(f'notice-title="{k}"' for k in keywords)
    payload = {
        "query": f"({query_parts}) AND publication-date>={since}",
        "fields": [
            "publication-number", "notice-title", "publication-date",
            "organisation-name-buyer", "organisation-name-tenderer",
        ],
        "limit": 100,
        "page": 1,
    }

    contracts: list[dict] = []
    for page in range(1, 6):
        payload["page"] = page
        try:
            r = requests.post(endpoint, json=payload, headers=DEFAULT_HEADERS, timeout=60)
        except requests.RequestException as e:
            log_manifest(slug, {"phase": "api_call", "api": "ted_eu",
                                "error": str(e)})
            break
        if r is None or r.status_code != 200:
            body = ""
            try:
                body = r.text[:300] if r is not None else ""
            except Exception:
                pass
            log_manifest(slug, {"phase": "api_call", "api": "ted_eu",
                                "http_status": r.status_code if r else None,
                                "body_excerpt": body})
            break
        data = r.json()
        notices = data.get("notices", []) or []
        for notice in notices:
            title = _pick_multilingual(notice.get("notice-title"))
            buyer = _pick_multilingual(notice.get("organisation-name-buyer"))
            supplier = _pick_multilingual(notice.get("organisation-name-tenderer"))
            pub_id = notice.get("publication-number", "")
            pub_date = (notice.get("publication-date") or "")[:10]
            contracts.append({
                "title": title,
                "value": None,
                "currency": "EUR",
                "date": pub_date,
                "contracting_authority": buyer,
                "supplier": supplier,
                "cpv_codes": [],
                "country": "",
                "source": "TED EU",
                "source_url": f"https://ted.europa.eu/en/notice/-/detail/{pub_id}",
            })
        if len(notices) < payload["limit"]:
            break

    log_manifest(slug, {"phase": "api_call", "api": "ted_eu",
                        "params": {"keywords": keywords, "months_back": months_back},
                        "result_count": len(contracts)})
    return contracts


def main() -> None:
    ap = argparse.ArgumentParser(description="TED EU procurement query")
    ap.add_argument("--keywords", required=True,
                    help="Comma-separated title-search keywords")
    ap.add_argument("--months", type=int, default=24)
    ap.add_argument("--slug", default="")
    args = ap.parse_args()

    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    emit_json(query_ted(keywords, months_back=args.months,
                        slug=args.slug or None))


if __name__ == "__main__":
    main()
