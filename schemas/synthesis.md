# Schema: Interview Synthesis

One file per assumption validation cycle: `reports/{slug}/03-validation/{A_ID}-{date}/interviews/synthesis.md`

Written by `startup:interview-synthesis` — either fired by the cron monitor when
cumulative score ≥ 10 or manually invoked. This is a LIVING file — the skill overwrites
it each time it runs, appending previous versions to a `## Prior versions` section at the
bottom.

## File format

```markdown
---
assumption_id: A2
assumption_text: "Pain is real and expensive for operations managers in the target vertical"
current_hunch: H1
synthesis_date: 2026-07-20
trigger: cron_threshold_hit                 # cron_threshold_hit | manual | early_kill_flag
cumulative_score: 11.5
interviews_completed: 5
outcome: next_assumption                    # next_assumption | new_vertical | mutate_thesis | kill
next_target: A3a                            # if outcome == next_assumption
---

# Synthesis: A2 · 2026-07-20

## TL;DR

<2-3 sentences the founder can read in 20 seconds. What was learned, what's the
recommendation, what's the reasoning in one line.>

## Score breakdown

| Contact | Role | Signal | Outcome | Score | Notes |
|---------|------|--------|---------|-------|-------|
| Sarah Chen | practitioner | post_engagement | strong_confirm | 4.0 | Named £8k/incident |
| Marcus Bell | practitioner | comment_signal | strong_confirm | 3.5 | Corroborated cost |
| Priya Shah | buyer | profile_fit | moderate_confirm | 3.0 | Confirmed budget exists |
| ... | ... | ... | ... | ... | ... |

Cumulative: **11.5 pts** (threshold: 10)

## Breakdown by contact role

| Role | Interviews | Confirms | Contradictions | Net contribution |
|------|-----------|----------|----------------|------------------|
| buyer | 1 | 1 | 0 | +3.0 |
| practitioner | 3 | 3 | 0 | +7.5 |
| expert | 1 | 1 | 0 | +2.0 |
| influencer | 0 | 0 | 0 | 0 |

**Split-signal check:** are any two roles pointing in opposite directions?
<Yes / No, with explanation. If Yes → this is the "new_vertical" trigger.>

## Recurring themes

- **Theme 1:** <one-line theme that came up in 3+ interviews>
  - Supporting quotes:
    > "..." — Sarah Chen
    > "..." — Marcus Bell

- **Theme 2:** ...

## Unexpected findings

<Things that came up that weren't in the assumption graph — potential new assumptions or
mutations. If any of these are strong, they inform the `outcome` decision.>

- "..."

## Assumption graph position

- **Node type:** root | mid | leaf
- **Parents:** [list of parent assumption IDs and their current status]
- **Children:** [list of child assumption IDs that are gated by this one]
- **If this node is confirmed →** which children become available to test?
- **If this node is killed →** what dissolves?

## Outcome and reasoning

**Outcome: next_assumption**

<Detailed reasoning — the decision tree walked through explicitly:>

1. Cumulative score 11.5 ≥ 10 → threshold met
2. Split-signal check: no disagreement across roles → not new_vertical
3. Unexpected findings scan: any surface a different root cause? → no → not mutate_thesis
4. Score is positive → not kill

**Recommendation:** confirm A2, mark `evidence_quality: customer_interview`, `confidence: high`.
Next assumption to test: **A3a — Technical FMF** (child of A2, next in lexicographic order).

## Actions taken

- Updated `graph.md`: A2 → `status: confirmed`, `evidence_quality: customer_interview`, `confidence: high`
- Appended 5 evidence entries to `evidence.md`
- Set `active_assumption: A3a` in `graph.md` frontmatter
- Notified user via push notification

## Actions requiring human decision

- <List anything the skill flagged but did not act on autonomously. E.g. "Two contacts
  mentioned a compliance angle — recommend adding A6 to graph." Founder decides whether
  to add it.>

## Shotgun re-entry

- **Required:** no
- **Packet:** none
- **Current hunch:** H1
- **Recommended lineage action:** retain

For `new_vertical`, `mutate_thesis`, or `kill`, set `Required: yes` and link the
packet at `reports/{slug}/01-ideation/reentry/{A_ID}-{date}.md`. The lineage
action is respectively `sibling`, `child`, or `retire`.

## Prior versions
<Previous synthesis runs archived below the current one, most recent first. Each version
retains its outcome + score + date.>
```

## Outcome definitions (used for `outcome:` frontmatter field)

**`next_assumption`** — assumption confirmed. All roles consistent. Move to the next
unconfirmed child assumption (or next Leap-of-Faith root if no children).

Trigger conditions:
- `cumulative_score ≥ 10`
- No split-signal across roles (all roles net positive)
- No unexpected root-cause findings

**`new_vertical`** — pain is real but the target segment is wrong. One role type net
positive, another net negative. The idea isn't dead — the audience is.

Trigger conditions:
- `cumulative_score ≥ 10`
- Split-signal: one role net positive, another net negative on the same assumption
- Example: buyers say fine, practitioners are screaming → re-target practitioner-led orgs

**`mutate_thesis`** — pain is real but the underlying root cause / desired solution is
different from what the graph assumed. Interviews surfaced something not in the graph.

Trigger conditions:
- `cumulative_score` positive (any amount)
- Unexpected findings section names a recurring theme in 3+ interviews that reveals a
  different root cause
- Handoff: writes a mutation-request note to `04-mutation/{date}-mutation-request.md` for
  `startup:mutate-thesis` to pick up

**`kill`** — assumption dead. If root node, whole idea dies.

Trigger conditions:
- `cumulative_score ≤ 0` after 3+ completed interviews (early-kill flag from cron), OR
- Majority of interviews contradict AND no positive counter-evidence

## Score calculation rules

Every completed interview contributes:
```
interview_score = (contact.role_pts × contact.signal_multiplier) + interview.outcome_modifier
```

Cumulative score is the sum across all interviews with `outreach_status: done` where
`assumption_id` in `contact.assumptions_tested`.

If the same contact is interviewed twice for the same assumption (rare), both interviews
contribute. If interviewed for two different assumptions, each counts toward its own
assumption's total.

## Living file behavior

- On first run: write file fresh
- On re-run: read existing file, move current content to top of `## Prior versions`
  (dated), then write new synthesis at top
- Frontmatter always reflects the CURRENT synthesis, not historical
