# Voice calibration — producing `content/x/voice.md`

Voice cannot be inferred from a repo. The artifacts here are written in a shared analytical
register that belongs to the framework, not to a person, and drafting from them without a
voice profile produces competent, generic, obviously-generated posts.

So the first run of this skill builds a profile from samples the founder supplies. It takes
one short conversation and then never has to happen again.

---

## Gathering samples

**Start with the transcripts.** The founder has already written thousands of words in their
own voice in past sessions, so asking them to go collect sample tweets is homework that
delays the first draft for no reason:

```bash
python3 .claude/skills/startup-x-draft/scripts/harvest_sessions.py --voice --min-chars 150
```

`--voice` drops bare operational instructions ("run it", "fix this") and keeps prose where
the founder is actually saying something. Forty of those messages is a better profile than
ten tweets, because they are unedited and unperformed.

One caveat to hold while reading them: this is the founder talking to an assistant, not to
an audience. Register carries over — word choice, sentence length, punctuation habits,
bluntness, how they hedge. Structure does not; nobody writes a hook for a coding session.

Then supplement, in descending order of usefulness:

1. **The founder's own posts**, if they have any — best, even the ones they think are bad.
   Especially those. Ask, but don't block the session waiting for them.
2. **Posts by others they'd be happy to have written** — reveals target register, which can
   differ from natural register and is worth knowing separately.
3. **Other writing in their voice** — a long DM, a Slack rant, a blog draft.

If transcripts are unavailable and nothing else exists, draft with `calibration: provisional`
built from the current conversation, mark queued drafts `voice: provisional`, and say plainly
that the first batch will be the weakest. Their edits become the samples.

---

## What to extract

Observable, checkable features. Vague notes ("conversational, authentic") don't constrain a
later draft, so record things a draft can be tested against.

- **Capitalization** — sentence case, all lowercase, or mixed? Consistent or mood-dependent?
- **Sentence length** — the actual distribution. Fragments? Long compound sentences?
- **Punctuation habits** — em-dashes, semicolons, ellipses, parentheticals. Note what they
  *don't* use; absences are as identifying as habits.
- **Profanity and intensity** — where the ceiling is.
- **Emoji and hashtags** — count them. Usually zero; record it explicitly so drafts don't add any.
- **Stance** — do they assert, hedge, ask, or undercut themselves? Self-deprecating or flat?
- **Technical density** — do they name specific tools and terms, or stay abstract?
- **Humor** — dry, absent, sarcastic, wordplay?
- **Recurring words and constructions** — their tics. Reproduce these; they carry more
  identity than any style adjective.
- **Openers and closers** — how a typical post starts and how it ends. Do they land on a
  question, a flat statement, a joke?
- **Non-English usage** — any second language that shows up, and in what contexts.

Also record what the founder is *not*, especially where the generic-LLM default would drift:
"never uses 'game-changer'", "never opens with a rhetorical question", "no thread emoji".

---

## Writing the profile

Write `content/x/voice.md` with frontmatter and prose:

```markdown
---
account: "@handle"
founder: <name — this file may name them; the skill body may not>
calibration: confirmed | provisional
sample_count: 14
sample_kind: own_posts | admired_posts | other_writing | conversation
last_updated: YYYY-MM-DD
---

# Voice profile

## Register
<2–4 sentences describing the voice as a person would hear it.>

## Observable rules
- <one checkable rule per line>

## Never
- <anti-patterns, including generic-LLM tells this founder would never write>

## Sample posts
<the raw samples, verbatim, so a later run can recalibrate without re-asking>

## Topic stance
<Where the founder sits on their own domain: confident about what, uncertain about what,
uninterested in what. Keeps drafts from putting opinions in their mouth.>
```

Keeping the raw samples in the file is what makes recalibration cheap later — a future run
can re-derive the rules rather than re-interviewing.

---

## Recalibration

Rerun this when the founder says drafts sound wrong, when they've edited several queued
drafts before posting (their edits are the best possible signal — diff the posted version
against the draft), or when they ask directly.

Update in place, bump `last_updated`, keep the accumulated samples and add the new ones.
Rewriting the profile from scratch throws away the calibration history that made it good.
