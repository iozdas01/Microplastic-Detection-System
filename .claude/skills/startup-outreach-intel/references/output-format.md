# Output Format — schemas for companies.md, companies.md, and pain scoring

This file specifies the exact structure the skill writes. `startup-outreach-targets` reads these files for company discovery, prioritisation, and contact enrichment. `startup-outreach-draft` does not treat this cache as message evidence; it verifies every Msg 1 claim against a fresh live-profile snapshot.

If you're editing this file, keep it in lockstep with the downstream skills' Read paths. Any field the downstream reads must be produced here; any field produced here must be documented in `schemas/contact.md` if it propagates onto contact cards.

---

## `reports/{slug}/outreach/companies.md`

The company registry. Consumed by `startup-outreach-targets` to decide which companies to search LinkedIn against.

### Frontmatter

```yaml
---
idea: {slug}
last_updated: 2026-07-08
last_intel_run:
  assumption: A2
  run_date: 2026-07-08
  companies_discovered: 47
  companies_updated: 12
  companies_skipped_cached: 8
totals:
  companies: 47
  by_tier:
    {demand_tier}: 18
    {supply_tier}: 6
    {supply_tier_2}: 12
    {supply_tier_3}: 8
    other: 3
---
```

### Company block format

Each company is a `##`-headed section. `pain_score` is the primary sort key.

```yaml
## {Operator Co}

id: CO1                          # CO{N}, monotonic across the file
company: {Operator Co}
canonical_name: {Operator Co}       # normalized name used for dedup
also_known_as: [{Operator Co} UK, {Operator Co} A/S, {Operator Co} Holdings]
lei: 529900FHVFMB48BLZR42        # GLEIF LEI, or empty if not resolved
parent_entity: ""                 # empty if this IS the parent
parent_lei: ""
linkedin_slug: {operator-co}      # empty at intel time — targets skill fills

tier: {demand_tier}                 # from icp_valid_tiers, per tier-inference.md
also_seen_as: []                  # other tiers this company appeared in
country: DK
sic_codes: [35110]                # from Companies House if available

pain_score: 9                     # 1-10, from Phase 3 scoring formula
pain_components:                  # transparent breakdown used for company prioritisation
  contract_score: 3
  hiring_score: 1
  news_score: 1

rationale: >
  Contracting authority for £4.2M {repair task} framework awarded 2025-11-15
  (UK Contracts Finder). Listed as UK operator of 847 {asset}, average age 8.3 years
  ({opted-in asset source}). 23 {operational-loss signal} events in the last 6 months
  ({opted-in operational source}).

assumptions_evaluated: [A2]       # which assumptions this company has been enriched for
first_added: 2026-07-08
last_intel_run: 2026-07-08
```

**Sort order:** by `pain_score` descending, then by `tier` (buyer tiers before supply-side tiers, per the assumption's `icp_valid_tiers` order).

**Update rules:**
- New companies get appended with the next CO{N} id.
- Existing companies get their `pain_score`, `pain_components`, `last_intel_run`, and `assumptions_evaluated` updated in place.
- `tier` is only updated if a new evidence source contradicts the current tier — in which case log the change to the manifest and keep the old tier in `also_seen_as`.
- `rationale` is appended, never overwritten. Each rerun appends a new evidence line if new signals were found.

---

## `reports/{slug}/outreach/companies.md`

The rich per-company intelligence file. Read by `startup-outreach-targets` during enrichment to prioritize companies and add auditable `profile_fit_signals` to contacts. Those cached signals remain discovery context only; `startup-outreach-draft` reopens the live profile before drafting.

### Frontmatter + run summary

```yaml
---
idea: {slug}
last_updated: 2026-07-08
schema_version: 1
---

## Run summary — A2 · 2026-07-08

| Rank | Company | Tier | pain_score | Top signal |
|------|---------|------|-----------|-----------|
| 1 | {Operator Co} | {demand_tier} | 9 | £4.2M {inspection task} framework awarded Nov 2025 (UK Contracts Finder) |
| 2 | {OEM Service Co} | {supply_tier} | 8 | 12 {operational-loss signal} events in Q4 2025 ({opted-in operational source}) |
| 3 | {Vendor Co} | {supply_tier_2} | 8 | Awarded £4.2M {inspection task} framework Nov 2025 (UK Contracts Finder) |
| 4 | {Operator Co 2} | {demand_tier} | 7 | 4 maintenance-role job postings (Adzuna) |
...
```

The summary table is regenerated on every run — never appended. It reflects the current state of the file.

### Company block format

```yaml
## {Operator Co}

id: CO1
canonical_name: {Operator Co}
also_known_as: [{Operator Co} UK, {Operator Co} Holdings]
lei: 529900FHVFMB48BLZR42
parent_entity: ""
parent_lei: ""
country: DK
tier: {demand_tier}
sic_codes: [35110]

# Non-assumption-scoped enrichment — set once, updated only when data changes

fleet:                           # omit block entirely if not applicable
  {asset}_count: 1847
  avg_age_years: 8.3
  oldest_year: 2010
  newest_year: 2024
  total_capacity_mw: 12140
  source: {opted-in asset source}
  source_url: {the query URL the source actually returned}
  fetched_date: 2026-07-08

companies_house:                 # omit if not UK / no result
  company_number: "04898482"
  incorporated: 2003-09-18
  filing_status: active
  source_url: https://find-and-update.company-information.service.gov.uk/company/04898482
  fetched_date: 2026-07-08

# Assumption-scoped enrichment — one block per assumption, append never overwrite

assumptions:

  A2:
    run_date: 2026-07-08
    search_terms_used:
      - {repair task}
      - {inspection task}
      - {regional variant}
      - {domain} maintenance
      - {asset} maintenance

    contracts:                            # sorted by date desc; contracts[0] is the freshest
      - title: "{Repair Task} Framework 2025-2028"
        value: 4200000
        currency: GBP
        date: 2025-11-15                  # award date — field name matches contact schema reader
        role: contracting_authority       # this company's role in the contract
        counterparty: {Vendor Co} AG
        cpv_codes: [45261000, 71600000]
        source: UK Contracts Finder
        source_url: https://contractsfinder.service.gov.uk/notice/abc-123

      - title: "{second contract title}"
        value: 890000
        currency: EUR
        date: 2025-08-02
        role: contracting_authority
        counterparty: {Supplier Co}
        source: TED EU
        source_url: https://ted.europa.eu/en/notice/def-456

    {operational-loss signal}:                          # omit block entirely if not applicable
      events_6m: 23                       # matches contact schema: {operational-loss signal}.events_6m
      gwh_6m: 145.3                       # matches contact schema: {operational-loss signal}.gwh_6m
      source: {opted-in operational source}
      source_url: {the query URL the source actually returned}
      fetched_date: 2026-07-08

    hiring:
      postings_count: 4
      top_titles:
        - "{on-ICP role title}"
        - "{Site} Maintenance Manager"
        - "{Site} Engineer"
      source: Adzuna GB
      source_url: https://api.adzuna.com/v1/api/jobs/{cc}/search/1?company={Operator+Co}&what={term}
      fetched_date: 2026-07-08

    news:
      - title: "{Operator Co} awarded {major contract}"
        date: 2026-06-14
        url: {the article URL}
        domain: reneweconomy.com.au
        source: GDELT
      - title: "{Operator Co} {pain event} prompts fleet-wide review"
        date: 2026-05-22
        url: {the article URL}
        domain: {trade-press domain}
        source: GDELT

    edgar_filings: []              # empty if not applicable / no US listing

    pain_score: 9
    pain_components:
      contract_score: 3
      hiring_score: 1
      news_score: 1

    top_signal_for_copy: >
      Contract: £4.2M {inspection task} framework awarded to {Vendor Co}
      on 2025-11-15 (UK Contracts Finder).
```

**The `top_signal_for_copy` field** retains its legacy schema name for compatibility. It is Phase 3's summary of the company's strongest discovery signal for this assumption. Priority order: contract > filing excerpt > {operational-loss signal} > news > hiring. `startup-outreach-targets` may use it to rank companies and avoid redundant enrichment calls; it never authorizes message wording.

**When a company has no signals from any source:** write the assumption block with empty arrays for each field, `pain_score: 1`, and `top_signal_for_copy: ""`. An empty block is valid — it means the company appeared in one API but nothing enriched. The targets skill can then use live-profile fit or its documented fallback enrichment steps.

---

## `reports/{slug}/outreach/.competitors-detected.md`

Companies flagged by SBIR / CORDIS / EDGAR as building in this space but whose tier is not in `icp_valid_tiers`. Separate from the outreach registry — the founder reviews and decides whether to interview any of them.

```yaml
---
idea: {slug}
last_updated: 2026-07-08
assumptions_scanned: [A2]
---

## {Vendor Co}

detected_role: grant_recipient
detected_in: sbir
grant_amount_usd: 1500000
year: 2024
abstract_excerpt: "{first line of the abstract} ..."
tier_would_be: competitor
reason_not_added: "competitor not in icp_valid_tiers for A2"
source_url: https://www.sbir.gov/node/12345

---

## Aerones

detected_role: grant_recipient
detected_in: cordis
project: HORIZON-CL5-2024-D3-01
year: 2024
abstract_excerpt: "{the paper's own opening sentences} ..."
tier_would_be: competitor
reason_not_added: "competitor not in icp_valid_tiers for A2"
source_url: https://cordis.europa.eu/project/id/...
```

---

## `reports/{slug}/outreach/.intel-manifest.jsonl`

Append-only JSONL log of every action the skill took. Used for reruns to identify cache hits and to give the founder an audit trail.

```jsonl
{"ts": "2026-07-08T09:14:22Z", "phase": "start", "assumption": "A2", "refresh": false}
{"ts": "2026-07-08T09:14:23Z", "phase": "derive_keywords", "terms": [...], "derivation": {...}}
{"ts": "2026-07-08T09:14:24Z", "phase": "api_decision", "api": "{opted-in asset source}", "decision": "fire", "reason": "tier is demand-side AND the assumption opted into it via domain_data_sources"}
{"ts": "2026-07-08T09:14:24Z", "phase": "api_decision", "api": "sbir", "decision": "skip", "reason": "category is pain, not timing/technical/competitive"}
{"ts": "2026-07-08T09:14:31Z", "phase": "api_call", "api": "ted_eu", "params": {...}, "result_count": 47, "duration_ms": 6892}
{"ts": "2026-07-08T09:14:38Z", "phase": "api_call", "api": "uk_contracts_finder", "params": {...}, "result_count": 23}
{"ts": "2026-07-08T09:15:02Z", "phase": "gleif_resolve", "input": "{Operator Co} A/S", "output_lei": "529900FHVFMB48BLZR42", "confidence": 0.97}
{"ts": "2026-07-08T09:15:44Z", "phase": "tier_assign", "company": "{Operator Co}", "role_in_api": "contracting_authority", "assigned_tier": "{demand_tier}", "conflicts": []}
{"ts": "2026-07-08T09:16:12Z", "phase": "enrich_company", "company": "{Operator Co}", "assumption": "A2", "apis_called": ["gdelt", "{opted-in operational source}", "adzuna"], "results": {...}}
{"ts": "2026-07-08T09:18:03Z", "phase": "score", "company": "{Operator Co}", "components": {...}, "score": 9}
{"ts": "2026-07-08T09:18:44Z", "phase": "end", "companies_written": 47, "companies_cached": 8, "duration_s": 262}
```

The manifest is the source of truth for what happened on a given run. If a downstream question comes up ("why does {Operator Co} have `tier: {demand_tier}`?"), the answer is grep-able from the manifest.

---

## Pain scoring formulas

Each component is scored independently, then summed and clamped to 1-10. Formulas below are what `intel_lib.score_company()` implements.

### contract_score (0-3)

Based on the company's contracts under the current assumption, weighted by recency, count, and value.

```
Let contracts = assumption block's contracts array for this company.
recency_weight(c) = 1.0 if c.awarded within last 12 months
                    0.5 if 13-24 months
                    0.0 if older (should already be filtered out at Phase 2)
total_weighted_value = sum(c.value_gbp_equivalent * recency_weight(c) for c in contracts)

if total_weighted_value >= 5,000,000 → 3
if total_weighted_value >= 1,000,000 → 2
if total_weighted_value > 0          → 1
else                                 → 0

Also: if len(contracts) >= 3 AND score is 1, bump to 2 (multiple contracts = pattern of buying).
```

### Components from a vertical source — none registered

`contract`, `hiring` and `news` are the three scored components today, because they
come from sources every idea can reach. A vertical adapter opted into via
`domain_data_sources` may add its own component, but none is registered — see
`api-registry.yaml`'s domain-specific section.

If you add one, declare its thresholds per idea in `companies.md` frontmatter under
`pain_scoring.{component}:` rather than in this file: "big enough to hurt" is a fact
about a market, not about this pipeline. Score 0 when the thresholds are not
declared — never guess them.

### hiring_score (0-2)

```
Let h = hiring block.
if h.postings_count >= 5 → 2
if h.postings_count >= 2 → 1
if h.postings_count >= 1 → 1  # even 1 posting is an active signal
else                     → 0
```

### news_score (0-1)

```
Let n = news array (max 5 items, filtered to allowlist domains, last 6 months).
if len(n) >= 1 → 1
else           → 0
```

News is a low-weight signal because "recent article about company X" doesn't always mean pain — it could be a positive PR piece. The domain allowlist and low score keep weak news from dominating company prioritisation; it is never sufficient evidence for Msg 1 wording.

### Final composition

```
raw = contract_score + hiring_score + news_score
final = max(1, min(10, raw))
```

Store both raw components (`pain_components` dict) and the final `pain_score`. The targets skill uses them to choose which companies and contacts to inspect first.
