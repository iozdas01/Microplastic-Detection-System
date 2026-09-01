# Phase mechanics — outreach intel

Loaded per phase by `startup-outreach-intel`. SKILL.md carries the decision procedure and
guardrails; this file carries how each phase runs, its output schema, and the invocation
examples. Phase 0.6's own mechanics live in `self-published-sweep.md`.

## Phase 0 — Contact harvest (founder-set)

**Goal:** every company that a real human in `contacts.md` actually works for is present in
`companies.md`. Phase 1 discovers companies from APIs; Phase 0 discovers them from the network
the founder has already built. Run it FIRST — it is free, it needs no API key, and it routinely
finds companies the API sweep never surfaces.

**Why this exists.** Outreach and the company map were built by different skills and never
reconciled, so they drifted. Measured in practice: 11 of the 14
employers behind the 12 drafted contacts were absent from a 35-company map. The reverse gap is
worse, because it is silent — `companies.md` already held a Physion Labs entry whose own text
said co-founder Bing Shuai was "ALREADY 1st degree, though no contact card was ever created for
him," with an explicit `ACTION: Create one and message him`. Nothing read it. The map also
recorded what Physion actually builds, which corrected a contact classification that had been
made from the LinkedIn headline alone.

The lesson generalises: **a contact card and a company entry are two views of the same fact, and
whichever was written second is usually the one that knows more.**

### Step 0.1 — Extract employers from `contacts.md`

Read every contact block. For each, take `company` and the current employer named in
`signal_excerpt` / `validation_rationale`. Skip contacts at `outreach_status: off_scope`,
`url_broken` or `queued` unless the founder asks for the full sweep.

Normalise before comparing, or the same company enters the map three times:

- Strip legal suffixes (`Inc`, `Ltd`, `Pte Ltd`, `GmbH`, `SA`, `Corporation`).
- Fold a division into its parent and keep the division in `also_known_as`:
  `Amazon Fulfillment Technologies & Robotics` → `Amazon`;
  `GM Autonomous Robotics Center` → `General Motors`;
  `NVIDIA GEAR Lab` → `NVIDIA`; `Autodesk Research` → `Autodesk`.
- Match case-insensitively against both `canonical_name` and every `also_known_as` value.
- Treat `Stealth`, `Self-employed`, `Freelance` and empty as UNRESOLVABLE. Do not create a
  company for them. Record `company_status: stealth` on the contact and move on.

### Step 0.2 — Classify each employer

| Result | Action |
|---|---|
| Already in `companies.md` | Cross-check (Step 0.3). Do NOT duplicate. |
| Missing, contact is in-ICP | Queue for Phase 2 enrichment |
| Missing, contact is `off_scope` | Skip unless the founder asked for the full sweep |
| Unresolvable (stealth/freelance) | Record on the contact, create nothing |

### Step 0.3 — Cross-check both directions, and reconcile conflicts

This is the step that pays. For every contact whose employer IS already mapped:

1. **Company → contact.** Does the company entry contain facts the contact card lacks — what
   they actually build, headcount, funding, `role`, `env_control`, or an explicit `ACTION`? If
   the company text contradicts the contact's `validation_rationale`, **the company entry wins**
   when it cites a fetched source and the contact card was written from a LinkedIn headline.
   Update the contact's `validation_rationale`, `tier` and `icp_fit`, and say so in `notes`.
2. **Contact → company.** Add a `known_contacts:` list to the company entry — `{contact_id},
   {name}, {role}, {outreach_status}` — so the map shows where a warm door already exists.
   `barrier_to_entry` almost always drops when a 1st-degree contact exists; re-score it.
3. **Orphan detection.** Flag any company whose entry names a person who has no contact card,
   and any contact whose employer entry names a different business than the profile implies.

Report every reconciliation to the founder explicitly. A silent correction to a contact's ICP
classification is how evidence ends up filed against the wrong assumption.

### Step 0.4 — Research the missing ones

Hand the queue from Step 0.2 to Phase 2 enrichment unchanged, with one addition: the
`rationale` for a Phase 0 company is the contact relationship itself, which always satisfies
the grounding rule because it is a verifiable fact about a real person:

> "Employer of {contact_id} {Name} (VP Global Strategy), 1st-degree connection accepted {date}."

Then run Phase 0.6 against the company's own site plus one secondary source, and fill the full
schema. Never infer `value_prop` or `works_on` from the contact's job title — fetch it. A company
added from a contact gets the same evidentiary standard as one found by an API, and it is exactly
the case Phase 0.6 exists for: a contact-sourced entry starts life describing one person's slice
of the company.

### Step 0.5 — Write back

- New companies → `companies.md`, full schema, `pain_score` from Phase 3.
- `known_contacts:` on every company that has one.
- Contact-card corrections → `contacts.md`, each with a dated `notes` line naming the company
  entry as the source.
- Regenerate the tracker.

---

## Phase 0.6 — Self-published source sweep (founder-set)

**Goal:** every company entry carries a `source_url` to the company's own words, and its mapping
dimensions match what the company publicly says it does. Free, no API key, no rate limit.

**Read `references/self-published-sweep.md` before running it.** Short version:

- **Sweep in priority order:** any company with no `source_url` first, then competitors and
  companies on the `stack_layer` the idea is entering, then any entry resting on a single
  informant. 90-day TTL — positioning moves slower than contracts.
- **Fetch the articles/newsroom index and the individual posts**, plus the named product page and
  the "About {company}" boilerplate. The homepage alone is the most abstracted page they own.
- **WebFetch first, browser second.** WebFetch fails on JS-rendered marketing sites by returning a
  near-empty page rather than an error — one word, a nav skeleton. That is a fallback trigger, not
  a finding. Dump every `<a href>` with `javascript_tool`, batch the article reads, close the tab.
- **Grade it as positioning, not verified demand.** Cheap-to-falsify facts (founding date, HQ,
  named investors and partners, disclosed round size) are usable; traction and market-position
  claims get quoted, not asserted. Record what is *absent* — no customers, no deployment count, no
  pricing is itself a finding. Never let an announcement set `deployment_maturity: production`.
- **When it contradicts an interview, keep both**, each labelled with source and date, and write
  the reconciliation into `entry_point`. Default reading is scope, not error: an informant
  describes the slice of the company they sit in. Compare publication dates against the call date.
- **`pain_score` is not touched here** — it is computed in Phase 3 from transactional signals only.

Report every changed mapping dimension in the run summary. A company moving from `seller_data` to
`integrator_deployer` is a competitive-position change, not a data cleanup, and the founder has to
see it. Competitors' own "why now" claims route to Phase 4 as `source_type: news`, `verdict:
ambiguous` — never enough on their own to move a thesis or a lane.

---

## Phase 1 — Discovery + tier assignment

**Goal:** produce a list of ~30-100 candidate companies operating in the assumption's space, each with a value-chain tier drawn from `icp_valid_tiers`.

### Step 1.1 — Derive search terms from the assumption

Read `references/keyword-derivation.md` for the full protocol. Short version: extract 4-8 technical noun-phrases the target segment would actually use in procurement documents, job descriptions, and grant applications. Filter out sales-speak, adjectives, verbs. Add regional variants where relevant.

Store the derived terms in `.intel-manifest.jsonl` at the start of the run so downstream steps use the same vocabulary.

### Step 1.2 — Decide which conditional APIs to fire

**Universal APIs run every time:**
- TED EU (`api.ted.europa.eu/v3`) — EU procurement
- UK Contracts Finder (`contractsfinder.service.gov.uk`) — UK procurement
- Adzuna (`api.adzuna.com/v1`) — job postings, tier signal from titles
- GLEIF (`api.gleif.org`) — LEI + parent entity resolution

**Conditional APIs fire only when the assumption context matches.** Read `references/api-catalog.md` for the full trigger table — each API card lists the assumption categories, ICP tier patterns, and text signals that make it relevant. Do not fire an API just because it's enabled — every wasted call is a rate-limit charge and a slower run.

**Two APIs have hard caps or default-off status the library MUST respect:**

- **Exa** — `enabled: false` by default in `api-registry.yaml`. Do not attempt to call unless the founder has explicitly re-enabled it after the "when to re-enable Exa" checklist in the api-catalog card. If the library sees Exa disabled, silently skip it — no error, no warning; the news fallback path just doesn't fire.
- **Adzuna** — capped at 50 calls/run + 200 calls/month + 30-day cache TTL + one call per unique company per run. All limits enforced by `intel_lib.query_adzuna()` reading `api-registry.yaml → adzuna.limits` before every call. If any cap is hit, remaining companies get `hiring: {}` and the manifest logs `hiring_skipped_rate_limit` — the run continues, it doesn't error.

Log which conditional APIs were selected and which were skipped (with reason) to the manifest. This makes reruns auditable.

### Step 1.3 — Fire the APIs

Use `scripts/intel_lib.py` (bundled with this skill). Every function returns a normalized list of dicts with a `source_url` field. Do not write anything to disk yet — the outputs are staged in memory (or scratchpad) until Step 1.5.

Discovery calls happen in this order to maximize dedup efficiency:
1. Procurement (TED EU, UK Contracts Finder) — highest-signal companies
2. Domain operator/asset databases — only those the assumption opted into via `domain_data_sources`
3. Filings (EDGAR full-text) — if applicable
4. Grants (SBIR, CORDIS) — if applicable
5. Adzuna — postings at companies already discovered above (existing-company lookup), THEN broad keyword search (to catch companies missed by procurement)

The library respects per-API rate limits and inserts backoff automatically. If any API returns nothing, log a `zero_results` entry with the exact query used, and continue.

### Step 1.4 — Clean names, deduplicate, resolve to canonical entities

**Step 1.4a — Clean raw names BEFORE dedup or GLEIF resolution.**

Different APIs return names in different polluted forms. Apply these strips in order to every name before it enters the dedup pass:

- **EDGAR** returns names like `"ALLIANT ENERGY CORP  (LNT)  (CIK 0000352541)"` — the ticker + CIK is metadata, not part of the name. Strip everything from the first `  (` onward: `ALLIANT ENERGY CORP`. Preserve the CIK separately as `edgar_cik` on the company record.
- **TED EU** occasionally returns names with contract-notice suffixes ("- Contract Award Notice"). Strip anything after ` - ` if it matches a known notice-suffix pattern.
- **UK CF** sometimes returns names with trailing procurement-body qualifiers ("Ministry of X, Rijksdienst voor Y") — these are actually ministry names, not operators. Filter them out entirely in Step 1.4b (below), don't try to clean.

If a name is a person's full name (first + last, no legal suffix), that's an EDGAR filer noise — skip.

**Step 1.4b — Filter out non-operator entities BEFORE tier classification.**

The following patterns must NEVER end up in `companies.md` regardless of what surfaced them. Filter at name-cleaning time and log to the manifest with `{"phase": "non_operator_filter", "name": ..., "matched_pattern": ...}`:

- **Mutual funds / investment vehicles / pension funds** — case-insensitive substring match on: `INVESTORS`, `FUND` (as standalone word), `HOLDINGS TRUST`, `CAPITAL PARTNERS`, `MULTI-ASSET`, `PENSION`, `SICAV`, `SIF`, `TRUST FUND`, `MASTER TRUST`, `DEFINED BENEFIT`, `DEFINED CONTRIBUTION`, `RETIREMENT TRUST`, `RETIREMENT PLAN`, `SAVINGS PLAN`, `ENDOWMENT`, `FOUNDATION` (when standalone — pattern seen 2026-07-08 A2: `"Dominion Energy, Inc. Defined Benefit Master Trust"` — a pension fund attached to a real utility, filter must strip the trust and NOT keep the plain company variant either, since the plain company also failed the second-signal rule)
- **Government agencies / ministries** — `MINISTRY OF`, `MINISTERIE`, `DEPARTMENT OF`, `AGENCY`, `RIJKSDIENST`, `AUTHORITY OF`, `COMMISSION OF`, `SECRETARIAT`
- **Financial holding companies** with no operating footprint — `HOLDINGS INC`, `GROUP INC` (unless ALSO surfaced as an operator by a real contract or an opted-in operator database)
- **Recruitment / staffing / consultancy firms** — these show up as EDGAR filers and TED contracting authorities but sell people, not operate assets:
  - `WARRIOR` (e.g. Ad Warrior Ltd — recruitment agency, observed 2026-07-08 A2 run)
  - `STAFFING`, `RECRUITMENT`, `RECRUITING`, `TALENT`, `RESOURCING`
  - `CONSULTANCY LTD`, `CONSULTING LTD`, `CONSULTANTS LTD`, `ADVISORY LTD`, `ADVISORS LTD`
  - `LEGAL LTD`, `LAW LLP`, `SOLICITORS`, `BARRISTERS`
  - `TECHNICAL LTD` (usually staffing e.g. HSB Technical Ltd — observed 2026-07-08)
  - `DIGITAL LIMITED`, `SERVICES LIMITED` (when standalone — these are usually IT/staffing houses)
- **Multi-industry sprawl** — a name that appears in EDGAR but the filer's SIC/industry code (when known) is banking / insurance / real estate / hospitality — filter regardless of textual match.

These names show up as EDGAR filers or TED contracting authorities but are NOT the operators of the assets. Adding them to the outreach registry pollutes the target list and misdirects tier classification. **Every filter drop must be logged** so a future run can audit whether a pattern was too aggressive.

**Exception override:** if the same name is ALSO surfaced independently by an operator database as a registered operator with actual assets, the operator signal wins and the filter is suppressed. Log `{"phase": "non_operator_filter_override", "name": ..., "reason": "operator_confirmed_by_{source}"}`.

**Step 1.4c — Deduplicate + resolve.**

Company names come back in many forms: "Mærsk", "Maersk A/S", "Maersk Power UK", "Mærsk UK Ltd". Left uncleaned, the same company appears three times in outputs.

Dedup runs in three passes:
1. **Fuzzy name normalization** — strip legal suffixes (Ltd, A/S, PLC, Inc, GmbH, Corp), diacritics, whitespace, punctuation. Group companies with identical normalized names.
2. **GLEIF resolution** — for each name group, resolve to LEI using the CLEANED name from Step 1.4a. Groups sharing an LEI collapse to one canonical entity.
3. **Parent lookup** — if a resolved LEI has a parent LEI, note both. The canonical entity is the parent; the subsidiary is stored under `also_known_as` so we can still map job postings and contracts back.

**Step 1.4d — Tier classification.**

Read `references/tier-inference.md` for the rules mapping API responses to tiers. Tiers are idea-defined: the code resolves each company to a structural **side** (demand / supply / competitor), then picks the assumption's declared tier on that side — it never hardcodes a tier name. Short version:

- **Contracting authority / operator / owner → demand side**, BUT only if confirmed by a second signal (hiring for relevant roles, or an operator registry). A single EDGAR mention or single contract award is not enough — that classifies too aggressively (see the AVIVA INVESTORS example on the 2026-07-08 A2 run).
- **Supplier / developer in a procurement record → supply side** → the assumption's first supply-side tier.
- **Operator in a domain operator-database → demand side** (strongest signal — the API attests operational role directly), when that domain source is opted in.
- **SBIR / CORDIS grant recipient → competitor** — surface for founder review, don't add to the outreach registry by default.
- **Hiring employer → side inferred from posted role title patterns** (see the reference card).
- **No second signal → `tier: other`** — do not default to a demand-side tier. `other` is valid and surfaces to the founder for manual review; over-classifying pollutes the outreach list.

The resolved tier always comes from the assumption's `icp_valid_tiers`. If the resolved side has no matching tier there, drop the company from this batch — even a real name is off-scope. The `icp_out_of_scope` field can eliminate additional matches (e.g., "no vendors", "no consultancies").

### Step 1.5 — Stage companies to `companies.md`

For each surviving canonical entity, write or update a row in `reports/{slug}/outreach/companies.md`:

- `company`, `linkedin_slug` (if inferable — otherwise empty for the targets skill to fill later), `tier`, `lei`, `parent_entity`, `also_known_as: [...]`
- `pain_score: null` (filled in Phase 3)
- `rationale` — a one-sentence factual statement of why this company was added, with the source. Examples:
  - "Contracting authority for £4.2M service framework awarded 2025-11-15 (UK Contracts Finder)."
  - "Listed as operator in a domain asset database with 847 units, average age 8.3 years."
  - "Supplier on 3 TED EU contracts in the last 24 months, total value €12.1M."

The rationale must be constructible from a specific API response with a URL. If you cannot write a factual rationale, do not add the company. This is the grounding rule expressed at the schema level.

Append new companies; update existing rows only if `tier`, `lei`, `parent_entity`, or `also_known_as` have changed. Never overwrite a rationale — instead append a new evidence line.

---

## Space mapping — the durable output

The registry is not a call list that gets consumed and thrown away. Over time it becomes a map
of the space this idea is entering, and the map is what shows where a new company can get in.

So every company block carries mapping dimensions, not just a pain score. Fill them for EVERY
company, including ones screened out — a screened-out company still occupies space on the map,
and knowing which layers are crowded is the point.

### The dimensions

Two of them are **idea-defined**: a value chain and a setting vocabulary are properties of the
market being mapped, not of the pipeline. Declare their value sets once in the registry's own
frontmatter (`stack_layers:` and `settings:`), then use only declared values. Everything else
below is structural and identical for every idea.

| Field | Values | What it tells you |
|---|---|---|
| `stack_layer` | **idea-defined** — the layers of this market's value chain, declared in `companies.md` frontmatter | Where they sit. Crowded layers are bad places to enter; empty ones are either an opportunity or a graveyard. |
| `value_prop` | one line, their words where possible | What they actually sell. Not what they say on a landing page — what a customer pays for. |
| `works_on` | task or problem, in the market's own words | The unit of work they are paid for. Determines whether this idea's approach or the incumbent one wins. |
| `works_at` | **idea-defined** — the settings this market operates in, declared in `companies.md` frontmatter | Where the work happens. Usually the single best predictor of how hard delivery is. |
| `buyer` | who signs the cheque | Often different from the user. Record the payer, not the user. |
| `business_model` | `product_sale` · `subscription` · `usage` · `services` · `data` · `licence` · `internal` | How money reaches them, which constrains who they can be to us. |
| `deployment_maturity` | `none` · `pilot` · `production` · `retreat` | `retreat` is the most valuable value in the whole schema — see below. |
| `industries` | list | The verticals they actually serve, from their own customer evidence. |
| `relationship` | `competitor` · `customer` · `partner` · `channel` · `informant` · `incumbent` | What they can be to us. A company can be two things; record both and say which dominates. |
| `entry_point` | free text, one line | The specific reason this company is a way INTO the space, or "none". This is the field the map exists to produce. |

### Why `deployment_maturity: retreat` matters more than the rest

A company that tried automation at scale and pulled back is the strongest signal available,
because the failure is documented, the people are still reachable, and nobody writes a press
release about it. When several companies retreat from the same problem in the same window, that
is a structural finding about the problem, not three separate execution stories — and it is
usually the most useful thing the registry will ever tell you.
Press releases announce successes, so a registry built only from news is systematically biased
toward companies whose pain is already SOLVED. Actively hunt retreats.

### Reading the map

Once ~20 companies carry these fields, three questions become answerable from the registry alone
and should be stated explicitly in the run summary:

1. **Which `stack_layer` has the most entries?** That is the crowded layer. Entering it means
   competing with everyone already listed.
2. **Which layer has entries only at `works_at: own_plant` or `lab`?** That is a layer nobody has
   made work in a customer environment, which is either the opportunity or the graveyard. Decide
   which by checking whether anyone tried and hit `retreat`.
3. **Where do `relationship: channel` and `relationship: customer` overlap?** A company that is
   both is a route to market, not just a logo.

Do not compute a score from these fields. They are a map, not a ranking, and collapsing them into
a number destroys the thing that makes them useful.

## Phase 2 — Company enrichment

**Goal:** for each company staged in Phase 1 (plus any existing companies without a fresh `assumptions.A{X}` block), gather deep intelligence and write `companies.md` (targeting fields).

### Step 2.1 — Check the cache

For each company, look at `companies.md` (targeting fields) → `{Company}` → `assumptions.A{X}.run_date`. If it's less than 30 days old, skip enrichment for this company on this assumption. The company still appears in the run summary, just as `cached`.

The cache exists because contracts don't materialize weekly and news within a month rarely adds new hooks. If the founder wants a forced refresh, they invoke with `--refresh`, which zeroes the manifest for the target assumption.

### Step 2.2 — Fetch enrichment signals

For each non-cached company, run the applicable API calls in parallel where possible. `scripts/intel_lib.py` (bundled with this skill) provides an `enrich_company(name, lei, tier, assumption_ctx, phase1_hits)` function that orchestrates:

- **Contract history** — **REUSE from Phase 1 discovery** (contracts already fetched via keyword-scoped TED/UK CF; keep them in memory between phases keyed by canonical company). Only fire a *second* per-company scoped call if Phase 1 returned fewer than 2 contracts for that company — otherwise pass the discovery contracts through unchanged. Returns: `[{title, value, currency, date, role, counterparty, source, source_url}, ...]`
- **Vertical signals** — none. A source named in `domain_data_sources` is fetched only if an adapter for it is registered in `intel_lib.DOMAIN_ADAPTERS`, and none is; a name with no adapter is logged to the manifest rather than silently skipped. See `api-registry.yaml`'s domain-specific section before adding one.
- **Company news** — GDELT (`api.gdeltproject.org/api/v2/doc/doc`) primary. Exa is DEFAULT OFF (see api-catalog card for the re-enable checklist). Filtered to last 6 months. Returns: `[{title, date, url, source}, ...]` — max 5 items sorted by date desc.
- **Hiring signal** — Adzuna scoped to this company + assumption keywords. **GATE BY SIDE**: fire only for in-market tiers (any `demand` or `supply` side tier from `icp_valid_tiers`). Skip `competitor` / `expert` / `other` — those companies don't post the roles the assumption is about. Skipping them reclaims ~30% of the Adzuna budget for real targets. Returns: `{postings_count, top_titles, source_url}`.
- **Filings mention** — EDGAR full-text if the company is US-listed and the assumption has attested-pain framing. Reuse Phase 1's EDGAR hits when the company was already surfaced by EDGAR. Returns: `[{form_type, filing_date, excerpt, source_url}, ...]`.

**Removed from Phase 2 (as overkill):** Companies House lookups. The identity fields (company_number, incorporated, sic_codes) are nice-to-know but do not change the discovery-priority hierarchy. Killing this cut ~1 call per UK company. If needed for tier-confirmation in edge cases, run it manually via `intel_lib.query_companies_house()` — do NOT re-add it to the default enrichment loop.

Every returned dict includes a `source_url`. If a call returns empty, the field is written empty in the output — never inferred, never guessed.

### Step 2.2b — Skip enrichment for garbage-tier companies

Before firing ANY enrichment API for a company, verify the company is worth enriching. Skip the whole enrichment loop for a company if any of these hold:

- `canonical_name` still contains ticker/CIK garbage after Phase 1 name-cleaning (e.g. `"XYZ CORP  (TIC)  (CIK 0000...)"` — cleaning should have run, this is a fallback)
- `tier: other` (unresolved — surface to founder for manual classification, don't waste API budget)
- Company name matches a `mutual_fund / holding_fund / pension_fund / ministry / agency` pattern (regex list in `intel_lib.NON_OPERATOR_PATTERNS`) — these show up in EDGAR filings but aren't operators
- Company name is nothing but a person's name (`^[A-Z][a-z]+\s+[A-Z][a-z]+$` — first + last name only, no legal suffix) — Phase 1 mistake, log for founder review

Log the skip: `{"company": "...", "phase": "enrich_skipped", "reason": "..."}`. This lets a rerun show exactly why the enrichment loop declined to spend on that company.

### Step 2.3 — Write to `companies.md` (targeting fields)

For each enriched company, append or update the `assumptions.A{X}` block. See `references/output-format.md` for the exact schema. Key rules:
- One block per assumption per company — never overwrite an existing block; a rerun replaces it in-place with the new payload but keeps the block ID.
- Non-assumption-scoped fields (fleet, gleif_lei, parent_entity, tier, sic_codes) live at the top of the company section — set once, updated only when the underlying data changes.
- Empty fields are written as empty strings / empty lists — never omitted, so downstream readers can see what was checked.

Log a manifest entry per company: `{"company": "...", "assumption": "A2", "phase": "enrich", "apis_called": [...], "results_count": {...}, "run_date": "..."}`.

---

## Phase 3 — Pain scoring + registry finalization

**Goal:** produce a `pain_score` per company, sort `companies.md` by it, and write a summary table at the top of `companies.md` (targeting fields).

### Step 3.1 — Compute pain_score

For each company, read its `assumptions.A{X}` block and compute:

```
pain_score = contract_score        (0-3, based on contract recency, count, value)
           + hiring_score          (0-2, Adzuna postings_count, log-scaled)
           + news_score            (0-1, 1 if any news in last 6 months, else 0)

clamp to 1-10.
```

Read `references/output-format.md` for the exact scoring formulas. Score is computed by `intel_lib.score_company()` — do not implement inline, use the library so scoring is consistent across runs and reproducible.

If a scoring component doesn't apply (e.g., no fleet API for a non-energy assumption), it contributes 0 and the max drops accordingly — clamp to 1-10 after.

### Step 3.2 — Update `companies.md`

Write `pain_score` back to each row. Sort `companies.md` by `pain_score` descending, then by `tier` (buyer tiers first). This is the sort order the targets skill uses when picking which companies to search LinkedIn against first.

### Step 3.3 — Write a summary at the top of `companies.md` (targeting fields)

Under the frontmatter, write a Markdown table summarizing this run:

```markdown
## Run summary — A{X} · {YYYY-MM-DD}

| Rank | Company | Tier | pain_score | Top signal |
|------|---------|------|-----------|-----------|
| 1 | Example Operator A | {demand_tier} | 9 | £4.2M service framework awarded Nov 2025 |
| 2 | Example Service Co | {supply_tier} | 8 | 12 operational-pain events in Q4 2025 |
...
```

This gives the founder an at-a-glance view of what the run found without having to scroll through per-company blocks. The table always reflects the latest run — regenerated each pass, never appended to.

### Step 3.4 — Regenerate the contact tracker

If `contacts.md` exists, regenerate the founder's contact dashboard so the two stay in sync:

```bash
python3 scripts/build_control_room.py {slug}
```

The tracker renders `contacts.md` only. `companies.md` are read directly as markdown — they are the intel deliverable, not an input to the HTML. Write them well enough to be read as-is.

The script is idempotent and safe to run repeatedly. If `contacts.md` doesn't exist yet (intel running before any outreach cycle), it prints a skip notice and writes nothing — that is expected, not an error.

---

## Phase 4 — Write to the evidence ledger

**Goal:** turn the raw API responses already in memory (from Phases 1-2) into claim-level entries in `reports/{slug}/03-validation/evidence.md` — the single source of truth for what we know about the active assumption, across API + interview evidence.

This phase absorbs what used to be `/startup-validate-assumption`. Same APIs, same input, one pass — no double-hitting rate limits.

### Step 4.1 — For each signal type, write one entry per meaningful hit

Evidence entries follow `schemas/evidence.md`. The library iterates over the data already staged in memory:

| Signal source | One entry per… | Suggested `verdict` inference |
|---|---|---|
| Contract (TED / UK CF) — this company is the buyer | contract | `supports` if the contract is on-scope for the assumption; else `ambiguous` |
| Contract (TED / UK CF) — this company is the supplier | contract | same (multiple suppliers named on one contract = one entry per) |
| EDGAR filing excerpt | filing | `supports` if the excerpt describes the pain; `contradicts` if it names the pain as already-solved |
| GDELT / Exa news article | article | `ambiguous` by default — news is descriptive, not attesting. Library flags articles matching the assumption's disconfirmation vocabulary as `supports` or `contradicts`. |
| Opted-in operational-pain source, event window | 6-month window per company | `supports` if aggregate events exceed the assumption's stated pain threshold |
| Adzuna hiring window | 30-day window per company | `supports` if postings named a role that the disconfirmation clause references |
| SBIR / CORDIS competitor grant | grant | `contradicts` (someone else is already funded to solve this) — but note the competitor is a signal that the pain exists |
| Opted-in fleet / asset source | company | `supports` if the asset scale meets the assumption's ICP threshold; otherwise omit (scale is context, not evidence) |

Each entry uses the schema fields verbatim:

```yaml
- id: E{N}                     # monotonic across the file — read existing max first
  date: {date}
  source: "UK Contracts Finder — Mærsk A/S"
  source_type: procurement     # procurement | filing | news | job_post | grant | market_report
  source_url: https://contractsfinder.service.gov.uk/notice/abc-123
  claim: >
    Mærsk awarded a £4.2M framework for {inspection task} services
    to {Vendor Co} on 2025-11-15.
  assumption_linked: A2
  verdict: supports
  confidence: 4                 # library assigns using quality hierarchy in schemas/evidence.md
  notes: "Framework runs 2025-2028; multi-year budget commitment materially attests pain exists."
  next_question_raised: "Is the £4.2M spread evenly across the 3 years, or front-loaded to Y1?"
  intel_run_ref:                # cross-link back to the intel invocation
    company: Mærsk A/S
    company_id: CO1
    api: uk_contracts_finder
```

The `intel_run_ref` block is the traceability link so a synthesis skill can jump from evidence entry → back to the exact company block in `companies.md` (targeting fields).

### Step 4.2 — Confidence assignment (from evidence quality hierarchy)

The library assigns `confidence` using the hierarchy in `schemas/evidence.md`:

- **Strong (4-5):** contracts with named counterparty + budget, EDGAR filings quoting the pain, an opted-in operational source's aggregates over the pain threshold, SBIR/CORDIS grants awarded to competitors
- **Medium (3):** hiring windows with named roles, contracts without counterparty (e.g. frameworks at issue time), news articles that name specific behaviours
- **Weak (1-2):** generic news mentions, fleet context, aggregate market data

Never assign 5 to a single API response — that reservation is for interview evidence + independently confirmed procurement.

### Step 4.3 — Deduplication

Before writing, check if an entry for the same `(source_url, assumption_linked)` already exists in `evidence.md`. If yes, update in place (refresh the date, verdict, and confidence if changed); if no, append with the next `E{N}` id. This makes the intel skill safely rerunnable — a 30-day cache hit produces zero new entries.

### Step 4.4 — Update the assumption node's confidence in `graph.md`

After writing evidence entries, recompute the assumption's rolled-up confidence and update the corresponding node in `graph.md`. Formula lives in `schemas/assumptions.md`. The library only touches the confidence field — never overwrites the assumption text, ICP, or disconfirmation.

---
