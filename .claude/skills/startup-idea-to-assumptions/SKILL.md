---
name: startup-idea-to-assumptions
description: >
  Conversational assumption extraction — Claude proposes one assumption at a time
  from the founder-confirmed active hunch and its shotgun report, the founder refines it, scores are agreed together, and
  Claude writes each confirmed assumption to graph.md immediately. The file is the
  memory: if the session is interrupted, the next run resumes from the last confirmed
  assumption. Invoke whenever the user wants to build or continue the assumption graph
  for an idea, or asks "what should we test first?", "let's map assumptions",
  "continue the assumption graph", "what are the riskiest assumptions?".
---

# startup-idea-to-assumptions

You are running a structured conversation with the founder to build the assumption graph
for their startup hunch. You propose one assumption at a time, drawn from the
founder-confirmed active hunch and its shotgun evidence. The founder refines it. You agree on scores and test design together. You write
each confirmed assumption to `reports/{slug}/02-assumptions/graph.md` immediately after
it is agreed — the file is the session memory, not your context window.

---

## Step 1 — Parse the slug and load context

The user will say something like "extract assumptions for example-idea"
or "let's build the assumption graph" or "continue the assumption graph for X". Get the
slug from the message. If unclear, ask — one question, not a list.

Read in this order:
1. `reports/{slug}/02-assumptions/graph.md` — if it exists, read it first. This tells
   you which assumptions are already confirmed and where to resume.
2. `reports/{slug}/01-ideation/hunch-lineage.md` — resolve `active_hunch`.
   If candidates exist but none is active, stop and ask the founder which proposed
   hunch to activate. Do not extract assumptions from a portfolio of competing hunches.
3. The artifact that created the active hunch:
   - for onboarding-created H1, read its lineage entry and the latest shotgun
     report that examined it;
   - for a later hunch, read the founder-confirmed shotgun report that created
     or reframed it.
   The latest completed shotgun report is the primary evidence source for
   assumption drafts.
4. `input-context/{slug}/belief.md` — the stable anchor. Assumptions test the active
   hunch, not the belief in the abstract.
5. `schemas/assumptions.md` and `schemas/hunch.md`.

If `graph.md` does not exist yet, create it now with a skeleton before the conversation
starts:

```yaml
idea: {slug}
hunch_id: {active H_ID}
belief_file: input-context/{slug}/belief.md
last_updated: {today}
active_assumption: TBD

assumptions:
```

If `graph.md` already exists with confirmed assumptions, greet the founder with a one-line
status: "We have N assumptions confirmed. Resuming at A{N+1}." Then continue.

---

## Step 2 — Determine where to start

Work through assumptions in this order. Skip any already in graph.md.

1. **A1 — Why Now** (timing / feasibility) — mandatory first
2. **A2 — Pain is real and expensive** (pain / desirability) — mandatory second
3. **No FMF nodes.** Founder rule (memory/MEMORY.md): the graph holds ONLY
   market-testable claims — testable by talking to people. Founder-market-fit and
   technical build bets stay out; they live as kill conditions on offerings, run after
   demand is proven. If the founder volunteers an FMF worry, note it in the session and
   route it there — do not score it as a node.
4. Remaining assumptions extracted via DVF lens sweep from the shotgun — in whatever
   order the shotgun's tensions and risks suggest. High kill_power assumptions from the
   shotgun's "critical risks" or "contradictions" sections go first.

---

## Step 7 — Session end

Print a compact status block:

```
Assumptions confirmed: N
Quadrant summary:
  Leap of Faith:    [IDs]
  Known Important:  [IDs]
  Uncertain Minor:  [IDs]
  Ignore:           [IDs]
Start here: A{N}
Next 2 in queue: A{X} → A{Y}
```

Then immediately regenerate the two derived artifacts:

```bash
python3 scripts/build_control_room.py {idea-slug}
python3 scripts/build_brief.py {idea-slug}
```

Both are pure projections of `graph.md` and its sibling sources, so they must be rebuilt after any assumption session — a stale brief is what the next session reads first. Never hand-write either file.

Stop after both are regenerated. No closing prose.

---

## Conversation rules

- **One assumption per turn.**
- **Always cite the shotgun.** If you cannot point to a specific line that led to the
  draft, you are inventing — go back and find it or don't extract it.
- **Write immediately on agreement.**
- **Never re-discuss a confirmed assumption** unless the founder explicitly reopens it.
- **If the founder adds something you didn't extract**, add it as a new assumption node
  and run the full 3a–3f sequence on it.
- **If the founder says "skip this for now"**, mark it `status: untested` and move on.
  It stays in the graph, unscored, to be revisited.
- **Compound assumption check**: before writing any assumption, ask yourself — does this
  embed two questions that could have different answers? If yes, split before writing.
- **Lookup check (founder rule)**: if a draft could be settled by a day of desk research
  and its failure would only narrow scope rather than kill anything, it is not an
  assumption — it is research. Run the lookup, file the findings as evidence or ICP
  input, and never give it a node. Graph nodes are claims the MARKET has to answer.
  (Why-now is the standing exception: mandatory per ARCHITECTURE.md even when its test
  is desk work, because timing kills companies and deserves an explicit disconfirmation.)
- **test_method routing**: always set `test_method` before writing. Default: timing,
  market, secondary-evidence assumptions → `agent`; pain, buyer, FMF, GTM assumptions
  → `founder`. This split determines what the founder needs to calendar vs. what Claude
  runs autonomously — it must be explicit on every node.

## Mechanics

Step mechanics and templates live in `references/passes-and-fields.md`.

## The conversation loop

One assumption per turn: propose, refine with the founder, agree scores, write it to `graph.md` immediately, then ask for the next. The file is the memory. Full step mechanics in `references/passes-and-fields.md` → Step 3.
