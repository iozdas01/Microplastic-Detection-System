---
name: startup-pitch-evolution
description: >-
  Owns the pitch narrative for one idea as a living artifact, keeps it honest against that
  idea's evidence ledger, and owns the one-slide version of it. Decomposes the pitch into
  claims, sources each to a ledger entry or the hunch lineage, and reports drift both ways:
  claims the evidence no longer supports, and evidence the pitch has not caught up with. Then
  drafts for a named audience, logs what changed, and rebuilds the slide. Use whenever the
  founder is preparing to pitch someone — investor, advisor, co-founder, or a contact who
  asked what they are building — or says "help me pitch X", "how do I explain this", "what's
  my story", "is my pitch still true", "what do I say about the market", "put this on one
  slide", or reads a pitch aloud and asks what is wrong with it. Also use after new evidence
  lands, to find the claims that just went stale. It never sends anything and never changes
  the hunch.
---

# Startup Pitch Evolution

A pitch is the founder's compressed claim about the world, and it moves faster than the
ledger does — it gets refined out loud, in conversations the repo never sees. That is fine
and normal. The failure is that nobody ever diffs the two, so the spoken version keeps a
clause the evidence killed three weeks ago, and the ledger keeps an answer to the exact
objection the founder is about to be hit with.

This skill is that diff, plus the drafting that follows it.

## What it owns

**One pitch file per idea**, holding every audience variant plus the version log. Find it
through the brief's `What already exists for this idea` inventory — a pitch author usually
already exists under `reports/{slug}/outreach/copy/`, sometimes hunch-scoped from when it was
written. Keep using whichever file the inventory names; a second pitch file is the drift this
skill exists to prevent. Only if none exists, create `outreach/copy/pitch.md`.

## Procedure

### 1 — Audience first, then load

Ask who the pitch is for if the founder has not said. It is not a stylistic question: the same
claim set is *ordered differently* for each audience, and using the wrong order is the common
way a pitch produces nothing. `references/audiences.md` has the four orders and what each
audience will check.

Then read, in this sequence: the brief; the active hunch's `### Statement` and `### Components`
in `01-ideation/hunch-lineage.md`; the whole of `03-validation/evidence.md`; the existing pitch
file. The ledger is the expensive read and the one that does the work — do not skip it to save
tokens, because the entire value here is knowing what is in it.

### 2 — Decompose into claims

Break the pitch — the existing one, or what the founder just said out loud — into individual
assertions about the world. One claim per row. Tag each with where it comes from:

| tag | means |
|---|---|
| `E{n}` | a ledger entry says this |
| `lineage` | it is in the hunch statement or components |
| `belief` | founder-owned, from `belief.md`, not something evidence decides |
| `edge` | a fact about the founder — background, capacity, access |
| **`UNSOURCED`** | nothing in the repo carries it |

Numbers are claims too, and they are where this goes wrong most often. A number without its
denominator named is unsourced even when the figure is right — "$3bn market" is not the same
claim as "$2.59bn of blind and shade *manufacturing shipments*", and an investor who checks
will find the difference. Carry the denominator into the pitch text itself, not just the table.

### 3 — Run the drift check, both directions

This is the part that is not drafting, and it is the reason the skill exists.

**Forward drift — the pitch is ahead of the evidence.** Every `UNSOURCED` row. For each,
either the founder names a source and it becomes a ledger entry, or it comes out of the pitch,
or it stays in explicitly marked as an assumption the founder is choosing to assert. Three
real options; picking silently is what gets someone caught.

**Backward drift — the evidence is ahead of the pitch.** Scan the ledger for entries dated
after the pitch's `last_updated` and ask two questions of each:

- Does any `contradicts` entry bear on a claim the pitch still makes? That clause has to be
  cut or narrowed to the part that survives. A contradicted claim is usually recoverable —
  there is a sharper true statement hiding inside the false one, and finding it is the job.
- Is there a high-confidence entry the pitch is *not* using? This is the quieter miss and
  often the more valuable one. Ledgers accumulate answers to objections nobody thought to
  put in the pitch, including arithmetic that pre-empts the exact question the audience opens
  with.

Report both lists before drafting. The founder decides what to do about each; several will be
judgement calls that only they can make.

### 4 — Draft, in the audience's order

Write the variant. `references/audiences.md` carries the order and the traps per audience.
General rules that survive every audience:

- **Mechanism before market.** A market number offered first is a number to be argued with.
  After the failure is pictured, it is a size.
- **Other people's behaviour beats your opinion.** Two companies spending money on the same
  gap is the strongest sentence available, and it costs nothing to say.
- **Volunteer the holes.** Anything checkable that you did not say is worth double against
  you when it is found. Name the unknowns as unknowns and they stop being ammunition.
- **The credential lands last.** Support, not a claim.

### 5 — Write it back, with traceability and a version entry

Append the variant to the pitch file with its claim table (the same claim-by-claim
traceability the outreach copy artifacts carry), then append to `## Version log`:

```
### {date} · {audience} · {what changed}
Forced by: {E-ids that moved it, or "founder judgement"}
Cut: {claims removed and why}
Added: {claims added and their source}
```

That log is the answer to "how is the pitch evolving" — the pitch itself only ever shows the
current state, and the shape of the change is what tells you whether the story is converging
or thrashing.

Then rerun the generators per `CLAUDE.md`.

### 6 — Rebuild the slide

A pitch that exists only as prose gets retyped into a deck by hand and drifts on the first
retype. So the short form lives in a `slide:` block inside the pitch file, and the page is
rendered from it — one author, and the slide cannot say something the pitch does not.

The block carries the five fields a panel or form asks for (one-liner, problem, solution,
team, market) plus the open questions, and every claim keeps its `cite`. Rendering the
citation on the slide is deliberate: on a page read by someone deciding whether to believe
you, "a customer told us this" and "we think this" must not look the same.

After changing the block, rebuild the page. The renderer flags on screen when content no
longer fits the fixed slide, because a bullet silently clipped off a fixed-size canvas is
invisible until the audience sees the gap — when that warning appears, cut copy rather than
shrinking type. Keep the slide's claims a strict subset of the long pitch's; if something
belongs on the slide but not in the pitch, it has skipped the drift check in step 3.

## Guardrails

- **Never invent a source.** If nothing in the repo carries a claim, it is `UNSOURCED`, even
  when it is obviously true and even when the founder said it confidently a minute ago.
- **Never change the hunch to make the pitch work.** If the pitch cannot be made honest
  without moving the hunch statement, stop and say so — that is a founder decision, and
  `CLAUDE.md` says only `[T]`/`[V]` buyer or site evidence may move it. Desk data and a good
  argument are not enough.
- **Log new facts as evidence, not as pitch prose.** Founders produce real evidence while
  talking through a pitch — a price, a conversation, a competitor's policy. That belongs in
  the ledger with a source, and the pitch then cites it. A fact whose only home is the pitch
  file has no confidence grade and no limits, and will be quoted forever.
- **Never send anything.** The founder pitches. This skill writes.
- **Write findings, never the method.** The output says what to say and what not to say. It
  does not explain what a hunch is, what an evidence grade means, or why the process works —
  the founder built the process.
