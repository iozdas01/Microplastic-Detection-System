# Reply drafting mechanics

Steps 5-8 and 11-13 of `startup-outreach-reply`: domain research, question pool, draft structure, calibration display, copy archive, rule log, tracker regen.

**Build a domain model covering:**

1. **Workflow model for their role.** What does someone with their title actually do in a job — planning, execution, reporting, budget sign-off? Who do they answer to? What does failure look like for them personally?

2. **Pain topology for their phase.** Where do delays, cost overruns, and friction typically occur in their part of the work? What are the known industry failure modes for their role? Use real sources — trade press, OEM guidelines, industry forums, procurement docs.

3. **Vocabulary map.** What words do practitioners in their phase use for the pain? Must match the contact's own reply vocabulary. If they said "scope creep," use "scope creep." Their language, not yours.

4. **Arc-stage specific depth:**
   - Msg 2 (frequency): What are the known frequencies of this problem? What's the range from industry data?
   - Msg 3 (magnitude): What are the known cost ranges? What does an overrun typically look like in their phase?
   - Msg 4 (scale): What is the scale of their market segment? Any fleet-size or job-volume benchmarks?

**Sources:** the domain's trade press, standards bodies and research institutes, OEM service reports, the company's targeting fields in `reports/{slug}/outreach/companies.md`, and their own LinkedIn activity.

**Minimum bar:** the question should sound like it comes from someone who has done real homework on their specific workflow phase, not someone who googled "{domain} maintenance."

## Step 6 — Generate the question pool

Generate 3–5 question candidates, each labeled:

```
Question pool for {Name} — Msg {N} ({arc stage}):

#1 [frequency] "{question text}"
   → Captures: {what data this surfaces}
   → Updates: {which assumption and how}

#2 [magnitude] "{question text}"
   → Captures: {what data}
   → Updates: {which assumption}

#3 [scale] "{question text}"
   → Captures: {TAM triangulation input}
   → Updates: {market size signal}

Pick a number, or say "draft with #N."
```

**Mom Test rules — always:**
1. Past behavior, not opinions. "Tell me about the last time" beats "do you think."
2. Specific, not general. "The last campaign" beats "campaigns in general."
3. Answer requires private knowledge only they have. If Google could answer it, rewrite.
4. No leading. No hinting at what you want to hear.
5. No product reveal. No features, no capabilities, no "we're building."
6. No call ask before Msg 5+.
7. Match their depth — roughly 60% of their reply length.
8. Never ask for a verdict on the opportunity. No "is there a business here", "would you use
   something that solved this", "do you think someone should build this", and no hypothetical
   version of the same. Ask what was already tried instead — see `LR-M3`.
9. Never praise their framing, only the usefulness of what they told you — see `LR-M2`.
10. **Segment competence gate — run this BEFORE generating the pool.** Name the assumption this
    contact can testify to from their own work, and ask only within it. A researcher can speak
    to what data their work needed; they cannot speak to deployment labour, site access or
    integration economics, because they have never done it. An integrator or plant operator is
    the mirror image. A question outside the set returns a plausible opinion that gets filed as
    evidence, which is the most expensive failure in the ledger — it is wrong AND it is durable.
    The per-idea table is `reports/{slug}/outreach/email/contact-routing.md → Segment
    competence`; if the contact's counterparty type is not in it, add the row before drafting.

Rules 8 and 9 both defend against **advisor conversion**: a practitioner who starts evaluating
your idea stops reporting their experience, and does not go back. It is the single most
expensive mistake available in a reply, because it costs you every remaining message in the arc,
and it is usually triggered by the founder's own sentences rather than by their questions.

**Question shapes by arc stage** (structure only — never copy verbatim):

*Frequency (Msg 2):*
- "What tends to take longer than expected once you're actually on site — is it {A from research}, {B}, or something else?"
- "Tell me about the last {campaign type they described} where something didn't go to plan — what was the thing that stretched it?"

*Magnitude (Msg 3):*
- "When {situation they confirmed} happens, where does the cost land — delay, rework, remobilisation, or all three?"
- "Roughly how often does a {their phrase} run significantly over the initial scope — and what does that look like on the invoice?"

*Scale (Msg 4):*
- "Is what you described specific to the type of sites you work on, or pretty consistent across the ones you see?"
- "Across the jobs you run, roughly how many units does a typical one cover?"
- "Do you see it differently in {segment A} vs {segment B}, or is the same pattern there?"

*Call ask (Msg 5+):*
- "You mentioned {specific thing they confirmed} costs {magnitude they confirmed} — I'm trying to understand if that's actually fixable. Would a 20-min call be easier than back-and-forth?"

### The five moves that build the pool

Arc stage says WHAT to learn next. These say HOW to shape the question. Apply them in order;
most pools use two or three. Full statements live in `schemas/copy-rules.md` as
`LR-M3`–`LR-M8` — read them before drafting a reply to any substantive contact.

**1. Drill the volunteered cause, don't accept it (`LR-M4`).** If their reply contains "because",
"the issue is", or any noun phrase naming a root cause, that sentence is a compression of years
of specifics, not a finding. Quote their phrase back and ask what specifically breaks. One
level down, one drill per message.

**2. Their number is the yardstick (`LR-M6`).** If they volunteered a figure, ask about variance
around it rather than requesting a fresh estimate. Recall beats estimation, and it makes them
name the cause of the variance instead of you.

**3. Substitute the graveyard for the verdict (`LR-M3`).** When the founder's underlying
question is "is there a business here", ask what teams already tried and why it didn't stick.
Never ask for a verdict, and never launder one into a hypothetical. Tell the founder plainly
that you are asking their question in the form that returns data — this move gets rejected as
evasion unless the reasoning is shown.

**4. Ask the same-or-different fork (`LR-M5`).** Once any recurring cost or failure is confirmed,
ask in one clause whether it is identical across sites or different every time. Same means
product, different means consultancy. Requires multi-site exposure; phrase it with no preferred
answer.

**5. Check the draft carries pain, not just process (`LR-M7`).** Before showing anything, verify
at least one question asks what it cost, who absorbed it, or what they already tried. A pool can
pass every Mom Test filter and still only produce a workflow map. Workflow maps do not
distinguish a painkiller from a vitamin.

Then set the close to their stated commitment level (`LR-M8`): mirror a hedge with an explicit
release, and leave an open invitation unspent rather than converting it into an early call ask.

## Step 7 — Draft structure

Three parts:

**1. Warm opener** — genuine, first name, 1 sentence. Reference something specific from their reply. Do not recite their title or company.

Good: "{Name} — really appreciate the detail in your last message."
Bad: "Hi {Name}, thanks for sharing your expertise as a specialist in this area."

**2. Scope frame** — one sentence scoped to THEIR workflow phase. Tells them why this question is for them specifically.

Good: "I'm mainly trying to understand what happens at the point where the team arrives on site and confirms scope."
Bad: "I'm researching automation in this industry."

**3. Question(s)** — from the pool, past-focused, non-googleable. Match depth to their reply length (~60%).

Total: 3–5 sentences. No em-dashes. No product reveal.

**Warm path only:** add "Happy to jump on a call if that's easier than back-and-forth." Never paste a booking link (LR-M9) — offer two or three concrete windows in their time zone, or ask what their week looks like. A founder's link lives in `founders/*.md → outreach_identity.booking_url` for the case where the contact asks for one.

## Step 8 — Calibration display

```
[C{ID} {Name} @ {Company} · Msg {N} · {arc stage} · {chars}]

{draft message text}

---
Their last reply: "{verbatim reply_excerpt}"
Arc stage: {frequency | magnitude | scale | call-ask}
Data this captures: {one line}
---
Enter=approve+send, e=edit, s=skip, q=quit
```

Track edits. Zero-edit = golden example candidate. Edited = rule candidate.

## Step 9 — Hand the reply to the founder

**Claude never sends a message** (`schemas/copy-rules.md` → Send permission). Print the
approved text in a copy-ready block, name the contact and the thread it belongs to, and stop.
The founder pastes and sends it from their own session.

Record the send only after the founder confirms it went out — an unconfirmed send in
`contacts.md` is worse than no record, because every reply-rate number downstream treats it
as real.


