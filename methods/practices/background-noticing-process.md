---
name: Background Noticing Process
category: signal-detection
excluded_because: "needs the world: continuous capture, monthly review → `signals/gaps-log.md`"
applicable_at: [ideation]
assumption_categories_it_helps: [pain, market]
source:
  title: "How to Get Startup Ideas"
  author: Paul Graham
  url: http://paulgraham.com/startupideas.html
---

## Core Insight

Trying to generate startup ideas in a session is a frontal attack that almost always fails — it produces ideas that sound plausible but aren't. The organic alternative isn't passive waiting either. It's running a *background process*: working on real problems out of curiosity, while a second self watches for gaps and anomalies and notes them without trying to immediately evaluate them as startup ideas.

PG: "Work on hard problems, driven mainly by curiosity, but have a second self watching over your shoulder, taking note of gaps and anomalies."

The mechanism: good ideas come from external stimuli hitting a *prepared* mind. You can't control the stimuli, but you can prime the mind and you can keep the noticing apparatus on while doing other things. The journal is the key — not a startup ideas journal, but a gaps-and-anomalies journal. You're not trying to evaluate; you're trying to notice.

This is distinct from:
- **Emotional Signal Capture** (high-intensity emotional reactions as signals) — Background Noticing is lower-frequency and more cognitive: "that seems wrong" or "why doesn't X exist?"
- **21-day problem diary** — that's a focused observation period; Background Noticing is a permanent ambient mode

## Process

1. Stop trying to think of startup ideas directly — that mode produces plausible-but-bad ideas
2. Work on problems you find genuinely interesting, driven by curiosity rather than commercial intent
3. Run a second self in the background: when something seems missing, wrong, or harder than it should be — *note it*, don't evaluate it
4. Keep a gaps-and-anomalies log: brief entries, just the observation. Not "startup idea" — "gap" or "this seems wrong"
5. Periodically (weekly or monthly) review the log: do any patterns emerge? Do multiple gaps point at the same underlying absence?
6. Apply evaluation (Well Test, Path-Out Test, assumption extraction) only once you have a candidate from the log

## Example

Drew Houston didn't sit down and try to think of startup ideas. He forgot his USB stick and thought "I really need my files to be online." That's a background process firing: a gap noticed in the middle of doing something else, by a mind prepared by years of living with the problem.

Bill Gates and Paul Allen heard about the Altair. Their prepared minds — they knew Basic, they knew how software was written — immediately saw a gap: no one had written a Basic interpreter for it. External stimulus + prepared mind = organic idea.

## Limitations

- This is a long-horizon method — the best ideas take months or years of background noticing before crystallizing
- Hard to run in parallel with a deadline ("I need an idea this week") — PG explicitly says this is Plan A and on-demand idea generation is Plan B
- Requires being genuinely working on interesting things, not just waiting — the background process needs real stimulus to notice against
- The log can fill with noise; review and curation are necessary

## Connection to the Loop

This is the pre-loop method — the one that generates the idea seed that enters the loop. Once you have a candidate from the log, bring it into the assumption extraction step. Don't skip from "gap noticed" directly to building.

## How this method is actually run here

**Never dispatched as a shotgun lens.** That is what `methods/practices/` means — it is deliberately absent from `methods/shotgun-routing.yaml` and must stay absent. The shotgun asks "what does this lens say about the belief on the table?" — this method has no answer, because it does not analyse an idea you already have. It is the thing that hands you the idea in the first place. A research subagent given this card can only paraphrase it and invent a plausible journal, which then enters synthesis looking like evidence.

Its execution path is `signals/gaps-log.md`, in two halves:

- **Capture** (founder, ambient, continuous) — a message starting with `gap:` in any session in this repo appends a one-line entry. No evaluation, no follow-up questions; see the Gap Capture rule in `CLAUDE.md`. Friction is what kills this method, so the capture path is deliberately four seconds long.
- **Review** (agent, batched, roughly monthly) — cluster the accumulated log by underlying absence, not surface topic. A cluster with independent sightings graduates into the loop through `/startup-belief-intake`, which writes the new idea's `input-context/{slug}/belief.md`. This half *is* a genuine research task; it is simply offset in time rather than run inline.

`startup-interview-capture` also feeds the log: pains a contact raises that map to no assumption in the current graph are harvested as `type: interview-residue`. Those are the strongest entries in the file — unprompted, specific, and from someone living in the domain full-time rather than one founder noticing from one vantage point.
