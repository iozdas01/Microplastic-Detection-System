---
account: "<HANDLE — not yet supplied>"
founder: Izgin Ozdas
calibration: confirmed
sample_count: 24
sample_kind: other_writing + posted_x
sample_source: Claude Code session transcripts 2026-08-09, one outbound research email, and one posted X reply 2026-08-10
last_updated: 2026-08-10
---

# Voice profile

## Two registers, and the one X needs

The samples split cleanly into two modes, and neither is the X voice on its own.

**Working mode** (talking to an assistant): all-lowercase, fast, run-on, typos left in,
double-dash and arrow connectors, heavy "basically" and "like", ALL CAPS and stacked
`????` when something is wrong, profanity when genuinely annoyed. Blunt corrections with no
softening — "no this is completely wrong", "HE IS THE WRONG PERSON TO TEST THIS".

**Outbound mode** (emailing a DeepMind researcher): fully formal, complete sentences,
precise technical vocabulary, careful qualification, institutional sign-off. "Am I reading
the training setup correctly that RoboBallet learns a policy and value functions from
multi-robot rollouts inside a separately generated kinematic environment, rather than
learning a predictive world model?"

**The X voice sits between them**: the directness and refusal to hedge from working mode,
the technical precision from outbound mode. Not the typos, not the run-ons, not the
Cambridge formality. Lowercase-leaning is authentic and should be kept — it reads as
someone typing fast because they have something to say, which is true.

## The posted register — the locked loop

First sample of the founder writing *for an audience* rather than to an assistant, and it
settles what the two-register guess above could only predict. The X voice is lowercase, and
the sentences are much shorter than any draft would make them.

The move itself is the finding. **Two flat clauses where the second inverts the first, so the
pair closes into a constraint that cannot be exited.** No connective, no "which means", no
conclusion. The reader closes it themselves, and that is the whole effect.

> the robot needs data to train on to be deployed. the data needs a deployed robot to be
> collected.

What this rules in and out when drafting:

- **State the trap, don't announce it.** No "here's the problem", no "the structural issue
  is". Two facts side by side do the work.
- **Do not draw the conclusion.** A drafted third sentence explaining the loop kills it.
- **Reply by adding a constraint, not by agreeing or disagreeing.** The post being replied to
  predicted a future ("I think the next big infra layer will be…"); the reply neither
  seconded nor contradicted it, it named a circularity the prediction had not priced in. This
  is the founder's default posture toward other people's takes.
- **Never open with "I think".** The source post did; the reply did not, and the asymmetry is
  most of why the reply lands harder.
- **Reply length is ~110 characters.** Replies are one move, not a compressed essay.

The same shape is the target for standalone posts, not only replies — a post whose last two
lines lock against each other is in voice; one that ends on a summarising sentence is not.

## Observable rules

- Lowercase-leaning. Sentence case is fine; Title Case and formal capitalization are not.
- Short declaratives. When a sentence runs long it is because a technical claim needs
  qualifying, not because it is building rhetoric.
- States positions flatly. No "I think maybe", no "it could be argued".
- Names the specific mechanism rather than the category — "simulating the physics of the
  joints inside the robot", not "technical challenges".
- Willing to say a thing is wrong, including their own earlier position.
- Comfortable with "basically", "tbh", "idk" in casual posts. One per post, not three.
- Uses `--` and `-->` as connectors. In posts these become line breaks; they are a
  thinking-speed artifact, not a style choice worth preserving.
- No emoji. No hashtags. None appear in any sample.
- Credential is real and understated when relevant: Institute for Manufacturing, Cambridge.
  It belongs in a bio, not in post bodies.

## Never

- Corporate-professional register. "Excited to share", "thrilled to announce", "humbled".
- LinkedIn-thought-leader cadence: "Here's the thing.", "Let that sink in.", "🧵👇".
- Generic-LLM tells: "it's not just X — it's Y", rhetorical-question openers, the tricolon,
  em-dash pivots for drama.
- Fake certainty. The samples are full of live uncertainty ("idk where it fits into in the
  chain") and that honesty is an asset, not a flaw to edit out.
- Hedging a claim that is actually held. The founder does not hedge when they are sure, and
  a drafted hedge will read as inauthentic to anyone who has met them.
- Reproducing the typos. They are typing speed, not voice.

## Topic stance

**Confident about:** manufacturing and plant reality; what a researcher can versus cannot
tell you; that assumptions must be testable by talking to the market, with the technical
route figured out afterwards; reading a robotics paper closely enough to ask its author a
sharp question.

**Live uncertainty, and says so:** where post-processed robot data sits in the value chain;
whether the binding constraint is the robot or the plant; how the two hunches relate.

**Uninterested in:** growth tactics, personal-brand building, engagement mechanics. Posting
is for exposure and reach into a real buyer segment, not for follower count.

## Sample posts

Raw samples retained so a later run can recalibrate without re-interviewing. Regenerate
with `python3 .claude/skills/startup-x-draft/scripts/harvest_sessions.py --voice` — note that
the harvest only reaches transcripts, so posted-X samples have to be added by hand.

Posted on X, 2026-08-10, as a reply to a post predicting that the next robotics-data infra
layer will be quality measurement and structuring:

> the robot needs data to train on to be deployed. the data needs a deployed robot to be
> collected.

Transcript samples:

> the assumptions have to be assumptions we can test with the market - we will figuree out
> a way to do it technically as longas the market wants the solution

> no this is completely wrong. HE IS THE WRONG PERSON TO TEST THIS!!! WE HAVE TO TEST THIS
> WITH PLANT OPERATORS AND INTEGRATORS INSTEAD DUDE!!!! LIKE ???? RESEARCHERS U CAN ONLY
> TEST THE DATA SIDE!!!

> he also said like the environment data isnt that important its all about simulating the
> physics of the joints etc. like inside of the robot thats why everyone focuses on the
> robot the environment changing ut the robot staying the same is not good enough data

> founder market fit i dont think needs to be an assumption - we should have the
> assumptions be able to be tested via talking with people

> i think we need to decide what the outcome we want is - so like what do we want to gain
> out of these emails

> Am I reading the training setup correctly that RoboBallet learns a policy and value
> functions from multi-robot rollouts inside a separately generated kinematic environment,
> rather than learning a predictive world model?
