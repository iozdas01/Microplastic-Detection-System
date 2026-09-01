# DVF lens, DAG pass, ranking pass, field reference

Steps 4-6 and the per-assumption field reference for `startup-idea-to-assumptions`. Loaded after the conversation loop has produced assumptions.

## Step 4 — DVF lens check (after mandatory foundations)

After A1 and A2 are confirmed, run a quick lens check before continuing:

Count confirmed assumptions per lens:
- Desirability (do users want this?)
- Viability (can this be a durable business?)
- Feasibility (can we deliver this now?)

If any lens has fewer than 2 confirmed assumptions, tell the founder: "We're thin on
[lens]. The shotgun flagged [specific tension]. Should we extract an assumption here?"

Do not invent assumptions. Pull them from the shotgun's tensions, contradictions, and
surfaced risks sections.

---

## Step 5 — DAG pass

After all assumptions are confirmed and written, propose the parent/child structure.
Show it as an indented tree:

```
○ A2 — Pain is real & expensive (root)
   ├─ ○ A5 — Buyers will pay >$8k/{asset} (child of A2)
   └─ ○ A4 — Industrial services firms are the right first buyer (child of A2)

○ A1 — Why Now (root)
   └─ ○ A6 — Rope-suspended system meets OEM coating spec (child of A1)
```

Ask: "Does this sequencing match the business logic — would you actually stop testing
A5 if A2 turned out to be false?"

Edit parent_assumptions and child_assumptions in graph.md after agreement.

---

## Step 6 — Ranking pass

Run the lexicographic ordering across all Leap-of-Faith assumptions:
1. Gate: must be in `quadrant: leap_of_faith`
2. DAG: roots before unconfirmed children
3. kill_power tier: higher first
4. uncertainty_score tier: higher first
5. test_cost tie-break: cheaper first

Present the result:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
★ START HERE: A{N} — {one-line assumption}
Scores: kill_power {k} · uncertainty {u} · test_cost {c}
Why first: {one sentence — which criterion decided}
Test: {one sentence — the next_action}
If false: {one sentence — what dissolves downstream}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Ask: "Does this feel right as the first thing to test, or is there something about the
business context that should move another assumption higher?"

After confirmation, edit `active_assumption: A{N}` in the graph.md header and
`last_updated` to today.

---

## Field reference (write these for every confirmed assumption)

```yaml
- id: A{N}
  assumption: ""               # one or two sentences, plain language, testable claim
  category:                    # timing | pain | buyer | market | technical | trust |
                               # distribution | competition | defensibility |
                               # founder-market-fit
  lens:                        # desirability | viability | feasibility
  validation_track:            # customer_adoption | strategic_partnership | investor_thesis
  test_method:                 # agent | founder
                               # agent = Claude can run this autonomously via desk research,
                               #   web mining, or secondary data — no founder time required
                               # founder = requires founder to get on calls, do discovery
                               #   interviews, or build relationships — cannot be delegated
  why_it_matters: ""           # one sentence — what dissolves if this is false
  importance:                  # high | medium | low
  # evidence_quality and confidence are NOT written here. Both are DERIVED from the
  # evidence ledger by scripts/idea.py (derive_assumption_evidence) and rendered by the
  # generators — hand-setting them on a node is the single-authorship violation the
  # repo validator rejects. Evidence is graded once, on the ledger entry.
  quadrant:                    # leap_of_faith | known_important | uncertain_minor | ignore
  uncertainty_score:           # 1–5 (only for leap_of_faith)
  kill_power:                  # 1–5
  test_cost:                   # 1–5 (use proxy cost if a proxy test was chosen)
  parent_assumptions: []
  child_assumptions: []
  evidence_for: []             # pull from shotgun; founder can add during conversation
  evidence_against: []
  status:                      # untested | testing | weakly_supported | confirmed |
                               # contested | killed
  next_action: ""              # one concrete sentence naming the specific action
  disconfirmation: ""          # specific measurable threshold that constitutes rejection
  stop_rule: ""                # time/spend/interview cap
```

---

## Step 1b — Hunch alignment (one question, not a re-run)

Before extracting any assumption, state the active hunch in its canonical
segment/problem/mechanism/why-now form. Then ask one question:

> "Is H{N} still the hunch you want to test, or has new evidence changed the segment,
> problem, mechanism, or why-now?"

If the founder confirms — move straight to Step 2. No further discussion.

If the founder says thinking has shifted, do not edit the hunch ad hoc inside the
assumption graph. Route back to `startup-ideate-shotgun` in reframe mode so the
new hunch gets evidence, a parent link, and a change reason. Resume extraction
only after the founder activates the proposed child or sibling hunch.

Do not rewrite or rerun the shotgun inside this skill. Hand off to
`startup-ideate-shotgun` and stop assumption extraction until a revised hunch is
founder-confirmed. Do not ask multiple questions.

Write the agreed hunch as a comment block at the top of graph.md before the
`assumptions:` list:

```yaml
# Active hunch H{N} (confirmed {today})
# {canonical hunch statement}
```

---

## Mechanics

Step mechanics, templates and the failure catalogue live in `references/passes-and-fields.md`. Read the section for the step you are running.

## Step 3 — The conversation loop (one assumption per turn)

For each assumption, run this exact sequence. Do not skip steps.

### 3a. Propose the draft

State the assumption in one or two plain sentences. Then cite the specific line or
section from the shotgun that surfaced it. Then ask one question — not a list:

> "Does this framing match what you know about the market, or is there something I'm
> getting wrong?"

Example opening for A1:
> "First assumption — Why Now. Based on the shotgun: [quote the specific convergence
> finding]. My draft is: [one sentence assumption]. Does this match your read, or did
> I miss something from what you know on the ground?"

Keep the draft short. The founder will correct the wording. That is the point.

### 3b. Refine based on founder response

Incorporate what the founder says. If they say "that's actually two things" — split it.
Propose the two separate assumptions, discuss each separately. If they say "we already
know this is true because X" — mark it as `confirmed` with their evidence, no further
discussion needed. Move on.

Restate the refined assumption clearly before moving to scores.

### 3c. Propose scores with reasoning

Propose each score with one sentence of reasoning. Do not just give numbers.

**kill_power (1–5):** "I'd score this 5 — if this is wrong the entire business case
dissolves because [reason from shotgun]. Agree?"

**uncertainty_score (1–5):** "I'd score this 4 — we have secondary evidence but no
primary customer confirmation yet. Does that match what you know?"

**test_cost (1–5):** "I'd score this 2 — cheapest path is [proxy]. Agree, or is there
a constraint I'm not seeing?"

The founder can override any score. When they do, ask for one sentence of reasoning so
you can record it. Then update.

### 3d. Agree on next_action and disconfirmation

**next_action:** Propose one concrete sentence — the cheapest way to get a verdict.
Name a specific action, not a category. Bad: "conduct customer research." Good: "3 cold
calls to operations directors at target operators framed as 'we're building capability
for the hard step — how do you currently manage the lag between the two stages?'"

**disconfirmation:** Propose a specific measurable threshold that would REJECT this
assumption. Bad: "if people don't seem interested." Good: "if fewer than 2 of 10 cold
outreach attempts yield a discovery meeting within 1 week."

**stop_rule:** Propose a resource cap. Cap at **1 week max** — no longer (see memory
`feedback_stop_rule_cap`). Example: "stop after 10 calls or 1 week, whichever comes first."

Ask the founder: "Does that test design make sense, or is there a faster/cheaper way
you can see?"

### 3e. Write to graph.md immediately

Once the founder confirms — any signal of agreement ("yes", "that's right", "ok",
"looks good", "let's move on") — write the assumption to graph.md using the Edit tool.
Append it to the `assumptions:` list with all fields filled. Do not wait for the end
of the session.

After writing, say one line: "Written as A{N}. Moving to the next."

Do not read the file back to verify — the Edit tool confirms success.

### 3f. Validation track and test method

Tag the `validation_track`:
- `customer_adoption` — tests whether a paying user will adopt and sustain the product
- `strategic_partnership` — tests whether a company will co-develop, invest, or distribute
- `investor_thesis` — tests whether financial investors will fund this bet

Most assumptions are `customer_adoption`. Ask if unsure — one question.

Tag the `test_method` — this is the routing decision for who actually runs the test:
- `agent` — Claude can run this autonomously using information that already exists online:
  desk research, web mining, secondary data, market sizing, competitor analysis, patent
  review, published regulatory requirements. No founder calendar time required.
- `founder` — requires the founder to personally get on calls, build relationships, or
  create something new that doesn't exist yet. Cannot be delegated to an agent because
  the signal depends on live human conversation OR the test requires actively shaping
  an outcome (e.g. negotiating a regulatory pathway, closing a pilot, getting a warm intro).

Critical rule: **if an assumption requires creating something new — a regulatory standard,
a partnership, a pilot agreement — it is always `founder`, even if background research
is available online.** An agent can read what regulations exist today; only a founder can
have the conversation that creates a new regulatory pathway. Never mark an assumption
`agent` just because some supporting research is online.

Default rules: timing, market sizing, competitor, and secondary-evidence assumptions →
`agent`. Pain, buyer willingness, FMF, GTM, regulatory acceptance, and partnership
assumptions → `founder`. When in doubt, ask one question.

---
