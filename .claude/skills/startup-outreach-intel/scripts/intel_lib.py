"""intel_lib.py — Outreach intel orchestrator.

Query functions live in :mod:`scripts.data` and are re-exported here for
backward compatibility. This module owns the higher-level pipeline:

    * canonical entity resolution via GLEIF (:func:`dedup_and_resolve`)
    * tier inference from role appearances (:func:`infer_tier`)
    * pain-score aggregation (:func:`score_company`)
    * :func:`phase_discover` / :func:`phase_enrich` / CLI entrypoint

Usage as library:
    from intel_lib import query_ted, resolve_gleif, score_company

Usage as CLI:
    python3 intel_lib.py run     --slug <slug> --assumption A2
    python3 intel_lib.py discover --slug <slug> --assumption A2
    python3 intel_lib.py enrich  --slug <slug> --assumption A2
    python3 intel_lib.py score   --slug <slug> --assumption A2
    python3 intel_lib.py status  --slug <slug> --assumption A2

    Flags:
        --refresh   Ignore cache; force re-fetch of every company/assumption block.
        --skip <api_key,api_key,...>   Skip named APIs for this run.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import yaml


# ---------------------------------------------------------------------------
# Path bootstrap — allow this file to import from scripts/data/ regardless of
# CWD (tests, subagents, and the outreach-intel skill all invoke it directly).
# ---------------------------------------------------------------------------

_REPO_ROOT_BOOTSTRAP = Path(__file__).resolve().parents[4]
if str(_REPO_ROOT_BOOTSTRAP) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT_BOOTSTRAP))


# ---------------------------------------------------------------------------
# Re-exports from the shared data-access layer
# ---------------------------------------------------------------------------

from scripts.data._common import (  # noqa: E402
    CURRENCY_TO_GBP,
    DEFAULT_HEADERS,
    IN_LIQUIDATION_PATTERNS,
    LATIN_FOLD,
    LEGAL_SUFFIXES,
    NEWS_DOMAIN_ALLOWLIST,
    NON_OPERATOR_PATTERNS,
    REPO_ROOT,
    USER_AGENT,
    clean_edgar_name,
    cutoff_date,
    http_get,
    is_enabled,
    is_name_out_of_scope,
    load_registry,
    log_manifest,
    manifest_path,
    normalize_name,
    to_gbp,
)
from scripts.data.adzuna import (  # noqa: E402
    ADZUNA_SUPPORTED_COUNTRIES,
    normalize_for_adzuna,
    query_adzuna,
)
from scripts.data.companies_house import query_companies_house  # noqa: E402
from scripts.data.cordis import query_cordis  # noqa: E402
from scripts.data.edgar import query_edgar_fulltext  # noqa: E402
from scripts.data.exa import query_exa  # noqa: E402
from scripts.data.gdelt import query_news as query_gdelt  # noqa: E402
from scripts.data.gleif import resolve_gleif  # noqa: E402
from scripts.data.sbir import query_sbir  # noqa: E402
from scripts.data.ted import query_ted  # noqa: E402
from scripts.data.uk_contracts import query_uk_contracts  # noqa: E402


# Backward-compat aliases — legacy underscore-prefixed helper names.
_normalize_for_adzuna = normalize_for_adzuna
_LATIN_FOLD = LATIN_FOLD


# ---------------------------------------------------------------------------
# Dedup + canonical entity resolution
# ---------------------------------------------------------------------------


@dataclass
class CanonicalCompany:
    display_name: str
    canonical_name: str
    also_known_as: list[str] = field(default_factory=list)
    lei: str = ""
    parent_entity: str = ""
    parent_lei: str = ""
    country: str = ""
    role_appearances: list[tuple[str, str, str]] = field(default_factory=list)
    # (source_api, role_in_source, source_url)

    def to_dict(self) -> dict:
        return {
            "company": self.display_name,
            "canonical_name": self.canonical_name,
            "also_known_as": sorted(set(self.also_known_as)),
            "lei": self.lei,
            "parent_entity": self.parent_entity,
            "parent_lei": self.parent_lei,
            "country": self.country,
            "role_appearances": self.role_appearances,
        }


def dedup_and_resolve(raw_names: list[tuple[str, str, str]],
                      slug: str | None = None) -> dict[str, CanonicalCompany]:
    """
    Input: list of (name, source_api, role_in_source, source_url) tuples from
    every discovery API. This shape ties each name back to how it was found so
    tier assignment can see the context.

    Output: dict keyed by canonical_name → CanonicalCompany with GLEIF
    resolution applied and subsidiaries collapsed onto parents.
    """
    # Group by fuzzy-normalized name
    groups: dict[str, list[tuple[str, str, str, str]]] = {}
    for name, api, role, url in raw_names:
        key = normalize_name(name)
        if not key:
            continue
        groups.setdefault(key, []).append((name, api, role, url))

    canonicals: dict[str, CanonicalCompany] = {}
    for canon_key, occurrences in groups.items():
        display = occurrences[0][0]  # first-seen spelling
        aliases = list({o[0] for o in occurrences if o[0] != display})

        # GLEIF resolve
        gleif = resolve_gleif(display, slug=slug) if is_enabled("gleif") else {}
        canonical_name = gleif.get("name") or display
        canon_key_final = normalize_name(canonical_name)

        # If a canonical bucket already exists (from a different name that
        # resolved to the same LEI), merge instead of creating a new bucket
        target: CanonicalCompany | None = None
        if gleif.get("lei"):
            for existing in canonicals.values():
                if existing.lei and existing.lei == gleif["lei"]:
                    target = existing
                    break

        if target is None:
            target = CanonicalCompany(
                display_name=canonical_name,
                canonical_name=canon_key_final,
                also_known_as=aliases,
                lei=gleif.get("lei", ""),
                parent_entity=gleif.get("parent_name", ""),
                parent_lei=gleif.get("parent_lei", ""),
                country=gleif.get("country", ""),
            )
            canonicals[canon_key_final] = target
        else:
            for alias in aliases:
                if alias not in target.also_known_as and alias != target.display_name:
                    target.also_known_as.append(alias)

        for _, api, role, url in occurrences:
            target.role_appearances.append((api, role, url))

    # Collapse subsidiaries onto their parents where the parent is also in the set
    for name, cc in list(canonicals.items()):
        if cc.parent_lei:
            for other in canonicals.values():
                if other.lei == cc.parent_lei and other is not cc:
                    other.also_known_as.append(cc.display_name)
                    other.role_appearances.extend(cc.role_appearances)
                    canonicals.pop(name, None)
                    break

    if slug:
        log_manifest(slug, {"phase": "dedup", "input_names": len(raw_names),
                            "canonical_companies": len(canonicals)})
    return canonicals


# ---------------------------------------------------------------------------
# Tier inference
# ---------------------------------------------------------------------------


ROLE_TO_TIER_BUCKET = {
    # (source_api, role_in_source) → generic bucket
    ("ted_eu", "contracting_authority"): "demand",
    ("ted_eu", "supplier"): "supply",
    ("uk_contracts_finder", "contracting_authority"): "demand",
    ("uk_contracts_finder", "supplier"): "supply",
    ("edgar_fulltext", "filer"): "demand",  # requires excerpt review — see tier-inference.md
    ("sbir", "grant_recipient"): "supply",
    ("cordis", "grant_recipient"): "supply",
    ("adzuna", "employer"): "demand",  # employer hiring for target roles = demand-side by default
}


# Structural sides — the ONLY domain-neutral tier axis. Tier NAMES are always
# idea-defined (declared per assumption); no tier name is ever hardcoded below.
DEMAND, SUPPLY = "demand", "supply"


def normalize_icp_tiers(icp_valid) -> tuple[list[str], dict[str, str]]:
    """
    Normalize an assumption's `icp_valid_tiers` into (ordered names, {name: side}).

    Accepts either shape:
      - side-tagged (current): [{name: <idea-defined>, side: demand}, ...]
      - flat legacy: [<name>, <name>, ...]  — side left unset gets a conservative
        best-effort from generic English hints (specialist/vendor/service → supply),
        else demand. This shim only covers untagged legacy data; the primary path
        is the founder-declared side.
    Declaration order is preserved and used as the per-side priority.
    """
    names: list[str] = []
    side_of: dict[str, str] = {}
    for entry in icp_valid or []:
        if isinstance(entry, dict):
            name, side = entry.get("name"), entry.get("side")
        else:
            name, side = entry, None
        if not name:
            continue
        if not side:
            low = str(name).lower()
            supply_hints = ("specialist", "vendor", "isp", "service",
                            "supplier", "partner", "reseller", "distributor")
            side = SUPPLY if any(h in low for h in supply_hints) else DEMAND
        names.append(name)
        side_of[name] = side
    return names, side_of


# Vertical-specific adapters an assumption may opt into by name. Empty by design:
# a source belongs here only once an idea's market actually needs it, and adding
# one means an entry in api-registry.yaml plus a card in api-catalog.md.
DOMAIN_ADAPTERS: dict[str, str] = {}


def enabled_domain_sources(assumption: dict, slug: str | None = None) -> set[str]:
    """
    Domain-specific data sources the idea has opted into (default: none).

    Decoupled from tier names entirely: an idea whose market one covers names it
    in `domain_data_sources` on the assumption; every other idea leaves it empty
    and no vertical source fires. A name with no registered adapter is logged
    rather than ignored — silently doing nothing is how an opt-in gate rots.
    """
    declared = set(assumption.get("domain_data_sources", []) or [])
    unregistered = declared - set(DOMAIN_ADAPTERS)
    if unregistered:
        log_manifest(slug, {"phase": "domain_source_unregistered",
                            "declared": sorted(unregistered),
                            "reason": "named in domain_data_sources but no adapter "
                                      "is registered in DOMAIN_ADAPTERS"})
    return declared & set(DOMAIN_ADAPTERS)


def infer_tier(role_appearances: list[tuple[str, str, str]],
               icp_valid_tiers) -> tuple[str, list[str]]:
    """
    Given a company's role appearances across APIs and the assumption's
    icp_valid_tiers whitelist, return (primary_tier, [also_seen_as tiers]).

    Routing is on structural SIDE only (demand/supply, via ROLE_TO_TIER_BUCKET);
    the concrete tier name comes from the assumption's own declaration. The
    first tier the founder listed on each side is that side's default.
    """
    names, side_of = normalize_icp_tiers(icp_valid_tiers)
    demand_tier = next((n for n in names if side_of.get(n) == DEMAND), None)
    supply_tier = next((n for n in names if side_of.get(n) == SUPPLY), None)

    buckets_seen: list[str] = []
    for api, role, _url in role_appearances:
        bucket = ROLE_TO_TIER_BUCKET.get((api, role))
        if bucket:
            buckets_seen.append(bucket)

    if not buckets_seen:
        # Fallback: if the only appearance is Adzuna without a role hint,
        # keep company but mark tier as unknown for founder review.
        return ("other", [])

    demand_count = buckets_seen.count("demand")
    supply_count = buckets_seen.count("supply")

    primary_bucket = "demand" if demand_count >= supply_count else "supply"

    primary = (demand_tier if primary_bucket == "demand" else supply_tier) or "other"
    alt = (supply_tier if primary_bucket == "demand" else demand_tier)
    also = [alt] if alt and (demand_count > 0 and supply_count > 0) else []

    if primary not in names:
        # Company appeared in an off-scope role for this assumption.
        return ("other", also)
    return (primary, [t for t in also if t in names])


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------


def score_contract(contracts: list[dict]) -> int:
    """
    Score 0-3 based on the company's contracts under this assumption, weighted
    by recency + monetary value + count.

    IMPORTANT: many TED / UK CF contracts publish with `value: null` (framework
    agreements have no fixed value, or values are in currencies we don't have
    conversion for). The value-based tiers must NOT gate the count-based
    fallback — a company with 13 framework contracts is clearly a pattern buyer
    even when total_weighted_value == 0.
    """
    total_weighted = 0.0
    count = 0
    now = datetime.now(timezone.utc).date()
    for c in contracts or []:
        try:
            d = datetime.strptime((c.get("date") or "")[:10], "%Y-%m-%d").date()
        except ValueError:
            continue
        months_ago = (now - d).days / 30
        weight = 1.0 if months_ago <= 12 else (0.5 if months_ago <= 24 else 0.0)
        if weight == 0.0:
            continue
        total_weighted += to_gbp(c.get("value"), c.get("currency", "GBP")) * weight
        count += 1

    # Value-based tiers (when TED/UK CF actually publishes monetary values)
    if total_weighted >= 5_000_000:
        return 3
    if total_weighted >= 1_000_000:
        return 2

    # Count-based fallback — fires INDEPENDENTLY of value data.
    if count >= 5:
        return 3
    if count >= 3:
        return 2
    if count >= 1:
        return 1
    return 0


def score_hiring(hiring: dict | None) -> int:
    if not hiring:
        return 0
    n = hiring.get("postings_count", 0) or 0
    if n >= 5:
        return 2
    if n >= 2:
        return 1
    if n >= 1:
        return 1
    return 0


def score_news(news: list[dict] | None, keywords: list[str] | None = None) -> int:
    """
    Score 0-1 for news_score. Only counts articles whose TITLE matches at least
    one of the assumption's pain keywords — bare "company mentioned in press"
    is not signal.
    """
    if not news:
        return 0
    if not keywords:
        return 1  # fallback for callers that don't pass keywords
    kw_lower = [k.lower() for k in keywords]
    for article in news:
        title = (article.get("title") or "").lower()
        if any(kw in title for kw in kw_lower):
            return 1
    return 0


def score_company(assumption_block: dict,
                  keywords: list[str] | None = None) -> tuple[int, dict]:
    """
    Compute pain_score components + total. Pass `keywords` (the assumption's
    pain vocabulary) so news_score can filter articles by topical relevance.
    """
    components = {
        "contract_score": score_contract(assumption_block.get("contracts") or []),
        "hiring_score": score_hiring(assumption_block.get("hiring")),
        "news_score": score_news(assumption_block.get("news"), keywords=keywords),
    }
    raw = sum(components.values())
    final = max(1, min(10, raw))
    return final, components


# ---------------------------------------------------------------------------
# File I/O — companies.md, company-intel.md
# ---------------------------------------------------------------------------


def _paths(slug: str) -> tuple[Path, Path, Path]:
    base = REPO_ROOT / "reports" / slug / "outreach"
    return (base / "companies.md",
            base / "company-intel.md",
            base / ".competitors-detected.md")


def _assumption_path(slug: str) -> Path:
    return REPO_ROOT / "reports" / slug / "02-assumptions" / "graph.md"


def read_assumption(slug: str, assumption_id: str) -> dict:
    """
    Extract a specific assumption block from graph.md. Supports two schemas:
      1. Flat YAML doc (current standard) — whole file parses as YAML with
         an `assumptions:` list of dicts keyed by `id`.
      2. Markdown-sectioned (legacy) — `## A{X}` heading with a ```yaml fenced
         block underneath.
    """
    p = _assumption_path(slug)
    if not p.exists():
        raise FileNotFoundError(f"graph.md not found at {p}")

    content = p.read_text(encoding="utf-8")

    try:
        doc = yaml.safe_load(content) or {}
    except yaml.YAMLError:
        doc = None
    if isinstance(doc, dict) and isinstance(doc.get("assumptions"), list):
        for item in doc["assumptions"]:
            if isinstance(item, dict) and item.get("id") == assumption_id:
                return item
        raise ValueError(f"Assumption {assumption_id} not found in {p}")

    heading_pattern = re.compile(rf"^##\s*{re.escape(assumption_id)}\b", re.M)
    m = heading_pattern.search(content)
    if not m:
        raise ValueError(f"Assumption {assumption_id} not found in {p}")

    remainder = content[m.end():]
    next_heading = re.search(r"^##\s+\w", remainder, re.M)
    section = remainder[:next_heading.start()] if next_heading else remainder

    yaml_block = re.search(r"```yaml\s*(.*?)\s*```", section, re.S)
    if not yaml_block:
        raise ValueError(f"No YAML block found under {assumption_id}")
    try:
        data = yaml.safe_load(yaml_block.group(1)) or {}
    except yaml.YAMLError as e:
        raise ValueError(f"YAML parse error for {assumption_id}: {e}")
    data["id"] = assumption_id
    return data


def read_intel_md(slug: str) -> dict[str, dict]:
    """Parse company-intel.md into a dict {canonical_name: block}."""
    _, intel_path, _ = _paths(slug)
    if not intel_path.exists():
        return {}

    text = intel_path.read_text(encoding="utf-8")
    sections = re.split(r"^##\s+", text, flags=re.M)[1:]
    out: dict[str, dict] = {}
    for sec in sections:
        header, _, body = sec.partition("\n")
        name = header.strip()
        if name.lower().startswith("run summary"):
            continue
        try:
            data = yaml.safe_load(body) or {}
        except yaml.YAMLError:
            continue
        if isinstance(data, dict):
            out[normalize_name(name)] = {"display_name": name, "block": data}
    return out


# ---------------------------------------------------------------------------
# Phase orchestrators — high level
# ---------------------------------------------------------------------------


def _derive_keywords(assumption: dict) -> list[str]:
    """Light heuristic keyword extraction. Claude usually passes explicit keywords."""
    text_parts = [assumption.get("assumption", ""),
                  assumption.get("disconfirmation", ""),
                  assumption.get("icp_segment", "")]
    text = " ".join(text_parts).lower()
    tokens = re.findall(r"[a-z][a-z\-]{3,}", text)
    unique = []
    for t in tokens:
        if t not in unique and t not in {
            "the", "and", "that", "with", "from", "into", "over", "under",
            "have", "been", "this", "these", "their", "them", "which",
            "would", "could", "should", "will", "when", "where", "what",
            "there", "than", "then", "primary", "assumption",
        }:
            unique.append(t)
    return unique[:6]


def phase_discover(slug: str, assumption_id: str, keywords: list[str] | None = None,
                   skip: set[str] | None = None) -> dict[str, CanonicalCompany]:
    """Phase 1 — API discovery + tier assignment. Writes draft rows to companies.md."""
    assumption = read_assumption(slug, assumption_id)
    icp_valid = assumption.get("icp_valid_tiers", []) or []
    icp_names, _icp_side = normalize_icp_tiers(icp_valid)
    enabled_domain_sources(assumption, slug)   # gate: warns on unregistered opt-ins
    category = assumption.get("category", "")
    if not keywords:
        keywords = _derive_keywords(assumption)

    skip = skip or set()
    log_manifest(slug, {"phase": "start", "assumption": assumption_id,
                        "keywords": keywords, "icp_valid_tiers": icp_valid})

    raw: list[tuple[str, str, str, str]] = []
    filtered_out: list[tuple[str, str]] = []

    def add(name: str, api: str, role: str, url: str) -> None:
        if not name:
            return
        if is_name_out_of_scope(name):
            filtered_out.append((name, api))
            return
        raw.append((name, api, role, url))

    phase1_ted: list[dict] = []
    phase1_ukcf: list[dict] = []

    if "ted_eu" not in skip:
        phase1_ted = query_ted(keywords, months_back=24, slug=slug)
        for c in phase1_ted:
            add(c["contracting_authority"], "ted_eu", "contracting_authority", c["source_url"])
            add(c["supplier"], "ted_eu", "supplier", c["source_url"])

    if "uk_contracts_finder" not in skip:
        phase1_ukcf = query_uk_contracts(keywords, months_back=24, slug=slug)
        for c in phase1_ukcf:
            add(c["contracting_authority"], "uk_contracts_finder", "contracting_authority", c["source_url"])
            add(c["supplier"], "uk_contracts_finder", "supplier", c["source_url"])

    # Adzuna in Phase 1 is skipped by default — used for per-company enrichment
    # in Phase 2 instead. See SKILL.md.
    log_manifest(slug, {"phase": "api_decision", "api": "adzuna",
                        "decision": "defer_to_enrichment",
                        "reason": "budget_conservation__personalization_priority"})

    if category in {"timing", "technical", "competitive"}:
        if "sbir" not in skip:
            for a in query_sbir(keywords, years_back=3, slug=slug):
                _append_competitor(slug, a, assumption_id)
        if "cordis" not in skip:
            for a in query_cordis(keywords, years_back=3, slug=slug):
                _append_competitor(slug, a, assumption_id)

    if "edgar_fulltext" not in skip and category in {"pain", "market", "buyer"}:
        for f in query_edgar_fulltext(keywords, slug=slug):
            cleaned, _cik = clean_edgar_name(f["filer"])
            add(cleaned, "edgar_fulltext", "filer", f["source_url"])

    if filtered_out:
        log_manifest(slug, {"phase": "name_filter",
                            "dropped_count": len(filtered_out),
                            "sample": filtered_out[:20]})

    canonicals = dedup_and_resolve(raw, slug=slug)

    # Second-pass name filter — GLEIF sometimes maps a short brand ("Aviva")
    # to a random subsidiary ("Aviva Investors Multi-Asset Plus Fund").
    post_gleif_drops: list[str] = []
    for key in list(canonicals.keys()):
        cc = canonicals[key]
        if is_name_out_of_scope(cc.display_name):
            post_gleif_drops.append(cc.display_name)
            del canonicals[key]
    if post_gleif_drops:
        log_manifest(slug, {"phase": "post_gleif_name_filter",
                            "dropped_count": len(post_gleif_drops),
                            "sample": post_gleif_drops[:20]})

    # Second-signal tier gate — single weak signals get demoted to "other".
    STRONG_SOURCES = {"ted_eu", "uk_contracts_finder"}
    filtered: dict[str, CanonicalCompany] = {}
    tier_downgrades: list[tuple[str, str, str]] = []
    for key, cc in canonicals.items():
        tier, alt = infer_tier(cc.role_appearances, icp_valid)

        sources = {api for (api, _role, _url) in cc.role_appearances}
        has_strong = bool(sources & STRONG_SOURCES)
        n_appearances = len(cc.role_appearances)
        if tier != "other" and not has_strong and n_appearances < 2:
            tier_downgrades.append((cc.display_name, tier, "single_weak_signal"))
            tier = "other"

        if tier == "other" and "other" not in icp_names:
            log_manifest(slug, {"phase": "tier_drop", "company": cc.display_name,
                                "reason": "off_scope"})
            continue
        cc.tier = tier            # type: ignore[attr-defined]
        cc.also_seen_as = alt     # type: ignore[attr-defined]
        filtered[key] = cc

    if tier_downgrades:
        log_manifest(slug, {"phase": "tier_second_signal_rule",
                            "downgraded_count": len(tier_downgrades),
                            "sample": tier_downgrades[:15]})

    _write_companies_md(slug, assumption_id, filtered)

    _write_phase1_cache(slug, assumption_id,
                        ted_hits=phase1_ted, ukcf_hits=phase1_ukcf)

    log_manifest(slug, {"phase": "discover_end", "assumption": assumption_id,
                        "companies_discovered": len(filtered)})
    return filtered


def _phase1_cache_path(slug: str, assumption_id: str) -> Path:
    return REPO_ROOT / "reports" / slug / "outreach" / f".phase1-contracts-{assumption_id}.json"


def _write_phase1_cache(slug: str, assumption_id: str,
                        ted_hits: list[dict], ukcf_hits: list[dict]) -> None:
    """Persist Phase 1's raw procurement hits so Phase 2 can reuse them."""
    path = _phase1_cache_path(slug, assumption_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"ted_eu": ted_hits, "uk_contracts_finder": ukcf_hits,
               "run_date": datetime.now().strftime("%Y-%m-%d")}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)


def _read_phase1_cache(slug: str, assumption_id: str) -> dict:
    """Load Phase 1 procurement hits; returns empty payload if cache missing."""
    path = _phase1_cache_path(slug, assumption_id)
    if not path.exists():
        return {"ted_eu": [], "uk_contracts_finder": [], "run_date": ""}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (ValueError, OSError):
        return {"ted_eu": [], "uk_contracts_finder": [], "run_date": ""}


def _phase1_contracts_for_company(canon_key: str, phase1: dict) -> list[dict]:
    """Filter Phase 1's raw TED/UK CF hits down to a single company's contracts."""
    out: list[dict] = []
    for c in phase1.get("ted_eu", []) or []:
        ca = normalize_name(c.get("contracting_authority", ""))
        su = normalize_name(c.get("supplier", ""))
        if ca == canon_key or su == canon_key:
            role = "contracting_authority" if ca == canon_key else "supplier"
            counter = c.get("supplier") if role == "contracting_authority" else c.get("contracting_authority")
            out.append({
                "title": c.get("title"), "value": c.get("value"),
                "currency": c.get("currency", "EUR"), "date": c.get("date"),
                "role": role, "counterparty": counter or "",
                "cpv_codes": c.get("cpv_codes") or [],
                "source": c.get("source", "TED EU"),
                "source_url": c.get("source_url"),
            })
    for c in phase1.get("uk_contracts_finder", []) or []:
        ca = normalize_name(c.get("contracting_authority", ""))
        su = normalize_name(c.get("supplier", ""))
        if ca == canon_key or su == canon_key:
            role = "contracting_authority" if ca == canon_key else "supplier"
            counter = c.get("supplier") if role == "contracting_authority" else c.get("contracting_authority")
            out.append({
                "title": c.get("title"), "value": c.get("value"),
                "currency": c.get("currency", "GBP"), "date": c.get("date"),
                "role": role, "counterparty": counter or "",
                "cpv_codes": c.get("cpv_codes") or [],
                "source": c.get("source", "UK Contracts Finder"),
                "source_url": c.get("source_url"),
            })
    out.sort(key=lambda x: (x.get("date") or ""), reverse=True)
    return out


def _append_competitor(slug: str, entry: dict, assumption_id: str) -> None:
    _, _, comp_path = _paths(slug)
    comp_path.parent.mkdir(parents=True, exist_ok=True)
    block = (f"\n## {entry.get('recipient', 'Unknown')}\n\n"
             f"detected_role: grant_recipient\n"
             f"detected_in: {entry.get('source', '')}\n"
             f"amount: {entry.get('award_amount_usd', '')}\n"
             f"year: {entry.get('year', '')}\n"
             f"assumption_scanned: {assumption_id}\n"
             f"abstract_excerpt: >\n  {(entry.get('abstract') or '')[:400]}\n"
             f"tier_would_be: competitor\n"
             f"source_url: {entry.get('source_url', '')}\n\n---\n")
    with open(comp_path, "a", encoding="utf-8") as f:
        f.write(block)


def phase_enrich(slug: str, assumption_id: str, refresh: bool = False,
                 skip: set[str] | None = None,
                 keywords: list[str] | None = None) -> None:
    """
    Phase 2 — Enrich each company with per-assumption signals. Contracts come
    from Phase 1's stashed procurement hits (no re-fetch — SKILL.md Step 2.2).
    News (GDELT) and hiring (Adzuna, tier-gated) are per-company.
    Cache-aware — 30-day TTL per (company, assumption).
    """
    assumption = read_assumption(slug, assumption_id)
    if not keywords:
        keywords = _derive_keywords(assumption)
    skip = skip or set()
    _icp_names, side_of = normalize_icp_tiers(assumption.get("icp_valid_tiers", []))
    enabled_domain_sources(assumption, slug)   # gate: warns on unregistered opt-ins

    existing_intel = read_intel_md(slug)
    companies_data = _read_companies_md(slug)
    phase1 = _read_phase1_cache(slug, assumption_id)

    for canon_key, row in companies_data.items():
        name = row["company"]
        tier = row.get("tier", "other") or "other"

        if tier == "other":
            log_manifest(slug, {"phase": "enrich_skipped",
                                "company": name, "reason": "tier_other"})
            continue
        if is_name_out_of_scope(name):
            log_manifest(slug, {"phase": "enrich_skipped",
                                "company": name, "reason": "non_operator_pattern"})
            continue
        if "(CIK" in name or ")  (" in name:
            log_manifest(slug, {"phase": "enrich_skipped",
                                "company": name, "reason": "unclean_edgar_metadata"})
            continue
        if re.match(r"^[A-Z][a-z]+\s+[A-Z][a-z]+$", name.strip()):
            log_manifest(slug, {"phase": "enrich_skipped",
                                "company": name, "reason": "personal_name"})
            continue

        current_intel = existing_intel.get(canon_key, {}).get("block", {}) or {}
        assumptions_block = current_intel.get("assumptions", {}) or {}

        if not refresh and assumption_id in assumptions_block:
            run_date = assumptions_block[assumption_id].get("run_date")
            if run_date and _days_ago(run_date) < 30:
                log_manifest(slug, {"phase": "enrich_cache_hit",
                                    "company": name, "assumption": assumption_id})
                continue

        block: dict[str, Any] = {"run_date": datetime.now().strftime("%Y-%m-%d"),
                                 "search_terms_used": keywords, "contracts": [],
                                 "news": [], "hiring": {}, "edgar_filings": []}

        block["contracts"] = _phase1_contracts_for_company(canon_key, phase1)

        if "gdelt_rest" not in skip:
            block["news"] = query_gdelt(name, keywords, months_back=6, slug=slug)

        # Hiring signal applies to any in-market tier (demand or supply side).
        if "adzuna" not in skip and side_of.get(tier) in {DEMAND, SUPPLY}:
            company_country_iso = (row.get("country") or "").strip().upper()
            country_iso_to_adzuna = {
                "GB": "gb", "UK": "gb", "IE": "ie", "US": "us", "DE": "de",
                "FR": "fr", "NL": "nl", "DK": "dk", "ES": "es", "IT": "it",
                "PL": "pl", "AT": "at", "AU": "au", "BR": "br", "CA": "ca",
                "CH": "ch", "IN": "in", "MX": "mx", "NZ": "nz", "RU": "ru",
                "SG": "sg", "ZA": "za",
            }
            adzuna_country = country_iso_to_adzuna.get(company_country_iso, "")
            all_postings: list[dict] = []
            if adzuna_country:
                all_postings = query_adzuna(
                    keywords, company=name, country=adzuna_country,
                    company_country_hint=company_country_iso, slug=slug,
                )
            else:
                log_manifest(slug, {"phase": "adzuna_country_fanout",
                                    "company": name,
                                    "reason": "unknown_company_country",
                                    "trying_countries": ["us", "gb", "de"]})
                for cc in ["us", "gb", "de"]:
                    hits = query_adzuna(keywords, company=name, country=cc, slug=slug)
                    if hits:
                        all_postings.extend(hits)
                        break
            kw_lower = [k.lower() for k in keywords]
            relevant_postings = [
                p for p in all_postings
                if any(kw in (p.get("title") or "").lower() for kw in kw_lower)
            ]
            postings = relevant_postings
            if postings:
                block["hiring"] = {
                    "postings_count": len(postings),
                    "top_titles": [p["title"] for p in postings[:5]],
                    "source": postings[0]["source"],
                    "source_url": postings[0]["source_url"],
                    "fetched_date": datetime.now().strftime("%Y-%m-%d"),
                }
            elif all_postings:
                log_manifest(slug, {"phase": "hiring_no_keyword_match",
                                    "company": name,
                                    "total_postings": len(all_postings),
                                    "kept_after_keyword_filter": 0})

        final_score, components = score_company(block, keywords=keywords)
        block["pain_score"] = final_score
        block["pain_components"] = components
        block["top_signal_for_copy"] = _top_signal(block)

        assumptions_block[assumption_id] = block
        current_intel.setdefault("id", row.get("id", ""))
        current_intel["canonical_name"] = canon_key
        current_intel["also_known_as"] = row.get("also_known_as", [])
        current_intel["lei"] = row.get("lei", "")
        current_intel["parent_entity"] = row.get("parent_entity", "")
        current_intel["parent_lei"] = row.get("parent_lei", "")
        current_intel["country"] = row.get("country", "")
        current_intel["tier"] = row.get("tier", "")
        current_intel["assumptions"] = assumptions_block
        existing_intel[canon_key] = {"display_name": name, "block": current_intel}

        log_manifest(slug, {"phase": "enrich_company", "company": name,
                            "assumption": assumption_id,
                            "contracts": len(block["contracts"]),
                            "news": len(block["news"]),
                            "hiring": bool(block.get("hiring")),
                            "pain_score": final_score})

    _write_intel_md(slug, existing_intel, assumption_id)
    _update_companies_pain_scores(slug, assumption_id, existing_intel)


def _days_ago(iso_date: str) -> int:
    try:
        d = datetime.strptime(iso_date[:10], "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return 10**9
    return (datetime.now().date() - d).days


def _top_signal(block: dict) -> str:
    """Choose the strongest company signal for discovery prioritization."""
    contracts = block.get("contracts") or []
    if contracts:
        c = contracts[0]
        val = c.get("value")
        val_str = f" ({val:,.0f} {c.get('currency', '')})" if val else ""
        return f"Contract: {c.get('title', '')} awarded {c.get('date', '')}{val_str} — {c.get('source', '')}"
    news = block.get("news") or []
    if news:
        return f"News: {news[0].get('title', '')} ({news[0].get('date', '')})"
    hiring = block.get("hiring") or {}
    if hiring:
        return f"Hiring: {hiring.get('postings_count')} open roles — top: {(hiring.get('top_titles') or [''])[0]}"
    return ""


# ---------------------------------------------------------------------------
# Markdown writers — companies.md and company-intel.md
# ---------------------------------------------------------------------------


def _read_companies_md(slug: str) -> dict[str, dict]:
    """Parse companies.md into {canonical_name: row}. Preserves existing pain_score."""
    companies_path, _, _ = _paths(slug)
    if not companies_path.exists():
        return {}
    text = companies_path.read_text(encoding="utf-8")
    sections = re.split(r"^##\s+", text, flags=re.M)[1:]
    out: dict[str, dict] = {}
    for sec in sections:
        header, _, body = sec.partition("\n")
        try:
            data = yaml.safe_load(body) or {}
        except yaml.YAMLError:
            continue
        if not isinstance(data, dict) or "company" not in data:
            continue
        key = normalize_name(data["company"])
        out[key] = data
    return out


def _write_companies_md(slug: str, assumption_id: str,
                        canonicals: dict[str, CanonicalCompany]) -> None:
    companies_path, _, _ = _paths(slug)
    companies_path.parent.mkdir(parents=True, exist_ok=True)

    existing = _read_companies_md(slug)
    next_id = 1 + max([int(re.sub(r"\D", "", r.get("id", "0") or "0") or 0)
                        for r in existing.values()], default=0)

    for canon_key, cc in canonicals.items():
        if canon_key in existing:
            row = existing[canon_key]
            row.setdefault("assumptions_evaluated", []).append(assumption_id)
            row["assumptions_evaluated"] = sorted(set(row["assumptions_evaluated"]))
            row["last_intel_run"] = datetime.now().strftime("%Y-%m-%d")
            if not row.get("tier") and getattr(cc, "tier", ""):
                row["tier"] = cc.tier
            new_line = _rationale_line(cc)
            if new_line and new_line not in (row.get("rationale") or ""):
                row["rationale"] = (row.get("rationale") or "").rstrip() + "\n" + new_line
        else:
            existing[canon_key] = {
                "id": f"CO{next_id}",
                "company": cc.display_name,
                "canonical_name": canon_key,
                "also_known_as": sorted(set(cc.also_known_as)),
                "lei": cc.lei,
                "parent_entity": cc.parent_entity,
                "parent_lei": cc.parent_lei,
                "linkedin_slug": "",
                "tier": getattr(cc, "tier", "other"),
                "also_seen_as": getattr(cc, "also_seen_as", []),
                "country": cc.country,
                "pain_score": None,
                "pain_components": {},
                "rationale": _rationale_line(cc),
                "assumptions_evaluated": [assumption_id],
                "first_added": datetime.now().strftime("%Y-%m-%d"),
                "last_intel_run": datetime.now().strftime("%Y-%m-%d"),
            }
            next_id += 1

    _dump_companies_md(slug, existing, assumption_id)


def _rationale_line(cc: CanonicalCompany) -> str:
    if not cc.role_appearances:
        return ""
    grouped: dict[str, list[str]] = {}
    for api, role, _url in cc.role_appearances:
        grouped.setdefault(f"{role}@{api}", []).append(_url)
    parts = []
    for key, urls in grouped.items():
        role, _, api = key.partition("@")
        parts.append(f"{role.replace('_', ' ')} in {api} ({len(urls)} record{'s' if len(urls) > 1 else ''})")
    return "- " + "; ".join(parts) + "."


def _dump_companies_md(slug: str, rows: dict[str, dict], assumption_id: str) -> None:
    companies_path, _, _ = _paths(slug)
    # Rank by pain first; tier is only a deterministic tie-break, sorted by name
    # (no hardcoded tier order — tier names are idea-defined).
    ordered = sorted(rows.values(), key=lambda r: (
        -(r.get("pain_score") or 0),
        r.get("tier", "other"),
        r.get("company", ""),
    ))
    by_tier: dict[str, int] = {}
    for r in ordered:
        by_tier[r.get("tier", "other")] = by_tier.get(r.get("tier", "other"), 0) + 1

    frontmatter = {
        "idea": slug,
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "last_intel_run": {
            "assumption": assumption_id,
            "run_date": datetime.now().strftime("%Y-%m-%d"),
            "companies_written": len(ordered),
        },
        "totals": {
            "companies": len(ordered),
            "by_tier": by_tier,
        },
    }
    lines = ["---", yaml.safe_dump(frontmatter, sort_keys=False,
                                    allow_unicode=True).strip(), "---", ""]
    for r in ordered:
        lines.append(f"## {r['company']}")
        lines.append("")
        lines.append(yaml.safe_dump(r, sort_keys=False, allow_unicode=True).strip())
        lines.append("")
    companies_path.write_text("\n".join(lines), encoding="utf-8")


def _write_intel_md(slug: str, intel: dict[str, dict], assumption_id: str) -> None:
    _, intel_path, _ = _paths(slug)
    intel_path.parent.mkdir(parents=True, exist_ok=True)

    ordered_names = sorted(intel.keys(),
                            key=lambda k: -(intel[k]["block"]
                                            .get("assumptions", {})
                                            .get(assumption_id, {})
                                            .get("pain_score", 0)))

    frontmatter = {
        "idea": slug,
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "schema_version": 1,
    }
    lines = ["---", yaml.safe_dump(frontmatter, sort_keys=False).strip(), "---", "",
             f"## Run summary — {assumption_id} · {datetime.now().strftime('%Y-%m-%d')}", "",
             "| Rank | Company | Tier | pain_score | Top signal |",
             "|------|---------|------|-----------|-----------|"]
    for i, k in enumerate(ordered_names, start=1):
        blk = intel[k]["block"]
        a_blk = blk.get("assumptions", {}).get(assumption_id, {})
        lines.append(f"| {i} | {intel[k]['display_name']} | {blk.get('tier', '')} | "
                     f"{a_blk.get('pain_score', '')} | {a_blk.get('top_signal_for_copy', '')} |")
    lines.append("")

    for k in ordered_names:
        display = intel[k]["display_name"]
        block = intel[k]["block"]
        lines.append(f"## {display}")
        lines.append("")
        lines.append(yaml.safe_dump(block, sort_keys=False, allow_unicode=True).strip())
        lines.append("")

    intel_path.write_text("\n".join(lines), encoding="utf-8")


def _update_companies_pain_scores(slug: str, assumption_id: str,
                                   intel: dict[str, dict]) -> None:
    rows = _read_companies_md(slug)
    for k, entry in intel.items():
        if k not in rows:
            continue
        block = entry["block"].get("assumptions", {}).get(assumption_id, {})
        rows[k]["pain_score"] = block.get("pain_score")
        rows[k]["pain_components"] = block.get("pain_components", {})
    _dump_companies_md(slug, rows, assumption_id)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _cli() -> None:
    p = argparse.ArgumentParser(prog="intel_lib",
                                 description="Startup outreach intel pipeline")
    sub = p.add_subparsers(dest="cmd", required=True)

    for cmd in ("run", "discover", "enrich", "score", "status"):
        sp = sub.add_parser(cmd)
        sp.add_argument("--slug", required=True)
        sp.add_argument("--assumption", required=True)
        sp.add_argument("--refresh", action="store_true")
        sp.add_argument("--skip", default="",
                        help="Comma-separated API keys to skip for this run")
        sp.add_argument("--keywords", default="",
                        help="Comma-separated keywords override (skips auto-derivation)")

    args = p.parse_args()
    skip_set = {s.strip() for s in args.skip.split(",") if s.strip()}
    keywords = ([k.strip() for k in args.keywords.split(",") if k.strip()]
                or None)

    if args.cmd in {"discover", "run"}:
        phase_discover(args.slug, args.assumption, keywords=keywords, skip=skip_set)
    if args.cmd in {"enrich", "run"}:
        phase_enrich(args.slug, args.assumption, refresh=args.refresh,
                     skip=skip_set, keywords=keywords)
    if args.cmd == "score":
        intel = read_intel_md(args.slug)
        _update_companies_pain_scores(args.slug, args.assumption, intel)
        print(f"Rescored {len(intel)} companies for {args.assumption}")

    # Auto-regenerate outreach_tracker.html.
    if args.cmd in {"run", "discover", "enrich", "score"}:
        try:
            import subprocess
            tracker_script = REPO_ROOT / "scripts" / "build_control_room.py"
            if tracker_script.exists():
                result = subprocess.run(
                    [sys.executable, str(tracker_script), args.slug],
                    capture_output=True, text=True, timeout=60,
                )
                if result.returncode == 0:
                    print(f"[dashboard] {result.stdout.strip()}")
                else:
                    print(f"[dashboard] build failed (exit {result.returncode}): "
                          f"{result.stderr.strip()[:200]}", file=sys.stderr)
            else:
                print(f"[dashboard] SKIP: {tracker_script} not found", file=sys.stderr)
        except Exception as e:
            print(f"[dashboard] regen error: {e}", file=sys.stderr)

    if args.cmd == "status":
        manifest = manifest_path(args.slug)
        if not manifest.exists():
            print(f"No manifest yet for {args.slug}")
            return
        with open(manifest) as f:
            lines = f.readlines()
        print(f"Manifest entries: {len(lines)}")
        for line in lines[-10:]:
            print("  " + line.strip())


if __name__ == "__main__":
    _cli()
