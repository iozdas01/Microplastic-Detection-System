---
name: startup-ideate-shotgun
description: >-
  Runs one evidence-backed ideation pass over a founder-confirmed belief. With an
  active hunch it tests that hunch through Public Signal Reconnaissance and a curated
  portfolio of methods, then recommends retaining, narrowing, branching, or retiring
  it. With a belief but no hunch it runs explore mode instead — recon, jobs and
  substitutes, then segment and wedge — and proposes two to four candidate hunches for
  the founder to choose from, which is the answer to "I have a belief, where do I even
  look?" and "which segment should we go after?". Use whenever the founder asks to
  shotgun a belief, investigate the current hunch through multiple methodologies,
  find candidate hunches or a segment to enter, or revisit any of it after interviews.
  Every method in a run examines the same run subject. This is not a
  specific-assumption validation workflow and not an instruction to run every method
  in the library.
---

# startup-ideate-shotgun

Examine one founder-confirmed run subject through a deliberately diverse set of
evidence-backed methods. Within a run, the methods are different views of the same
subject, not independent idea generators — each returns its own reading, and only
the final stage composes them into a proposal.

## The object model

- **Belief** — the founder's durable field-level conviction. Preserve it
  verbatim; only the founder changes it.
- **Hunch** — a falsifiable segment/problem/mechanism/why-now interpretation of
  the belief. It is expected to change.
- **Assumptions** — what must be true for a hunch; handled downstream by
  `startup-idea-to-assumptions`.
- **Evidence/context** — this run's public signals, interviews, contradictions,
  raw inputs, current hunch, and explicit evidence delta.

The loop is:

```
intake → belief ─┬─(no hunch)→ shotgun EXPLORE → proposed hunches → founder picks
                 │                                                      │
                 └─────────────── active H1 ←───────────────────────────┘
                                     ↓
                     shotgun TEST → assumptions → interviews/evidence
                        ↑                              ↓
                        └── retained, child, sibling, or retired hunch
```

Killing a hunch does not automatically kill the belief.

## Modes

`methods/shotgun-routing.yaml` → `run_modes` is the authority. Infer one of three
from the lineage, never from the founder's phrasing:

1. **Explore** — belief confirmed, no active hunch. Runs `explore_pool`: recon,
   then JTBD and segment/wedge over the corpus, then propose. Output is two to four
   candidate hunches written `status: proposed`, each component cited to a cluster or
   `unknown`. **Never sets `active_hunch`** — the founder promotes one.
2. **Initial test** — an active hunch exists and no shotgun has examined it yet.
3. **Reframe** — an active hunch and new evidence exist. Retain, narrow, branch, or
   retire it.

**Every mode stops at the scout gate.** Recon runs, the scout summary is written,
and the founder chooses: proceed with the four required lenses, add a named
conditional lens, re-collect, or stop with the scout as the output. Conditional
lenses never fire on their own — the corpus holds most of a run's decision value
and the lens portfolio most of its cost, so a hunch the recon already contradicts
should die at the gate. A scout-only run is a complete run.

An active hunch that already exists blocks explore mode. Re-exploring the field
underneath a hunch currently under test produces a run competing with the hunch it
was meant to serve; retire or supersede it first, with founder confirmation.

## Inputs

Require in every mode:

1. `input-context/{slug}/belief.md`, including `## Belief boundaries` — in explore
   mode the in-scope list is what the recon search frame is derived from, so an empty
   boundaries section stops the run;
2. `reports/{slug}/01-ideation/hunch-lineage.md`.

Require in the test modes additionally:

3. exactly one `active_hunch`, with its canonical statement and components;
4. raw inputs and, during reframe, the explicit evidence delta and relevant
   interview synthesis.

Never read another idea's reports. Prior state enters only through the lineage
and evidence-delta manifest.

The `## Starting point and SISP check` section in `belief.md` is intake context,
not a conclusion. Preserve the founder's starting solution or analogy, but do
not treat it as a hunch or as evidence. If its status is `possible`, `probable`,
or `unresolved`, test whether the solution-free problem appears independently
in external behavior and language.

If the **belief** or its SISP section is missing, invoke `startup-belief-intake`.
Never infer the belief from an inline sentence — it is the one object the founder
must author.

A missing **active hunch** is not an error — it selects explore mode, whose whole
purpose is to produce candidates for one.

## Run artifacts

Every per-idea artifact goes below `reports/{slug}/`. Tree, run-id scheme and the
explore-mode variants: `references/report-templates.md` → Run artifacts.

## Interview-loop routing

Interpret interview-synthesis outcomes consistently:

| Outcome | Shotgun effect |
|---|---|
| `next_assumption` | Keep the hunch; continue validation without rerunning shotgun unless new context materially changes it. |
| `new_vertical` | Reframe with the same belief; propose a sibling hunch for another segment. |
| `mutate_thesis` | Reframe with the same belief; propose a child hunch with a different mechanism or problem. |
| `kill` | Retire the hunch with founder confirmation, then rerun this skill in **explore mode** to propose the next hunch beneath the same belief from a fresh corpus. Only route back to intake if the belief itself is what the evidence threatened. |

## Failure modes

- **Running explore mode's proposal stage as a recommendation** — present each
  candidate with its evidence and let the founder choose. A ranked list is a
  recommendation wearing a table's clothes, and the founder's choice is what makes the
  hunch theirs.
- **Filling an explore candidate's components to look complete** — `unknown` is the
  correct value for anything the corpus does not support, and a candidate with no
  citable segment and no citable problem is not a candidate at all.
- **Letting methods choose different subjects** — every method gets the same
  manifest. Adjacent discoveries are out-of-scope alternatives.
- **Running every ideation-tagged method** — bypasses the routing portfolio and
  reintroduces cost and duplicated thinking.
- **Dispatching source modes as lenses** — Reddit, LinkedIn, jobs, reviews,
  public proof, and triangulation belong to Public Signal Reconnaissance.
- **Spending agents where a payload would do** — batch the analysis lenses into
  one agent rather than dispatching them separately, keep at most three research
  agents live, and pass `raw-corpus.json` only when a lens needs verbatim
  evidence; most reason over `pain-clusters.json` alone.
- **Running dependent methods in parallel** — interpretation must precede
  targeted research, and Segment/Wedge must consume the JTBD output.
- **Treating the belief as the hunch** — makes contradictory evidence impossible
  to absorb without abandoning the whole field.
- **Overwriting the context file** — destroys lineage. Keep raw inputs and
  evidence append-only; generate a per-run context manifest.
- **Reading volume as evidence** — crossposts, repeated authors and one loud
  community are not convergence, and public pain is an invitation to test rather
  than a purchase.
- **Re-mining Reddit in every method** — use the shared corpus and make only
  targeted follow-ups.
- **Comparing arbitrary old runs** — compare only the active hunch, its direct
  lineage, and the explicit evidence delta.
- **Silently rewriting the belief** — flag it for founder review instead.
- **Re-running SISP Detection as a shotgun lens** — how the founder arrived is
  intake evidence. The shotgun tests the recorded problem externally; it does
  not ask a research agent to invent the founder's origin story.
- **Searching the proposed solution first** — makes the corpus inherit the
  founder's frame. For possible/probable SISP cases, establish whether the
  problem exists using solution-free workflow language before researching the
  proposed approach.
- **Collecting a corpus you already have** — check
  `01-ideation/recon/*/context-manifest.json` before step 2; reuse only when the
  hunch ID and statement match, and refresh per TTL. Round two is conditional
  too: run it against a named gap, not by default.
- **Forcing generic output over a method card** — preserve Five Whys' literal
  chain and each consolidated card's native structure.
- **Letting each method generate hunches** — methods evaluate components; only the
  final stage proposes (one revision in a test mode, the candidate set in explore).
- **Updating lineage before the founder decides** — a recommendation is not an
  active hunch.

## Trigger boundaries

Trigger for:

- “shotgun this belief and hunch”, or “just scout it first”
- “test this hunch through the methods”
- “research whether H1 holds up”
- “rerun ideation with these interview findings”
- “our hunch was wrong; what does the evidence suggest instead?”

Do not trigger for:

- one named method;
- one named assumption validation;
- a general field with no founder-confirmed BELIEF — run belief intake first;
- generating interview questions;
- capturing or synthesizing raw interview notes;
- casual brainstorming without a request for evidence-backed exploration;
- requests that only ask which methods exist.

## Mechanics

Step mechanics and templates live in `references/report-templates.md`.
