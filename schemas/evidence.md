# Schema: Evidence Ledger

One file per idea. Every claim that informs the assumption graph lives here.
Each entry is linked to a specific assumption — never free-floating.

```yaml
idea: example-idea
entries:
  - id: E1
    date:
    source:                     # URL, author, company, interview subject
    source_type:                # vocab:evidence_source_type
    claim: ""
    assumption_linked: A1       # ID from assumption graph
    verdict:                    # vocab:verdict
    confidence:                 # vocab:evidence_confidence (1–5). Defaults from
                                # maps.source_type_to_confidence; may be graded
                                # DOWN with a stated reason in `notes`, never up.
    notes: ""
    next_question_raised: ""    # what this evidence makes you want to know next
```

## Evidence Quality Hierarchy

Declared once in `schemas/vocabularies.yaml` → `vocabularies.evidence_confidence`,
with the default grade per source type in `maps.source_type_to_confidence`. This is
the ONE hand-assigned strength grade in the repo — assumption-level strength is
derived from linked entries by the generators (`scripts/idea.py`).

Do not restate the ladder here or anywhere else. It previously existed in three
mutually incompatible forms; `scripts/validate_repo.py` now fails the commit if a
value outside the registry appears.

## Key rule

Every entry must answer: **which assumption does this update, and in which direction?**
If you can't answer that, the evidence isn't ready to log — figure out the link first.
