"""SEC EDGAR full-text filings search — US public-company disclosures.

CLI:
    python -m scripts.data.edgar --keywords "deferred maintenance,equipment downtime" \
        [--forms 10-K,10-Q,8-K]

Python API:
    from scripts.data.edgar import query_edgar_fulltext

Registry gate: ``edgar_fulltext``. Public keyless API — but SEC asks callers
to identify themselves in the User-Agent (name + email).
"""

from __future__ import annotations

import argparse
import time
from datetime import datetime

from scripts.data._common import (
    USER_AGENT,
    cutoff_date,
    emit_json,
    http_get,
    is_enabled,
    log_manifest,
)


def query_edgar_fulltext(keywords: list[str],
                         form_types: tuple[str, ...] = ("10-K", "10-Q", "8-K")) -> list[dict]:
    if not is_enabled("edgar_fulltext") or not keywords:
        return []

    endpoint = "https://efts.sec.gov/LATEST/search-index"
    filings: list[dict] = []
    for kw in keywords:
        params = {
            "q": f'"{kw}"', "forms": ",".join(form_types),
            "dateRange": "custom",
            "startdt": cutoff_date(24),
            "enddt": datetime.now().strftime("%Y-%m-%d"),
        }
        r = http_get(endpoint, params=params,
                     headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        if r is None or r.status_code != 200:
            continue
        try:
            data = r.json()
        except ValueError:
            continue
        for hit in data.get("hits", {}).get("hits", []) or []:
            src = hit.get("_source", {}) or {}
            cik = src.get("ciks", [""])[0] if src.get("ciks") else ""
            accession = hit.get("_id", "").replace("-", "")
            filings.append({
                "filer": (src.get("display_names") or [""])[0],
                "cik": cik,
                "form_type": src.get("form", ""),
                "filing_date": src.get("file_date", ""),
                "excerpt": (hit.get("highlight", {}).get("content", [""])[0])[:500],
                "source": "SEC EDGAR",
                "source_url": f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession}",
            })
        time.sleep(0.3)
    log_manifest({"phase": "api_call", "api": "edgar_fulltext",
                        "keywords": keywords, "result_count": len(filings)})
    return filings


def main() -> None:
    ap = argparse.ArgumentParser(description="SEC EDGAR full-text query")
    ap.add_argument("--keywords", required=True,
                    help="Comma-separated exact-phrase keywords")
    ap.add_argument("--forms", default="10-K,10-Q,8-K",
                    help="Comma-separated SEC form types to search")
    args = ap.parse_args()
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    forms = tuple(f.strip() for f in args.forms.split(",") if f.strip())
    emit_json(query_edgar_fulltext(keywords, form_types=forms))


if __name__ == "__main__":
    main()
