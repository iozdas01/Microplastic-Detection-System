---
name: Daily Truth Log
category: founder-process
excluded_because: "needs the founder at the end of a real working day; nothing to run in a shotgun → `reports/progress-log.md`"
runs_as: /startup-daily-log
applicable_at: [ideation, validation, mutation]
assumption_categories_it_helps: [pain, buyer, market]
---

## Core Insight

A founder log fails for one of two reasons: it records activity, or it costs too much to
write. Activity logs make a busy week and a productive week look identical, which is exactly
the discrimination the founder needs. And any format over about four minutes gets skipped on
the day it is most needed — the bad day, which is the day worth recording.

So this log records **one question, not a day's work**: *what truth am I seeking right now?*
One sentence, phrased so that an answer would change what happens next.

The value is not in any single entry. It is in **the diff on that one line**. Three states,
and each means something different:

- **The truth changed and evidence caused it.** This is progress, and it is the only kind.
- **The truth changed and no evidence caused it.** This is drift — a new lane because the old
  one got boring, not because it got answered. The log is the only place this is visible,
  because in the moment it always feels like insight.
- **The truth has not changed for ten days and nothing was learned.** This is a stall. Usually
  it means the question cannot be answered by the activity being done — desk research against
  a question only a buyer can settle.

Writing the question down daily costs four minutes. Not being able to tell those three states
apart costs weeks, and the predecessor repo lost several to exactly that.

## Process

At the end of the working day, append five lines to `reports/progress-log.md`. Never
edit yesterday's entry; the point is the sequence.

1. **Truth** — the one question you are trying to answer, as a question. If it is the same as
   yesterday, write it again anyway rather than referring back. Re-typing an unchanged
   question for the ninth day is the alarm doing its job.
2. **Moved** — what actually happened. Conversations held, messages sent, evidence logged.
   Reading and thinking are not moves. Be honest; nobody else reads this.
3. **Learned** — and what it changes. **"Nothing" is a legitimate and common entry.** A log
   where every day produces a learning is a log being written to look good.
4. **Next** — the cheapest thing that would move the Truth line. One sentence.
5. **Parked** — what you deliberately chose not to do today. This is the field founders skip
   and the one that later explains the whole month.

**Weekly, on the last entry of the week**, answer one extra question: *did the Truth change,
and did evidence cause it?* Three words is enough.

**A good Truth line names a quantity or a behaviour**, not a topic. "How often does a
made-to-order part arrive wrong, and who pays?" is a truth. "Understanding the
market" is a topic, and a topic can absorb infinite work without ever resolving.

## Where it lives

`reports/progress-log.md` — per-idea, append-only. Per-idea state never goes to a
root-level file or to memory. Two ideas run two logs, and that is correct: the truth being
sought is a property of the idea, not of the founder.

The log does not duplicate anything. Evidence lives in `evidence.md`, contacts in
`contacts.md`, hunches in `hunch-lineage.md`. This file owns exactly one fact those cannot
hold: **what the founder was trying to find out on a given day, and whether that changed.**
