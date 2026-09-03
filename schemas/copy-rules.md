# Copy rules — the durable outreach copy contract

Loaded before drafting any outreach message, by `startup-outreach-draft` (Msg 1) and
`startup-outreach-reply` (Msg 2+). **This file is the single author of what copy may say
and of what Claude may click.** A skill body that contradicts a rule here is wrong.

Rule IDs (`LR-B*` draft, `LR-M*` reply) are cited across `contacts.md` notes and the
per-idea copy archives, so they never get renumbered. The dated evidence behind each rule —
which contact, which founder edit, which reply — lives in the per-idea journal at
`reports/{slug}/outreach/copy-rules-log.md`; this file carries only the rule that survived.

---

## Send permission — the hard boundary

**Claude NEVER sends a message it drafted on its own authority.** Draft it, show it, and
wait. The founder decides what leaves the account.

**AMENDED 2026-08-25 (founder decision): Claude MAY send a message whose exact final text
the founder has approved in chat.** The approval workflow:

1. The draft is logged in the copy archive and visible in the control room's Pending
   tasks panel; the founder reads the actual text there or in chat.
2. The founder approves in chat, naming the contacts ("approved: C23, C41" or "send all
   the Msg 1 drafts"). An approval names the logged draft as it stands; if the draft is
   edited afterwards, the approval lapses.
3. Before each send Claude opens the contact's own message thread from their profile,
   confirms the thread header name matches the intended contact, pastes the approved text
   VERBATIM (no edits, however small — an edit needs re-approval), and sends.
4. Each send is logged in the contact's notes as `[msg{N} sent]` with date, "sent by
   Claude, founder-approved in chat", and the founder-visible dashboards are rebuilt.

Approval is per-message and does not roll forward: yesterday's "send them all" does not
cover drafts written today. On any mismatch (wrong name in the thread header, draft
missing from the archive, text differs from the approved version) Claude stops and
reports instead of sending. Unapproved messages remain founder-sent by hand, always.

**Claude MAY send a bare connection invite** to a 2nd/3rd-degree contact — always
"Send without a note". A note is message text riding on an irreversible send, so it falls
under the message ban.

**LR-B29 — First invites NEVER carry copy (founder rule, 2026-08-24).** A 2nd/3rd-degree
first touch is a bare connection request, always — no connection note, whether Claude
clicks it or the founder does. Connection notes are retired entirely: the first copy any
contact receives is Msg 1, a DM drafted after they accept (or immediately, for a
1st-degree contact). This supersedes every older reference to a "connection note" or its
250-char cap.

Before any invite click: read the display name from the live profile heading, confirm it
matches the intended contact, and confirm the button belongs to the primary profile card
rather than a sidebar recommendation ("People also viewed" cards carry their own invite
affordances, and a loose selector once hit one). On any mismatch, stop and report.

**The only safe selector is the one carrying the contact's NAME (measured 2026-09-03).**
Scoping to the primary card is not enough and neither is excluding `<aside>`: the
"People similar to…" strip renders other people's Connect buttons in the page body, outside
any aside. Gate every click on `aria-label` matching `Invite {intended name} to connect`, and
confirm again against the name printed in the invitation modal before pressing send. Two
name checks, or don't click. Also expect the control to be an `<a>` on some profiles and a
`<button>` on others, the modal to live in a shadow root, and Connect to sit inside the
"More" menu on 3rd-degree profiles rather than on the card.

**Fastest reliable route:** `linkedin.com/preload/custom-invite/?vanityName={slug}` opens the
invitation modal directly, skipping the card and the More menu entirely. The modal names the
recipient, which is the second name check, so this route is both quicker and safer.

**No daily invite cap (founder decision, 2026-09-03).** The previous "roughly 20 invites/day,
100/week" guidance is removed at the founder's explicit instruction. Send as many invites in a
day as the founder asks for; do not defer or trim a batch on volume grounds, and do not
re-raise the cap as a concern on later runs — it has been decided.

**AMENDED same day (founder instruction, 2026-09-03): space the sends out.** The cap is still
gone — VOLUME is not limited — but the founder asked that a batch not be fired at machine
speed, to keep the account clear of LinkedIn's rate heuristics. Leave roughly 20-40 seconds
between invites and vary it; a 70-invite batch is therefore a ~40-minute run, and that is the
expected shape, not a problem to optimise away. The two rules are not in tension: send every
invite the founder asked for, just not all in the same minute.

Nothing here licenses re-opening the cap question. If a run needs to be cut short, that is a
platform response (below) or a founder decision, never a volume judgement of Claude's own.

What remains is LinkedIn's own behaviour, which is theirs and not ours to set: the account can
be rate-limited or restricted, and the warning signs are a captcha, an "unusual activity"
interstitial, or the Connect button silently failing. On any of those, STOP sending
immediately and report — that is a platform response to observe and act on, not a quota to
pre-empt.

---

## Msg 1 — the first DM (after acceptance, or to a 1st-degree contact)

**LR-B1 — Translate title into observable activity.** The grounded clause transforms the
contact's role into an activity they would recognise as what they actually do:
`you + verb + concrete noun + at {company}`. Never the raw title, never certifications. It
proves a human looked at the profile; a generic bridge reads as formulaic and is discounted.

**LR-B23 — The research anchor is per-sender. Never borrow one founder's verifiable claim
into a message sent from another's account.** Read `linkedin_account` and use that sender's
own anchor, from `outreach_identity.credibility_hook` in that founder's `founders/{name}.md`.
An anchor survives a click-through only on the account whose profile actually carries it; used
from any other account it is a claim that fails verification, which is the failure LR-B14
already bans, applied to the sender's profile instead of the recipient's.
A sender with a strong track record uses a **credential** anchor, not a humility one: the
most relevant verifiable thing on their own profile, then the LR-B1 grounded clause, then a
reciprocity offer ("happy to share back whatever's useful"), which gives the recipient a
reason the exchange is not purely extractive. No trailing smiley, per LR-B3.
**Language exception:** match the thread's language. Russian threads keep the Russian `)`
convention, which is ordinary punctuation there rather than the emoticon LR-B3 bans.

**LR-B26 — When a real shared context exists, lead with it and name a specific human inside
it.** If sender and contact share an institution, cohort, course or programme the sender was
actually present in, that context REPLACES the research anchor as the opening, and the message
names a specific human inside it by first name with regards passed on. Naming the shared human
is unforgeable — anyone can claim an affiliation, only someone who was there produces the
instructor's name unprompted. It also inverts the power dynamic: an alumna is useful TO the
contact rather than extracting FROM them. Pair it with volunteering a short finding from the
sender's own research instead of requesting one. Does not apply to generic overlap ("we both
studied engineering") or anything inferred from a profile field.
**The trap, and it is the important half.** This shape reaches naturally for a reassurance like
"based solely on your personal opinions and experience". That is excellent for reply rate and
the exact opposite of Mom Test discipline. Acceptable in Msg 1, whose only job is to earn a
yes — but it sets an expectation the drafter must then deliberately break. **Msg 2 must not
harvest opinions.** Pivot to what the contact has done, in the same warm register. A message
that invites opinions and then collects them produces generous, articulate, unusable answers
that enter the ledger as durable soft evidence. See LR-M3.

**LR-B2 — The research statement is a puzzle, not a topic label.** Puzzle shape: `why X
differs from Y`, `where the money actually goes when Z`, `what makes some A behave like B`.
Not `researching {domain}`. A topic label reads as extraction; a puzzle reads as a question
the recipient is probably curious about too.

**LR-B17 — The frame is the last thing you cut, not the first.** Every message opens with
the research question before the grounded clause. Over the cap, compress the ANCHOR. An
anchor with no frame is not a shorter message, it is an audit: a stranger naming something
you did and asking a pointed question about it. Self-check: read only the first sentence —
does it state a question someone could disagree with? A pointer ("that is the part I wanted
to ask about") names no question and is not a frame.

**LR-B16 — Anchor on something CENTRAL, not merely verbatim.** Preferring the contact's own
words is not licence to grab any quotable line. Rank profile material by weight (years in
role, whether it is current, share of the role description) and draw from the heaviest.
A clause built on a minor bullet from a role they left proves you looked and still got the
emphasis wrong — worse than generic. Position and tenure are legitimate anchors; keep them
precise ("seven years at the company, now in R&D" ≠ "seven years in R&D").

**LR-B4 — Domain-scope every ambiguous noun.** `fleets`, `campaigns`, `assets`, `sites`,
`platforms` all carry cross-industry meanings. Cold recipients scan in under five seconds;
one ambiguous noun forces a re-parse and loses them.

**LR-B18 — Msg 1 asks permission. It never asks the question.** This is the default for
EVERY first message, not only for contacts who could buy later — widened 2026-08-10 after
the narrower "could become a customer" wording let a batch of site/data-source drafts open
with the substantive question instead. The grounded clause and the research frame stay; only
the close changes, and the specific question moves to Msg 2 after they say yes.

The shape, and nothing more than the shape — greeting, research frame, grounded clause,
permission ask, stop:

> {First name} hi! How are you?
>
> I am currently researching {the puzzle, per LR-B2} {sender's anchor, per LR-B23}, and
> specifically {the segment clause, per LR-B28}. {One grounded clause about them, per LR-B1}.
> Would you be open to some questions by any chance for our research?

**Sent specimens live with the idea that produced them**, in
`reports/{slug}/outreach/copy/{A_ID}-linkedin.md`, never here: a specimen is evidence about one
market and one contact, and a rule page that accumulates them turns into that idea's archive.
Read the shape here; read real sent copy there.

**LR-B27 (2026-08-10, founder-set; CORRECTED the same day from the founder's own sent copy) —
never "my research partner". Substitute a verifiable institutional anchor, do not just delete
the clause.** Founder instruction, verbatim: *"don't say research partner just say I am
researching."*

**The first version of this rule over-corrected**, to first-person singular throughout —
"my research" in the close as well. The founder's own next sent message did neither, and it is
what settled the rule: it named an institution and kept the plural close.

So the objection was never to the plural. It was to naming an unidentified second **person**. An
institution is not a person: it is checkable in one click, adds standing rather than confusion,
and makes "our research" coherent instead of raising "whose?".

**What to write.** Drop "my research partner" always. Then either name the sending founder's own
verifiable institution — their `outreach_identity.credibility_hook` in `founders/{name}.md`, which
is the one author of that anchor, and per LR-B23 only ever their own — or say plainly "I am
researching". "Our research" in the close is fine and is the founder's own habit; do not change
it to "my".

The rule is about who the recipient thinks they are talking to. A named-but-absent second person
adds a party the recipient cannot see, cannot address and did not agree to, and it makes a
one-to-one message read as a project. The plural close compounds it: "our research" invites the
question "whose?" at exactly the moment the message is asking for a yes. Both founders may work
on the same research; the message is still from one person.

Applies to every message from either account. `linkedin_account` already decides whose anchor is
used (LR-B23); this rule decides the voice, and the voice is always singular.

Why the permission ask rather than the question, given it carries no payload: the ask is
small enough to answer in one word, and a yes converts a cold contact into an open thread
where the real question arrives as a reply rather than as an ambush. The campaign's measured
reply rate on this shape has run around 30% of contacted (see the campaign's own
`results-{A_ID}.md`), which is the evidence that settles it. Do not "improve" Msg 1 by moving the question forward.

**Scope limit — this governs FIRST contact only.** A follow-up to someone who already
received the permission ask and did not answer must NOT repeat it: that ask has already
failed for that person once, and re-sending it is the same message with a stamp on it. Second
attempts carry the question, on the reasoning that a person who ignored a low-information ask
may still answer a concrete one.

**LR-B28 (2026-08-11, founder-set) — the research frame names what you want to learn FROM THAT
SEGMENT. There is no house frame.**

The opening stays constant across segments — the puzzle and the sender's anchor. The
`and specifically…` clause is what moves, and it names the thing *that segment* has first-hand
knowledge of. Write one frame clause per segment the campaign touches, and keep each in the
segment's own words rather than the market's.

**What went wrong, because the failure is subtle and will recur.** A batch of six was drafted
with the assumption node's own internal puzzle pasted into all six, regardless of segment. It
passed every other rule on this page. It was still wrong, for two reasons:

1. **It is a restatement of the assumption, which is LR-2 in a costume.** The axis a node turns
   on is OUR framing of OUR node; the people we are writing to think in terms of their own
   workflow, not our dichotomy. The test LR-2 already states applies here too: would this phrase
   appear in a post the contact wrote?
2. **The second attempt named a topic, not a problem.** Naming the subject area tells the
   recipient what you are interested in and gives them nothing to answer. LR-B2 already requires
   the frame be a puzzle; the segment clause is where that puzzle actually lives.

**The knock-on effect is the tell that this rule is right.** Once the frame matched the segment,
the grounded clause that fit it changed too, and improved — in the redraft, hedged alternate
anchors became obvious ones, because a clause that answers the segment's own question is exactly
the clause that fits. **If the frame is right, the best anchor becomes obvious. If you are
agonising over which anchor to use, check the frame first.**

Every message also got 50 to 65 characters shorter, because the abstract puzzle was buying
nothing.

**LR-B11 — No money question in Msg 1 or Msg 2.** Ask about time, surprises and unplanned
work. Time is free to disclose and flatters expertise; cost asks a stranger for
commercially sensitive information, and time answers usually contain the cost structure
anyway. Escalation ladder:

| Msg | Ask |
|---|---|
| 1 | the puzzle + one specific past event |
| 2 | what took the longest / what surprised them |
| 3 | whose scope it fell on, theirs or the customer's |
| 4 | roughly what share of the job went to it |
| 4b | who at their company actually sees that cost land (the referral ask) |

An assumption whose `next_action` names a money question is describing the *interview*, not
the first message. Do not copy it into cold copy.

---

## Register and banned forms

**LR-B24 — No cliché or stock cold-outreach phrases.** Reject any draft containing a
blacklisted stock phrase before it reaches the founder, case-insensitive, the same mechanism
as the em-dash and cert-token checks. Add newly caught phrases as they turn up. This closes
the gap adjacent to LR-B1: that rule bans the generic *bridge*, this one bans borrowed
*sales*-speak going the other direction. It is a style floor, not a substitute — a message can
be cliché-free and still be a generic bridge if it skips the grounded clause.

**LR-1 — Never recite the raw title, certifications or headline.** Acknowledge experience
through the observed-activity clause.

**LR-2 — No internal research vocabulary.** Terms coined in the assumption graph, intel
files or method outputs never appear unless the contact used that exact term publicly
first. Test: would this phrase appear in a post the contact wrote?

**LR-3 — Full sentences; ZERO em-dashes.** Every beat is a sentence a human would type on
their phone. Em-dashes are a recognised AI-tell and are banned outright. If characters are
tight, cut a whole element rather than compressing into fragments.

**LR-B3 — No emoji, smileys or tone-softening exclamation marks in Msg 1.** The puzzle
carries the tone; punctuation stays neutral.

**LR-6 — Honorific register consistency.** In languages with a formal/informal split, an
honorific locks the whole message to the formal register. Mixing reads as machine
translation. Informal register only for warm 1st-degree contacts without the honorific.

**LR-B14 — The sender's own claims must survive a profile click.** Any first-person claim
must be corroborated by the sender's own profile as it currently reads. LR-B6 pointed the
other way, and it binds for the same reason: an interested recipient clicks, and one
incongruence stops the read. Affiliations that carry no recognition with the target
population cost a clause and return nothing. "I have not built anything yet and would
rather hear it from someone who has" is congruent, lands where the sales filter fires, and
hands the recipient the higher-status seat. Founder credibility hooks live in
`founders/*.md → outreach_identity.credibility_hook`; use the sending founder's own.

### Rejection rules (auto, before the clause reaches the review table)

1. Message over its cap: **~450 chars** for a DM (connection notes no longer exist — LR-B29).
2. Contains the contact's raw `role` substring (case-insensitive).
3. Contains a cert token: `IRATA`, `L1`, `L2`, `L3`, `GWO`, `NDT`, `LEEA`, `PDCA`, `PMP`,
   `PMI`, `PE`, `PhD`, `MPhil`, `MSc`, `MBA`, `CEng`, `CFA`, `Prince2`, `Six Sigma`.
4. Contains internal research shorthand (LR-2).
5. Uses a hyphen-joined fragment as the primary clause structure (LR-3).
6. Contains a cliché: `hope this message finds you well`, `came across your profile`,
   `pick your brain`, `circle back`, `touch base`, `synergy`/`synergies`, `leverage` (verb),
   `move the needle`, `low-hanging fruit`, `at the end of the day`, `in this day and age`,
   `game changer`, `no brainer`, `thought leader`, `deep dive` (verb), `double-click on`,
   `let's connect` (close), `quick question` (opener), `just following up`,
   `reaching out because`, `I'd love to`.

**Placeholders in negative examples.** Every *negative* example in any skill file uses
`{placeholders}` — never a real contact, company or cert string. Positive examples may use
reply-backed specimens, but the rule text must direct imitation of *structure*, not content.

---

## Pre-draft verification

**LR-B25 — Check the SENDING account's inbox first; "1st degree" is not "never messaged."**
Mandatory before drafting any Msg 1, on the account named in `linkedin_account`.

**SEARCH THE FIRST NAME, NOT THE SURNAME. Corrected 2026-08-10 after the surname form produced
five false negatives in a single session.** This rule previously said to search
`?searchTerm={surname}`. That instruction is wrong and it is dangerous, because it fails
SILENTLY — an empty result looks identical to a genuine no-thread.

Measured the same day, on the same account, minutes apart:

| Contact | surname search | first-name search | truth |
|---|---|---|---|
| Zach Collins | "Collins" → nothing, twice | "Zach" → thread, Jul 28 | already messaged |
| Filippo Mearini | "Mearini" → nothing | "Filippo" → thread, 17:39 | already messaged |
| Joey Marimberga | "Marimberga" → nothing | "Joey" → thread, 18:29 | already messaged |
| Clynton Thoresson | "Thoresson" → nothing | "Clynton" → thread, 17:13 | already messaged |
| Olgac Aker | "Aker" → nothing | "Olgac" → thread, 20:37 | already messaged |

**Procedure.** Search the FIRST name. If the first name is short or is a substring of a common
word, it will match message *bodies* and return noise — "Engin" matches "engineer" — so in that
case search the COMPANY instead ("Robust" also found Zach Collins). Always run a positive
control in the same batch: a contact known to have a thread must come back with it, or the
search is not live and every negative in that batch is void.

The inbox state decides what this message even is:

| Inbox state | What to draft |
|---|---|
| No thread | Msg 1 as normal |
| Thread exists, they replied | Not this skill — hand to `/startup-outreach-reply` |
| Thread exists, ours is last, < ~7 days | **Nothing.** Say so and hold |
| Thread exists, ours is last, silent ≥ ~2 weeks | A follow-up, not a re-introduction |

Degree alone cannot catch this: a 1st-degree contact is *more* likely than average to have been
messaged before, because something caused the connection. A contact card cannot catch it either
— it records when this repo found them, not when the founder last wrote. And a missing
`private/linkedin-export/` makes `startup-outreach-targets` Pass 0 fail silently, so a batch
looks cold when it is not. Missing export means "prior contact unknown, go and look."
A follow-up after silence carries NO research anchor (the frame is established; restating it
reads as a mail merge) and does NOT repeat the ignored ask — a second unanswered call ask
converts silence into a decision.

**LR-B30 — Re-contact decays with time and is bought back only by position (founder rule,
2026-09-02).** LR-B25 says what the inbox state IS; this says whether to write at all. The
founder's instruction, verbatim: *"the people i messaged before i dont want to message again
depending on how old they are and the importance of their position."*

Two variables, and they are not symmetric. Time is a gate; seniority is a modifier that only
operates once the gate is open.

| Prior state | Age | Buyer-authority role | Anyone else |
|---|---|---|---|
| Ours last, no reply | < 3 months | **Do not write.** | **Do not write.** |
| Ours last, no reply | 3 to 12 months | Follow-up, no anchor, no repeat of the ignored ask | Drop |
| Ours last, no reply | > 12 months | Fresh Msg 1 | Drop |
| **They replied** | any | Not a re-contact at all | Not a re-contact at all |

**Buyer-authority role** means a leadership token per LR-B5: Chief / VP / President / Head of
/ Director / Owner / Managing Director. Seniority never opens the < 3 month gate. A VP who
ignored a message three weeks ago ignored it as deliberately as an engineer did, and writing
again converts a soft non-answer into a hard one for someone worth more later.

**A reply, at any age, is not a re-contact.** It is an open thread and it is the most valuable
asset in the ledger, so it routes to `/startup-outreach-reply` rather than being counted
against this rule. Do not let "I do not want to message people again" retire the people who
answered; they are the opposite case.

Below the gate the contact is not off_scope, because nothing about their ICP fit failed, and
it is not `no_reply` either: that status means "we messaged them for THIS assumption and they
went quiet", and it counts as contacted in the funnel. Set **`outreach_status: held`**, add a
dated note citing this rule and the date they become eligible, and let them age back in.
A held contact is not in the campaign and must never appear in a contact-rate or reply-rate
denominator.

**LR-B6 — Claims must be live-snapshot verifiable.** Every factual claim about the contact
must be derivable from a live profile snapshot taken in the current session. `contacts.md`
notes and any cached intel are advisory only. Cached descriptions drift, and the recipient
knows their own role better than any cache.

**LR-B13 — Read connection degree, and always fetch the experience detail page.**
Degree decides which message this is: `1st` with a Message button → DM, `accepted`
connection → Msg 1 DM, `2nd`/`3rd+` with an invite affordance → bare invite, nothing to
draft (LR-B29), `Pending` → nothing to draft. Fetch `{profile_url}details/experience/` as a separate page: the main profile
lazy-loads, and the experience page carries each role's verbatim description — the contact
describing their own work, which is the best possible source for an LR-B1 clause because it
cannot be wrong.

**LR-B7 — ICP fit before generating any clause.** Read `icp_segment`, `icp_valid_tiers`,
`icp_valid_titles` and `icp_out_of_scope` from `reports/{slug}/02-assumptions/graph.md`
(the single ICP author) and apply them to the live profile. Never carry a fixed industry
token list from another idea. Fails the ICP or hits an out-of-scope rule → SKIP, and set
`outreach_status: off_scope` with the specific failing evidence in notes.

**LR-B8 — Prior-domain variant.** A senior contact with an ambiguous current profile but a
verified past role inside the active ICP is drafted from that prior role, never from an
inferred current one.

**LR-B12 — Partial ICP match is a real third outcome.** Company inside the ICP, title
outside it → draft for them, and record the boundary in `validation_rationale`: which half
of the assumption their evidence can bear on and which it cannot. ICs describe the
mechanism in concrete detail a director would summarise away; the danger is the opposite
error, filing an IC's impression as evidence on the economics. If the *company* fails, it
is a SKIP, not a partial.

**LR-B5 — Seniority-tier register.** Standard variant (IC, engineer, practitioner,
researcher, analyst): casual, compare-notes close. Senior variant (any leadership token —
`CTO/CEO/CFO/COO/VP/Managing Director/Founder/President/Chair/Head of/Director/Manager/
Lead/Chief`): formal, low-commitment close *"would you be open to a few questions for my
research?"*. Managers and above sit closer to budget authority; the transactional framing
works where a vague compare-notes ask would not.

**LR-B15 — Record `close_variant` at draft time, and cross it against tier.**
`direct_question` (ends on a concrete question about a past event) vs `soft_ask` (ends on a
low-commitment permission ask), set when drafting and never reconstructed — a variant
recorded after the reply is known is a rationalisation. Because LR-B5 defaults seniors to
soft and ICs to direct, deliberately place some seniors on `direct_question` and some ICs
on `soft_ask` so all four cells fill; otherwise the two variables are confounded. Put the
batch's *weakest-fit* contact in the empty cell, never the strongest. Below 5 replies within
a tier, report counts and say the comparison is not yet interpretable.

**LR-B10 — Block detection: judgment plus capture-and-learn.** After every meaningful
action, snapshot the tab and use judgment to detect blocks, throttles, challenges, expiry
or captchas — no fixed string list, because platform wording drifts. Deterministic signals:
URL contains `/login` or `/checkpoint/challenge`; an iframe whose title or src includes
`captcha`. On detection: HALT, capture the exact text, save the snapshot for founder review,
alert, and append the verified signal to the per-idea journal. Grow verified tables; never
pre-seed guesses.

---

## Msg 2+ — reply drafting

**The failure mode all of these defend against: advisor conversion.** A senior practitioner
who starts evaluating your idea stops reporting their experience, and they do not go back.

**LR-M2 — Thank the fact, not the analysis.** An opener may name the specific data point
that landed; it must not praise their model, framing or thinking. Praising the reframe tells
them reframing earned the reply, so the next one arrives as more framing and less
operational detail — and it seats them as adviser.

**LR-M3 — Graveyard substitution.** Never ask whether there is a business here, whether they
would use something that solved it, or whether someone should build it. Replace, don't
soften: *"What did the teams actually try in order to fix that, and why didn't it stick?"*
A verdict is free, flattering and worthless; the graveyard is expensive, cannot be faked,
and answers the real question better. A hypothetical ("if someone built X…") is the same
violation with a conditional in front.

**LR-M4 — A volunteered cause is a symptom to drill, not a finding to log.** When a reply
contains "because", "the issue is", or any root-cause noun phrase, go one level below and
ask what specifically breaks first, quoting their phrase back so the drill is theirs. A
clean one-line cause is years of specifics compressed for a DM, and the specifics are the
part with the money in them.

**LR-M5 — The same-or-different fork belongs in every practitioner arc.** Once a recurring
cost or failure is named: *"Was it roughly the same list at every site, or a different list
every time?"* This is the productisability test and it is nearly free. Same → one artifact
built once, a product. Different → irreducibly bespoke, a consultancy. Requires multi-site
exposure; never signal which answer you want.

**LR-M6 — Use the number they volunteered as the yardstick.** Ask about variance around
THEIR figure, quoted exactly, rather than requesting a new estimate. A requested estimate is
produced on the spot to be helpful; variance around a committed figure is recall, and it
makes them name the cause.

**LR-M7 — Pain-first, not workflow-mapping.** Every reply must carry at least one of: what
it cost, who absorbed the cost, or what they already tried. Questions can be perfectly Mom
Test compliant and still only produce a process map — which tells you how the work happens,
not whether it hurts enough to pay to remove.

**LR-M8 — Match the close to their stated commitment level.** If they hedged ("no guaranteed
answers", "busy at the moment"), the close explicitly releases them. If they offered more,
the close need not ask permission at all. Never add a deadline; never add a call ask to a
hedged contact.

**LR-M9 — Never send a scheduling link.** Offer two or three concrete windows in their time
zone, or ask what their week looks like. A booking link transfers the work to the person
doing you the favour and reframes whose time is scarce; it also pattern-matches to sales,
which is the exact filter these contacts apply. Send a link only if they ask for one; a
founder's link is recorded in `founders/*.md → outreach_identity.booking_url` for that case.
If one has already gone out, never mention it again.
