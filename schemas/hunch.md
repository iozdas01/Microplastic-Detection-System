# Schema: Belief and Hunch Lineage

One living lineage file: `reports/01-ideation/hunch-lineage.md`. Founder onboarding
creates it alongside `belief.md`, empty. The shotgun proposes the first hunch in explore
mode; it never tests without a current hunch.

The belief is the durable founder-owned anchor. A hunch is a falsifiable
interpretation of that belief for one segment, problem, and mechanism. Evidence
normally changes hunches before it changes the belief.

## Stable belief

Store the canonical belief verbatim in `input-context/belief.md`:

```yaml
---
idea: Example idea            # the display name — every generated page titles from it
created: YYYY-MM-DD
last_confirmed: YYYY-MM-DD
---

# Belief

> <ONE SENTENCE. The founder's field-level belief, in their own words.>

## How the founder states it

<The longer version — the reasoning, the distinctions, the way they actually talk about it.
Everything that did not fit the sentence goes here, still in their words.>

## Belief boundaries

- In scope:
- Out of scope:

## Starting point and SISP check

- Starting solution, technology, or analogy: <verbatim, or "none">
- Origin: <vocab:sisp_origin>
- Problem stated without the solution: <founder's words, or "not yet articulated">
- Founder-reported observations (context, not independent evidence):
  - <specific past observation or behavior; do not list assumptions as observations>
- SISP status: <vocab:sisp_status>
- What the shotgun must test independently:
  - <problem claim to search without relying on solution vocabulary>

## What would threaten the belief itself

- <Evidence that would challenge the anchor, not merely one hunch>
```

Changing the belief requires explicit founder confirmation. A shotgun may flag
`belief_at_risk`, but it must not silently rewrite this file.

The SISP section preserves the founder's starting solution without promoting it
to a hunch. Founder-reported observations remain context until corroborated.
`possible` and `probable` are research instructions, not rejection decisions.
The shotgun must look for the solution-free problem independently and may
return a hunch that retains, changes, or ignores the starting solution.

## Hunch lineage

Onboarding helps the founder express one initial hunch beneath the belief. It
structures the founder's current view; it does not validate or strengthen it.
Unknown components stay unknown. Once the founder confirms that this is the
hunch they want researched, onboarding records H1 as `active` and
`validation_status: untested`.

```yaml
---
belief_file: input-context/belief.md
active_hunch: H2
next_hunch_id: H4
last_updated: YYYY-MM-DD
---

# Hunch Lineage

## H1

status: retired                 # vocab:hunch_status
validation_status: untested     # vocab:hunch_validation_status
parent_hunch: null
created: YYYY-MM-DD
retired: YYYY-MM-DD
created_by: startup-belief-intake
created_by_artifact: input-context/example/belief.md
change_reason: founder-confirmed initial hunch
evidence_delta:
  - E1
  - reports/example/03-validation/A1-YYYY-MM-DD/synthesis.md

### Statement

We believe **[segment]** experiences **[specific recurring problem]** because
**[mechanism]**, and **[recent change]** makes a new approach viable now.

### Components

- Segment:
- Problem:
- Mechanism:
- Why now:
- Existing workaround:
- Plausible buyer:
- Cheapest next test:
- Hunch disconfirmation:

### Evidence

- Supports:
- Contradicts:
- Still unknown:

### Relationship to belief

- How this hunch expresses the belief:
- Evidence that would threaten only this hunch:
- Evidence that would threaten the underlying belief:
```

## Lineage rules

0. **Hunch IDs are `H1`, `H2`, `H3`… — unpadded, allocated per idea, never
   reused.** `next_hunch_id` in the frontmatter is the single allocator; take it
   and increment it in the same write. Assumption IDs are scoped to their hunch
   as `H{n}A{m}` (`H12A{m}` for a node shared by H1 and H2). Zero-padded `H00n`
   and unscoped `A{n}` are the pre-2026-08-09 forms: they are still valid inside
   dated artifacts already written, and are never minted again. Parsers match
   `^## (H\d+)` and accept both.
1. Founder onboarding creates H1 after the founder confirms both the belief
   and the initial hunch to test. H1 is `active` and `untested`, not validated.
2. A shotgun requires exactly one active hunch. If none exists, return to
   onboarding instead of inventing one. **The rule binds shotguns, not
   validation.** `active_hunch` accepts a scalar or a list: an idea probing one
   transaction through more than one entry point may run a hunch per door in
   parallel, each with its own nodes, converging on a shared root assumption.
   Evidence never transfers between doors — they name different payers buying
   different things — so each hunch carries its own kill conditions and its own
   contacts. A shotgun still takes exactly one; name which door it is running.
3. Every method in one shotgun run examines the same active hunch and belief.
4. A retain decision keeps the active hunch.
5. A narrow or `mutate_thesis` decision proposes a child hunch.
6. A branch or `new_vertical` decision proposes a sibling hunch.
7. A proposed replacement becomes active only after founder confirmation. Do
   not retire or replace the current hunch before that confirmation.
8. `kill` retires the hunch after founder confirmation. It does not retire the
   belief automatically.
9. `next_assumption` retains the active hunch and continues validation.
10. Retired hunches are kept by default; the lineage explains why the current
    hunch exists. A founder may direct that a retired ancestor be removed from
    the living file when it has become noise in the artifact read first every
    session. Before removing one: inline anything a surviving hunch borrows from
    it (kill conditions, workarounds, carried components) so the survivor is
    self-contained, record the removal and its reason in the file header, and
    leave the dated source artifacts untouched. Git history holds the rest.
    Never remove an active hunch or one another active hunch still depends on.
