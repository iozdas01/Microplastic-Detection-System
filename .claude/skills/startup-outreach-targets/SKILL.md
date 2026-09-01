---
name: startup-outreach-targets
description: >-
  Finds and scores LinkedIn contacts to interview for a specific assumption, from the founder's LinkedIn data export plus the founder's own logged-in Chrome. Use when the founder asks who to interview, wants a target list, needs high-intent leads, or is beginning customer outreach for an assumption. Filters the exported 1st-degree network against the assumption's ICP, backfills who has already been messaged, then searches LinkedIn content and 2nd-degree profiles for the rest. Verifies ICP fit, deduplicates contacts.md, and appends qualified candidates. Runs the ICP audit over contacts.md automatically on every pass — there is no separate audit skill to invoke afterwards. Browser passes drive that Chrome via the claude-in-chrome tools and need an already-authenticated LinkedIn session; it never handles credentials or sends invitations.
---

# Startup Outreach Targets

Find LinkedIn contacts worth interviewing for a specific assumption. Two sources, in this order:

1. **The founder's LinkedIn data export** (`private/linkedin-export/`, parsed by `scripts/data/linkedin_export.py`) — the complete 1st-degree network and full message history, as local files. Free, exhaustive, no rate limits.
2. **The founder's own Chrome**, driven by the claude-in-chrome tools against LinkedIn's own search URLs — for everything the export can't see: post authors, groups, 2nd-degree profiles, and live profile state.

No paid API, no MCP. Always exhaust source 1 before touching source 2 — browsing is the expensive path and most of what it used to do is now a file read.

## The one non-negotiable

**The user sends every message manually.** This skill finds candidates and writes them to `contacts.md`. It does NOT send invites, auto-connect, or mass-scrape. Reading and browsing LinkedIn is fine; automated sending gets accounts banned.

## The filter — MUST be ICP-driven, per-assumption

**Do NOT accept contacts based on a hardcoded keyword list.** The filter derives its rules from the specific assumption being tested, read from `graph.md`:

- `icp_segment` — one-line description of who can validate the assumption
- `icp_valid_tiers` — allowed tier values for this idea, each tagged with a `side`
- `icp_valid_titles` — whitelisted role titles
- `icp_out_of_scope` — explicit rejects (industries, company types, role types)

**Before adding ANY contact to `contacts.md`, verify:**
1. Contact's `tier` ∈ `icp_valid_tiers` for the target assumption
2. Contact's `role` / `company` / `signal_excerpt` doesn't hit any `icp_out_of_scope` pattern
3. Contact has a `validation_rationale` explaining WHY this specific person can validate this specific assumption (not "domain-adjacent" or "might intro" — a named specific pain visibility)

If the assumption doesn't have ICP fields filled in `graph.md`, **STOP and ask the founder to declare the ICP first**. Don't infer it from the assumption text — declared ICP is the durable contract.

## Post-write audit — MANDATORY

After every batch write to `contacts.md`, run `python3 scripts/audit_target_list.py {slug}`. This audits the tracker against every assumption's declared ICP and flags:
- Off-scope contacts (hard fail — must mark `off_scope` with rationale note; see rules below)
- `tier: other` contacts (soft fail — needs manual classification)
- Missing/vague `validation_rationale` (soft fail — needs filling)

Surface soft fails to the founder for review.

### Status handling when a contact fails ICP audit — READ CAREFULLY

**NEVER silently flip a contact's `outreach_status` during a rerun or audit.** The status is founder-facing state and audit trail — overwriting it without explanation breaks the tracker and confuses which contacts need action.

**Correct handling for contacts that fail the ICP audit:**

1. **If `outreach_status: pending`** (invite not yet sent) — safe to change status to `off_scope` AS LONG AS a `notes:` entry is written explaining WHY (specific ICP field that failed + what the profile visit actually revealed). No note = you didn't do the audit properly, redo it.

2. **If `outreach_status` is already `invited` / `accepted` / `replied` / `scheduled` / `done`** — DO NOT change status. The founder is mid-conversation with this person. Instead, add a `notes:` entry flagging the audit concern and surface to founder for decision.

3. **`declined` vs `off_scope` — these are DIFFERENT statuses, do not conflate:**
   - `declined` = the contact declined the invite ON LINKEDIN (their action). Only `startup-outreach-check` sets this, and only on confirmed negative replies with founder confirmation.
   - `off_scope` = OUR audit rejected them for ICP mismatch (our action). Set by this skill during audit, with mandatory rationale note.

**Rationale note requirements when marking `off_scope`:**
- Which specific ICP field failed (`icp_valid_tiers` / `icp_valid_titles` / `icp_out_of_scope` / `validation_rationale`)
- What the profile visit actually revealed (current role, current company, why it's outside the domain)
- Prefix the note with `[audit off_scope YYYY-MM-DD]` so it's greppable across reruns

**Example (well-formed):**
```
outreach_status: off_scope
notes: "[audit off_scope {date}] Profile visit revealed NOT at {Supplier Co} (was misclassified from scraping). Currently at {Other Co} as investor/entrepreneur. No in-domain role. Fails icp_valid_tiers for A{X}."
```

**Example (broken — this is what NOT to do):**
```
outreach_status: declined       ← wrong status word for our-side audit action
notes: "1st-degree connection — existing network warm path"    ← no audit rationale, doesn't explain the flip
```

### When a contact moves to `off_scope`, exclude them from outreach

`startup-outreach-draft` only accepts contacts whose `outreach_status` is `pending`, so the status change plus the required audit note is the canonical exclusion mechanism. If a legacy draft for the contact still exists under `reports/{slug}/outreach/copy/{A_ID}-linkedin.md`, remove that stale section during the same operation so an archived artifact cannot be mistaken for an approved send. This skill does not create new message drafts.

## Auto-progression between passes

Passes chain automatically based on ICP-fit yield. **Do NOT ask the founder to
approve moving from Pass 1 → Pass 4, or from tier to tier.** Just do it.

**The gate is the 50-contact batch cap, not a per-pass quota.** After each pass,
count in-ICP contacts written this batch. Under 50 → run the next pass
immediately, without pausing. At 50 → stop and hand off. This applies at every
boundary:

- Pass 0 + 1 (export) leaves the batch under 50 → auto-run Pass 2 (content search)
- Pass 2 + 3 (content + verify) leaves it under 50 → auto-run Pass 3b (LinkedIn Groups)
- Pass 3b leaves it under 50 → auto-run Pass 4 (2nd-degree)
- Pass 4 yields < 15 at the current tier → auto-drop to the next tier in
  `icp_valid_tiers` declaration order

**Pass 3b exception:** if the sending founder is not yet a member of any relevant group, don't auto-skip to Pass 4 — instead surface the top 3-5 groups to join, let the founder request membership, and proceed to Pass 4 for this session. Pass 3b will run next session.

Rationale: not every accepted contact replies (typical 5-25% reply rate),
and not every reply schedules a call. 50 contacts is what reliably produces
3+ interviews per assumption, which means fanning across degrees. Asking
the founder each boundary adds friction and burns browser session time.

The only time you STOP mid-pass to ask the founder:
- 50-per-batch cap reached
- LinkedIn shows captcha / "unusual activity" prompt
- All valid tiers exhausted with < 20 total contacts (data quality problem —
  intel might need to be rerun with better keywords)

### Pagination is mandatory on every pass

Every search MUST paginate through all pages of results, not just page 1.
A single page = ~10 candidates; the ICP filter typically drops 60-80% of
those, leaving ~2-4 keepers per page. Reaching 20 kept contacts requires
paginating 5-10 pages of results per keyword.

Never accept the page 1 sample as "the network sweep is done." The click-based
`Next` flow is under "Pagination — mandatory for every search" below.

### Batch cap and repeat

Every batch is capped at **50 total contacts** in `contacts.md` per assumption. That's:
- Enough volume for a real outreach cycle at ~5-10 sends/day
- Small enough that every contact actually gets used before the signal goes stale
- Small enough to enrich fully in one session, well inside LinkedIn's ~100/day profile-view cap

Larger batches were queue-clogging: outreach is one-at-a-time, so contacts 50+
sat unused for weeks while their `post_engagement` excerpts decayed. Refill on
exhaustion rather than stockpiling.

**When the batch is exhausted (all contacts sent to invited/done/no_reply), repeat all 5 passes with:**
- Pass 0/1 rerun against a refreshed export if the last one is more than ~3 months old
- Fresh keywords for the browser passes (rotate — proven ones get fished-out)
- Updated `companies.md` (new companies discovered during the last batch)
- Updated `icp_out_of_scope` (patterns that leaked into last batch)

## Deduplication — MANDATORY before every write

Before appending a new row to contacts.md:

1. **In-file check.** Read contacts.md, search for `linkedin_url:` matching the candidate. If found, append the current `assumption_id` to their existing `assumptions_tested` list — do NOT create a duplicate block.

2. **Cross-project check.** If the founder keeps a separate outreach tracker outside this repo (path recorded in their machine-local session memory, never here), check it for this contact.
```bash
grep -l "<linkedin_url_slug>" "$HOME/Documents/Personal/Linkedin Outreach/outreach_data.json" 2>/dev/null
```

If they're already in there, note in `notes:` that they exist in the other tracker with which status. That other tracker is the founder's active LinkedIn outreach project — don't step on that flow.

## What this skill does NOT do

- **Doesn't send invites.** Founder clicks send in the browser. This skill only finds and classifies.
- **Doesn't generate outreach messages.** Every pending contact goes through `/startup-outreach-draft`; time-sensitive `post_engagement` and `group_active` contacts are simply prioritized in that handoff.
- **Doesn't run interview capture.** That's `/startup-interview-capture` after each call.
- **Doesn't touch any outreach tracker outside this repo.** A founder's separate project is a read-only cross-check for dedup, no writes; its path lives in machine-local session memory.

## Reference files

- `schemas/contact.md` — exact contact card format + scoring formula
- `schemas/assumptions.md` — assumption graph format (for ICP extraction)

## Mechanics

Step mechanics and templates live in `references/search-passes.md`.
