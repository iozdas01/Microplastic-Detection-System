---
name: startup-belief-intake
description: >-
  Drills down on one founder-held belief until it is sharp enough to build on, grounds it in
  real examples found by research, and writes `input-context/belief.md`. Also
  initializes the idea — an empty `hunch-lineage.md` and the first `BRIEF.md`. Runs a
  long interrogation, not a form: what the belief
  claims, where it stops, who it excludes, what would falsify it, and whether it is a belief
  at all rather than a hunch wearing one's coat. Includes SISP Detection to separate the
  problem from any favoured solution. Use for "start a new idea", "I have a belief I want to
  test", "onboard me", "create a belief file", "run intake", "sharpen my belief", "help me
  figure out what to work on". **It never writes a hunch** — hunches come from
  `startup-ideate-shotgun` in explore mode, from evidence rather than from the founder's
  imagination or the model's.
---

# startup-belief-intake

Produce one object: `input-context/belief.md`, drilled down and research-grounded.

**This skill does not write hunches.** Not H1, not a candidate, not a "working hypothesis" in
a comment. If the founder offers one, record it in the SISP section as a starting point and
leave the lineage empty. The shotgun proposes hunches from a real corpus in explore mode; a
hunch invented here becomes the run subject of its own test, and the pipeline spends its
budget agreeing with itself.

**One question at a time.** A long conversation that should feel like one.

---

## The single most important constraint

**The belief must be founder-authored.**

You will be tempted to tidy it. The founder's raw sentence will be hedged, oddly specific in
places, vague in others, and will not sound like a thesis; yours will sound sharper. Write
yours and the framework detaches from reality — they spend months testing a claim they never
made, and feel no pull to update when evidence contradicts it, because it was never theirs.
Quote them, keep the clumsiness when it is precise, show every compression back, and write
`unknown` rather than filling a gap.

---

## Step 1 — Load

Read `founder.md`, then the profile it names for the founder in the session. Specific
questions reach memory; generic ones get a CV recital you already have. Never ask what the
profile records. Note anything stale for the end.

Check `input-context/` for an existing belief covering this ground; if one exists, read it,
say so, and ask whether to continue it or start a new lineage. Two files for one belief is
how cross-idea bleed starts. If it predates `## Starting point and SISP check`, resume only
that section.

---

## Step 2 — Get the raw belief, unedited

> "What do you believe is true about the world that most people working near it don't?"

Take whatever comes out, do not improve it, and read it back verbatim before touching
anything else. Everything below refines this sentence, so it has to be theirs.

**The belief is ONE SENTENCE** (`schemas/hunch.md`) — a paragraph lets two claims hide inside
one belief, and nothing downstream can then tell which one the evidence moved. The real
sentence usually surfaces mid-drill-down rather than at the start; offer it back and let the
founder fix the wording. Everything else goes under `## How the founder states it`, in their
words.

---

## Step 3 — Drill down

The core of this skill, and the reason it is long. Five lines of questioning — what the
belief claims, where it stops, whether it is the founder's to hold, what it survives, and
whether it is a belief at all rather than a hunch wearing one's coat. Full question bank:
`references/interview-guide.md` → Step 3.

Push on vagueness every time. A belief that survives this is worth months of work; one that
doesn't is better found out now. **A belief that took four questions is usually a hunch** —
if it could be falsified by one study, one quarter or one customer conversation, say so and
go up a level: ask what has to be true for that hunch to matter.

### The precedent lens — standing, not optional

**Whenever the founder calls a constraint permanent, find who hit it first**, and offer it
inside the question rather than researching it silently afterwards — it changes what they are
being asked to judge:

> *"Elevators, boilers and pressure vessels were all once 'a qualified human must inspect and
> sign'. All three moved to certification regimes and insurance products. Does that transfer
> here, or is something different about your case?"*

Read every precedent twice. **If it happened before it can happen again**, which turns
"impossible" into "nobody has done it here yet". And **why the predecessor's fix stalled is
usually the real constraint** — find what they substituted instead. Both readings are useful;
a belief with neither attached is still floating.

Constraint-shape lookup and reporting rules: `references/interview-guide.md` → precedent lens.

## Step 4 — Ground it in real examples

A belief stated in the abstract stays negotiable; the same belief with three named cases
under it becomes something you can be wrong about. So research it — but for a narrower
purpose than the shotgun's.

**The line, and it matters:** intake research is *definitional*. It asks "does this belief
say what the founder thinks it says, and where does it stop?" The shotgun's research is
*empirical* — "is there a real problem here and who has it?" Do not start finding pain,
sizing markets or naming segments. That is the next stage's job, and doing it here produces
a hunch by the back door.

Search targets, in order: `references/interview-guide.md` → Step 4. Always includes the
field that hit this constraint first, per the precedent lens.

Bring findings back as questions, never verdicts — *"this looks like your belief but they did
X instead, does that count?"* Each one either tightens the boundaries or gets rejected, and
both improve the file. Record what survives in `## Belief boundaries`, with links.

---

## Step 5 — SISP check

Card: `methods/intake/sisp-detection.md`. Never skipped, and run hardest when the belief
arrived fully formed or as an "X for Y" analogy — that is exactly where a favoured solution
hides as an invisible premise, and a founder who has been pitching has had practice making
one sound like a problem statement. Never propose candidate problems; a problem statement
supplied by the interviewer defeats the diagnostic.

Record all six fields into `belief.md`, observations labelled founder-reported context rather
than evidence. `possible` and `probable` are not verdicts.

---

## Step 6 — The belief-level disconfirmer

> "What would you have to see to conclude the whole belief is wrong — not just that one
> version of it failed?"

Push for something observable. *"If customers don't like it"* is not a disconfirmer; *"if the
three largest operators all have this in-house already"* is. A threat at this level
invalidates every hunch beneath it — that is what separates it from a hunch's kill condition.

If they can't name one, say so plainly. A belief nothing could falsify absorbs any evidence
and never updates.

---

## Step 7 — Write, register, generate

Template: `references/interview-guide.md` → Step 8.

1. Agree the idea's name — it names the **field**, never the solution — and record it as
   `idea:` in the belief frontmatter; the brief and control room title from it.
2. Write `belief.md` as soon as the statement is agreed, before boundaries and threats are
   finished — the file is the session memory, so an interrupted conversation resumes from the
   missing section instead of re-interviewing. Set `last_confirmed` only once the founder
   confirms the whole file.
3. Create `reports/01-ideation/hunch-lineage.md` if absent, frontmatter only,
   `active_hunch: none`. **No H-entries.** The shotgun fills it.
4. `python3 scripts/build_brief.py`.
5. Append every observation about something missing, broken or harder than it should be
   to `signals/gaps-log.md`, which specifies its own format. Observations only.

---

## Step 8 — Hand off

```
Belief: input-context/belief.md — "{one-line quote}"
Lineage: reports/01-ideation/hunch-lineage.md — active_hunch: none
Brief: reports/BRIEF.md
Gaps logged: {N}

Next: /startup-ideate-shotgun   → explore mode: proposes candidate hunches
```

---

## Failure modes

- **Writing a hunch.** The one this skill exists to avoid. No H1, no working hypothesis, no
  "we might guess that…". An empty lineage is the correct output.
- **Writing the belief in your voice.** If the file reads more fluently than the founder
  speaks, you have replaced their anchor with yours.
- **Letting Step 4 become the shotgun.** Definitional research only — stop the moment you
  are ranking segments or sizing pain.
- **Accepting the first version.** Step 3 is the skill. A belief that took four questions is
  usually a hunch.
- **Asking a question without offering the precedent.** The founder is being asked to judge
  whether a constraint is permanent; handing them the field that already faced it is what
  makes that judgement possible instead of a guess. Silence here is not neutrality.
- **Turning SISP detection into a verdict.** It records how the founder arrived. Fluency is
  not clearance.
- **Asking what the founder's profile already answers.** Wastes intake's one advantage.
- **Letting the belief creep.** They refine it while talking, which is fine — the file records
  the confirmed version, not the most recent sentence.
- **Finishing without Step 7 items 3-5.** The ones that get skipped, leaving the next session
  with a stale brief.
