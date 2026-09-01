"""Exa AI neural search — semantic news / article discovery (default OFF).

CLI:
    python -m scripts.data.exa --query "hospital equipment downtime 2026" [--months 6] [--results 5]

Python API:
    from scripts.data.exa import query_exa

Registry gate: ``exa_ai``. Default ``enabled: false`` — turn on only after
verifying GDELT gaps per the api-catalog checklist. Requires EXA_API_KEY.
"""

from __future__ import annotations

import argparse
import os
import urllib.parse

import requests

from scripts.data._common import (
    cutoff_date,
    emit_json,
    is_enabled,
    log_manifest,
)


def query_exa(query: str, months_back: int = 6, num_results: int = 5,
              slug: str | None = None) -> list[dict]:
    if not is_enabled("exa_ai") or not query:
        return []

    endpoint = "https://api.exa.ai/search"
    payload = {
        "query": query,
        "numResults": num_results,
        "type": "neural",
        "startPublishedDate": cutoff_date(months_back),
    }
    headers = {"x-api-key": os.environ["EXA_API_KEY"], "Content-Type": "application/json"}
    try:
        r = requests.post(endpoint, json=payload, headers=headers, timeout=30)
    except requests.RequestException:
        return []
    if r.status_code != 200:
        return []

    results = []
    for res in r.json().get("results", []) or []:
        results.append({
            "title": res.get("title", ""),
            "date": (res.get("publishedDate") or "")[:10],
            "url": res.get("url", ""),
            "domain": urllib.parse.urlparse(res.get("url", "")).netloc.lower(),
            "source": "Exa",
        })
    log_manifest(slug, {"phase": "api_call", "api": "exa_ai", "query": query,
                        "result_count": len(results)})
    return results


def main() -> None:
    ap = argparse.ArgumentParser(description="Exa AI neural search")
    ap.add_argument("--query", required=True)
    ap.add_argument("--months", type=int, default=6)
    ap.add_argument("--results", type=int, default=5)
    ap.add_argument("--slug", default="")
    args = ap.parse_args()
    emit_json(query_exa(args.query, months_back=args.months,
                        num_results=args.results, slug=args.slug or None))


if __name__ == "__main__":
    main()
