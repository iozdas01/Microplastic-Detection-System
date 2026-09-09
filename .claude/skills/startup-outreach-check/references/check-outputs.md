# Inbox check outputs

Classification taxonomy, routing table and reply-rate calibration formats for `startup-outreach-check`. The check flow itself is in SKILL.md.

## By strategy (outreach_pattern)

| pattern | sent | replied | rate | status |
|---------|------|---------|------|--------|
| hot_signal_specific_question | 3 | 2 | 67% | ok |
| cold_buyer_reciprocity | 5 | 1 | 20% | ok |

## Contact routing

| id | name | reply_type | next_step |
|----|------|------------|-----------|
| {id} | {Name} | substantive | → /startup-outreach-reply |
| {id} | {Name} | soft | → /startup-outreach-reply |
| {id} | {Name} | no_reply_14d | → flag / retire |
```

### Variant performance tracking

When writing `results-{A_ID}.md`, add or update a `variant_performance` block:

```yaml
variant_performance:
  V-close-A:
    sent: N          # count of contacts with this variant who have been invited
    accepted: N      # accepted the connection
    replied: N       # replied to the DM
    reply_rate: X%   # replied / accepted
  V-close-B:
    sent: N
    accepted: N
    replied: N
    reply_rate: X%
```

To compute this: read `contacts.md` → for each contact with `assumptions_tested` including the active assumption → read the `variant:` marker from their `[msg1 sent ...]` note (or the matching blast-session row as a fallback) → tally by outreach status and confirmed reply routing.

Report a "winner so far" line if either variant has ≥5 replies: "V-close-B leading: X% vs Y% reply rate (N total replies)." If fewer than 5 replies total, report "insufficient data — continue sending."

### Close-type performance — always report this cross-tabulated

The founder is running a standing comparison between two ways of ending a message, recorded per contact in `contacts.md` as `close_variant`:

- `direct_question` — ends on a concrete question about a specific past event
- `soft_ask` — ends on a low-commitment permission ask

Add a `close_performance` block to `results-{A_ID}.md`, **broken down by seniority tier, not pooled**:

```yaml
close_performance:
  direct_question:
    senior:   {sent: N, accepted: N, replied: N, reply_rate: X%}
    standard: {sent: N, accepted: N, replied: N, reply_rate: X%}
  soft_ask:
    senior:   {sent: N, accepted: N, replied: N, reply_rate: X%}
    standard: {sent: N, accepted: N, replied: N, reply_rate: X%}
```

**Why the breakdown is mandatory.** LR-B5 assigns the soft ask to senior contacts and the direct question to ICs by default, so a pooled reply rate confounds close-type with seniority: a weak `soft_ask` number could mean the close is worse, or simply that senior people reply less to everyone. Only the within-tier comparison isolates the close.

If any of the four cells is empty, say so explicitly rather than reporting a pooled number:

> Close-type comparison not yet interpretable: {cell} has 0 sends. Pooled rates would confound close with tier.

Recommend which cell to fill next, preferring the founder's lowest-value pending contact for the experimental cell — a weak-fit contact is the cheapest place to spend a send on learning.

Do not call a winner below 5 replies **within a tier**. Reply-rate differences on single-digit samples are noise, and acting on them would rewrite copy rules that were built on real evidence.

### Step 7 — Regenerate the tracker

```bash
python3 scripts/build_control_room.py
```

### Step 8 — Handoff

Tell the founder:

```
Inbox check complete for A{X}.

{N} new replies since {last_checked}.
  {N} substantive → Msg 2 (money question); capture after an interview happens
  {N} soft → Msg 2 (light follow-up, no money question yet)
  {N} negative → marked declined
  {N} no reply > 14 days → flagged in results file

{If any cluster hit regenerate threshold:}
  ⚠️  Cluster "{signal_type}/{degree}" has 0/{N} replies after 14 days — consider
  regenerating the angle before the next blast.

Results written to: reports/outreach/results-{A_ID}.md
Tracker regenerated.

Next steps:
  → /startup-outreach-reply A{X} for: {names of substantive + soft replies}
     Reply excerpts are in contacts.md → notes field. Skill reads them to anchor Msg 2.
  → /startup-interview-capture after a customer interview actually happens
```

## Reply-rate calibration

Treat prior reply-rate ranges as hypotheses, not promises. Compare the actual `variant_performance` and signal-type cohorts in this idea's results. `post_engagement` may be a stronger targeting signal, but Msg 1 wording still comes from the blast skill's fresh live-profile verification. `soft` replies that convert to substantive after a follow-up are common — don't abandon them.

If you're at 0/6 after 14 days on a cluster: the angle is wrong, not the list. Regenerate strategy before giving up on the contacts.
