---
name: startup-interview-synthesis
description: Aggregates across all interviews for a specific assumption, computes cumulative evidence score, decides which of four outcomes to recommend (next_assumption / new_vertical / mutate_thesis / kill), and updates the assumption graph confidence. Reads all interview note files, contact card scores, and the assumption's position in the DAG. Writes synthesis.md, appends outcomes to evidence.md, and updates graph.md. Fires automatically via the outreach monitor cron when cumulative score ≥ 10 or when the founder invokes it manually. Use this skill whenever the user wants to decide what to do next after a batch of interviews — triggers on "synthesize interviews for A{X}", "what have we learned about assumption", "decide next step after interviews", "assumption synthesis", "should we keep testing", "kill or continue", "run synthesis", "cross the threshold", "aggregate interview evidence".
---

# Startup Interview Synthesis

Aggregate evidence across all interviews for one assumption, decide the next step, and update the assumption graph. This is the decision layer of the customer development pipeline — the skill that turns a pile of interview notes into a "do X next" recommendation.

## When you're invoked

Two entry points:

1. **Automatic** — the outreach monitor cron detected cumulative score ≥ 10 for an
   assumption and invoked you. Frontmatter of the invocation will note
   `trigger: cron_threshold_hit`.
2. **Manual** — the founder wants a mid-cycle read: "what have we learned about A2 so
   far, should we keep going?" Fire even if score is below threshold — the founder is
   asking for a status assessment, not just an outcome recommendation.

Either way, the synthesis is the same process. The difference is only in how you frame
the recommendation (with or without a strong "outcome" verdict).

## Inputs you need

1. **The assumption** — from `reports/{slug}/02-assumptions/graph.md`, find node
   `id: {A_ID}`. Read `assumption`, `category`, `parent_assumptions`, `child_assumptions`,
   `disconfirmation`, `stop_rule`. This tells you the DAG position — crucial for the
   outcome decision.

2. **All interview notes for this cycle** — glob
   `reports/{slug}/03-validation/{A_ID}-*/interviews/*.md`. Read every file. Skip files
   that only have raw notes above the `---` divider (uncaptured — those don't contribute
   to score yet). Read structured capture sections from all captured files.

3. **Contact cards** — read `reports/{slug}/outreach/contacts.md`. For every contact block
   where `{A_ID}` is in `assumptions_tested` AND `outreach_status == done`, pull:
   - `name`, `contact_role`, `role_pts`, `signal_type`, `signal_multiplier`
   - `outcome_modifier` (this is the founder-confirmed classification)
   - `evidence_score` (contact's contribution to this and any other assumptions)

4. **Existing evidence ledger** — `reports/{slug}/03-validation/evidence.md`. Filter to
   entries with `assumption_linked: {A_ID}`. This is your pre-existing base — synthesis
   incorporates it into the decision but doesn't double-count.

5. **Previous synthesis, if any** — check if
   `reports/{slug}/03-validation/{A_ID}-{date}/interviews/synthesis.md` exists. If it does,
   this is a re-run. Read it to know what you concluded last time and what's changed.

6. **Belief and hunch lineage** — read `input-context/{slug}/belief.md` and
   `reports/{slug}/01-ideation/hunch-lineage.md` when present. Resolve the active
   hunch so an outcome can distinguish “this assumption failed,” “this hunch
   failed,” and “the underlying belief is at risk.”

## The core calculation — score, then breakdown

### Cumulative score

For each done interview, compute:
```
interview_score = (contact.role_pts × contact.signal_multiplier) + interview.outcome_modifier
```

Where `outcome_modifier` maps:
- `strong_confirm` → +1
- `moderate_confirm` → 0
- `weak` → -0.5
- `contradiction` → -1

Sum across all done interviews for this assumption.

### Breakdown by role (this drives the outcome decision)

Group interviews by `contact_role` and compute:
- Per role: interview count, confirms count (any positive outcome_modifier), contradictions count, net contribution
- Look for **split signals** — is any one role net positive while another is net negative on the same assumption? That's the `new_vertical` trigger.

### Breakdown by signal_type

Also compute score contribution by signal_type. If all your evidence came from
`profile_fit` (cold contacts) and the score just barely made threshold, that's much weaker
signal than the same score from `post_engagement` contacts. Note this in the recommendation
even if the outcome is `next_assumption`.

## The decision tree — pick ONE outcome

Walk this in order. Stop at the first one that fires.

### 1. `kill`

Fires when:
- `cumulative_score ≤ 0` AND `interviews_completed ≥ 3`, OR
- Majority of interviews contradict AND no positive counter-evidence

If this assumption is a **root node** in the DAG (no parents), killing it kills every
child too. This normally retires the active hunch, not the belief. Create the
shotgun re-entry packet described below and flag any evidence that genuinely
threatens the belief for founder review.

If it's a **child node**, only this branch dies. Note which siblings are still alive.

### 2. `new_vertical` (segment is wrong)

Fires when:
- `cumulative_score ≥ 10`, AND
- Split signal: one contact_role is net positive, another is net negative on the same
  assumption

Concrete pattern: buyers say fine, practitioners are screaming (or vice versa). The pain
exists, but the ICP is wrong.

Create a shotgun re-entry packet for a sibling hunch focused on the role or
segment with positive signal. Do not launch outreach against the new segment
until that hunch is explicit and the founder activates it. Do NOT overwrite the
assumption's status — set it to `contested`.

### 3. `mutate_thesis` (different root cause)

Fires when:
- `cumulative_score` positive (any amount), AND
- The `unexpected findings` scan surfaces a recurring theme in 3+ interviews that reveals
  a different underlying problem than what the assumption states

Concrete pattern: assumption A2 was "H&S managers want robots to touch bolts"; interviews
consistently reveal that they actually want better *inspection data*, not physical
intervention. Same pain domain, different desired solution.

Create a shotgun re-entry packet for a child hunch with the different mechanism
or root cause. Include the specific interview quotes that caused the change.

### 4. `next_assumption` (confirmed, move on)

Fires when:
- `cumulative_score ≥ 10`, AND
- All roles net positive (or at least neutral), AND
- No `mutate_thesis` trigger, AND
- No `kill` trigger

Update `graph.md`:
- Set `status: confirmed`
- Set `evidence_quality: customer_interview` (assumption schema drives confidence
  automatically from this)
- Update `active_assumption` in the frontmatter to the next unconfirmed child assumption
  (or next Leap-of-Faith root if this had no children)
- Ranking rule: among unconfirmed children of this node, pick the one with highest
  `kill_power` tier, then highest `uncertainty_score` tier, then lowest `test_cost` (per
  the lexicographic ranking in `schemas/assumptions.md`)

If below threshold and manually invoked, don't force an outcome. Give the founder a
status report: "score X, {N} interviews done, {Y} until threshold, currently trending
positive/negative, keep going or pause."

## Common failure modes to avoid

- **Firing on a manual invocation when score is below threshold and the founder wanted a
  status check.** Read the invocation carefully. If it says "run synthesis" force it;
  if it says "how's it going" give a status.
- **Fabricating themes.** Every theme must be backed by 3+ actual interview quotes.
  Cherry-picking one contact's quote to invent a theme corrupts the whole system.
- **Missing the split-signal check.** This is the single easiest failure mode. Always
  compute per-role breakdowns before picking outcome.
- **Auto-killing children of a killed root without noting it.** The founder needs to see
  the blast radius, not just that A2 died.
- **Overwriting evidence.md entries.** Only APPEND. Never edit existing entries. The
  synthesis-level rollup goes at the bottom, not in place of individual interview entries.
- **Skipping the "actions requiring human decision" section.** Some things the skill sees
  but shouldn't act on autonomously (adding a new assumption node, restructuring the
  DAG). Surface them, let the founder decide.
- **Treating a killed root assumption as automatic proof the belief is dead.**
  Retire the hunch and flag belief-level tension; only the founder changes the belief.
- **Sending outreach to a newly inferred vertical before creating the sibling
  hunch.** The segment change needs an auditable hunch and founder activation first.

## Reference files

- `schemas/synthesis.md` — exact synthesis.md format + outcome decision tree
- `schemas/assumptions.md` — assumption graph node format + lexicographic ranking
- `schemas/evidence.md` — evidence entry format + quality ladder
- `schemas/contact.md` — contact card format + scoring formula
- `schemas/interview.md` — interview note format (what capture writes for you to read)
- `schemas/hunch.md` — belief/hunch distinction and lineage rules

## Mechanics

Step mechanics, templates and the failure catalogue live in `references/outputs.md`. Read the section for the step you are running.
