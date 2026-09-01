# Outreach Monitor Cron — Configuration & Activation

This file is the source-of-truth for the cron monitor that watches every idea's
`outreach/contacts.md`, computes cumulative evidence score per assumption, and fires
`startup:interview-synthesis` when the threshold is crossed.

Two ways to run it — pick one based on how persistent you need it.

---

## Option A — Session-scoped monitor (in-session cron)

Uses Claude Code's `CronCreate` tool. Runs only while a Claude Code session is open.
Auto-expires after 7 days per Anthropic's runtime rules. Best for when you're actively
working through a validation cycle and want reminders while Claude is up.

**How to activate** (paste to Claude in an active session):

> Set up a daily outreach monitor cron. Use the prompt in
> `scripts/cron/monitor-outreach.md` under "Monitor prompt". Schedule for 09:23 local
> time daily (avoid the top of the hour to stay off the fleet-collision minute).

That will trigger Claude to call:

```
CronCreate(
  cron: "23 9 * * *",
  prompt: <see "Monitor prompt" below>,
  recurring: true
)
```

**Limitations:**
- Session only — closes when Claude Code exits
- 7-day auto-expiry per job
- Fires only when the REPL is idle

---

## Option B — Persistent monitor (cloud routine)

Uses the `/schedule` skill (cloud agent / routine). Runs anywhere, anytime, without
Claude Code being open. Best for when you have multiple ideas in-flight and want the
monitor running continuously in the background.

**How to activate** (paste to Claude in any session):

> Invoke the `/schedule` skill to create a persistent daily routine that runs the outreach
> monitor. Use the prompt in `scripts/cron/monitor-outreach.md` under "Monitor prompt".
> Schedule: daily at 09:23 local time. Name the routine `outreach-monitor`.

That will trigger the `/schedule` skill to create a cloud routine.

**Advantages over Option A:**
- Persists across sessions
- No 7-day expiry
- Runs even when you're offline

---

## Monitor prompt (used by both options)

```
Run the outreach synthesis monitor for the Startup Assumption Lab.

Working directory: /Users/izgin.ozdas/Documents/Personal/Startup Ideation

Steps:

1. Discover all active idea slugs by listing directories under `reports/` (each dir is one
   idea slug). Skip any dir that doesn't have `outreach/contacts.md` inside it.

2. For each idea slug:
   a. Read `reports/{slug}/outreach/contacts.md`
   b. Read `reports/{slug}/02-assumptions/graph.md` for assumption metadata
   c. Group contacts by their `assumptions_tested` field. A contact tested for A2 and A5
      contributes to both totals independently.
   d. For each assumption_id, sum `evidence_score` across contacts where
      `outreach_status == done` (only completed interviews count)
   e. Also count the number of completed interviews per assumption

3. For each (slug, assumption_id) pair, evaluate:
   - **Threshold fire**: cumulative_score >= 10 AND
     no `synthesis.md` exists for this validation cycle yet
     (or the existing synthesis has `trigger: manual` and score has grown by 2+ since)
     → invoke `startup:interview-synthesis` for that assumption. Do NOT wait for its
     completion; it can take a few minutes.
   - **Early-kill flag**: cumulative_score < 0 AND interviews_completed >= 3 AND
     no `likely_dead: true` flag exists on the graph node
     → set `likely_dead: true` in graph.md and notify the founder (don't auto-kill; the
     founder confirms)
   - **Stalled**: interviews_completed >= 3 AND 0 < cumulative_score < 5 AND
     no update in 5+ days → flag as stalled, suggest re-targeting

4. Build a summary of what fired vs what didn't:

```
Outreach monitor — {date}
─────────────────────────────────

Idea: {slug-1}
  A2  score 11.5  interviews 5   → SYNTHESIS FIRED (threshold met)
  A3a score 3.0   interviews 2   → below threshold, keep going
  A5  score -2.5  interviews 4   → EARLY-KILL FLAG raised (likely_dead)

Idea: {slug-2}
  A1  score 8.5   interviews 3   → below threshold
  A2  score 1.0   interviews 3   → STALLED (no update in 7 days)

No action needed on 2 other assumptions across 1 other idea.
```

5. Push a notification to the founder via any available channel (Claude Code push
   notification, push notification, or fallback: write summary to
   `reports/_monitor-log/{YYYY-MM-DD}.md`)

If any step errors (missing file, malformed YAML), log the error and continue with the
next assumption. Do not halt the whole monitor run because one slug is broken.

Be conservative with firing synthesis — it's a substantial operation. Better to skip a
borderline case (score 9.8) and let it fire tomorrow than to fire twice on the same cycle.

At the end, no unnecessary output — just the summary above.
```

---

## Testing before activating

Before scheduling either option, run the monitor prompt manually once to verify it works
with your current state:

> Run the outreach synthesis monitor once, right now, using the prompt in
> `scripts/cron/monitor-outreach.md`. Show me the summary but do NOT actually fire
> synthesis this run — I want to sanity-check what it would do.

If the dry-run summary looks right, activate Option A or Option B.

---

## Adjusting the threshold

The threshold `>= 10 points` is a project-wide default. If you want to tune it per idea
(e.g. "this idea needs stronger evidence, threshold 15"), add a `synthesis_threshold: N`
field to the graph.md frontmatter. The monitor prompt should be updated to read this field
and fall back to 10 if absent.

---

## What the monitor does NOT do

- **Doesn't run interview-capture.** That's the founder's manual step after each call.
- **Doesn't kill assumptions autonomously.** Early-kill flag is a suggestion; the founder
  confirms.
- **Doesn't re-target.** If synthesis outcome is `new_vertical`, the monitor doesn't spawn
  new outreach — the founder invokes `/startup-outreach-targets` with new ICP.
- **Doesn't chase no-reply contacts.** No auto-follow-ups from the monitor. Those live in
  the linkedin-outreach webhook flow.

---

## Deactivation

**Option A:**
```
CronList()
CronDelete(id: <the id it returns for outreach-monitor>)
```

**Option B:**
Invoke `/schedule` skill and remove the `outreach-monitor` routine.
