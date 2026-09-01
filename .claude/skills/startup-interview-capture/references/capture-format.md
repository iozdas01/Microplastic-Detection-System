# Interview capture output format

The structured-capture scaffolding written below the `---` divider in an interview note, plus the evidence-entry and contact-card write formats for `startup-interview-capture`.

## Writing the output

### 1. Write structured capture below the divider

Follow the exact structure in `schemas/interview.md`. Every section is required — if a section has no content, write "(none observed)" so the founder can see you looked.

```markdown
---

## Structured capture
_Written by `startup-interview-capture` — human confirms outcome_modifier below._

### Mom Test signals

Unprompted mentions of the pain:
- <quote or paraphrase>

Past behaviour cited:
- <quote>

Specific costs named:
- Time: <if any>
- Money: <if any>
- Frequency: <if any>

Things they've tried to solve it:
- <list>

False positives detected:
- <quote> — <why it's a false positive>

### Signal summary
Assumption: {A_ID} — {assumption text}
Verdict: supports | contradicts | ambiguous
Confidence: N/5

### Proposed outcome_modifier
**{strong_confirm | moderate_confirm | weak | contradiction}** ({+1 | 0 | -0.5 | -1})

Reasoning: <cite specific raw-notes evidence>

_Founder confirms or overrides → set contact card `outcome_modifier` accordingly._

### Direct quotes worth preserving
> "..."

### Referrals offered
- Name — Role, Company — how framed

### Next questions raised
- <question>

### Cross-idea gaps harvested
<off-graph pains, drafted as gaps-log entries — or "(none)". These are appended to
signals/gaps-log.md, NOT to evidence.md, and never affect the score.>

### Evidence entries to append
<draft the YAML block(s) here so evidence.md gets a copy-paste-ready insertion>
```

### 2. Ask the founder to confirm outcome_modifier

Before touching contacts.md or evidence.md, ask:

> "I've drafted the structured capture with outcome_modifier: **{proposed}**. Reasoning: {one-line summary}. Confirm this, or override to {strong_confirm | moderate_confirm | weak | contradiction}?"

If the founder overrides, update the "Proposed outcome_modifier" line in the notes file to reflect their choice (and preserve your original proposal with a `~~strikethrough~~` so the audit trail survives).

### 3. Update the contact card in contacts.md

Find the contact block and update:
- `outreach_status`: → `done`
- `interview_date`: today's ISO date (or the frontmatter's interview_date)
- `outcome_modifier`: whatever the founder confirmed
- `evidence_score`: compute `(role_pts × signal_multiplier) + outcome_modifier` — this is the score contribution FROM THIS INTERVIEW; add it to any pre-existing evidence_score (contact could have been interviewed for another assumption before)
- `interviews`: append the relative path to this notes file

Also update the frontmatter `totals.done` counter (increment by 1) and `last_updated` (today's date).

### 3a. Regenerate the control room

After the contact card is updated, run:

```bash
python3 scripts/build_control_room.py {slug}
```

This refreshes `reports/{slug}/control-room.html`, where the outreach dashboard
lives. Never leave the session with contacts.md ahead of the control room.

### 4. Append evidence entries to evidence.md

For each substantive signal (usually 1–3 entries per interview), append a YAML block to `evidence.md` matching `schemas/evidence.md`. Ids continue monotonically from the highest existing.

Confidence rules for evidence entries:
- `strong_confirm` → confidence 4
- `moderate_confirm` → confidence 3
- `weak` → confidence 2
- `contradiction` → confidence 4 (contradictions are strong evidence too, they just point the other way)

`verdict` reflects direction: supports (any confirm) / contradicts (contradiction) / ambiguous (weak).

### 5. Append harvested gaps to signals/gaps-log.md

For each entry under "Cross-idea gaps harvested", append to the `## Entries` section of `signals/gaps-log.md` in the format that file specifies:

```markdown
- {interview_date} — {the observation, in the contact's terms, no evaluation}
  type: interview-residue
  source: {contact_id} ({role}, {sector}) · {relative path to this notes file}
  unprompted: {yes if they raised it themselves; no if it came out only after you asked}
  status: open
```

Two hard constraints, both from the "What must never go in" section of the log:

- **Carry a path pointer, not a summary of what the interview proved.** No assumption IDs, no confidence, no verdict, no evidence grades. The log is cross-idea; anything idea-scoped that leaks in re-introduces context bleed through the back door.
- **Record the observation, not a conclusion.** "Reconciles contractor invoices by hand, ~2 days/month" is an entry. "There's a product in invoice reconciliation" is not — that judgement belongs to a review pass, months from now, with the whole log in view.

This step never touches evidence.md, contacts.md, or the score. If there were no harvested gaps, skip it silently.

### 6. Give the founder a summary

End with a 3-4 line summary the founder can read in 15 seconds:

```
Captured: {contact_name} · A{X} · {outcome_modifier} ({±score})
Contact evidence_score updated: {old} → {new}
Evidence entries added: E{a}, E{b}, E{c}
Off-topic mentions surfaced: {list, or "none"}
Gaps logged: {count, or "none"} → signals/gaps-log.md
```
