---
name: startup-x-draft
description: >-
  Talks with the founder about what to post on X (Twitter), then drafts it in their voice.
  Mines recent session transcripts for what they actually said, offers concrete candidate
  topics, then drafts one post at a time and revises until they'd send it. Also pulls from
  an idea's `reports/` artifacts, outreach reality, or a pasted thought; drafts
  replies to posts the founder pastes in; and captions factory photos and videos staged in
  `content/x/media/`. Applies a disclosure ladder to private material, records grounding
  for checkable claims, and queues approved drafts in `content/x/queue.md`. It never
  posts; the founder posts by hand. Use whenever the user wants something posted on X or
  Twitter: "tweet this", "what should I post", "I need content", "make this a thread",
  "help me reply to this post", "caption this photo", or figuring out what's worth
  posting. Also to sanity-check a post they wrote, or build the voice profile at
  `content/x/voice.md`.
---

# Startup X Draft

Have a conversation about what's worth posting, then write it in the founder's voice.

This is a working session, not a batch job. The founder knows which of their thoughts has a
post in it and Claude knows what's in the files — neither half produces good posts alone.
So the shape is: arrive with concrete candidates, talk about them, draft one, revise it
together, queue it when they'd actually send it.

Two constraints hold throughout. **The founder posts** — public is irreversible and
screenshots outlive deletions. And **the readers overlap with the outreach targets**: the
plant managers, integrators, and lab researchers being cold-messaged also read X, so a post
that reads as growth-hacking or that quotes a private conversation costs a reply rate that
took months to build.

## Load first

1. `content/x/voice.md` — the profile. Missing? Run **Calibration** below first; it's fast
   and needs nothing from the founder. Drafting without it produces generic, obviously
   generated posts.
2. `references/craft.md` — hooks, what to cut, the CTA tactics that are off-limits here.
   Short; read every time.
3. `references/disclosure.md` — the four-tier ladder. Read whenever material comes from a
   private conversation, which is most of it.
4. `references/sources.md` — where postable material hides in each source, and the angle
   routing table.

## The conversation

### 1. Arrive with candidates, not questions

Opening with "what do you want to post about?" puts the work on the founder and usually
gets "I don't know." Instead, harvest first and come back with specifics:

```bash
python3 .claude/skills/startup-x-draft/scripts/harvest_sessions.py --days 14 --min-chars 120
```

That returns the founder's own messages from recent Claude Code sessions — where the real
thinking happened, in their own words. Skim for the things listed in `references/sources.md`:
a moment of surprise, a correction of their own earlier belief, a distinction that took
effort, a sentence sharper than anything a draft would produce.

Then open with **3–5 concrete candidates**, one line each: the thought, where it came from,
and which angle it would be. Something like "you said a lab told you data collection is
red-ocean and the evaluation layer is missing — that's a domain-insight post, and it
contradicts what you assumed three weeks ago."

Ask which one they want to take, and whether there's something on their mind that isn't on
the list. What they came in wanting to say beats anything harvested — the harvest exists to
prime the conversation, not to overrule it.

### 2. Talk before drafting

Once a topic is picked, spend a turn on it rather than jumping to text. What's the actual
claim? Who is it for? What do they know that the reader doesn't? Is there a number, and is
it real?

This is where most of the quality comes from. A post drafted from a half-understood topic
takes four revisions; a post drafted after one clarifying exchange usually takes one.

If it becomes clear there isn't a post here yet — the thought is real but thin, or the
evidence isn't there — say so and go back to the candidate list. That's a good outcome, not
a failed one.

### 3. Check disclosure before writing

Place every factual claim on the ladder in `references/disclosure.md`. Tier 0 and Tier 1
draft freely (Tier 1 anonymized to role plus company category). Tier 2 — naming a company or
person, or quoting anyone — needs an explicit yes, asked *before* drafting, since asking
after means handing them a draft they now have to reject. Tier 3 is never drafted.

Respect the evidence grade too: an `untested` assumption stated as a finding is the fastest
way for a knowledgeable reader to write the account off, and those readers are exactly the
ones worth reaching. The grade-to-phrasing table is in `disclosure.md`.

### 4. Draft one post, then revise with them

Show **one post, plus at most one genuinely different framing** — not four variants. Four
variants is a menu, and a menu turns a conversation into a selection task; the founder stops
telling you what's wrong and just picks the least bad one.

Write in the voice profile's terms and check against its **Never** list. The specific failure
mode is generic-LLM cadence: "it's not just X — it's Y", the rhetorical-question opener, the
tricolon, the em-dash pivot. If a line pattern-matches to generated text, rewrite it flatter.

Then ask what's wrong with it, and mean it. Revise in the session, as many rounds as it
takes. When the founder rewrites a line themselves, keep their wording — that line is now
the most accurate voice sample in the conversation, and it beats anything drafted.

When the source was a raw pasted thought, the job is compression, not addition: find the
load-bearing clause, cut what protects it, put it first. Never bolt on evidence they didn't
mention or numbers they can't source.

### 5. Queue it, then offer the next one

When the founder says they'd send it, append to `content/x/queue.md` using the entry format
at the top of that file (create it from `assets/queue-template.md` if absent). Record
`status`, `angle`, `disclosure`, `source`, and a **Grounding** table with one row per
checkable claim — that table is what makes the post defensible when someone replies
"source?", and writing it catches claims that drifted a grade stronger than the evidence.

Then offer the next candidate. A session that produces three posts is worth more than one
that produces a perfect one, and the founder is already warmed up.

### 6. Report honestly

Say which claims are Tier 1 anonymizations and what they were anonymized from, so the
founder can judge whether the disguise holds in a small industry. Flag anything resting on
an untested assumption.

## Replies and media posts

Two more entry points. Same conversation, same disclosure ladder, same queue.

**Replying to someone's post.** The founder pastes the post — text, link, or screenshot.
Reply craft has its own section in `references/craft.md`: shorter, one beat, add something
or don't send. Before drafting, check the author against the active idea's
`reports/contacts.md` — a public reply to someone mid-outreach is an outreach move,
and the founder decides it as one. Queue with `reply_to:` set to the post's URL.

**Captioning factory photos and videos.** The founder stages files in `content/x/media/`.
Section 5 of `references/sources.md` covers what to ask about a clip, what a caption does,
and the rights questions past-employer footage raises. Queue with `media:` set to the file
path; the founder attaches it by hand when posting.

## Calibration

No `content/x/voice.md`? Build it from the transcripts — the founder has already written
thousands of words in their own voice and should not be asked for homework:

```bash
python3 .claude/skills/startup-x-draft/scripts/harvest_sessions.py --voice --min-chars 150
```

`references/voice-calibration.md` says what to extract and how to write the profile. Confirm
the result with the founder in a few lines rather than a questionnaire — they'll correct it
faster than they'd fill it in. If they also have real posts of their own, those are better
still; ask, but don't block on it.

Recalibrate when drafts sound wrong, and whenever a queued draft gets posted — the diff
between drafted and posted text is the highest-quality voice signal available, because it's
a correction rather than an example. Ask for the live URL on the entry.

## Guardrails

- **Never post, never open a browser, never touch an X account.** This skill writes files.
- **Never invent a number, quote, or anecdote.** A fabricated figure in public is
  unrecoverable. If a draft needs a number the repo lacks, leave `<NEED: …>` and say so.
- **Never name a contact, quote a private thread verbatim, or post a screenshot of one.**
  Someone who replied to a cold DM did not consent to being a case study.
- **Never queue media the founder hasn't confirmed they may post.** Past-employer and
  customer-site footage can show proprietary parts, nameplates, or faces; ask whose
  facility it is and record the answer in the entry's Notes.
- **Never pull material from an idea the founder didn't name.** Cross-idea bleed is worse in
  public than in analysis.
- **Never write per-idea findings into `content/x/`.** Entries carry a `source:` pointer; the
  finding stays in `reports/`.
- **Never hand-maintain a count or status summary in `queue.md`** — it drifts from the rows
  beneath it.
- **Don't inflate.** If the thought was modest, the post is modest. A small true post
  outperforms a large inflated one to the readers who can tell the difference.

## Handoff

- The material is thin because the idea is early → the gap is evidence, not copy. Say so.
- The post being replied to is by someone in an idea's `contacts.md` → the reply is an
  outreach move; decide it with the founder against that idea's outreach position, and
  note it on the contact so the outreach skills see it.
- A draft exposes a real contradiction in the repo's evidence → note it and point at the
  assumption or synthesis skill. Don't resolve it inside a tweet.
