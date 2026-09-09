"""CORDIS — EU Horizon research projects and participating organisations.

CLI:
    python -m scripts.data.cordis --keywords "chiller efficiency,building retrofit" [--years 3]

Python API:
    from scripts.data.cordis import query_cordis

Registry gate: ``cordis``. Public keyless API.
"""

from __future__ import annotations

import argparse
from datetime import datetime

from scripts.data._common import (
    emit_json,
    http_get,
    is_enabled,
    log_manifest,
)


def query_cordis(keywords: list[str], years_back: int = 3) -> list[dict]:
    if not is_enabled("cordis") or not keywords:
        return []

    endpoint = "https://cordis.europa.eu/api/projects"
    since_year = datetime.now().year - years_back
    query = " OR ".join(keywords)
    params = {"q": query, "startYear": since_year, "pageSize": 100}
    r = http_get(endpoint, params=params, timeout=45)
    if r is None or r.status_code != 200:
        return []
    try:
        data = r.json()
    except ValueError:
        return []

    projects: list[dict] = []
    rows = data.get("projects", data if isinstance(data, list) else [])
    for p in rows:
        participants = p.get("participants") or p.get("organisations") or []
        for org in participants:
            projects.append({
                "recipient": org.get("name") if isinstance(org, dict) else str(org),
                "project": p.get("acronym") or p.get("title", ""),
                "year": p.get("startYear") or p.get("start_date", "")[:4],
                "abstract": (p.get("objective") or p.get("abstract") or "")[:800],
                "source": "CORDIS",
                "source_url": p.get("url") or f"https://cordis.europa.eu/project/id/{p.get('id', '')}",
            })
    log_manifest({"phase": "api_call", "api": "cordis",
                        "keywords": keywords, "result_count": len(projects)})
    return projects


def main() -> None:
    ap = argparse.ArgumentParser(description="CORDIS project query")
    ap.add_argument("--keywords", required=True,
                    help="Comma-separated keywords (ORed in a single call)")
    ap.add_argument("--years", type=int, default=3)
    args = ap.parse_args()
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    emit_json(query_cordis(keywords, years_back=args.years))


if __name__ == "__main__":
    main()
