# Synthesis outputs

The synthesis.md template, graph/evidence write formats, the shotgun re-entry packet and the notification format for `startup-interview-synthesis`.

## Writing synthesis.md

Follow `schemas/synthesis.md` exactly. The file lives at
`reports/03-validation/{A_ID}-{date}/interviews/synthesis.md`.

Structure:

```markdown
---
assumption_id: A{X}
assumption_text: "..."
synthesis_date: <today ISO>
trigger: cron_threshold_hit | manual | early_kill_flag
cumulative_score: <N>
interviews_completed: <N>
outcome: next_assumption | new_vertical | mutate_thesis | kill
next_target: <A_ID if next_assumption, else empty>
---

# Synthesis: A{X} · <date>

## TL;DR
<2-3 sentences: what was learned, recommendation, one-line reasoning>

## Score breakdown
<Table: contact, role, signal, outcome, score, notes>

Cumulative: **{N} pts** (threshold: 10)

## Breakdown by contact role
<Table: role, interviews, confirms, contradictions, net>

**Split-signal check:** <yes/no with explanation>

## Recurring themes
- Theme 1: <one-liner>
  Supporting quotes:
  > "..." — Contact name

## Unexpected findings
<Things surfaced that weren't in graph — potential new assumptions or mutations>

## Assumption graph position
- Node type: root | mid | leaf
- Parents: [...]
- Children: [...]
- If confirmed → children available to test: [...]
- If killed → what dissolves: ...

## Outcome and reasoning
**Outcome: {outcome}**

<Decision tree walked through explicitly:>
1. Cumulative score {N} vs threshold 10
2. Split-signal check: ...
3. Unexpected findings scan: ...
4. Score direction: ...

**Recommendation:** <what to do next>

## Actions taken
- <List of files updated>

## Actions requiring human decision
- <Things the skill surfaced but did not act on — founder decides>

## Shotgun re-entry
- Required: yes | no
- Packet: <path or none>
- Current hunch: <H_ID or unknown>
- Recommended lineage action: retain | child | sibling | retire
```

If this is a re-run (previous synthesis exists), move the previous content to a
`## Prior versions` section at the bottom (most recent first, each version keeps its date
and outcome).

## Updating graph.md

Based on outcome:

- **next_assumption:**
  - Target node: `status: confirmed`, `evidence_quality: customer_interview`
  - Frontmatter: `active_assumption: {next A_ID}`
  - Add evidence IDs to target node's `evidence_for: []`

- **new_vertical:**
  - Target node: `status: contested`
  - Frontmatter: `last_updated: <today>` (keep same `active_assumption` — the founder
    will re-target)
  - Add a note in the node's `notes:` field: "Segment split — buyers positive,
    practitioners negative. Re-targeting via new ICP."

- **mutate_thesis:**
  - Target node: `status: contested`
  - Add evidence IDs to `evidence_against: []` for the OLD framing
  - Frontmatter: `active_assumption` unchanged (mutation may add new assumption; the
    ideation shotgun will propose a child hunch before graph edits)

- **kill:**
  - Target node: `status: killed`
  - If root node: mark all children `status: killed` too, add note "Auto-killed via parent"
  - Add evidence IDs to `evidence_against: []`
  - Frontmatter: `active_assumption` → next unkilled root Leap-of-Faith assumption (or
    empty if idea is dead)

## Appending to evidence.md

For each interview that hasn't already been captured to evidence.md (some may have been
appended by interview-capture already — read the file, check for entries linked to
`{A_ID}` with the same date), add a summary-level entry with the aggregate finding. Not
one per interview — one per theme.

Confidence for synthesis-level entries: use the AVERAGE outcome_modifier as a proxy:
- Avg >= 0.5 → confidence 5
- Avg 0-0.5 → confidence 4
- Avg -0.5-0 → confidence 3
- Avg <= -0.5 → confidence 4 (contradictions are strong evidence)

## Writing the shotgun re-entry packet

For `new_vertical`, `mutate_thesis`, or `kill`, write:

`reports/01-ideation/reentry/{A_ID}-{date}.md`

```yaml
---
idea: {idea name}
belief_file: input-context/belief.md
current_hunch: H{N} | unknown
trigger_outcome: new_vertical | mutate_thesis | kill
assumption_id: A{X}
synthesis_path: reports/03-validation/{cycle}/interviews/synthesis.md
recommended_lineage_action: sibling | child | retire
evidence_delta:
  - E{N}
  - reports/03-validation/{cycle}/interviews/{file}.md
---

# Ideation Shotgun Re-entry

## What the interviews changed
<Evidence-led description; do not propose a product yet.>

## What remains intact
<Parts of the current hunch and belief not contradicted by this evidence.>

## Constraints for the next hunch
<Segment, mechanism, buyer, or timing constraints the next shotgun must respect.>

## Evidence that may threaten the belief
<None, or the exact evidence requiring founder review.>
```

Do not create a packet for `next_assumption`; that outcome retains the hunch and
continues validation. Do not automatically run the expensive shotgun from a
cron-triggered synthesis. Surface the packet path as the next action so the
founder can invoke `startup-ideate-shotgun` in reframe mode.

## Sending a notification

After writing synthesis.md and updating graph.md, produce a founder-facing summary. If the
skill was invoked by the cron monitor, this summary is what gets pushed as a notification:

```
SYNTHESIS FIRED · {idea} · A{X}
Outcome: {outcome}
Score: {N}/10 across {M} interviews
TL;DR: <2 lines>

Next action:
  {outcome-specific — either continue with the next assumption, or run
   /startup-ideate-shotgun in reframe mode using the re-entry packet}

Full synthesis: reports/03-validation/{A_ID}-{date}/interviews/synthesis.md
```
