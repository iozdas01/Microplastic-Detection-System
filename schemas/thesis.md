# Schema: Thesis Version

Every time the thesis materially changes, create a new versioned file.
Not a git diff — a human-readable before/after with what caused the change.

Filename: `<idea>_v<N>.md`

```yaml
idea: example-idea
version: 1
date:
previous_version_file:          # null for v1

thesis: |
  # The current thesis in 3–5 sentences.
  # What is the idea? Who is the customer? What must be true?
  # What is the wedge? What is the long-term vision?

core_bet: ""                    # one sentence — the single most important thing that must be true

what_changed_from_previous: ""  # null for v1
evidence_that_caused_change:    # assumption IDs or evidence IDs
  - 

open_questions:                 # what's still most uncertain
  - 

assumptions_confirmed_so_far:   # IDs
  - 
assumptions_killed_so_far:      # IDs — these are valuable, note what they taught you
  - 
assumptions_still_untested:     # IDs
  - 
```
