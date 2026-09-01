# Mining sources for post material

Four kinds of raw material feed this skill. Each hides its posts in a different place, so
this file says where to look rather than asking for a full read of every artifact — most of
these files are large and only a few lines of each are postable.

Read only the source the founder's request points at. If the request doesn't point at one
("write me some tweets"), start with the active idea's `BRIEF.md`, which is a generated
digest of the rest, then open at most one full artifact.

---

## 1. Conversation — the live session and past transcripts

The richest source, and the one the founder means when they say "pull from our convos."
Two halves:

**The live session** — the founder says "tweet this" about something just discussed. No file
reading needed; it's already in context.

**Past sessions** — `scripts/harvest_sessions.py` extracts the founder's own messages from
Claude Code transcripts, filtering out harness noise (slash-command wrappers, tool results,
system reminders, subagent sidechains).

```bash
python3 .claude/skills/startup-x-draft/scripts/harvest_sessions.py --days 14 --min-chars 120
python3 .claude/skills/startup-x-draft/scripts/harvest_sessions.py --voice --min-chars 150
python3 .claude/skills/startup-x-draft/scripts/harvest_sessions.py --json --limit 40
```

What to look for, in either half:

- **A sentence sharper than anything a draft would produce.** Use their words. Resist
  improving them — the impulse to smooth a rough phrase is what makes posts sound generated.
- **Surprise or annoyance.** "I don't get it, like where is A1, A2, A3????" marks something
  that genuinely mattered. Frustration is a reliable pointer to a real problem.
- **A correction of their own earlier belief.** The strongest post type available.
- **A distinction that took effort** — two things the founder separated that most people
  conflate.
- **Something a contact said, reported secondhand in the founder's words.** Often already
  half-anonymized by the retelling; still check it against `disclosure.md`.

Note what harvested messages are *not*: the founder writing for an audience. They're
thinking out loud with an assistant. The thought is the raw material; the post still has to
be built. Quoting a transcript line verbatim as a tweet usually reads as a fragment,
because it was one.

The failure mode is inflation: turning a modest observation into a Big Take. If the thought
was small, the post is small. A small true post beats a large inflated one.

---

## 2. Repo artifacts — `reports/{slug}/`

Start with `BRIEF.md` (generated, ~90 lines, current). Go deeper only for the specific
angle in play.

| File | What's postable in it |
|---|---|
| `01-ideation/hunch-lineage.md` | Retired and superseded hunches — finished stories with a wrong belief, a specific cause of death, and what replaced it. The best build-in-public material in the repo. |
| `02-assumptions/graph.md` | The riskiest untested assumption, phrased as an open question. Kill conditions — "here's what would prove me wrong" is a strong, rare post. |
| `03-validation/evidence.md` | `contradicts` entries first: evidence against the founder's own thesis. Then clusters — the same thing said independently by several people. |
| `03-validation/*/synthesis.md` | A decision made from evidence: what was killed, what survived, and the count behind it. |
| `04-mutation/thesis-v{N}.md` | The current position, and — more usefully — the diff from v{N-1}. What changed and why. |

The pattern that recurs: **a delta is a post, a state is not.** "The thesis is X" is a
brochure. "The thesis was X, N interviews later it's Y, here's the sentence that moved it"
is a post.

---

## 3. Outreach and interview reality — `outreach/`

The operational texture nobody else publishes. `contacts.md` and `outreach/email/` hold
reply rates, ignored messages, and what actually got a response.

Postable without touching Tier 2 disclosure:
- Aggregate response data on the founder's own sends — rates, what changed when copy changed.
- The category of message that worked, described structurally: what the opening line did,
  not who received it.
- Honest failure: a campaign that got nothing, and the diagnosis.

Never postable: contact names, message screenshots, anything that lets a recipient recognize
themselves. See `disclosure.md`. The person who replied to a cold DM did not sign up to be
a case study.

---

## 4. Founder-pasted raw thought

The founder drops a half-formed thought and wants it sharpened. No repo grounding required
or implied — do not go looking for evidence to bolt onto it, and do not add numbers that
weren't in what they said.

The job is compression, not addition: find the load-bearing clause, cut everything
protecting it, and put it first. Then offer variants that differ in *framing*, not in
decoration.

If the thought contains a factual claim the founder can't source, say so and offer the
hedged version alongside the confident one — they can pick.

---

## 5. Media — `content/x/media/`

Factory photos and videos the founder staged for posting. The visual is the post; the
caption's job is the context the pixels can't give. Filenames carry no context, so ask what
the clip shows — what part, what machine, what went wrong or what took skill — before
drafting. Photos can be read directly; videos can't be watched, so the founder's description
is the source.

What a caption does, in descending value:

- Names the thing a lay scroller can't see ("that chatter mark is a scrapped part").
- Says why it was hard, with a number where one exists.
- Ends. A media post rarely needs a third line, and never a CTA.

Disclosure is the sharp edge: footage from a past employer or a customer site can show
proprietary parts, fixtures, nameplates, or faces. Before drafting, ask whose facility it is
and whether the founder has the right to post it; the answer goes in the entry's **Notes**.
Old footage also invites "is this yours? recent?" replies — the caption should be honest
about when and where before anyone asks.

Queue entries for media posts set `media:` to the file path. The founder attaches the file
by hand when posting, same as the posting itself. A backlog of clips drafts well in batch:
caption several in one session, one queue entry each.

---

## Angle routing

Four angles, different audiences, different grounding bars. The angle changes who replies,
so pick deliberately rather than defaulting to whatever the source suggests.

| Angle | Audience | Grounding required | Where material lives |
|---|---|---|---|
| **Build in public** | Founders, potential hires, investors watching | The founder's own activity counts and decisions — Tier 0, so nearly always clearable | hunch-lineage, synthesis, outreach aggregates, live session |
| **Domain insight** | The actual buyers and operators — the outreach targets | Highest bar. Anything a practitioner could falsify must be `[V]`/`[T]` grade or attributed | evidence.md, companies.md, public sources |
| **Method / process** | Founder-adjacent, high engagement, low buyer value | Tier 0 by construction — it's the founder's own process | graph.md, methods library, the loop itself |
| **Contrarian** | Broad reach, high variance | Must be a position the founder can actually defend in replies, with the receipt in hand | `contradicts` evidence, retired hunches |

Two notes on the mix. **Domain insight doubles as outreach** — a plant engineer who argues
with a post is warmer than any cold DM, which makes it the highest-value angle even though
it reaches fewest people. And **contrarian without a receipt is just noise**: the test is
whether the founder can answer "source?" in one reply. If not, it's a method post instead.
