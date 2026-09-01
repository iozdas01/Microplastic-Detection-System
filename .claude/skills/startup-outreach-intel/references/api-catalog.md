# API Catalog — Startup Outreach Intel

One card per API: **what the data means, when to fire it, what it returns, and how it maps to `icp_valid_tiers`.**

**Reachability is not here.** Whether a source is enabled, what auth or env keys it needs, and why a disabled one is disabled all live in `api-registry.yaml` — the file `_common.is_enabled()` actually reads. Endpoint URLs and auth bullets were removed from these cards on 2026-08-07 for that reason: `uk_contracts_finder` had been recorded as disabled in three prose files while the registry said `enabled: true`, so the only copy that governed behaviour was the wrong one.

> **Do not add `Auth:`, `Env vars:`, `Endpoint:` or `STATUS: DISABLED` bullets to any card below.**
> They belong to `api-registry.yaml`. `validate_repo.py` enforced this with a regex until
> 2026-08-07; the check was removed because it hardcoded this file's exact markdown shape and
> would have broken on the first restructure. The rule did not go away — it moved here, where
> the person about to break it is already reading.

Add an API by writing `scripts/data/<name>.py`, registering it, then writing its card here. To skip one for a single run without touching the registry, pass `--skip <api_key>` to the CLI.

---

## Universal APIs (always run)

### ted_eu — TED EU (Tenders Electronic Daily)

- **Library function:** `intel_lib.query_ted(keywords: list[str], months_back: int = 24, cpv_codes: list[str] = None) -> list[dict]`
- **Trigger:** always. TED indexes every EU public procurement notice — it works for any assumption where the buyers are public-sector or public-adjacent (utilities, transport, healthcare, energy, education).
- **What it returns:** contract notices matching the keywords. Every notice has a `contracting_authority` (buyer) and a `supplier` (winner, if the contract is awarded). Both are named companies.
- **Tier mapping:**
  - `contracting_authority` → demand-side tier, whichever name `icp_valid_tiers` gives that side.
  - `supplier` (when award notice) → supply-side tier, by the same whitelist.
  - Read the assumption's tier vocabulary and pick the closest match.
- **Response shape (normalized):**
  ```json
  [{"title": "...", "value_eur": 4200000, "date": "2025-11-15",
    "contracting_authority": "{Operator Co}", "supplier": "{Vendor Co} AG",
    "cpv_codes": ["45261000", "71600000"], "country": "DK",
    "source": "TED EU", "source_url": "https://ted.europa.eu/en/notice/..."}]
  ```
- **Notes:** Values sometimes appear in currencies other than EUR — the library normalizes to EUR-equivalent using the notice's own conversion. CPV codes can be reused across assumptions in the same domain — cache them per assumption to speed up future queries.

### uk_contracts_finder — UK Contracts Finder + Find a Tender

- **Reachability:** see `api-registry.yaml` → `uk_contracts_finder` (currently off; the probe record is in the `scripts/data/uk_contracts.py` docstring). This card does not restate whether it runs.
- **Library function:** `intel_lib.query_uk_contracts(keywords: list[str], months_back: int = 24) -> list[dict]`.
- **Trigger:** would be always, if reachable.
- **What it returns:** same shape as TED but for UK. Field names differ (`contract_authority` vs. `contracting_authority` in the raw API); library normalizes.
- **Tier mapping:** identical to TED (buyer + supplier). Where both TED and UK Contracts Finder surface the same entity, dedup keeps the union of contracts under one company.
- **Response shape (normalized):**
  ```json
  [{"title": "...", "value_gbp": 4200000, "date": "2025-11-15",
    "contracting_authority": "The Crown Estate", "supplier": "{Service Co} Ltd",
    "cpv_codes": [...], "region": "UK-South",
    "source": "UK Contracts Finder", "source_url": "https://contractsfinder.service.gov.uk/notice/..."}]
  ```
- **Notes:** Framework agreements often have no supplier at issue time — the library records these with `supplier: null` and marks the notice as "framework". These still indicate demand.

### adzuna — Adzuna Jobs API

- **Library function:** `intel_lib.query_adzuna(keywords: list[str], country: str = "gb", company: str = None, results_per_page: int = 50) -> list[dict]`

- **CRITICAL: batch keywords into ONE call per company, NEVER one call per keyword.**
  Adzuna's `what` parameter accepts a boolean expression: `what=(kw1) OR (kw2) OR (kw3)`. The library MUST build the query as:
  ```python
  what_expr = " OR ".join(f"({kw})" for kw in keywords)
  params = {"app_id": ..., "app_key": ..., "what": what_expr, "company": company, ...}
  ```
  This is 1 call per company total, not `len(keywords)` calls. On 2026-07-08 the library was seen doing 6 Adzuna calls per company (one per keyword) → would bust the 50/run cap after only 8 companies. Adzuna's boolean-OR `what` param is native and documented — no need for multiple calls.

- **Company-name normalization before Adzuna scoping.** Adzuna's `company` param does substring matching on employer names, and it's brittle. Before passing:
  - Strip legal suffixes (`Ltd`, `Limited`, `A/S`, `GmbH & Co. KG`, `Inc`, `Inc.`, `PLC`, `LLC`, `Corp`, `Corporation`) — Adzuna's index doesn't include most of these
  - Strip diacritics (`{Operator Co}` → `Maersk`) — Adzuna often indexes ASCII-only
  - **Strip operational-arm suffixes that pollute the match**: `SERVICE COMPANY`, `SERVICES`, `POWER`, `RENOUVELABLES`, `RENEWABLES`, `HOLDINGS` (when it's an operational sub-brand, e.g. `EVERSOURCE ENERGY SERVICE COMPANY` → `{Utility Co} Energy`, `EDF RENOUVELABLES OMAN SOLAR` → `EDF Renouvelables`, `AVANGRID POWER, LLC` → `{Utility Co}`). These are the trading arms; Adzuna typically indexes the parent brand.
  - **Geographic tails**: strip trailing country/region names (e.g. `EDF RENOUVELABLES OMAN SOLAR` → `EDF Renouvelables` — Adzuna GB isn't going to have Oman postings anyway; even for a matched region the parent-name search yields more hits).
  - Try the parent name from GLEIF first, fall back to canonical name
  - **Country gate**: if the company's `country` field is not in `{GB, IE, US, DE, FR, NL, DK, ES, IT, PL}` (Adzuna's supported markets), don't call Adzuna at all — log `{"reason": "adzuna_country_unsupported", "country": "..."}` and skip. Adzuna GB is UK-only; hitting it for `country: OM` (Oman) or `country: DK` (Denmark, no Adzuna market) burns cap for guaranteed zeros.
  - If the scoped call returns 0, log `{"reason": "no_adzuna_match", "tried": "..."}` and skip — do NOT keep retrying variants (busts the cap).

- **Rate-limit caps (enforced by the library — read `api-registry.yaml` → `adzuna.limits`):**
  - `max_calls_per_run: 50` — hard cap per intel invocation. If a run would exceed this, remaining companies get `hiring: {}` and the manifest logs `hiring_skipped_rate_limit`.
  - `max_calls_per_month: 200` — safety valve at 20% below the 250/month free-tier ceiling. The library reads `calls_this_month` from `api-registry.yaml` before every call and refuses when the cap is hit.
  - `per_company_per_run: 1` — one call per unique canonical company per run. **This means 1 keyword-batched call, not 6.** Multiple contacts at the same company share the same Adzuna lookup — never per-contact fan-out.
  - `cache_ttl_days: 30` — company results are cached in `.intel-manifest.jsonl` for 30 days. Reruns within 30d hit the cache and burn zero calls.

- **Trigger:** always (subject to caps above). Jobs are the leading indicator of pain — companies hire when the pain is felt but not solved.
- **What it returns:** current job postings matching keywords, optionally scoped to a company. Each posting has employer name, title, description (full JD text), location, and salary.
- **Tier mapping:** infer from the posted title against known role patterns. Examples:
  - "Head of Operations", "Director of X", "VP" → buyer role at the employer
  - "Engineer", "Technician", "Coordinator" → practitioner role
  - "Contract Manager", "Procurement Lead" → buyer-side procurement
  The company's tier is inferred from what kind of roles it posts + which industry the assumption is in. Read `tier-inference.md` for the pattern table.
- **Response shape (normalized):**
  ```json
  [{"title": "{on-ICP role title}", "employer": "{Operator Co} UK Ltd",
    "location": "Grimsby, UK", "salary_min_gbp": 45000, "salary_max_gbp": 55000,
    "description": "...", "posted_date": "2026-06-14",
    "source": "Adzuna GB", "source_url": "https://www.adzuna.co.uk/details/..."}]
  ```
- **Notes:** the `description` field is used for tech-stack signal extraction downstream. Cache descriptions in the manifest so the enrichment step can reuse them without a second API call.

### gleif — GLEIF LEI API

- **Library function:** `intel_lib.resolve_gleif(company_name: str, country_hint: str = None) -> dict`
- **Trigger:** always, once per discovered canonical name. Purpose: resolve to LEI so subsidiaries collapse to their parent.
- **What it returns:** the top LEI match with parent-child relationships if any.
- **Tier mapping:** GLEIF doesn't assign tier — it only resolves identity. But it produces `parent_entity`, which is what actually gets stored as the canonical company. If a name maps to multiple LEIs, the library picks the highest match_score and logs the alternatives for founder review.
- **Response shape (normalized):**
  ```json
  {"lei": "529900FHVFMB48BLZR42", "name": "MÆRSK A/S", "country": "DK",
   "parent_lei": null, "parent_name": null, "match_score": 0.97,
   "source": "GLEIF", "source_url": "https://api.gleif.org/api/v1/lei-records/529900FHVFMB48BLZR42"}
  ```
- **Notes:** GLEIF only covers entities that have applied for an LEI — many private SMEs don't. If `lei: null`, that's OK — the company still gets a `companies.md` row using its normalized name as canonical.

---

## Conditional APIs (fire only when triggers match)

### edgar_fulltext — SEC EDGAR Full-Text Search

- **Library function:** `intel_lib.query_edgar_fulltext(keywords: list[str], form_types: list[str] = ["10-K", "10-Q", "8-K"]) -> list[dict]`
- **Trigger:** fire if EITHER of these holds:
  - the assumption's demand-side buyers are plausibly US-listed companies
  - assumption `category` is `pain` AND assumption text mentions US market
- **What it returns:** filings mentioning the keywords, with the filer's CIK, form type, filing date, and a text excerpt around the match.
- **Tier mapping:** the filer is the potential buyer (or the incumbent, if the excerpt discusses the pain as a competitor). Assignment depends on excerpt content — library returns the excerpt for downstream reasoning, does not auto-assign tier.
- **Response shape (normalized):**
  ```json
  [{"filer": "NextEra Energy Inc", "cik": "0000753308",
    "form_type": "10-K", "filing_date": "2025-02-14",
    "excerpt": "...{the pain} costs represent a material...",
    "source": "SEC EDGAR", "source_url": "https://www.sec.gov/cgi-bin/browse-edgar?..."}]
  ```
- **Notes:** filings mentioning pain in risk factors are legally attested and provide high-signal buyer evidence for discovery and prioritisation. They do not replace live-profile verification before outreach wording is drafted.

### sbir — SBIR.gov

- **Library function:** `intel_lib.query_sbir(keywords: list[str], years_back: int = 3) -> list[dict]`
- **Trigger:** fire if `category` is `timing` OR `technical` OR `competitive`. SBIR awards reveal companies getting government R&D money in the space — these are usually named competitors, occasionally incumbents.
- **What it returns:** grant awards matching keywords with recipient, agency, amount, year, abstract.
- **Tier mapping:** recipient → likely `vendor` / `competitor`. Do NOT add to outreach registry by default — surface to founder in the manifest under `competitors_detected`. If founder confirms they want to interview competitors, they add manually.
- **Response shape (normalized):**
  ```json
  [{"recipient": "{Grantee Co}", "agency": "DOE",
    "award_amount_usd": 1500000, "year": 2024,
    "abstract": "{first line of the abstract}...",
    "source": "SBIR", "source_url": "https://www.sbir.gov/node/..."}]
  ```

### cordis — CORDIS (EU Horizon)

- **Library function:** `intel_lib.query_cordis(keywords: list[str], years_back: int = 3) -> list[dict]`
- **Trigger:** same as SBIR. EU competitor / incumbent detection.
- **Tier mapping:** same as SBIR (competitor by default, surfaced for founder review).

### gdelt — GDELT REST API

- **Library function:** `intel_lib.query_gdelt(company: str, keywords: list[str], months_back: int = 6) -> list[dict]`
- **Trigger:** always during enrichment. GDELT is the primary news source.
- **What it returns:** article title, source domain, date, URL.
- **Tier mapping:** doesn't assign tier.
- **Response shape:**
  ```json
  [{"title": "{Operator Co} awarded {major contract}",
    "date": "2026-06-14", "url": "https://reneweconomy.com.au/...",
    "domain": "reneweconomy.com.au", "source": "GDELT"}]
  ```
- **Notes:** GDELT returns raw article URLs; the library filters to reputable domains (see `intel_lib.NEWS_DOMAIN_ALLOWLIST`) to avoid hooking on blog spam.

### exa — Exa AI (fallback, DEFAULT OFF)

- **Library function:** `intel_lib.query_exa(query: str, months_back: int = 6, num_results: int = 5) -> list[dict]`
- **Default:** **`enabled: false` in `api-registry.yaml`.** Do not turn on for smoke tests or first runs.
- **When to re-enable (checklist — all three must hold):**
  1. You've run intel on the target assumption with only GDELT enabled.
  2. Manual grep of `companies.md` (targeting fields) shows `news: []` for ≥ 40% of companies with `pain_score ≥ 5`.
  3. Spot-checking 3 of those empty-news companies against Google News (or manually) confirms real news exists that GDELT missed — i.e., it's a GDELT gap, not a genuinely-quiet company.
  If all three hold, flip `enabled: true` in `api-registry.yaml` and rerun with `--refresh news`. If any of the three fails, keep it off — you're about to pay for noise.
- **Trigger (when enabled):** only if GDELT returned zero relevant news for a company. Not used for discovery — Exa is too broad, would flood the pool with adjacent noise.
- **What it returns:** semantic search results with title, URL, published date.
- **Tier mapping:** doesn't assign tier.

### companies_house — Companies House (UK)

- **Library function:** `intel_lib.query_companies_house(company_name: str) -> dict`
- **Trigger:** fire for any company whose GLEIF country is `GB` OR whose name contains "Ltd" / "PLC" / "LLP".
- **What it returns:** company number, incorporation date, SIC codes, filing status, registered address, active directors.
- **Tier mapping:** doesn't reassign tier, but SIC codes can validate the tier assignment (e.g., SIC 35110 = "Production of electricity" → confirms an operator, i.e. the demand tier).
- **Response shape (normalized):**
  ```json
  {"company_number": "04898482", "incorporated": "2003-09-18",
   "sic_codes": ["35110", "35120"], "filing_status": "active",
   "registered_address": "5 Howick Place, London, SW1P 1WG",
   "source": "Companies House",
   "source_url": "https://find-and-update.company-information.service.gov.uk/company/04898482"}
  ```

---

## API selection procedure (used in Phase 1 Step 1.2)

For each conditional API card above, evaluate its `Trigger` field against the assumption. Fire if all conditions in the trigger are met. Log the decision to the manifest:

```jsonl
{"api": "sbir", "decision": "skip", "reason": "category is 'buyer', not timing/technical/competitive"}
```

This makes reruns auditable — a new maintainer can see exactly why the skill made each choice on the last run.

---

## Adding a new API

To add a new API:
1. Add a card to this file with all seven required fields (endpoint, auth, env vars, library function signature, trigger, tier mapping, response shape).
2. Implement the function in `scripts/intel_lib.py` (bundled with this skill) returning the documented shape.
3. Register the API in `api-registry.yaml` at repo root with `used_by: [startup-outreach-intel]`.
4. If it's a discovery API, add its call to `discover.py`'s orchestrator. If enrichment, add to `enrich.py`.

No changes to `SKILL.md` are needed — the workflow is API-agnostic by design.
