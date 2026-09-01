# Schema: Interview Note

One file per interview: `reports/{slug}/03-validation/{A_ID}-{date}/interviews/{contact-slug}-{YYYY-MM-DD}-notes.md`

An interview note has two halves separated by `---`:

- **Above the divider** — raw notes from the founder (freeform, stream-of-consciousness)
- **Below the divider** — structured capture written by `startup:interview-capture`

The founder writes the top half. The skill writes the bottom half, keyed off metadata in
the frontmatter.

## Full file format

```markdown
---
contact_id: C1                              # links back to outreach/contacts.md
contact_name: Sarah Chen
assumption_id: A2                           # from graph.md
interview_date: 2026-07-15
interview_stage: problem_discovery          # problem_discovery | solution_validation
interviewer: Izgin                          # which founder ran the call — a name listed in founders/
duration_min: 32
medium: linkedin_video                      # linkedin_video | zoom | phone | in_person
consent_recording: false
---

# Interview: Sarah Chen · A2 · 2026-07-15

## Raw notes

<freeform notes here — anything you heard, in the order you heard it. No structure
required. Timestamps optional. Direct quotes helpful but not required.>

---

## Structured capture
_Written by `startup:interview-capture` — human confirms outcome_modifier below._

### Mom Test signals

Unprompted mentions of the pain:
- "..."                                     # verbatim quote or paraphrase with "verbatim: no"

Past behaviour cited:
- "Last month we put two people on it for three days to get it done by hand."

Specific costs named:
- Time: ~3 hours/week reconciling reports
- Money: £8k per job, ~6/year

Things they've tried to solve it:
- Off-the-shelf tools (inadequate — don't cover the hard part)
- Adding more headcount (too expensive)

False positives detected:
- "This would be amazing" — hypothetical, not past behaviour. Flagged.

### Signal summary

Assumption: A2 — Pain is real and expensive for operations managers in the target vertical
Verdict: supports
Confidence: 4/5

### Proposed outcome_modifier

**strong_confirm** (+1)

Reasoning: Contact described the problem unprompted within the first 5 minutes. Named a
specific per-incident cost (£8k) and annual frequency (~6/year = £48k/year). Has already
tried two workarounds. Offered to introduce two peers at other sites.

_Founder confirms or overrides here → set contact card `outcome_modifier` accordingly._

### Direct quotes worth preserving

> "The existing tools just don't cut it for the part of the job that actually matters."
> "We budget £50k a year for this on one site alone."
> "If someone could just automate that one step, I'd sign tomorrow."

### Referrals offered

- Marcus Bell — Operations Lead, Example Corp B (introduce via LinkedIn)
- Priya Shah — Ops Director, Example Corp C (offered to make intro directly)

### Next questions raised

- Are operations managers or directors the actual budget holders?
- Does the £8k per-job figure hold across smaller operators?
- What's the specific failure mode of the current tools — coverage, accuracy,
  or something else?

### Cross-idea gaps harvested

Pains the contact raised that map to no assumption in the current graph. Appended to
`signals/gaps-log.md` by the capture skill. Never linked to evidence, never scored.

- 2026-07-15 — reconciles contractor invoices against work orders by hand, ~2 days/month
  type: interview-residue
  source: C7 (Operations Manager) · reports/{slug}/03-validation/A2-2026-07-15/interviews/sarah-chen-2026-07-15-notes.md
  unprompted: yes
  status: open

_(write "(none)" if the contact raised nothing off-graph — that's the common case)_

### Evidence entries to append

For `03-validation/{A_ID}-{date}/../evidence.md`:

- id: E{N}
  date: 2026-07-15
  source: Sarah Chen (Operations Manager, Example Corp)
  source_type: customer_interview
  claim: "Operations managers pay ~£48k/year per site to do this step by hand because existing tools can't cover the hard part."
  assumption_linked: A2
  verdict: supports
  confidence: 4
  notes: "Named specific £ and cadence. Has tried alternatives. Offered peer intros."
  next_question_raised: "Is £8k/incident representative across smaller UK contractors?"
```

## Rules for the raw notes half

- Don't reformat notes into structure — the capture skill does that
- Direct quotes in double-quotes. Paraphrases without quotes
- If unsure whether something was said or you inferred it, prefix with `(inferred)`
- If the contact went off-topic to another assumption, note it but don't try to link — the
  capture skill will surface it

## Rules for the structured capture half

- Every quote in `### Direct quotes worth preserving` must appear verbatim somewhere in
  raw notes
- False positives must be flagged, not silently dropped
- The proposed `outcome_modifier` MUST have reasoning that cites specific evidence from
  raw notes
- Evidence entries drafted here are appended to `evidence.md` by the capture skill, not
  copied manually
- Cross-idea gaps go to `signals/gaps-log.md` only. They carry the observation plus a path
  pointer — never an assumption ID, confidence, or verdict, because that log is read by
  every idea's sessions

## Naming convention

`{contact-slug}-{YYYY-MM-DD}-notes.md`

- `contact-slug` — lowercase kebab-case of the contact name (`sarah-chen`)
- If the same contact is interviewed twice on different dates, that's two files. If
  interviewed twice on the same date (rare), append `-v2`.
