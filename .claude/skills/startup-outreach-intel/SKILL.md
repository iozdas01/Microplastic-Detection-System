---
name: startup-outreach-intel
description: >-
  Runs enabled data sources for one assumption and produces optional company intelligence plus API-derived validation evidence. Use when the founder asks to find or enrich target companies, prioritize outreach with company-level signals, or validate an assumption with external APIs. Also use whenever the founder hands over a company's own URL or site, says a link "should be added to the companies", asks what a company actually does or sells, or wants a company entry checked against its public record — Phase 0.6 reads the company's own articles and product pages into its `companies.md` entry, needs no API keys, and reconciles the result against any interview already on file. It is not a prerequisite for LinkedIn outreach.
---

# Startup Outreach Intel

## GLOBAL by default — never UK-only, never single-region

**This skill is global, not regional.** The founder's ICP for any assumption is a MULTI-COUNTRY target list unless the assumption explicitly restricts it. Every API call that has a country/region parameter MUST select the country based on the target company's own country of operation — not a hardcoded default.

Concrete rules:
- **Adzuna calls** must route by company country: US companies → `country=us`, German → `de`, Danish → `dk`, etc. See the country dispatch table in `api-catalog.md` → adzuna card. Never hardcode `country=gb` at the library level.
- **Discovery keywords** must include vocabulary from EVERY target region:
  - Procurement vocab from the target geography, in that market's words
  - Operator/practitioner vocab from the target geography
  - Never present only one region's vocabulary — Claude at derivation time MUST list keywords in all target-region forms.
- **News allowlist** must include outlets from every target region. `NEWS_DOMAIN_ALLOWLIST` in `intel_lib.py` is a starting set — extend it with this idea's own trade press, per region, before the first enrichment run.
- **When a company you know is real and active enriches to zero signals**, suspect a routing bug before concluding "no signal exists" — the enrichment call probably went to the wrong country's index.

Failure mode this guards against: library-default keywords in one market's vocabulary return nothing in another's, and the run reports an empty result rather than a vocabulary mismatch.

## Single entry point for API-driven work on an assumption

One invocation queries every relevant enabled API, then writes to three files at once:

1. `reports/outreach/companies.md` — company registry: tiers, pain scores and the
   per-company signal blocks that drive both targeting and message personalisation
2. `reports/03-validation/evidence.md` — claim-level entries for the validation ledger
   (drives assumption confidence updates)

The same TED / EDGAR / GDELT / SBIR call feeds all three destinations — pay once, write everywhere. This replaces the retired `/startup-validate-assumption` (whose logic is absorbed here) and supplies the evidence that `startup-outreach-targets` uses for discovery and contact enrichment. `startup-outreach-draft` then verifies each message claim against the contact's live profile before drafting. Nothing is hardcoded to any industry — routing is driven by the assumption's `category` field and `icp_valid_tiers`.

## Why this skill exists

The outreach pipeline used to start with a hand-picked `companies.md`. That works for the first idea and breaks for every idea after — the founder can't know every company in every space, and even in a familiar space, "who's actually under pain right now" is not the same as "who I remember." This skill replaces guesswork with API-grounded evidence:

- **TED EU + UK Contracts Finder** name real contract buyers AND suppliers, giving both sides of the market from one query.
- **EDGAR** names owners and legally-attested buyers.
- **Adzuna** names companies actively hiring for the role the assumption is about.
- **GLEIF** resolves every discovered name to its parent entity so we don't waste outreach on subsidiaries.
- **GDELT + Exa** enrich each company with recent news and operational pain.
- **Any source the assumption opted into** via `domain_data_sources:` in `graph.md` — the one
  gate for vertical-specific sources. An idea that declares none never calls them, which is
  what keeps this skill industry-agnostic.

Every field in every output is backed by a source URL. If an API returns nothing, the field is left empty — never filled from model knowledge. Bad company intelligence produces false-flag hooks the contact can immediately disprove; empty fields degrade gracefully to generic outreach.

## Load before starting

1. **The active assumption** — `reports/02-assumptions/graph.md`, node `id: A{X}`. Read fields: `assumption`, `category`, `icp_segment`, `icp_valid_tiers`, `icp_out_of_scope`, `disconfirmation`. If any of the first four are missing, STOP and ask the founder to declare them before running the skill.
2. **API registry** — `api-registry.yaml` at repo root. Only APIs with `enabled: true` will be called. Some APIs need credentials (Adzuna, Companies House, Exa) — the library skips them cleanly if env vars are missing.
3. **Existing `companies.md`** — `reports/outreach/companies.md` if it exists. Companies
   already enriched within the last 30 days for THIS assumption are skipped (cache); new
   companies are appended, and existing rows are updated in place when their `pain_score` changes.

If input 1 is missing, stop and ask. Everything else is optional — the skill creates it if missing.

## The four phases

The skill runs four sequential phases. Each phase is idempotent — rerunning it should produce the same output modulo new data appearing at the sources. Each phase writes to a manifest file at `reports/outreach/.intel-manifest.jsonl` so a rerun knows what was already done.

| Phase | What it produces |
|---|---|
| 0. Contact harvest | Employers of everyone in `contacts.md` reconciled against `companies.md` |
| 1. Discovery + tier assignment | Draft `companies.md` (new companies staged with tier + rationale) |
| 2. Company enrichment | `companies.md` (targeting fields) populated with per-assumption signal blocks |
| 3. Pain scoring + registry finalization | `pain_score` + `top_signal_for_copy` on every company; summary table + dashboard regen |
| 4. Evidence ledger write | Claim-level entries in `reports/03-validation/evidence.md` |

Under normal use, all phases run in one invocation. Phases can be run independently via the CLI (see Invocation examples). See `scripts/intel_lib.py` (bundled with this skill) for the phase orchestrators.

---

## Grounding rule — no hallucinations, ever

Every field in every output file must be backed by an API response in the current session. The output schema requires a `source_url` (or equivalent) for every field that could conceivably be hallucinated. If an API returns nothing:

| Case | Action |
|---|---|
| Contract search returns zero | `contracts: []` — never invent a plausible one |
| GDELT + Exa both empty | `news: []` — never fill from training data |
| GLEIF has no record | `gleif_lei: ""`, `parent_entity: ""` — do not guess |
| An opted-in domain source has no record | omit that source's block entirely — never infer its numbers from elsewhere |

The rationale for this rule: the whole point of API-grounded outreach is that the founder can send a message referencing a real contract and the contact will confirm it exists. A fabricated hook the contact can immediately disprove destroys trust worse than a generic message would.

---

## Idempotency + rerun behaviour

The skill is designed to be rerun freely. Rerun semantics:

- **Same assumption, same day, no data changed** → no-op. Cache hits everywhere. Manifest logs a `no_change` run.
- **Same assumption, 30+ days later** → refetches enrichment for every company. Contract history and news get refreshed; static fields (LEI, parent, fleet baseline) are updated only if changed.
- **New assumption on same idea (different A_ID)** → for each existing company, appends a new `assumptions.A{X}` block. Universal identity fields are reused from the cache — no re-fetch of GLEIF etc.

The `--refresh` flag zeroes the manifest for the target assumption and forces a full re-enrichment. Use sparingly — it's expensive.

---

## Connecting downstream

This skill's outputs feed two skills + one dashboard:

**`startup-outreach-targets`** may read `companies.md`
when this optional skill has been run. It uses `pain_score`, parent mappings,
and company-level signals for prioritization, but it can run entirely from
LinkedIn searches and live profile evidence when those files do not exist.
See `startup-outreach-targets/references/enrichment.md` → Step 0 for the
optional field mapping.

**`startup-outreach-draft`** consumes the enriched contact record produced by `startup-outreach-targets`, but treats company-level signals only as discovery context. Before drafting Msg 1, it reopens the contact's live LinkedIn profile and makes every `{work_context}` claim traceable to that fresh snapshot; it never treats cached `companies.md` (targeting fields) as message evidence.

**`companies.md` are read as markdown** — there is no HTML view of them, so they are the founder-facing artifact themselves. Order fields so the highest-signal ones (contract values, {operational-loss signal}, hiring surges) lead each company block, and keep every claim's `source_url` inline: the file has to be scannable without a renderer.

**No other skill writes to `companies.md` or `companies.md` (targeting fields).** These are exclusively populated by this skill. Downstream skills are read-only consumers.

---

## What this skill does NOT do

- Does not browse LinkedIn — that's `startup-outreach-targets`. This skill never opens the browser.
- Does not write outreach messages — `startup-outreach-targets` owns contact discovery, `startup-outreach-draft` owns Msg 1, and `startup-outreach-reply` owns approved follow-ups. This skill produces the raw evidence used to find and prioritise relevant contacts.
- Does not capture interviews — that's `startup-interview-capture`.
- Does not decide which assumption to work on — that's a founder call. This skill runs against whatever assumption ID the founder passes.
- Does not fabricate. If an API is disabled or missing credentials, its output slot in the intel file is empty. Empty is a valid state.

---

## Reference files

- `references/api-catalog.md` — one card per API: endpoint, params, response shape, when to fire, what it tells us about tier
- `references/keyword-derivation.md` — protocol for deriving procurement search terms from assumption text, with worked examples across multiple domains
- `references/tier-inference.md` — rules for mapping API responses to `icp_valid_tiers` — the discipline for "this company appeared here → therefore they are tier X"
- `references/self-published-sweep.md` — Phase 0.6 mechanics: which companies to sweep, which pages to fetch, the WebFetch→browser fallback, how to grade company-authored material, and how to reconcile it against an interview without overwriting either
- `references/output-format.md` — exact YAML schema for `companies.md` (including the targeting fields merged in from the retired `companies.md` (targeting fields)), plus the pain_score formula

## Bundled scripts

- `scripts/intel_lib.py` (bundled with this skill) — Python library + CLI. Every API call goes through here. All rate limiting, retries, GLEIF resolution, dedup, and scoring live in the library — never re-implemented inline. If the founder wants to add a new API, they add a function to `intel_lib.py` and a card to `api-catalog.md` — nothing else changes.

## Mechanics

Phase mechanics, output templates and the failure catalogue live in `references/phases.md`;
Phase 0.6's sweep procedure lives in `references/self-published-sweep.md`. Read the section
for the stage you are running.

## Testing

This skill calls external APIs and depends on live credentials, so skill-creator evals are
not run for it (repo rule: no evals for external-API skills). Test manually against a live
assumption with credentials set, verify `companies.md` is populated with real data plus
source URLs, then verify the downstream skills read the new fields.
