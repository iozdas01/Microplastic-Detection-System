"""GLEIF (LEI) — resolve a company name to its Legal Entity Identifier + parent.

CLI:
    python -m scripts.data.gleif --name "Mærsk A/S" [--country-hint DK]

Python API:
    from scripts.data.gleif import resolve_gleif
    lei_data = resolve_gleif("Mærsk A/S")

Registry gate: ``gleif``.
"""

from __future__ import annotations

import argparse

from scripts.data._common import (
    emit_json,
    http_get,
    is_enabled,
    log_manifest,
    normalize_name,
)


def _score(record: dict, input_name: str) -> float:
    entity = record.get("attributes", {}).get("entity", {}) or {}
    legal_name = entity.get("legalName", {}).get("name", "")
    n1 = normalize_name(legal_name)
    n2 = normalize_name(input_name)
    if not n1 or not n2:
        return 0.0
    if n1 == n2:
        return 1.0
    overlap = len(set(n1.split()) & set(n2.split()))
    return overlap / max(len(n2.split()), 1) * 0.85


def resolve_gleif(company_name: str, country_hint: str | None = None) -> dict:
    """Return `{lei, name, country, parent_lei, parent_name, match_score, ...}`.

    Returns empty dict on no match or low confidence (score < 0.4).
    """
    if not is_enabled("gleif") or not company_name:
        return {}

    endpoint = "https://api.gleif.org/api/v1/lei-records"
    params = {"filter[fulltext]": company_name, "page[size]": 5}
    r = http_get(endpoint, params=params,
                 headers={"Accept": "application/vnd.api+json"})
    if r is None or r.status_code != 200:
        return {}
    try:
        data = r.json()
    except ValueError:
        return {}

    records = data.get("data") or []
    if not records:
        log_manifest({"phase": "gleif_resolve", "input": company_name,
                            "output_lei": None, "reason": "no_match"})
        return {}

    ranked = sorted(records, key=lambda r: _score(r, company_name), reverse=True)
    best = ranked[0]
    best_score = _score(best, company_name)

    if best_score < 0.4:
        log_manifest({"phase": "gleif_resolve", "input": company_name,
                            "output_lei": None,
                            "reason": f"low_confidence({best_score:.2f})"})
        return {}

    attrs = best.get("attributes", {}) or {}
    entity = attrs.get("entity", {}) or {}
    lei = attrs.get("lei", "")

    parent_lei = ""
    parent_name = ""
    rels = best.get("relationships", {}) or {}
    direct_parent = rels.get("direct-parent", {}).get("links", {}).get("related")
    if direct_parent:
        pr = http_get(direct_parent,
                      headers={"Accept": "application/vnd.api+json"})
        if pr is not None and pr.status_code == 200:
            try:
                pdata = pr.json().get("data") or {}
                parent_lei = pdata.get("attributes", {}).get("lei", "") or ""
                parent_name = (pdata.get("attributes", {})
                                    .get("entity", {})
                                    .get("legalName", {})
                                    .get("name", "")) or ""
            except ValueError:
                pass

    result = {
        "lei": lei,
        "name": entity.get("legalName", {}).get("name", ""),
        "country": entity.get("legalAddress", {}).get("country", ""),
        "parent_lei": parent_lei,
        "parent_name": parent_name,
        "match_score": round(best_score, 2),
        "source": "GLEIF",
        "source_url": f"https://api.gleif.org/api/v1/lei-records/{lei}",
    }
    log_manifest({"phase": "gleif_resolve", "input": company_name,
                        "output_lei": lei, "confidence": result["match_score"]})
    return result


def main() -> None:
    ap = argparse.ArgumentParser(description="GLEIF LEI resolver")
    ap.add_argument("--name", required=True)
    ap.add_argument("--country-hint", default="")
    args = ap.parse_args()
    emit_json(resolve_gleif(args.name,
                            country_hint=args.country_hint or None))


if __name__ == "__main__":
    main()
