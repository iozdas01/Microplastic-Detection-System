"""SBIR / STTR — US federal small-business grant awards.

CLI:
    python -m scripts.data.sbir --keywords "robotic inspection,sensor fusion" [--years 3]

Python API:
    from scripts.data.sbir import query_sbir

Registry gate: ``sbir``. Public keyless API.
"""

from __future__ import annotations

import argparse
import time
from datetime import datetime

from scripts.data._common import (
    emit_json,
    http_get,
    is_enabled,
    log_manifest,
)


def query_sbir(keywords: list[str], years_back: int = 3) -> list[dict]:
    if not is_enabled("sbir") or not keywords:
        return []

    endpoint = "https://api.www.sbir.gov/public/api/awards"
    since_year = datetime.now().year - years_back
    awards: list[dict] = []
    for kw in keywords:
        params = {"keyword": kw, "start": 0, "rows": 50, "year": since_year}
        r = http_get(endpoint, params=params, timeout=30)
        if r is None or r.status_code != 200:
            continue
        try:
            data = r.json()
        except ValueError:
            continue
        rows = data if isinstance(data, list) else data.get("results", [])
        for a in rows:
            awards.append({
                "recipient": a.get("firm", ""),
                "agency": a.get("agency", ""),
                "award_amount_usd": a.get("award_amount"),
                "year": a.get("award_year"),
                "abstract": (a.get("abstract") or "")[:800],
                "source": "SBIR",
                "source_url": a.get("award_link") or "https://www.sbir.gov/",
            })
        time.sleep(0.5)
    log_manifest({"phase": "api_call", "api": "sbir",
                        "keywords": keywords, "result_count": len(awards)})
    return awards


def main() -> None:
    ap = argparse.ArgumentParser(description="SBIR/STTR awards query")
    ap.add_argument("--keywords", required=True,
                    help="Comma-separated keywords (one call per keyword)")
    ap.add_argument("--years", type=int, default=3)
    args = ap.parse_args()
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    emit_json(query_sbir(keywords, years_back=args.years))


if __name__ == "__main__":
    main()
