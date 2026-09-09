# Report templates — ideation shotgun

The stage-output and synthesis-report scaffolding for `startup-ideate-shotgun`. Loaded when writing the run report, not at routing time.

## Verdict on Current Hunch
[support | tension | contradiction | unknown]

## Component Implications
- Segment:
- Problem:
- Mechanism:
- Why now:
- Existing workaround:
- Plausible buyer:

## Evidence References

## Counterevidence and Unknowns

## Out-of-Scope Alternatives

## Confidence
```

Every numerical claim, company fact, or attributed outcome needs a URL actually
read by the agent. Unsupported specifics are `[UNVERIFIED]` until retracted or
sourced.

Individual methods do not generate replacement hunches. If a technology,
analogy, segment, or product pattern suggests another opportunity, label it
`out_of_scope_alternative`. Only synthesis may compose a revised hunch, and it
must independently evidence the problem under the SISP guard.

The agent writes the full output to
`reports/01-ideation/methods/{run-id}/{method-slug}.md` and returns only
the path confirmation.

### 6. Synthesize with controlled lineage

Use a fresh synthesis agent to weigh the method outputs, evaluate the one
current hunch, and judge whether the belief itself is at risk.

Its manifest contains only:

- belief;
- intake SISP context and the result of its required independent test;
- current hunch and its direct parent;
- explicit evidence delta;
- final pain clusters and source status;
- successful method output paths.

It may not read arbitrary prior reports. In `reframe` mode, synthesis must
compare the current hunch with the explicit evidence delta. This comparison is
the point of the run.

The synthesis must:

1. produce a component-level verdict for the current hunch;
2. decide `retain`, `narrow`, `branch`, or `retire`;
3. preserve the current statement for `retain`;
4. compose at most one recommended revised hunch for `narrow` or `branch`;
5. keep other discoveries as out-of-scope alternatives;
6. identify the cheapest evidence that could kill the current or revised hunch;
7. separate hunch risk from belief risk;
8. apply the independent-problem SISP guard before recommending any
   solution-shaped revision.

### 7. Write the report

Write `reports/01-ideation/{run-id}-shotgun.md`:

```markdown
# Belief Shotgun — {idea}
Date:
Mode:

## Belief

## Intake Starting Point and SISP Test
[Starting solution/analogy, intake status, independent search result, and what
remains unproven. Omit only when the belief file explicitly records no starting
solution and `not_indicated`.]

## Current Hunch
[Exact H_ID, statement, components, and hunch-level disconfirmation.]

## Evidence Delta
[Reframe mode only. What changed since the current hunch was created.]

## Public-Signal Evidence Matrix

## Root-Cause Chain

## Job and Current Substitutes

## Segment and Wedge

## Why-Now and Predecessors

## Conditional Lens Findings

## Component Verdict
[segment | problem | mechanism | why now | workaround | buyer]

## Contradictions and Counterevidence

## Hunch Decision
[retain | narrow | branch | retire]

## Recommended Revised Hunch
[Only for narrow or branch. Mark `pending founder confirmation`.]

## Out-of-Scope Alternatives

## Belief Status
[intact | under tension | at risk — founder decision required]

## Cheapest Next Test

## Source Limitations and Failures

## Appendix: Lens Outputs
```

Do not average away contradictions. Separate pain existence, pain intensity,
organizational budget, buyer reachability, and willingness to pay.

### 8. Verify claims

Every number, real-company fact and attributed outcome in the synthesis must
carry a URL that is already in the relevant method output on disk. Verification
reads those artifacts; it collects nothing new.

A claim with no such URL is marked `[UNVERIFIED]` or deleted, and the choice is
recorded. When an unverified claim is load-bearing for the verdict, say so at the
founder gate — sourcing it is the founder's call, and their decision, not this
step's.

API emptiness and blocked sources remain visible limitations.

### 9. Founder decision gate

Present the exact current hunch, recommended action, strongest support,
strongest contradiction, and any proposed revised statement. Then stop and ask
the founder to retain, accept the revision, edit it, or reject it.

Do not change `active_hunch`, retire the current hunch, or activate a child or
sibling before explicit founder confirmation. The dated report is sufficient
session memory while the decision is pending.

### 10. Update hunch lineage after confirmation

Use `schemas/hunch.md`.

- `retain` keeps the active hunch and records the run as new evidence.
- `narrow` or `mutate_thesis` creates and activates a child; retire the parent.
- `branch` or `new_vertical` creates and activates a sibling; retire the
  previous active hunch.
- `retire` or `kill` retires the active hunch. If no replacement was confirmed,
  leave `active_hunch: null` and route to intake before another shotgun.
- Never rewrite `belief.md` without founder confirmation.

Every new hunch records its parent, run path, evidence IDs or synthesis paths,
and reason for change. Never delete retired hunches.

### 11. Refresh the dashboard

After the founder decision and any confirmed lineage update, run both generators:

```bash
python3 scripts/build_control_room.py
python3 scripts/build_brief.py
```

The dashboard shows the stable belief, hunch under test, method findings,
component verdict, confirmed lineage, and the assumption matrix when available
(spec: `scripts/references/thesis-tab-spec.md`). The brief is what the next
session reads first, so it must not be left stale.

## Process

### 1. Build the context manifest

Create `context-manifest.json` with an immutable `run_subject`:

```json
{
  "idea": "...",
  "mode": "initial_test | reframe",
  "belief_file": "input-context/belief.md",
  "belief_verbatim": "...",
  "hunch_lineage_file": "reports/01-ideation/hunch-lineage.md",
  "hunch_id": "H1",
  "hunch_statement": "...",
  "components": {
    "segment": "...",
    "problem": "...",
    "mechanism": "...",
    "why_now": "...",
    "existing_workaround": "...",
    "plausible_buyer": "...",
    "hunch_disconfirmation": "..."
  }
}
```

Also include intake SISP fields, every raw source, evidence-delta and interview
synthesis paths, and only the previous run that directly parents the active
hunch.

Every method receives this exact manifest. It may challenge any hunch component
but must not select a different hunch, segment, or pain cluster as its subject.
Record interesting adjacent findings as `out_of_scope_alternative`.

In reframe mode, explicitly separate:

- evidence that affects the current hunch;
- evidence that points to a different segment or root cause;
- evidence that threatens the belief itself;
- unrelated evidence that should not influence this run.

### 2. Run Public Signal Reconnaissance

Read `methods/ideation/public-signal-reconnaissance.md` and
`references/public-signal-stage.md`, then follow that protocol completely. This
mandatory pre-lens stage runs once in the main process and consumes no lens
agent. It searches the active hunch neutrally, uses registered sources for named
evidence gaps, and records support, contradiction, uncertainty, and
out-of-scope alternatives.

### 3. Expand and normalize the evidence packet

Produce the complete packet required by the method card and reference:
`raw-corpus.json`, `pain-clusters.json`, `source-status.json`, and
`evidence-matrix.md`. Do not let a stronger adjacent cluster replace the run
subject.

Round two is conditional. Run it only against a named gap from the trigger list
in `references/public-signal-stage.md`, and record `round_2: skipped` with its
reason when round one already answers the run subject.

### 3a. Scout gate — always stop here

Use the scout template, recommendation rules and freshness rules in
`references/public-signal-stage.md`. Write the scout summary into the shotgun
report and source-status artifacts, present it with the proposed portfolio and a
one-line recommendation, then **stop and wait**.

The founder's answer is one of: proceed with the four required lenses; proceed
and add a named conditional lens; revise the queries and re-collect; or stop
here with the scout as the run's output.

A scout-only run is complete and valid — write the report through its scout
section, change no lineage, and say the run stopped at the gate.

A later session may reuse only evidence tied to the identical hunch, subject to
per-source freshness.

### 4. Select a lens portfolio

Read `methods/shotgun-routing.yaml`. It is the ideation allowlist and dependency
map. Do not enumerate methods by `applicable_at`.

Select the lens portfolio the founder approved at the scout gate — four required
lenses by default, five or six only when they named a conditional family. Public
Signal Reconnaissance is the required pre-lens and does not count toward the
total:

- **only from `methods/ideation/`** — that folder is the lens pool. Every other
  folder is out by construction: `validation/` runs assumption- or
  experiment-specific tests, `mutation/` requires an interview evidence delta,
  `intake/` needs the founder in the room, and `practices/` needs real traffic
  or a real buyer. A subagent handed any of them does not report that it cannot
  run — it invents a fluent result that reaches synthesis looking like
  evidence;
- one primary method from each of the four required families;
- conditional lenses **only when the founder named one at the gate**. Never add
  one because its `when:` reads as satisfied — the conditions are prose, a model
  can always argue one is met, and each conditional family costs a research
  agent. Zero is the default and the common case;
- one method per family; alternatives are mutually exclusive;
- no method with an unmet prerequisite;
- every method evaluates the manifest's same `belief_verbatim`, `hunch_id`, and
  `hunch_statement`.

**Verify every selected path resolves before dispatching.** If a `primary` points at a file
that no longer exists, promote one of that family's alternatives and say so in the preview.
If a *required* family has no resolving method at all, name the gap in the preview and in the
report's "Source Limitations and Failures" section — never let a required family drop out
silently. A missing card is invisible in the output otherwise: the run looks complete and the
missing lens is simply never missed.

Prefer diversity of questions over method count. Read each selected family's
`execution.stage`, `execution.mode`, `execution.order`, and `depends_on` from
the routing file, and the stage's `model:` from `execution_stages` — a stage with
none inherits the session model. Do not hardcode method membership or a model in
this skill; the routing file is the one author for both.

Print the selected portfolio before dispatch:

```
Mode: {initial_test|reframe} · Recon: {fresh|partially refreshed|resumed}
Belief: {one-line verbatim belief}
Hunch under test: {H_ID} — {canonical statement}
Public-signal packet: {N records, source coverage, limitations}
Interpretation stage: {ordered methods} → one batched agent ({model})
Targeted-research stage: {methods} → {N} agents ({model})
Lens concurrency: max 3 agents at once
Synthesis: one agent after both stages
```

### 5. Execute the routed stages

Run selected methods only after the final recon packet exists.

**Interpretation stage:** send all selected `analysis_batch` methods to one
agent. It must apply them in routing order, write one output file per method,
and preserve intermediate outputs for declared dependencies. In particular:

- Five Whys starts from the current hunch's problem observation verbatim and
  asks only `WHY?`;
- JTBD/Substitute examines the current hunch's segment, problem, and workaround;
- Segment/Wedge consumes the JTBD output and tests the current segment rather
  than silently choosing another;
- a reframing method, when selected, runs after the required interpretation
  methods and records alternatives without replacing the run subject.

**Targeted-research stage:** after interpretation finishes, dispatch the routed
`research_agent` methods on the stage's declared model. Give them the interpretation outputs so timing,
predecessor, statistical, and analogy research tests the same hunch rather than
the field in the abstract. Never keep more than three research agents active.

Each agent receives the same context manifest, `pain-clusters.json`,
`source-status.json`, `evidence-matrix.md`, selected method card, dependency
outputs, and its output path. Give `raw-corpus.json` only when verbatim evidence
is needed. Agents may make targeted follow-up searches but must not repeat broad
public-signal reconnaissance.

Preserve the native output format in each method card. Append this common
footer instead of replacing the method's own structure:

```markdown

## Mechanics

Phase mechanics, output templates and the failure catalogue live in `references/report-templates.md`. Read the section for the stage you are running.

---

## Run artifacts

Write every per-idea artifact below `reports/`:

```
reports/01-ideation/
  {run-id}-shotgun.md
  hunch-lineage.md
  methods/{run-id}/{method-slug}.md
  recon/{run-id}/
    context-manifest.json
    round-1-query-plan.json
    round-1-corpus.json
    round-1-clusters.json
    round-2-query-plan.json
    round-2-corpus.json
    raw-corpus.json
    pain-clusters.json
    source-status.json
    evidence-matrix.md
```

Set `{run-id}` to `YYYY-MM-DD`, appending `-02`, `-03`, and so on for additional
runs that day.

Explore mode writes the same `recon/{run-id}/` packet plus
`methods/{run-id}/{jtbd,segment-wedge}.md`, and its `{run-id}-shotgun.md` closes with
the candidate table instead of a verdict. Candidates are appended to
`hunch-lineage.md` as `status: proposed`; nothing else in the lineage changes.
