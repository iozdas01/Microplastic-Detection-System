# Startup Assumption Lab — Architecture

_Durable design reasoning. Structure derivable from the repo — field lists, vocabularies,
skill inventories — is not restated here; it lives in `schemas/`, `api-registry.yaml`, and
the skill definitions. Version history is git's._

---

## The Core Insight

A startup idea is not one thing. It is a bundle of assumptions.

The system's job is not to evaluate static ideas. Founder onboarding first confirms a durable
belief and one falsifiable initial hunch beneath it. The shotgun examines that same pair
through multiple methods, then the assumption layer finds the cheapest evidence that could
kill or confirm its claims. Evidence normally changes the hunch before it changes the belief.

## The Loop

```
Founder onboarding (belief only — never a hunch)
         ↓
Belief (stable)
         ↓
Shotgun EXPLORE (recon → jobs/substitutes → segment/wedge)
         ↓
2-4 proposed hunches → founder picks one
         ↓
   active Hunch (mutable, untested)
         ↓
Ideation shotgun TEST (public signals + curated methods on the same pair)
                          ↓
Assumption extraction → prioritize → select the riskiest
                          ↓
Test: historical validation → market signals → substitutes → customer calls → technical
                          ↓
Evidence → grade → update confidence
                          ↓
Retain / branch / mutate / retire the hunch → shotgun again when needed
```

The methods library feeds three points: forming the first hunch when the founder has a
belief but no hunch, the first test of that hunch, and reframing after evidence moves it.
The last two examine one explicit belief/hunch pair.

**A belief with no hunch is a first-class state, not an error.** It was the pipeline's
sharpest edge: the only entry point ran a six-method elicitation funnel designed to *find*
a belief, so a founder who already had one was interrogated for something they were holding,
and the shotgun refused to run at all until a hunch existed — which pushed them into
inventing one. An invented hunch is worse than none, because the entire shotgun then aims
at it and the narrow/branch budget is spent correcting a guess rather than finding a claim.
The data model already permitted the hunchless state (`vocab:hunch_status` declares
`proposed`; `build_brief.py` renders `active_hunch: none`); only the two skills forbade it.

---

## The 5 Modules

### 1. Belief and hunch lineage
The belief is founder-owned and changes only with explicit confirmation. Onboarding writes
the belief and an empty lineage; **every hunch, including the first, comes from the shotgun**
in explore mode, proposed as `status: proposed` from a real corpus. Only the founder promotes
one to `active`.

Splitting it this way is a founder decision (2026-08-20) and it costs nothing to honour: the
first hunch used to be authored at the moment the founder knew least about the market, then
inherited by every downstream stage as the thing being tested. Proposing it from evidence
instead means the shotgun's first run discovers rather than confirms. Hunches then form a lineage: evidence can retain the
current hunch, propose a child with a different mechanism, propose a sibling for a new
segment, or retire it. Every replacement needs founder confirmation. Format: `schemas/hunch.md`.

### 2. Assumption graph
One per idea, structured as a DAG rather than a flat list: some assumptions gate others, and
if a parent fails its children dissolve instead of needing their own test. Always test root
nodes first — do not validate autonomy assumptions before confirming a pain exists.

Every node carries the cheapest test that would settle it, an explicit disconfirmation, and a
stop rule, so "inconclusive" is a decidable state rather than drift.

Three assumptions are mandatory for any idea: **why now** (what changed in the last 12–36
months — timing failures are the most common death for companies with correct market theses),
**is the pain real and expensive**, and **does this team have a path to this market**.

Fields: `schemas/assumptions.md`. Vocabularies: `schemas/vocabularies.yaml`.

### 3. Evidence ledger
Every claim links back to a specific assumption; an entry that cannot name the assumption it
moves, and the direction, is not ready to log.

**One hand-assigned grade:** the per-entry `confidence` 1–5. Assumption-level strength (best
entry, entry count, verdict split, and a low/medium/high confidence) is **derived** by
`scripts/idea.py` and rendered into the brief and dashboard. Three parallel ladders and three
reconciliation maps used to exist here; they drifted, so grading happens once, on the entry.

Fields: `schemas/evidence.md`.

### 4. Methods library
Ideation and validation methods extracted from articles and frameworks. `methods/ideation/`
is the shotgun's pool; every card outside it carries `excluded_because:` — why it cannot be
shotgun-run.

That "why not" is load-bearing: an agent handed a card it cannot run does not report that it
cannot run it. It produces a fluent, well-formed, entirely invented result, indistinguishable
from evidence by synthesis time.

Card fields: `schemas/method.md`. Routing: `methods/shotgun-routing.yaml`. The pool and every
exclusion: `methods/index.md` (generated by `scripts/build_methods_index.py`).

### 5. Thesis evolution log
Each mutation writes a new versioned file — not a git diff, but a readable before/after naming
the evidence that forced the change. Versioning rather than overwriting is what lets a later
session see that a belief survived three mechanism changes, which a diff cannot show.

Fields: `schemas/thesis.md`.

---

## Folder Structure

> **Cold by default.** Skip at session start; read before creating a file type you have not
> created before, or when deciding where a new artifact lives.

Three tiers: **root config + docs** (no global "current state" file), **reusable libraries**
(content that lives across ideas), and **per-idea outputs under `reports/{slug}/`**.

```
  ARCHITECTURE.md  CLAUDE.md  README.md  api-registry.yaml  founder.md

  /schemas/               one file per artifact type + vocabularies.yaml + copy-rules.md
  /input-context/{slug}/  belief.md (the pipeline seed) + dated raw snapshots
  /methods/               index.md (generated), shotgun-routing.yaml, and the card folders:
                          ideation/ (the pool) · validation/ · mutation/ · intake/ ·
                          practices/ · unused/
  /founders/              durable per-founder record; founder.md indexes both
  /private/               GITIGNORED first-party dumps holding other people's data —
                          linkedin-export/ is read by scripts/data/linkedin_export.py.
                          Never commit, never quote a connection or message into an artifact
  /signals/gaps-log.md    cross-idea pre-idea observations; feeds the loop, not produced by it
  /memory/MEMORY.md       shared founder preferences + cross-idea process decisions only
  /scripts/               idea.py (the one loader) · build_brief.py · build_control_room.py
                          · build_methods_index.py · validate_repo.py · validate_skill_catalog.py
                          · audit_target_list.py · data/ (one module per source) · hooks/
  /content/x/             cross-idea publishing queue + voice profile (never per-idea state)
  /tests/  /infra/        unit tests; optional self-hosted services
  /.claude/skills/        canonical skill definitions   /.agents/skills/  Codex bridges
```

One tree sits outside all three tiers:

```
  /research/              The market-evidence pipeline that produced the active idea —
                          collectors, models and HTML reports, self-contained with its own
                          scripts/, data/, reports/ and README. Path-anchored to its own
                          root, so it runs unchanged from where it sits.
```

`research/` is deliberately not folded into `reports/{slug}/`. It is a measurement pipeline,
not a per-idea artifact: it re-runs against live sources, it produced the evidence that
*chose* the current idea, and it would survive the idea being killed. What crosses the
boundary is graded ledger entries citing its files — never a number quoted straight out of it.

Per idea, under `reports/{slug}/`:

```
  BRIEF.md              GENERATED session entry point — read first, never edit
  control-room.html        GENERATED
  /01-ideation/         hunch-lineage.md (LIVING) · {date}-shotgun.md · methods/{run-id}/ ·
                        recon/{run-id}/
  /02-assumptions/      graph.md (LIVING) · {date}-extraction.md
  /03-validation/       evidence.md (LIVING) · {A_ID}-{date}/interviews/
  /04-mutation/         offerings.md (LIVING) · thesis-v{N}.md · {date}-mutation.md
  /outreach/            contacts.md, companies.md, research-map.md (LIVING) ·
                        results-{A_ID}.md (GENERATED) · copy/ · email/{campaign}/
```

`reports/lifecycle.yaml` is the one authored slug → `active`/`dormant`/`superseded-by` index.
It deliberately records no findings and no hunch ID: the hunch has exactly one author
(`hunch-lineage.md` frontmatter), which makes a lifecycle-vs-lineage contradiction
unrepresentable rather than merely fixed.

**The core rule:** every per-idea output goes into `reports/{slug}/`. Reusable libraries live
at root. `outreach/` sits outside the numbered stages because it is a relationship layer
spanning validation cycles — a contact found testing A1 may surface A5 later.

**Living vs point-in-time.** Living artifacts update in place; dated or versioned artifacts
are never overwritten.

**Two encodings, and no third.** (1) *YAML-block artifacts* — frontmatter plus a YAML list in
the body (`graph.md` unfenced from `assumptions:`, `evidence.md` and `offerings.md` fenced).
(2) *Record files* — `## Heading` sections of `key: value` lines with folded scalars (`>`),
inline `[a, b]` lists and one level of nested mapping (`contacts.md`, `companies.md`,
`transaction-map.md`). Both are parsed by `scripts/idea.py`, the single parsing authority. A
new encoding means a new parser and a new class of silent bug — there were three parsers once,
and the one the dashboard used discarded every folded scalar in `contacts.md`.

**Every artifact declares its own purpose.** A `purpose:` line in frontmatter says what fact
the file authors. `build_brief.py` renders those into the brief's `What already exists`
inventory, so a session can answer "does a file already cover this?" from the entry point.
Nothing is registered in the generator — a new artifact appears the moment it exists.

### Naming discipline

- The idea slug is one lowercase-hyphenated string, identical in `input-context/` and `reports/`.
- Dated files use ISO `YYYY-MM-DD`.
- Files in `input-context/{slug}/` get descriptive names — subagents identify raw material by filename alone.
- Every living artifact opens with `purpose:`.

### Artifact schemas

| File | Defines |
|---|---|
| `schemas/hunch.md` | Belief format + hunch lineage entries |
| `schemas/assumptions.md` | Assumption node format + the lexicographic ranking procedure |
| `schemas/evidence.md` | Evidence ledger entry + the one grading scale |
| `schemas/method.md` | Method card format + canonical categories |
| `schemas/thesis.md` | Thesis version format |
| `schemas/contact.md` | Contact card format + scoring |
| `schemas/interview.md` | Interview note format (raw + structured halves) |
| `schemas/synthesis.md` | Per-assumption synthesis + four-outcome decision tree |
| `schemas/offerings.md` | Offering format + the citation rule that keeps the set honest |
| `schemas/copy-rules.md` | The outreach copy contract and Claude's send boundary |
| `schemas/vocabularies.yaml` | **Every controlled vocabulary and derivation map.** Referenced as `vocab:{name}` |

Two artifacts are authored by the skill that owns them rather than by a file here, because
their *fields* are idea-defined and only their shape is fixed: `companies.md`
(`startup-outreach-intel` → `references/output-format.md`) and `research-map.md`
(`startup-paper-mine` → `references/batch-format.md`). Both declare their own value sets in
their own frontmatter. That is the rule, not an exception to it — see the `tier_side` entry
under load-bearing choices.

---

## Load-bearing choices — do not "simplify" these

Each looks like a removal candidate until you know why it is there.

- **Per-card `excluded_because:` plus the deleted-card ledger** — makes a deliberate exclusion
  distinguishable from an oversight, which is the difference between a curated pool and a pile.
- **`infra/firecrawl/`** — six containers for one source. Reddit blocks unauthenticated search
  from non-browser clients, and the PRAW path needs API approval this project does not expect;
  the self-hosted stack is what makes Reddit reachable keylessly, and Reddit is half the Public
  Signal Reconnaissance corpus. **Cold by default:** kept in the repo, not kept running. Bring
  it up when a shotgun run is planned; between runs `community_recon` degrading to Hacker News
  only is the expected state, not a failure. Do not delete it without replacing the Reddit half.
  Operating instructions: `infra/firecrawl/README.md`.
- **The `gap:` protocol's one-line reply** — the method depends on capture being frictionless.
- **Worktree sparse-checkout** — enforces no-cross-idea-bleed at the filesystem layer rather
  than by instruction.
- **The living-vs-dated split** and the `reports/{slug}/` rule.
- **`tier_side` as the only market vocabulary anything routes on.** Tier *names* are declared
  per idea in each assumption's `icp_valid_tiers`; the four sides (demand, supply, competitor,
  expert) are the only part global code may branch on. The predecessor repo instead declared a
  vertical's value chain globally — eleven vocabularies naming that market's layers and roles,
  plus the dashboard tabs that rendered them — and every one of them was per-idea state living
  in a shared file. A vertical's own axes belong in that idea's own artifact frontmatter
  (`companies.md`, `research-map.md`), never in `schemas/` and never in a generator.
- **`api-registry.yaml`'s "nothing aspirational" rule** and the `domain_specific` opt-in gate.
  A source fires only for an assumption that named it in `domain_data_sources`, so a vertical
  adapter can exist here without any idea that did not ask for it ever calling it. **The gate
  is what is load-bearing, not any adapter behind it** — and it currently holds none
  (`intel_lib.DOMAIN_ADAPTERS` is empty, by design). The two that used to sit here were the
  predecessor idea's wind sources: dormant, unnamed by any live idea, and dragging their
  vocabulary and scoring plumbing through shared code that every idea reads (founder decision,
  2026-08-20). An empty gate demonstrates the rule better than a stocked one. Keep the gate —
  remove it and the framework stops being industry-agnostic — and register an adapter only when
  a live idea's market actually needs it.
- **Generated artifacts committed to git**, with a `merge=keep-ours` driver — a generated file
  that is absent from a fresh clone is a file nobody reads.

---

## Customer Development Pipeline

Extends the loop with outreach → interview → synthesis. Formats: `schemas/contact.md`,
`schemas/interview.md`, `schemas/synthesis.md`, `schemas/copy-rules.md`.

**Contact taxonomy** — three orthogonal tags: `signal_type` (how they were found),
`contact_role` (what they can validate), `assumptions_tested` (one contact can inform several).
The first two are weighted: a practitioner who volunteered the pain in public is worth more
than a buyer who merely matches the ICP on paper.

**Evidence scoring** — the weights, formula, synthesis threshold and early-kill rule are
declared once in `schemas/vocabularies.yaml`. `outcome_modifier` is the one manual
classification per interview: the capture skill proposes it with reasoning, the founder
confirms. Everything else derives from tags already on the card.

**Synthesis** fires at the declared threshold and picks one of four outcomes —
`next_assumption`, `new_vertical`, `mutate_thesis`, `kill`. An early-kill flag fires when the
score trends negative after 3+ interviews, so the founder can stop without waiting.

**ICP has one author:** the assumption's `icp_*` fields in `graph.md`. Campaign files and
outreach skills read them; they never restate them.

---

## Skills

Definitions live in `.claude/skills/`, with `.agents/skills/` symlinked for Codex discovery.
**There is no skill inventory here or in `CLAUDE.md`** — both drifted from the definitions and
were deleted. Each skill's `description:` is the sole author of what it does and when it
fires, and descriptions are injected into every session, so route from those. Parked skills
live in `.claude/skills-parked/`; `scripts/validate_skill_catalog.py` reports the active set
and enforces the contract.

What this section owns is the wiring — how stages hand off, which no single description states.

```
                    ┌─ optional outreach-intel ─→ companies.md
                    │
outreach-targets → outreach-draft → outreach-check → outreach-reply
 (who to interview)  (Msg 1 prep)     (who replied?)   (Msg 2 drafted)
       ↓                  ↓                 ↓                ↓
 contacts.md    copy/{A_ID}-linkedin.md  results (generated)  ↓
                  founder sends every message      interview-capture
```

- `startup-belief-intake` runs before anything else. It drills down on one founder-held
  belief — what it claims, where it stops, what falsifies it — grounds it in real examples
  through definitional research, and runs SISP Detection. It writes
  `input-context/{slug}/belief.md`, an EMPTY `hunch-lineage.md`, the `lifecycle.yaml` entry
  and the first brief. **It never writes a hunch.** Intake methods are never
  shotgun-dispatched.
- `startup-ideate-shotgun` runs in explore mode on a belief with no hunch, or reads the exact
  belief/H1 pair plus any explicit evidence delta in the two test modes.
  Every selected method examines the same run subject. It writes the dated report, recon
  packet and method outputs, and a retain/narrow/branch/retire recommendation; lineage changes
  only after founder confirmation.
- `startup-idea-to-assumptions` reads the shotgun report → writes `02-assumptions/graph.md`.
- Validation skills read `graph.md` → write `03-validation/{A_ID}-{date}/`, update `evidence.md`.
- `startup-outreach-targets` reads `graph.md` + `contacts.md`, filters the founder's LinkedIn
  export against the declared ICP, then searches for post authors, groups and 2nd-degree
  profiles. Uses `companies.md` for prioritization when present; never requires it.
- `startup-outreach-draft` takes profile URLs → live snapshot including the experience page →
  degree-aware note vs DM → ICP check → logs to `contacts.md` + the copy archive.
- `startup-outreach-check` scans inbox previews → founder confirms classifications → updates
  `contacts.md`; the results files regenerate from it.
- `startup-outreach-reply` consumes confirmed check results → one grounded Msg 2 at a time.
- **Neither drafting skill sends.** Claude may send a bare connection invite; the founder sends
  every message by hand. `schemas/copy-rules.md` is the single author of that boundary.
- `startup-interview-capture` reads raw notes → writes structured capture below the `---`
  divider, appends to `evidence.md`, updates `contacts.md`.
- The cron monitor watches `contacts.md` and fires `startup-interview-synthesis` at the
  declared threshold (or flags likely-dead on a negative trend after 3+ interviews).
- `startup-interview-synthesis` reads interview notes + `contacts.md` + `graph.md` → writes the
  cycle's `synthesis.md`, updates the graph, picks an outcome. `new_vertical`, `mutate_thesis`
  and `kill` route back to the shotgun; `next_assumption` retains the hunch.
- `startup-x-draft` is conversational: its bundled `harvest_sessions.py` mines the founder's own
  messages out of their Claude Code transcripts → arrives with candidate topics → discusses →
  drafts one post at a time → applies the disclosure ladder → queues to `content/x/queue.md`
  with a grounding table. It never posts. Voice comes from `content/x/voice.md`.

`content/x/` is the only output tree outside `reports/{slug}/`, and deliberately so: a
publishing queue is cross-idea by nature, and splitting it across idea folders would make
"what have I not posted yet" unanswerable. It holds no findings — every entry carries a
`source:` pointer back into `reports/{slug}/` instead of restating what it found.

### Data-access layer (not skills — importable + CLI-callable)

`scripts/data/` is the shared query library: every module exposes a Python function AND a
JSON-emitting CLI (`python -m scripts.data.<name> --help`). Callers are
`startup-outreach-intel` (via its bundled `intel_lib.py`), shotgun subagents, method cards and
ad-hoc work. `community_recon` composes Reddit and HN into one normalized, deduplicated corpus
— an LLM plans and interprets the search while the collector stays deterministic.

**`api-registry.yaml` is the sole author of source reachability** — which sources exist,
whether each is enabled, what keys it needs, why a disabled one is disabled. It is not a
convenience index: `scripts/data/_common.is_enabled()` reads it at call time, so it is what
actually gates every request. That rule exists because it was broken — a table here once
mirrored all seventeen entries, and one source's disabled state was independently recorded in
nine files.

### Generated artifacts and their sources

| Generated | Built by | From |
|---|---|---|
| `reports/{slug}/BRIEF.md` | `build_brief.py` | every living artifact + `lifecycle.yaml` |
| `reports/{slug}/control-room.html` | `build_control_room.py` | the same, plus copy archives |
| `reports/{slug}/outreach/results-{A_ID}.md` | `build_control_room.py` | `contacts.md` |
| `methods/index.md` | `build_methods_index.py` | card frontmatter × `shotgun-routing.yaml` |

`--all` on the brief and dashboard generators is lifecycle-gated to `active` ideas; pass a
slug explicitly to rebuild a dormant one.

Skills get written when the workflow makes them obvious. Not before.
