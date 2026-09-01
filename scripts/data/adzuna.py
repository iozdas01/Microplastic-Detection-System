"""Adzuna Jobs API — company-scoped or broad keyword search.

CLI:
    python -m scripts.data.adzuna \
        --keywords "field technician,maintenance engineer" \
        --country us \
        [--company "Alliant Energy"] [--per-page 50]

Adzuna's ``what`` parameter accepts a boolean OR — the library batches every
keyword into ONE call to keep rate budget tight. Company names are normalised
(strip legal suffixes, diacritics, operational-arm sub-brands) before the
brittle substring `company` filter is applied.

Python API:
    from scripts.data.adzuna import query_adzuna, ADZUNA_SUPPORTED_COUNTRIES

Registry gate: ``adzuna``.
"""

from __future__ import annotations

import argparse
import html as _html
import os
import re
import unicodedata

from scripts.data._common import (
    LATIN_FOLD,
    LEGAL_SUFFIXES,
    emit_json,
    http_get,
    is_enabled,
    log_manifest,
)


# Countries Adzuna indexes. Calling /gb/ for a Danish or Omani company burns
# rate budget for guaranteed zeros — skip when country_hint is out of range.
ADZUNA_SUPPORTED_COUNTRIES = {
    "gb", "ie", "us", "de", "fr", "nl", "dk", "es", "it", "pl", "at",
    "au", "br", "ca", "ch", "in", "mx", "nz", "ru", "sg", "za",
}

# Operational-arm suffixes that break Adzuna's employer substring match.
# Companies index under their parent brand.
_ADZUNA_ARM_SUFFIXES = [
    "service company", "services", "power", "renouvelables", "renewables",
    "holdings inc", "holdings", "capital", "resources",
    "windkraft gmbh", "biomass liberia ab", "oman solar",
]


def normalize_for_adzuna(company: str) -> str:
    """Prepare a company name for Adzuna's brittle substring match."""
    if not company:
        return ""
    name = _html.unescape(company).translate(LATIN_FOLD)
    name = unicodedata.normalize("NFKD", name)
    name = "".join(c for c in name if not unicodedata.combining(c))
    lowered = name.lower()
    lowered = re.sub(r"[,;\.]+", " ", lowered)
    lowered = re.sub(r"\s+", " ", lowered).strip()

    tokens = lowered.split()
    while tokens and tokens[-1] in LEGAL_SUFFIXES:
        tokens.pop()
    lowered = " ".join(tokens)

    for _ in range(3):
        changed = False
        for suffix in _ADZUNA_ARM_SUFFIXES:
            if lowered == suffix:
                lowered = ""
                changed = True
            elif lowered.endswith(" " + suffix):
                lowered = lowered[: -(len(suffix) + 1)].rstrip()
                changed = True
        if not changed:
            break

    tokens = lowered.split()
    while tokens and tokens[-1] in LEGAL_SUFFIXES:
        tokens.pop()
    return " ".join(tokens).strip()


def query_adzuna(keywords: list[str], country: str,
                 company: str | None = None,
                 results_per_page: int = 50,
                 slug: str | None = None,
                 company_country_hint: str | None = None) -> list[dict]:
    """Search Adzuna jobs. If `company` is set, scoped to that employer.

    Issues ONE call per keyword phrase using plain ``what=`` and merges the
    results, deduplicating on ``redirect_url``.

    Do NOT batch keywords into ``what=(kw1) OR (kw2)``. Adzuna does not parse
    that as a boolean OR — it degrades the match badly and silently. Measured
    2026-07-27 against the live API, gb, ``commissioning engineer``:

        what=(commissioning engineer) OR (controls engineer)  ->     33 hits
        what=commissioning engineer                          ->  1,820 hits
        five keywords batched with the OR syntax             ->      0 hits

    Zero results are indistinguishable from "no hiring demand", so this bug
    produced false negative evidence rather than an error.
    """
    if not is_enabled("adzuna"):
        log_manifest(slug, {"phase": "api_call", "api": "adzuna",
                            "decision": "skip", "reason": "not_enabled"})
        return []
    if not keywords:
        return []

    country = (country or "gb").lower()
    if company_country_hint:
        hint = company_country_hint.lower()
        if hint and hint not in ADZUNA_SUPPORTED_COUNTRIES:
            log_manifest(slug, {"phase": "api_call", "api": "adzuna",
                                "company": company, "decision": "skip",
                                "reason": "adzuna_country_unsupported",
                                "country": hint})
            return []

    app_id = os.environ["ADZUNA_APP_ID"]
    app_key = os.environ["ADZUNA_APP_KEY"]
    endpoint = f"https://api.adzuna.com/v1/api/jobs/{country}/search/1"

    results: list[dict] = []
    http_failures = 0
    for keyword in keywords:
        params = {
            "app_id": app_id, "app_key": app_key,
            "results_per_page": results_per_page,
            "what": keyword,
            "content-type": "application/json",
        }
        if company:
            adzuna_company = normalize_for_adzuna(company) or company
            params["company"] = adzuna_company

        r = http_get(endpoint, params=params, timeout=30)
        if r is None or r.status_code != 200:
            http_failures += 1
            log_manifest(slug, {"phase": "api_call", "api": "adzuna",
                                "company": company, "keyword": keyword,
                                "http_status": r.status_code if r else None,
                                "result_count": 0})
            continue
        try:
            results.extend(r.json().get("results", []) or [])
        except ValueError:
            continue

    if http_failures and not results:
        return []

    postings: list[dict] = []
    seen_urls: set[str] = set()
    for job in results:
        url = job.get("redirect_url", "")
        if not url or url in seen_urls:
            continue
        seen_urls.add(url)
        postings.append({
            "title": job.get("title", ""),
            "employer": (job.get("company") or {}).get("display_name", ""),
            "location": (job.get("location") or {}).get("display_name", ""),
            "salary_min": job.get("salary_min"),
            "salary_max": job.get("salary_max"),
            "salary_currency": "GBP" if country == "gb" else job.get("salary_currency", ""),
            "description": job.get("description", ""),
            "posted_date": (job.get("created") or "")[:10],
            "source": f"Adzuna {country.upper()}",
            "source_url": url,
        })

    log_manifest(slug, {"phase": "api_call", "api": "adzuna",
                        "params": {"country": country, "company": company,
                                   "keywords": keywords,
                                   "calls": len(keywords),
                                   "http_failures": http_failures},
                        "result_count": len(postings)})
    if company and not postings:
        log_manifest(slug, {"phase": "api_call", "api": "adzuna",
                            "reason": "no_adzuna_match", "tried": company})
    return postings


def main() -> None:
    ap = argparse.ArgumentParser(description="Adzuna jobs query")
    ap.add_argument("--keywords", required=True,
                    help="Comma-separated `what` keywords (all batched into one call)")
    ap.add_argument("--country", required=True,
                    help="Adzuna country code (gb, us, de, fr, nl, dk, ie, es, it, pl, ...)")
    ap.add_argument("--company", default="",
                    help="Optional employer scope (substring match)")
    ap.add_argument("--per-page", type=int, default=50)
    ap.add_argument("--slug", default="")
    ap.add_argument("--company-country-hint", default="")
    args = ap.parse_args()

    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    emit_json(query_adzuna(
        keywords, country=args.country,
        company=args.company or None,
        results_per_page=args.per_page,
        slug=args.slug or None,
        company_country_hint=args.company_country_hint or None,
    ))


if __name__ == "__main__":
    main()
