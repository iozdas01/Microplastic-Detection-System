# Intake mechanics — question bank and templates

## Step 3 — Drill down

The core of this skill. Work through these, adapting as the answers open threads. Push on
vagueness every time; a belief that survives this is worth months of work, and one that
doesn't is better found out now.

**What it actually claims**
- What has to be true about the world for this to hold?
- Is this a claim about a *durable structure*, or about a moment? A belief that expires in
  eighteen months is a timing bet — useful, but say so.
- What's the mechanism? Why is the world this way rather than some other way?

**Where it stops**
- Who does this obviously apply to? Name real organisations, not categories.
- Who does it obviously NOT apply to, and why not? This is the harder half and the more
  valuable one — it becomes `out of scope`.
- Where is the edge — the case you genuinely can't call?

**Whether it's yours to hold**
- What did you see that made you believe this? Push for the specific occasion.
- Which part is first-hand and which part is inference from something you read?
- Where does your advantage stop? The edge of what you can see is the edge of the belief.

**What it survives**
- What's the strongest argument against it, made by someone smart who disagrees?
- If it's obviously true, why hasn't it been acted on? "Nobody noticed" is almost never the
  answer; find the real reason and it is usually load-bearing.

**Is it a belief at all**
- Could it be falsified in one study, one quarter, one customer conversation? Then it's a
  hunch, and it belongs in the shotgun's output rather than here. Say so and go up a level
  — ask what has to be true for that hunch to matter.

---

---

The question bank for Step 3, and the exact file scaffolding written in Step 7. Loaded when running that step, not before.

## Step 7 — Write the belief and initialize the idea

Agree the idea's name once the founder confirms the belief. Propose one — descriptive of
the *field*, not the solution (name the market, never the product) — and let them correct
it. It is recorded once, as `idea:` in the belief frontmatter, and every generated page
titles from it.

Write `belief.md` per the "Stable belief" spec in `schemas/hunch.md`:

```markdown
---
idea: {idea name}
created: {YYYY-MM-DD}
last_confirmed: {YYYY-MM-DD}
---

# Belief

{The founder's field-level belief, in their own words.}

## Belief boundaries

- In scope:
- Out of scope:

## Starting point and SISP check

- Starting solution, technology, or analogy:
- Origin: problem_observed | solution_or_analogy_first | mixed | unclear
- Problem stated without the solution:
- Founder-reported observations (context, not independent evidence):
- SISP status: not_indicated | possible | probable | unresolved
- What the shotgun must test independently:

## What would threaten the belief itself

- {Evidence that would challenge the anchor, not merely one hunch}
```

**Write it as soon as the belief statement is agreed, before the boundaries and threats are
done.** Set `last_confirmed` only once the founder has confirmed the full file. The file is the session
memory — if this conversation is interrupted, the next run reads the partial file and resumes
from the missing section rather than re-interviewing the founder from scratch. Nobody wants to answer
Step 2 twice.

For the last section, no method card covers it, so ask directly:

> "What would you have to see to conclude the whole belief is wrong — not just that this
> particular version of it failed?"

Push for something observable. "If customers don't like it" is not a disconfirmer. "If the
three largest UK operators all have this in-house already" is. The distinction that makes this
section worth writing: a threat to the *belief* invalidates every hunch beneath it, whereas
evidence that kills one hunch usually just sends you back for another. If they can't name a
belief-level threat, the belief may actually be a hunch — worth saying so and narrowing it,
because a belief that nothing could falsify will absorb any evidence and never update.

Read the finished file back and get explicit confirmation before setting
`last_confirmed`.

**Re-intake versioning (when a belief already exists and has changed).** Never overwrite or
delete the old statement. Move it verbatim — with its original `created` and
`last_confirmed` dates and a one-line note on what displaced it — into a `## Version history`
section at the bottom of `belief.md`, oldest first. The file's top always holds the current
confirmed belief; the history holds every prior iteration. The founder's requirement is
exact iterations of every belief and hunch: hunch iterations live as H-entries in
`hunch-lineage.md` (never deleted, only re-statused), belief iterations live in this
section. A drift-check proposal from another skill (see `startup-outreach-reply` Step 3b)
that reaches belief level routes HERE — this skill is the only place a belief version can
be confirmed.

Then create `reports/01-ideation/hunch-lineage.md` — **frontmatter only**:

```markdown
---
idea: {idea name}
belief_file: input-context/belief.md
active_hunch: none
next_hunch_id: H1
last_updated: {YYYY-MM-DD}
---

# Hunch Lineage

_No hunch yet. Run `/startup-ideate-shotgun` in explore mode: it proposes
candidates from a real corpus, and the founder promotes one to `active`._
```

**Write no H-entries here.** Intake does not author hunches — not H1, not a candidate, not
a working hypothesis in a comment. `next_hunch_id: H1` reserves the id for the shotgun; the
founder's own starting guess, if they had one, lives in `belief.md`'s SISP section as a
starting point rather than as a claim under test.

## Step 2 — Mine candidates

Cards: `methods/intake/previous-job-need-mining.md` (work life) and
`methods/intake/wish-it-existed-sourcing.md` (personal life)

Two cards, one stage. They differ only in where the memory comes from, and asking both is
worth it because they fail in opposite directions: work pain is well-validated but you may
have normalised it, personal wants are vividly felt but frequently idiosyncratic.

Open here, because these are the easiest questions to answer honestly and they produce raw
material rather than abstraction. Adapt the prompts to their actual history:

> "In any of your roles — did you ever catch yourself saying *why doesn't someone make X, we'd
> buy it in a second*?"

> "And outside work — anything you've wished you could just buy or use, and couldn't?"

Follow each candidate with the filters, one at a time:

- What exactly was missing, and what did you do instead?
- Did everyone around you feel it, or mainly you?
- Is it recurring, or a one-off annoyance? A want felt repeatedly is a far stronger signal.
- Would a crappy first version have been used immediately? (the Well Test — urgency, not
  elegance)
- For work candidates: is your depth here an asset, or have you normalised the problem so
  thoroughly you can't see it any more?
- For personal candidates: are you a representative user, or an outlier with idiosyncratic
  taste?

Those last two are the highest-yield questions in this step and the easiest to skip. Deep
domain experience makes problems invisible because the workaround became muscle memory; a
personal want feels universal precisely because you feel it so strongly.

Collect two to four candidates across both sources. Don't evaluate them yet — you are filling
a slate, and a slate is what makes the later filters discriminating. Judging the first
candidate on arrival is how you end up with the first candidate.

---

## Step 3 — Separate the problem from the starting solution

Card: `methods/intake/sisp-detection.md`

Run this for every surviving candidate, and immediately when the founder arrives saying "I
want to build X," names a technology before a workflow, or uses an "X for Y" analogy.

The goal is not to talk the founder out of the solution. It is to preserve what they favour
while preventing that preference from becoming an invisible premise in the shotgun.

Ask one question at a time:

> "What came first for you: something you observed people struggling with, or this
> solution, technology, or analogy?"

Then:

> "Can you describe the problem without mentioning that solution, product, technology, or
> analogy?"

Ask for the specific past observation behind the answer: who experienced it, what happened,
and what they did instead. Do not help by proposing possible problems. A polished problem
statement supplied by the interviewer defeats the diagnostic.

Record:

- the starting solution, technology, or analogy verbatim;
- whether the origin was `problem_observed`, `solution_or_analogy_first`, `mixed`, or
  `unclear`;
- the founder's solution-free problem statement;
- founder-reported observations already available, labelled as context rather
  than independent evidence;
- SISP status: `not_indicated`, `possible`, `probable`, or `unresolved`;
- what the shotgun must test independently.

`possible` and `probable` do not kill the candidate. They prevent solution vocabulary from
driving the discovery search. The shotgun may return evidence for the problem and still
recommend a different solution.

---

## Step 4 — Find the collision

Card: `methods/intake/domain-expertise-collision.md`

> "Which two fields do you know well enough that you can see across them — where what's
> obvious in one looks like an unsolved problem in the other?"

You are after the moments of *wait, why doesn't anyone just…* — where their home-field toolkit
makes a second field's accepted limitation look unnecessary. Practitioners inside a field
stop seeing their own workarounds; an outsider with a different toolkit doesn't.

Two things come out of this step:

1. **Which candidates from Step 2 sit on a collision** — those are the ones where they can see
   something the incumbents can't, rather than just being annoyed by something.
2. **The raw material for `## Belief boundaries`** — the edge of the collision is the edge of
   where their advantage is real. In-scope is where they can see; out-of-scope is where they'd be
   guessing like everyone else.

---

## Step 5 — Test intensity

Card: `methods/intake/emotional-signal-capture.md`

For the surviving candidates:

> "Which of these actually makes you angry when you think about it? Which one do you start
> talking faster about?"

Emotion is compressed experience — you get furious about friction you've hit from many angles,
not once. It's a real signal about which candidate has depth behind it.

But hold the card's own limitation in view and say it out loud if they start treating heat as
proof: **founder frustration is not market pain.** It tells you which candidate is worth the
pipeline's time. It tells you nothing about whether anyone else has the problem. That is what
the shotgun and the interviews are for. If they begin arguing that the market must want this
because they want it so much, name that — gently, once — and move on.

---

## Step 6 — Test durability

Card: `methods/intake/obsession-persistence-filter.md`

This is the filter that decides. Ask them separately:

- Would you work on this in your free time, unpaid?
- When you're on it, do you lose track of time — or is there something you'd rather be doing?
- Has it kept coming back after you rejected it? For how long? (months, not days)
- Is the pull toward *this problem*, or toward *being a founder*? Only the first survives a
  pivot.

The candidate that survives becomes the belief. If two survive, that is a real finding — say
so, and let the founder choose which lineage to start; the other is parked in
`signals/idea-parking.md` for later. Don't merge them into one broader belief to avoid the choice. A belief broad enough to
contain two obsessions is too broad to anchor anything.

If **nothing** survives — "good idea, but I could take it or leave it" — say that plainly.
That's a legitimate outcome, not a failed session. Founder-market fit is a real assumption and
it just came back negative before a month went into outreach. Offer to log the candidates as
gap entries (Step 9) and stop. Do not manufacture a belief to have something to show for the
conversation.

---

---

## Precedent lens — running it


**Whenever the founder names a constraint as permanent, go and find who hit it first.**
Almost nothing is new. Some field met this constraint decades ago, and what they did about
it is the most informative thing available — more informative than any opinion about the
future, including the founder's and yours.

Ask it out loud as a hint during the drill-down, not silently afterwards. It changes the
question the founder is answering:

> *"Elevators, boilers and pressure vessels were all once 'a qualified human must inspect
> and sign'. All three moved to certification regimes and insurance products. Does that
> transfer here, or is there something different about your case?"*

Two readings, and take both — the founder's rule is the first, the repo's memory is the
second, and the second is where the value usually is:

1. **If it happened before, it can happen again.** A precedent turns "impossible" into
   "nobody has done it here yet", which is a different and much better problem.
2. **Why their fix stalled is usually the real constraint.** The predecessor rarely solved
   it cleanly; find what they substituted instead and you have found the thing that actually
   binds

A precedent that transferred and a precedent that stalled are equally useful. A belief with
neither attached is still floating.

Related cards, for the shotgun's later use rather than this conversation:
`methods/ideation/why-now-predecessor-analysis.md`, `methods/ideation/proven-model-transplant.md`.

### Finding the predecessor

Strip the constraint of its industry — "a human must certify this before it operates", "the
failure mode is physical and irreversible", "the buyer cannot verify quality before purchase"
— then ask which field met *that* first. Regulated physical industries are the usual answer
and are often a century ahead.

| Constraint shape | Fields that hit it first |
|---|---|
| A qualified human must sign before operation | Elevators, boilers, pressure vessels, electrical installation, aviation maintenance |
| Physical failure is irreversible and injures people | Rail signalling, medical devices, nuclear, industrial machinery |
| Nobody will insure a novel risk | Marine shipping, early aviation, autonomous vehicles |
| Quality cannot be verified before purchase | Assaying, food safety, materials testing, structural certification |

Report the answer as a question, never a conclusion. The founder decides whether the
precedent transfers; the research only makes that decision possible.

---

## Step 4 — definitional research: what to search for

In order of how often each changes the belief file:

1. **The field that hit this constraint first** — the precedent lens above. Usually the
   single most informative search of the whole conversation.
2. **Real cases clearly inside the belief.** Named organisations, not categories. Three of
   these turn an abstract claim into one the founder can be wrong about.
3. **Real cases that look like they belong and don't.** The boundary-sharpening half, and
   the one that gets skipped. `out of scope` is written from these.
4. **The strongest published counter-argument**, made by someone competent who disagrees.
5. **Prior attempts to act on this belief, especially failed ones** — what they tried, and
   what they did instead once it failed.

Stop rules. You are done when the boundaries stop moving. You have gone too far the moment
you are ranking segments, sizing a market or naming a buyer — that is the shotgun's job, and
doing it here produces a hunch by the back door.

---

## Boundaries are not segment selection

Founders push back on the boundary questions with a version of *"it's just a belief, it
shouldn't be bounded — I don't know where the biggest problem is yet."* They are half right,
and the half they are right about is important enough that pushing past it damages the file.

- **A boundary says where the belief APPLIES.** Outside it, the belief makes no claim. This
  is knowable now, and the founder almost always knows it — they just have not said it.
- **A segment says where the sharpest pain IS, inside that boundary.** This is not knowable
  now. It is the shotgun's output, and a founder who guesses it here has written a hunch.

Say the distinction out loud when the pushback comes. Then look at what they have already
told you: the boundary is usually sitting in a qualifier they used without noticing — an
industry shape, a scale, a process type. Offer it back as a boundary and it is usually
accepted immediately, because it was theirs.

A boundary can also arrive by the founder amending the belief sentence itself, which is the
cleanest form: a qualifier in the sentence IS a boundary, and the `In scope` line just records
what it excludes.
