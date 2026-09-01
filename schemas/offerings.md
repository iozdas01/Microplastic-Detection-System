# Offering format — `reports/{slug}/04-mutation/offerings.md`

**LIVING artifact.** One per idea. Updates in place; never dated, never versioned — a
retired offering changes its `status`, it does not get a new file.

An offering is a candidate answer to *"what would we actually sell?"*, derived from pain
patterns that the evidence ledger already carries. It is not a product plan and not a
commitment. Its job is to make a hunch concrete enough that a buyer can react to it.

**The rule that makes this file worth having:** an offering must name the pain patterns it
came from and the evidence entries behind them. An offering that cannot cite either is an
idea someone had in the shower, and it goes in `signals/idea-parking.md` instead. The
Offerings tab of `control-room.html` renders the citation chips, so an uncited offering is
visibly uncited rather than quietly indistinguishable.

## File shape

Frontmatter, then one fenced `yaml` block holding an `offerings:` list. Both are parsed by
`scripts/idea.py`; the two-encodings rule in `ARCHITECTURE.md` applies.

```markdown
---
purpose: Candidate offerings derived from the pain patterns in the evidence ledger.
status: candidate          # the SET's maturity, not any one offering's
last_updated: YYYY-MM-DD
---

# Offerings

```yaml
offerings:
  - id: O1                 # O{N}, monotonic, never reused (a retired id is burned)
    name: Short handle for the thing
    one_line: >
      What it is, in the buyer's words, in one sentence. Not a pitch.
    buyer: >
      Who signs for it — the payer, who is often not the user. Name a role and the
      kind of organisation, and keep it consistent with the tier vocabulary this
      idea declared in `icp_valid_tiers`.
    the_case: >
      Why this would be bought. The argument, not the enthusiasm.
    derived_from: [P1, P3]           # pain-pattern ids from 03-validation/evidence.md
    evidence: [E4, E11, E12]         # ledger entry ids that carry those patterns
    proof_it_is_wanted: >
      The strongest observed thing short of a purchase — a workaround someone built,
      a budget line, a tool they already pay for. Not an opinion anyone expressed.
    already_sold_by: >
      Who sells this today, or the nearest substitute. "Nobody" is a finding that
      needs its own explanation, not a green light.
    biggest_risk: >
      The one thing most likely to make this wrong.
    second_risk: >
      The next one. Two is the cap: a list of six risks is a way of not choosing.
    authority_gate: >
      What would have to be true before building this, and who has to say yes.
    status: candidate      # candidate | testing | parked | retired
```
```

## Fields the generators depend on

`id`, `name`, `derived_from` and `evidence` are read by `build_control_room.py`. Everything
else renders if present and is omitted if absent — an empty field is better than a filled-in
guess, because the tab is read as a record of what is known.

## `status`

| Value | Means |
|---|---|
| `candidate` | Derived and written down. No one has been asked about it. |
| `testing` | An assumption in `graph.md` is currently testing this offering's core claim. |
| `parked` | Still plausible, not being pursued now. Say why in `the_case`. |
| `retired` | Ruled out. Keep the row and the reason — a retired offering that keeps recurring is a signal. |

Offerings are never deleted. The set is a record of what was considered, which is what stops
the same idea being re-derived and re-abandoned every few months.
