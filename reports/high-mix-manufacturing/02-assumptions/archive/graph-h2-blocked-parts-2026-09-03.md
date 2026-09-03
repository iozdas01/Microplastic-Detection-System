---
purpose: The assumption DAG for H2 (blocked-part machining) — parked with its hunch, not falsified.
idea: high-mix-manufacturing
hunch_id: H2
parked: 2026-09-03
last_updated: 2026-09-03
reconstructed: true
---

# Assumption graph — H2 (superseded, revivable)

H2 was superseded on 2026-09-03 when the founder moved to H3. **Not falsified.** One message
went out against it (C20, Viliam Kacerik, 2026-09-02), unanswered when the lane was parked.
The bottom-up sizing in `../../research/REPORT-h2.md` stands.

## ⚠️ This file is RECONSTRUCTED, and one node is LOST

On 2026-09-03 two sessions wrote `graph.md` concurrently. The archive step ran after the other
session had already replaced the file with H3 content, so it captured an H3 node instead of the
H2 nodes it was supposed to preserve. `reports/` is untracked in git, so there was no history
to recover from.

- **H2A1, H2A2, H2A3** below are restored verbatim from the session transcript that authored
  them. They are believed exact but have not been diffed against a saved copy.
- **H2A4 IS LOST.** It was authored by the other session and never entered this one's context.
  All that survives is what cites it: `evidence.md` E2 (`contradicts`) and E3 (`supports`), both
  from a Google Trends demand sweep, which together imply H2A4 claimed something about
  **measurable inbound search demand for blocked-part vocabulary**. E2 records that all four
  swept terms — "obsolete parts", "custom replacement part", "part no longer available",
  "reverse engineering" — had no measurable US search demand.

**H2A1-H2A4 remain allocated and must never be reissued.** If H2 is revived, H2A4 must be
rewritten from scratch under a new ID or restored from the other session's own record; do not
guess it back into existence from the evidence entries above.

assumptions:
  - id: H2A1
    assumption: >-
      Supply chain, procurement and maintenance people can name, unprompted, a recent part
      they could not get on the lead time they needed — and attach a real cost to the wait.
    hunch: H2
    category: pain
    lens: desirability
    validation_track: customer_adoption
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 4
    kill_power: 5
    test_cost: 1
    parent_assumptions: []
    child_assumptions: [H2A2, H2A3]
    status: untested
    disconfirmation: >-
      If fewer than 4 of 10 can name a specific recent instance without prompting, or if the
      median reported cost is absorbed without anyone escalating it, the pain is not sharp
      enough to price against and H2 needs a different problem.
    icp_valid_tiers:
      - {name: supply_chain_procurement, side: demand}
      - {name: maintenance_reliability, side: demand}
      - {name: manufacturing_operations, side: demand}

  - id: H2A2
    assumption: >-
      When a part is blocked, they will accept a non-OEM machined replacement — the
      qualification, warranty and drawing-ownership barrier is negotiable rather than absolute.
    hunch: H2
    category: trust
    lens: viability
    validation_track: customer_adoption
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 5
    kill_power: 5
    test_cost: 1
    parent_assumptions: [H2A1]
    child_assumptions: []
    status: untested
    disconfirmation: >-
      If 7 of 10 say a non-OEM part is categorically not permitted in their equipment, the
      addressable slice is only uncertified/legacy assets and the hunch narrows hard or dies.
    icp_valid_tiers:
      - {name: maintenance_reliability, side: demand}
      - {name: supply_chain_procurement, side: demand}
      - {name: manufacturing_operations, side: demand}

  - id: H2A3
    assumption: >-
      What keeps them from having it made is quote speed and confidence on a variable one-off
      — not the price of the part.
    hunch: H2
    category: competition
    lens: desirability
    validation_track: customer_adoption
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 4
    kill_power: 4
    test_cost: 1
    parent_assumptions: [H2A1]
    child_assumptions: []
    status: untested
    disconfirmation: >-
      If the dominant answer is "we got quotes quickly and they were simply too expensive",
      the mechanism is wrong and this is a cost play, not a software play.
    icp_valid_tiers:
      - {name: supply_chain_procurement, side: demand}
      - {name: manufacturing_operations, side: demand}
      - {name: maintenance_reliability, side: demand}

  # - id: H2A4  — LOST, see the warning above. Do not reissue this ID.
