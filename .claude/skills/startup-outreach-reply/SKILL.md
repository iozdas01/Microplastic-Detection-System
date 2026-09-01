---
name: startup-outreach-reply
description: >-
  Drafts LinkedIn replies after a contact responds — one contact at a time. It never sends: the founder sends every message by hand (schemas/copy-rules.md). Determines which message number this is (Msg 2, 3, 4…), deep-researches the contact's workflow phase, extracts evidence data points from their last reply into evidence.md, then drafts the next question designed to advance a progressive discovery arc toward assumption and TAM validation. Use for "what do I say to people who replied", "send Msg 2", "draft follow-ups", "respond to LinkedIn replies", "draft the next message to this contact", or any time a contact has replied and needs a response. Runs startup-outreach-check first when reply data is missing or stale. Drives the founder's own Chrome via the claude-in-chrome tools and needs an already-authenticated LinkedIn session.
---

# Startup Outreach Reply

Each message in a multi-turn conversation is a data collection exercise — not just a polite reply. The goal across the arc is to progressively surface frequency → magnitude → scale, in that order, through natural past-behavior questions. By Msg 4–5 you have enough to ask for a call anchored to what they confirmed.

## Load first — always

1. `references/config.md` (this skill) — check `calendly_url`. If still `PLACEHOLDER`, flag it: "⚠️ Calendly URL not set — warm-path drafts will be shown but not sent."
2. `schemas/copy-rules.md` — the shared copy contract (draft + reply).
3. `reports/{slug}/outreach/contacts.md` — contact list + full notes history.
4. `reports/{slug}/outreach/results-{A_ID}.md` — reply classifications from `startup-outreach-check`.
5. `reports/{slug}/outreach/companies.md` — optional per-company hooks (contracts, fleet, {operational-loss signal}, hiring). If absent, use the contact's live LinkedIn profile and public company research.
6. `reports/{slug}/02-assumptions/graph.md` — active assumption text and domain vocabulary.
7. `reports/{slug}/03-validation/evidence.md` — evidence ledger to append into.

If contacts.md or graph.md is missing, STOP and tell the founder.

## Inputs — ask if not provided

- **Idea slug** — prompt: "Which idea? (e.g. `example-idea`)"
- **Assumption ID** — prompt: "Which assumption? (e.g. `A2`)"
- **Contact** — optional; if the founder names a specific contact, go straight to that person.

## Step 1 — Ensure check results are fresh

Read `results-{A_ID}.md`. Treat results as usable when the file exists, contains a routing table, and every routed reply has a matching `[reply {date}]` excerpt in `contacts.md`. If stale or missing, run `startup-outreach-check` first, then reload.

## Step 2 — Build the reply list

Collect contacts routed as `substantive` or `soft` whose status is not already `call_booked` or `declined`. For each, read the full `notes:` history — this tells you which message number you're drafting next.

**Detect arc stage from notes history:**
- No `[msg2 sent` in notes → drafting **Msg 2**
- Has `[msg2 sent` → drafting **Msg 3**
- Has `[msg3 sent` → drafting **Msg 4**
- Has `[msg4 sent` or beyond → drafting **Msg 5+**

If no contacts qualify, report it and stop without opening LinkedIn.

## Step 3 — Extract evidence from their last reply

Before drafting anything, read their most recent reply verbatim from `contacts.md` notes. Pull out every data point that informs the active assumption — frequency signals, cost signals, market observations, vocabulary they used. Log to `reports/{slug}/03-validation/evidence.md`:

```yaml
- id: E{next_id}
  date: {today}
  source: "{Name} ({contact_id}) — {role}, {company}"
  source_type: expert_call
  claim: "{verbatim or close-paraphrase of the specific data point}"
  assumption_linked: {A_ID}
  verdict: supports | contradicts | ambiguous
  confidence: 1–5
  notes: "{why this confidence; what it does and doesn't prove}"
  next_question_raised: "{what you still need to know}"
```

One entry per distinct data point. If their reply has three things worth logging, write three entries. Skip vague agreement — only log specific claims with a verifiable data point.

**Confidence guide:**
- 5: Practitioner confirms specific mechanism from direct operational experience
- 4: Practitioner confirms cost or frequency with rough quantification
- 3: Published source or secondhand industry observation
- 2: Single data point without quantification
- 1: Vague agreement, no specifics

## Step 3b — Lineage drift check (runs after every evidence write)

After appending evidence entries, reread the ACTIVE hunch's statement and components in
`reports/{slug}/01-ideation/hunch-lineage.md`. Check three triggers:

1. **Contradiction:** two or more evidence entries (across the campaign, not just this
   session) carry `verdict: contradicts` against the same component (segment, problem,
   mechanism, why-now, buyer).
2. **Orphaned assumption:** `active_assumption` in `graph.md` tests a claim that does not
   appear in the active hunch's statement.
3. **Framing drift:** the founder's approved outgoing messages are built on a framing the
   lineage does not contain.

On any trigger: **do NOT rewrite the belief or the hunch.** Instead:

- Append a new hunch with `status: proposed` and the next H-id to `hunch-lineage.md`,
  with `evidence_delta` listing the triggering evidence IDs verbatim and
  `created_by: drift-check (startup-outreach-reply)`.
- Draft the proposed statement from the founder's OWN words in messages and replies wherever
  possible; mark every clause that is agent-phrased.
- Put a DRIFT notice at the TOP of the handoff summary:

```
⚠ LINEAGE DRIFT: outreach is testing "{X}" but the active hunch says "{Y}".
Proposed H{N} written to hunch-lineage.md (evidence: E{i}, E{j}).
Reply "confirm H{N}" to activate it, edit it first, or "reject H{N}" to retire the proposal.
```

Activation requires the founder's explicit word — `schemas/hunch.md` rule. One proposed
hunch at a time: if an unconfirmed proposal already exists, update it in place rather than
stacking a second. The belief itself is never auto-edited; if drift reaches belief level
(the proposed hunch cannot express the recorded belief), say so in the notice and route to
`/startup-belief-intake`.

## Step 4 — The conversation arc

Every message advances one step along this arc. A contact who volunteers data early lets you skip stages. A contact who stays shallow requires patience — don't push the arc faster than they respond.

| Arc stage | Message | Goal | Data to capture | Call ask? |
|---|---|---|---|---|
| **Frequency & context** | Msg 2 | What workflow phase? How often? | Frequency language ("most jobs", "every campaign"), their vocabulary | No |
| **Magnitude & cost** | Msg 3 | What does it cost when it happens? | Time, money, invoice overrun, who absorbs it | No |
| **Scale & market signals** | Msg 4 | Widespread or specific to their setup? | Fleet/site count, job volume, whether they see it across the industry | No |
| **Call ask** | Msg 5+ | Anchor call to what they confirmed | — | YES — only now |

**TAM triangulation (Msg 4 only):** These questions sound natural but surface market scale data. Never frame them as market research — frame them as wanting to understand whether their experience is representative.
- How many units/sites does a typical job cover? → job density
- How many jobs per year? → job volume
- Is this specific to their portfolio or consistent across the industry? → penetration signal
- Which kinds of sites have it worst? → segmentation

## Step 9 — Hand the reply to the founder

**Claude never sends a message** (`schemas/copy-rules.md` → Send permission). Print the
approved text in a copy-ready block, name the contact and the thread it belongs to, and
stop. The founder pastes and sends it from their own session.

Record the send only after the founder confirms it went out — an unconfirmed send in
`contacts.md` is worse than no record, because every reply-rate number downstream treats it
as real.

## Step 10 — Update contacts.md

Once the founder confirms the message was sent:

- `outreach_status` → `msg{N}_sent`
- Append to `notes:` → `[msg{N} sent {date}] arc: {stage} · question_target: "{what data this question is designed to surface}" · edit_count: {N}`

## Handoff summary

```
Reply round for {A_ID} complete.

  {N} sent — Msg 2: {N}, Msg 3: {N}, Msg 4: {N}, Msg 5+: {N}
  {N} skipped
  {N} evidence entries logged to evidence.md

Evidence ledger status:
  A{ID} frequency: {confirmed | partial | open}
  A{ID} magnitude: {confirmed | partial | open}
  TAM signals: {confirmed | partial | open}

Next steps:
  → Re-run /startup-outreach-reply when their next reply lands
  → Call ask ready for: {names where arc = call-ask}
  → /startup-interview-capture only after a live call happens
```

## What this skill does NOT do

- Msg 1 — that's `/startup-outreach-draft`
- Finding contacts — that's `/startup-outreach-targets`
- Interview capture (post-call) — that's `/startup-interview-capture`
- Inbox scanning — that's `/startup-outreach-check`

## Common failure modes

- **Skipping deep research.** If the question could have been written without the research, the research wasn't deep enough.
- **Pushing the arc too fast.** Don't ask magnitude before frequency is confirmed. Don't call-ask before magnitude is confirmed.
- **Googleable question.** If a search could answer it, rewrite to require their private operational knowledge.
- **Product reveal.** No features until they name a specific bleeding pain and its cost.
- **Title recitation.** Their name + what they said. Not their title.
- **Logging vague agreement as evidence.** "Sounds like there's pain" is not an evidence entry. Only log specific claims with a data point.
- **Missing the call-ask window.** Once frequency + magnitude are confirmed, the next message is a call ask anchored to what they told you. Don't keep extracting data indefinitely.

## Mechanics

Step mechanics, templates and the failure catalogue live in `references/drafting-steps.md`. Read the section for the step you are running.
