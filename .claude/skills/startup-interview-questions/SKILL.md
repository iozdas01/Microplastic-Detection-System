---
name: startup-interview-questions
description: >-
  Generates a tailored Mom Test customer-interview guide for a specific assumption and segment. Use whenever the user wants to prepare for a customer call, design discovery questions, test whether a pain is real, validate an assumption through interviews, or asks what they should ask customers. Produces behavior-focused questions and avoids leading, hypothetical, or product-pitch questions.
---

# Customer Interview Question Generator

You generate a ready-to-use customer interview guide based on a specific assumption the founder wants to test. The guide is grounded in the Mom Test framework — every question must be about the customer's actual life and past behaviour, never about their opinions of the idea.

## Gather inputs

You need four things. Ask for any that weren't provided:

1. **assumption** — the specific belief being tested (e.g. "physical therapists spend 3+ hours/week on insurance paperwork and find it genuinely painful")
2. **assumption_category** — the type of assumption: `pain`, `timing`, `market`, `willingness_to_pay`, `behaviour`, `switching`, or `segment`
3. **customer_segment** — who will be interviewed (be specific: "independent PTs in private practice", not just "physical therapists")
4. **stage** — `problem_discovery` (is the pain real and big enough?) or `solution_validation` (do they want what we've built?)

If any are missing, ask. Don't generate the guide until you have all four.

**Optional fifth input — `job_statement`.** If the idea's ideation shotgun produced a job statement for this segment (`methods/ideation/jtbd-substitute-map.md`, run as the `job_and_substitute` lens), pull it from the shotgun report and use it. Don't block on it — but check before generating, because it makes the core questions substantially sharper. Look in the latest `reports/{slug}/01-ideation/{date}-shotgun.md` or the lens output under `01-ideation/methods/`.

## The core principle behind every question

The biggest mistake in customer interviews is asking for opinions about your idea — people will be polite and give you false positives. Instead, every question must anchor to their actual past behaviour and real life. The question "would you ever use a product that..." is useless. The question "talk me through the last time this happened" is gold.

There are two dangerous traps to avoid:
- **False positives from compliments**: "That's a great idea!" means nothing. Only concrete past behaviour and real commitments count as evidence.
- **Premature zoom**: In problem_discovery stage, never ask about the specific problem domain until the interviewee surfaces it themselves. Start broad. If the problem is genuinely painful, they'll mention it.

## Deriving questions from a job statement

When a `job_statement` is available, use it as the skeleton for the core questions rather than ad-libbing them. Its four slots map one-to-one onto the four required core question types below, which is not a coincidence — both frameworks are built to separate a durable need from a proposed solution:

| Job slot | Becomes | Why |
|---|---|---|
| **When I** [context] | the *"walk me through the last time"* question | The context names a specific recurring occasion. Anchoring to that occasion is what stops the interviewee generalising. "Tell me about the last time you were doing X" beats "do you ever struggle with X". |
| **But** [barrier] | the *"what else have you tried"* question | The barrier is your hypothesis about what blocks them. What they've tried reveals whether that's the real obstacle or your invention. |
| **Help me** [goal] | the *"why do you bother"* question | The goal is what you think they want. Asking why they bother tests whether the stated goal is the actual motivation or a proxy for something underneath. |
| **So I** [outcome] | the *"what are the implications"* question | The outcome is what makes the job worth paying for. If they can't name what it unlocks, you have a vitamin. |

Two rules when using this mapping:

**Never say the job statement out loud.** It is your hypothesis, and reading it back is the purest form of leading the witness — they will agree with a well-written statement about their own life almost regardless of whether it's true. The statement shapes what you ask; it never appears in what you say.

**Treat unfillable slots as the finding.** If the interview cannot fill a slot — they don't recognise the context, the barrier isn't what stops them, the outcome doesn't matter to them — that is a specific, actionable contradiction of the job statement, and it's worth more than the interview confirming the three slots you got right. Flag it in the guide's "what to listen for" section so the founder notices it live rather than in the transcript a week later. A contradicted job statement routes back to ideation, not to another interview.

When no `job_statement` is available, generate the four core questions from the assumption directly, as normal. The mapping is a sharpening tool, not a prerequisite.

## Output format

Generate the guide in this exact structure:

---

# Interview Guide: [one-line description of what's being tested]

**Assumption:** [restate the assumption]
**Segment:** [customer segment]
**Stage:** [problem_discovery / solution_validation]

---

## Opening script

A short paragraph (3–5 sentences) the founder can actually say out loud to open the meeting. Use the Vision / Framing / Weakness / Pedestal / Ask structure:
- **Vision**: half a sentence on the space you're working in — without mentioning the idea
- **Framing**: you're early, you have nothing to sell, you just want to learn
- **Weakness**: the specific thing you don't understand yet (this is what makes them want to help)
- **Pedestal**: why this specific person can help you better than anyone
- **Ask**: a simple request for their time

Keep it conversational. It should sound like a human being, not a pitch deck.

---

## Opener questions (2–3)

[For problem_discovery]: These must be wide open — about their work/life in general, not about the problem domain. The goal is to see whether the problem surfaces on its own. If they don't mention it, that's already a signal.

[For solution_validation]: You can zoom in to the problem domain immediately since you already know it's real. These questions warm up the conversation and re-establish what their current situation looks like.

Each question: write the question itself, then a one-line note in italics on what you're really listening for.

---

## Core questions (4–6)

Assumption-specific questions, all anchored to past behaviour. Required coverage:
- At least one **"walk me through the last time"** question — gets a specific past example instead of a generic opinion
- At least one **"why do you bother"** question — digs from the surface complaint to the real underlying motivation
- At least one **"what are the implications"** question — separates painful problems from merely annoying ones
- At least one **"what else have you tried"** question — the single best signal of how much they actually care (if they haven't even googled for a solution, they probably won't pay for one either)

If a `job_statement` was supplied, derive these four from its slots using the mapping above, and note in italics which slot each question is testing so the founder can see live which part of the hypothesis is holding.

For each question: write the question, a one-line italic note on what to listen for, and flag with ⚠️ *watch for false positives* if the question format could invite a polite non-answer.

---

## "Does this problem matter" probes (2–3)

Short follow-up questions used when a signal is ambiguous — to distinguish a painkiller problem from a vitamin. Pull from this battery and adapt to the specific assumption:
- How much time does this take per week/month?
- What does it cost you when this goes wrong?
- What are you currently doing to deal with it?
- Is this one of the top three things you're trying to fix right now?
- Have you looked for tools or services to solve this? What did you find?

---

## Commitment and advancement questions

[Only include this section if stage = solution_validation]

Soft commitment questions (test genuine interest):
- Questions that ask them to invest time or introduce you to someone

Hard commitment questions (test real intent):
- Questions that ask for something with real currency: a deposit, a signed letter of intent, agreeing to be a case study, or paying for a trial

For each: write the question and a note on what a real "yes" looks like vs. a polite brush-off.

---

## Closing (always include)

- "Who else should I talk to about this?" — End every conversation here. If they won't make intros, that's a signal.
- "Is there anything I should have asked but didn't?" — Lets them fix your blind spots.

---

## What to listen for

A short paragraph specific to this assumption explaining:
- What a **real signal** looks like: e.g. they describe the problem unprompted, they've already tried to fix it, they get emotional about it, they mention specific costs or time lost
- What a **false positive** looks like: e.g. "yeah that's kind of annoying" with no evidence they've ever tried to fix it; agreeing with your leading question; saying "I would definitely use that"
- One **green flag** and one **red flag** specific to this assumption category

---

## The "do not ask" list

After the guide, add a short section listing 2–3 questions the founder might be tempted to ask but shouldn't, with one-line explanations of why each one produces bad data. Tailor these to the assumption — don't just repeat generic Mom Test warnings.

---

## Important constraints

- Never generate a question in the form "would you ever...", "do you think...", "how much would you pay for...", or "what would your ideal product do..." — these all invite false positives
- Never generate a question that can be answered with desk research (competitor pricing, market size, regulatory landscape) — use interview time for things only a human can tell you
- If a question is phrased in the future tense ("would you", "could you", "might you"), rewrite it in the past tense ("when did you last...", "have you ever...")
- Feature request questions ("what would make it better?") are only acceptable if immediately followed by a "why?" probe built into the question itself
