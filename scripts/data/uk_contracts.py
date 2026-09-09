"""UK Contracts Finder + Find-a-Tender — no-op. Authoritative switch: api-registry.yaml.

Whether this source is on is recorded in ONE place, `api-registry.yaml`
(`uk_contracts_finder.enabled`), because `_common.is_enabled()` reads it at call time.
This docstring holds the probe record instead — the detail a reviver needs, which the
registry has no business carrying.

Probe record, 2026-07-08 — every known surface ignores the keyword:

- ``GET /Published/Notices/OCDS/Search`` accepts a ``keyword`` param and silently
  ignores it; every request returns the same ~100 most-recent notices. Verified across
  ``keyword``, ``searchText``, ``text``, and unset.
- ``POST /api/Search/notices`` with ``{"searchCriteria": {"keyword": ...}}`` — the
  endpoint documented as correct — returns HTTP 404. Probed 8 variants of case,
  versioning and path prefix (``/api/Search/notices``, ``/api/search/notices``,
  ``/api/notices/search``, ``/api/1.0/…``, ``/api/rest/1.0/…``, ``/api/2.0/…``,
  ``/Published/api/Search/notices``). None exist. Either removed after the original
  card was written, or never public.
- ``find-tender.service.gov.uk/api/1.0/ocdsReleasePackages`` works but has no
  server-side text filter; client-side filtering over a full paginated catalogue is
  impractical (thousands of pages, ~2% domain match rate).

The callable is preserved so upstream code stays branch-free — do not delete the stub.
If UK Gov publishes a working keyword search, re-implement here and flip `enabled` in
the registry; callers expect the same shape as ``ted.query_ted``.
"""

from __future__ import annotations

import argparse

from scripts.data._common import emit_json, log_manifest


def query_uk_contracts(keywords: list[str], months_back: int = 24) -> list[dict]:
    log_manifest({"phase": "api_call", "api": "uk_contracts_finder",
                        "decision": "skip",
                        "reason": "endpoint_ignores_keyword_param",
                        "note": "Use TED EU + Adzuna instead."})
    return []


def main() -> None:
    ap = argparse.ArgumentParser(description="UK Contracts Finder (disabled)")
    ap.add_argument("--keywords", required=True)
    ap.add_argument("--months", type=int, default=24)
    args = ap.parse_args()
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    emit_json(query_uk_contracts(keywords, months_back=args.months))


if __name__ == "__main__":
    main()
