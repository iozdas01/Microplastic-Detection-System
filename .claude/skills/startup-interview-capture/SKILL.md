---
name: startup-interview-capture
description: Parses raw customer-interview notes for a founder into structured evidence — extracts Mom Test signals (unprompted mentions, past behaviour, specific costs, things they've tried), flags false positives, proposes an outcome_modifier classification (strong_confirm / moderate_confirm / weak / contradiction) with reasoning, drafts evidence-ledger entries, and updates the contact card in outreach/contacts.md. Use this skill whenever the user finishes a customer interview and wants to log it — triggers on "capture interview notes", "process interview notes", "structure my interview", "log this interview", "add interview to evidence", "categorize this interview", "score this interview", "parse the interview I just did", or when the user pastes raw notes and asks what to do with them. Also use it any time a raw interview notes file exists under `reports/03-validation/{A_ID}-{date}/interviews/` with only content above the `---` divider — the file is waiting to be captured.
---

# Startup Interview Capture

Convert raw stream-of-consciousness customer-interview notes into structured evidence for the Startup Assumption Lab. This is the foundational skill of the customer development pipeline — every downstream synthesis, score update, and outcome decision reads what this skill writes.

## The one hard rule

Never modify the raw notes above the `---` divider. The founder wrote those in the moment; they're the ground truth. Only write below the divider. If a file has no divider yet, add one at the end of the raw notes before writing structured capture.

## What triggers this skill

The founder just finished a customer interview and either:
- Has a notes file at `reports/03-validation/{A_ID}-{date}/interviews/{contact-slug}-{date}-notes.md` waiting to be processed
- Pastes raw notes into the chat and asks what to do with them (in this case, ask them for the file path and confirm the schema before starting)
- Explicitly asks you to capture, log, structure, parse, or categorize an interview

If no file exists yet, create one following the schema in `schemas/interview.md` — but the raw notes must come from the founder, never fabricated.

## Inputs you need

Before parsing, load these:

1. **The interview notes file** — top half is raw notes, frontmatter has `contact_id`, `assumption_id`, `interview_date`, `interview_stage`
2. **The contact card** — find the block with matching `id: {contact_id}` in `reports/outreach/contacts.md`. Read `contact_role`, `signal_type`, `role_pts`, `signal_multiplier`, current `evidence_score`
3. **The assumption** — find node with matching `id: {assumption_id}` in `reports/02-assumptions/graph.md`. Read `assumption`, `category`, `disconfirmation`
4. **Existing evidence ledger** — `reports/03-validation/evidence.md` (or the older path if `03-validation/` doesn't exist yet). Find the highest existing entry `id` so you can number the next one `E{N+1}`

If the contact card isn't found, ask before proceeding — a missing contact means the outreach layer is broken and capture would create orphaned evidence.

## The parsing pass — what to look for

Read the raw notes carefully. Interviews are messy. The founder wrote in the moment and may have paraphrased, gone off-topic, or made typos. Your job is to surface what actually happened without adding what didn't.

### Mom Test signals (extract every instance)

**Unprompted mentions of the pain** — did the contact bring up the assumption's topic before the founder did? This is the single strongest signal. If the founder had to lead them to it with a leading question, note that instead.

**Past behaviour cited** — anything phrased in past tense. "Last month we had to send two riggers up..." is gold. "We would probably..." is not — future conditional is worthless.

**Specific costs named** — extract every number the contact quoted:
- Time (hours/week, days/month)
- Money (per incident, per year, per project)
- Frequency (X times per month, Y events per year)

**Things they've tried** — every workaround, tool, vendor, hack the contact has actually used to address the pain. If they haven't even googled for a solution, they probably don't care enough to pay. Note this explicitly.

**Referrals offered** — names, roles, companies. Include how the contact framed the intro ("I can introduce you", "you should talk to X" without offering to intro, etc.). Unforced intros are a stronger signal than pried-out names.

### False positives — flag, don't silently drop

The most dangerous outputs of customer interviews are compliments. Flag every one:

- "This would be amazing / great / a game-changer" without past behaviour cited → false positive
- "I would definitely use that" — future conditional, not evidence → false positive
- Agreement with a leading question — if the founder said "X is really hard, right?" and they said "yeah", that's not signal
- "You should build X" — feature requests aren't evidence of pain unless anchored to past behaviour

For each false positive, quote the specific line and note why it's a false positive. Never drop them — the founder needs to see what they might have mistaken for signal.

### Off-topic mentions

Off-topic material splits two ways, by whether it lands anywhere in the current graph:

**Maps to a different assumption in the graph** → note it under "Next questions raised". Do NOT link it to the current assumption's evidence — that contaminates the score. The founder decides whether to test that assumption separately.

**Maps to no assumption in the graph at all** → this is a *cross-idea gap*, and it goes to `signals/gaps-log.md`. Historically this material was dropped entirely, which was the right call for scoring and wasteful for everything else: a contact volunteering the thing that actually ruins their week is unprompted, specific, and comes from someone living in the domain full-time. That is the highest-quality input the Background Noticing Process (`methods/practices/background-noticing-process.md`) will ever get.

Harvest an off-graph mention when it describes something **missing, broken, or harder than it should be** in the contact's working life. Don't harvest general industry commentary, opinions about competitors, or pleasantries. Rough rule: if it names a recurring manual workaround, a cost, or a "why doesn't someone just…", take it. Most interviews yield zero to two. Zero is a normal result — write "(none)" rather than reaching.

## The classification pass — propose outcome_modifier

After parsing, propose ONE outcome_modifier. This is the single manual classification for the interview — the founder confirms or overrides it before you finalize the score.

**strong_confirm (+1)** — all four should be true:
- Contact described the pain unprompted
- Named at least one specific cost (time or money)
- Has already tried to solve it (workarounds, tools, competitors)
- Any one of: offered a referral without being asked, expressed intent to pay, offered to be a case study

**moderate_confirm (+0)** — pain is clear when probed but weaker signal:
- Confirmed the pain exists when asked directly (not unprompted)
- May have named vague costs ("takes forever", "expensive") without specifics
- No active solution attempts, or only passive complaining
- Not naming this as a top-3 priority

**weak (−0.5)** — reasons to doubt:
- Polite agreement without evidence
- Feature-request language without past-behaviour anchor
- Contact couldn't cite a specific incident
- Multiple false positives detected

**contradiction (−1)** — clear evidence against:
- Contact said the pain doesn't exist for them
- Already solved with existing tools and satisfied
- Wrong segment entirely (they're not who you thought)
- Actively pushed back on the premise

Ties break toward the weaker outcome. When in doubt between strong and moderate, propose moderate. Between weak and contradiction, propose weak. The founder can upgrade, not just downgrade — but you should surface an honest read, not an optimistic one.

Your reasoning MUST cite specific evidence from the raw notes. Not "seems positive" — the exact behaviour or quote that triggered the classification.

## Common failure modes to avoid

- **Fabricating quotes.** Every quoted line under "Direct quotes worth preserving" must appear verbatim in raw notes. If you paraphrased or invented, you've broken the audit trail. Check every quote before finalizing.
- **Silently dropping false positives.** A capture with no false positives listed is suspicious — most interviews have at least one. If you genuinely observed none, write "(none observed)".
- **Linking off-topic evidence to the current assumption.** Contaminates the score. When in doubt, surface under "Next questions raised" and let the founder decide.
- **Auto-updating contact card before founder confirms outcome_modifier.** The confirm step exists because outcome classification is where the whole score comes from. Never skip it.
- **Routing an off-graph pain into evidence.md instead of the gaps log.** If it doesn't map to an assumption in the current graph, it is not evidence for this idea — it's a gap. Putting it in evidence.md inflates the score with material that supports nothing being tested.
- **Writing idea-scoped detail into gaps-log.md.** Assumption IDs, confidence numbers, or "this contradicts A2" in the log means the next idea's session reads this idea's findings. Observation plus path pointer, nothing more.
- **Reaching for gaps to avoid writing "(none)".** Most interviews produce zero. A log padded with general industry commentary is worse than an empty one, because the monthly review clusters on noise.
- **Assuming the contact card exists.** If it doesn't, stop and ask. Don't create one from thin air.
- **Off-by-one on evidence IDs.** Read `evidence.md` first to find the highest existing E{N}, then continue from N+1. Don't restart at E1 or guess.

## When the founder disagrees with your classification

Sometimes they'll override with a stronger classification than you proposed. That's fine — the founder has context you don't (tone of voice, body language, the trajectory of the relationship). But if they override to `strong_confirm` when your reasoning cited multiple false positives and no past-behaviour anchors, gently push back once:

> "You overrode to strong_confirm — my read was weak because I flagged {X} and {Y}. If you're seeing signal I missed (tone of voice, follow-up commitment I couldn't parse), that's fair. Just noting for the audit trail."

Then respect their decision. This isn't a debate — it's a sanity check.

## Reference files

For the exact YAML shape and field definitions, always defer to:
- `schemas/interview.md` — full interview note structure
- `schemas/contact.md` — contact card format + scoring formula
- `schemas/evidence.md` — evidence entry format + quality ladder

If a schema and this SKILL.md ever contradict, schemas win. Schemas are the source of truth.

## Mechanics

Step mechanics, output templates and taxonomies live in `references/capture-format.md`.
