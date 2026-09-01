"""Companies House (UK) — official company registry lookup.

CLI:
    python -m scripts.data.companies_house --name "Deutsche Windtechnik UK Ltd"

Python API:
    from scripts.data.companies_house import query_companies_house

Registry gate: ``companies_house``. Auth: Basic auth with API key as username.
"""

from __future__ import annotations

import argparse
import os

import requests

from scripts.data._common import (
    DEFAULT_HEADERS,
    emit_json,
    is_enabled,
    log_manifest,
)


def query_companies_house(company_name: str, slug: str | None = None) -> dict:
    if not is_enabled("companies_house") or not company_name:
        return {}
    key = os.environ["COMPANIES_HOUSE_API_KEY"]

    search_url = "https://api.company-information.service.gov.uk/search/companies"
    r = requests.get(search_url, params={"q": company_name, "items_per_page": 5},
                     auth=(key, ""), headers=DEFAULT_HEADERS, timeout=30)
    if r.status_code != 200:
        return {}
    items = r.json().get("items", []) or []
    if not items:
        return {}
    top = items[0]
    company_number = top.get("company_number", "")

    detail_r = requests.get(
        f"https://api.company-information.service.gov.uk/company/{company_number}",
        auth=(key, ""), headers=DEFAULT_HEADERS, timeout=30,
    )
    detail = detail_r.json() if detail_r.status_code == 200 else {}

    result = {
        "company_number": company_number,
        "incorporated": detail.get("date_of_creation", top.get("date_of_creation", "")),
        "sic_codes": detail.get("sic_codes", []) or [],
        "filing_status": detail.get("company_status", ""),
        "registered_address": ", ".join(filter(None, [
            (detail.get("registered_office_address") or {}).get("address_line_1", ""),
            (detail.get("registered_office_address") or {}).get("locality", ""),
            (detail.get("registered_office_address") or {}).get("postal_code", ""),
        ])),
        "source": "Companies House",
        "source_url": f"https://find-and-update.company-information.service.gov.uk/company/{company_number}",
    }
    log_manifest(slug, {"phase": "api_call", "api": "companies_house",
                        "input": company_name, "result": bool(company_number)})
    return result


def main() -> None:
    ap = argparse.ArgumentParser(description="Companies House company lookup")
    ap.add_argument("--name", required=True)
    ap.add_argument("--slug", default="")
    args = ap.parse_args()
    emit_json(query_companies_house(args.name, slug=args.slug or None))


if __name__ == "__main__":
    main()
