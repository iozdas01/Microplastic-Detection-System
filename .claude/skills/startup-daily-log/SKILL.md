---
name: startup-daily-log
description: >-
  Runs the founder's end-of-day close for one idea — appends a five-field entry (Truth, Moved,
  Learned, Next, Parked) to that idea's progress log, deriving what moved from the day's real
  file and git activity so the founder only supplies judgement. Then diffs today's Truth line
  against previous entries and says which of three states the work is in: progress, drift, or
  stall. Use whenever the founder wants to close out the day, log progress, write up what they
  did, check whether they are actually moving, or asks "what am I even working on" or "what
  truth am I chasing". Also use at the natural end of a working session even when the founder
  only says something like "right, that's me done" — the log is worth almost nothing as a
  record and almost everything as a stall detector, and it only works if it happens daily.
  Not for capturing a one-off observation; that is gap capture.
---

# Startup Daily Log

The founder's own words for why this exists: *"I constantly have to keep doing this at the end
of every day so that I can keep track of my own progress and what I am constantly working on."*

The method — what the five fields mean, why the Truth line is the only one that matters, and
the three states its diff can be in — is authored once in
`methods/practices/daily-truth-log.md`. **Read it before the first entry of a session.** This
skill is the procedure for running it, not a second copy of the reasoning.

## The split that makes this worth automating

Some of the entry is mechanical and some is judgement, and confusing the two is why founder
journals get abandoned.

- **Moved is mechanical.** It is recoverable from git and the filesystem. Derive it. Never ask
  the founder to remember what they did — at 9pm they will under-report, and an
  under-reported Moved makes a productive day look like a stall.
- **Truth, Learned, Next and Parked are judgement.** Only the founder has them. Ask.

That asymmetry is the whole value: four minutes of thinking instead of twenty of recall.

## Procedure

### 1 — Identify the idea and read the tail

Take the active idea from the founder's prompt; ask if genuinely unclear, never infer it.
Read the **last five entries** of `reports/progress-log.md` — you need the Truth history
to run step 4, and five is enough to see a stall forming.

If the log does not exist, create it with the header from an existing idea's log, the
`purpose:` line, and a note that it starts today. Do not backfill invented entries.

### 2 — Derive Moved

Reconstruct the day from evidence rather than memory:

```bash
git log --since=midnight --oneline --stat
git status --short
find reports input-context -newermt "today" -type f
```

Then read what changed, not just the filenames. What counts as a move: a conversation held, a
message actually sent, an evidence entry logged, a contact reaching a new status, an artifact
that changes a decision. What does not: reading, drafting that was not sent, refactoring,
regenerating derived files. Say so plainly when a day produced no moves — that is the reading
the log exists to make possible, and softening it destroys the instrument.

Derived files (`BRIEF.md`, `control-room.html`, `results-*.md`, generated pages) are noise
here. Filter them out; they change on every run and would make every day look busy.

### 3 — Ask for the judgement fields

Ask for all four in one message, not as an interrogation. Show the derived Moved alongside so
the founder is reacting to their real day rather than staring at a blank prompt. Yesterday's
Truth and Next are the strongest prompts available — show them.

Push back exactly twice, and only on these two failure modes, because everything else is
theirs to decide:

- **A Truth that is a topic, not a question.** "Understanding the market" can absorb
  infinite work and never resolve. A real Truth names a quantity or a behaviour and could be
  answered. Offer a rewrite rather than a lecture.
- **A Learned that asserts more than the day supports.** Desk research that confirmed a prior
  is not a learning. "Nothing" is a legitimate and frequent answer, and a log where every day
  produces insight is a log being written to look good.

### 4 — Run the diff and name the state

Compare today's Truth to the previous entries and say which state the work is in. This is the
part the founder cannot easily do for themselves, because each day feels locally reasonable.

- **Progress** — the Truth changed and evidence caused it. Name the evidence.
- **Drift** — the Truth changed and no evidence caused it. Say so directly. A new lane because
  the old one got boring always feels like insight at the time, and this is the only place it
  is visible. Do not soften it; also do not moralise, the founder may have good reasons.
- **Stall** — the Truth is unchanged and Learned has been empty for several days running.
  Report the count. The usual cause is a question that the activity being done cannot answer:
  desk work aimed at something only a buyer can settle. Name that possibility.

A Truth unchanged for a few days while conversations are happening is **not** a stall. It is
what a well-posed question looks like mid-test. Distinguish these; crying stall at healthy
persistence will get the log ignored.

### 5 — Show, confirm, append

Show the assembled entry and wait. Append only after the founder confirms — this is their
record of their own days and an entry they did not agree with poisons the sequence.

Append under `## Entries`, newest at the bottom, dated. **Never edit a previous day's entry.**
Amending the current day before it is closed is fine and normal.

On the last working day of the week, add one line answering: *did the Truth change this week,
and did evidence cause it?* Three words is enough.

## Guardrails

- **This file owns one fact:** what the founder was trying to find out on a given day, and
  whether it changed. Evidence belongs in the evidence ledger, contacts in the contact ledger,
  hunches in the lineage. If a Learned contains a citable claim, say it should be logged as
  evidence — do not log it here and call it done, and do not write it into both.
- **Never let the entry grow.** Five fields, a few lines each. The instinct to make it a proper
  status report is the thing that kills it. If the founder writes long, keep it; if the model
  writes long, cut it.
- **Per-idea state stays in `reports/`.** Two ideas keep two logs. The truth being
  sought is a property of the idea, not of the founder.
- **The log never changes a hunch or an assumption.** If the diff shows drift, say so and stop.
  Activating or retiring a hunch needs the founder's explicit word and belongs to the lineage.
