---
purpose: The assumption DAG for H1 (remanufacturing) — parked with its hunch, not falsified.
idea: high-mix-manufacturing
hunch_id: H1
parked: 2026-09-02
last_updated: 2026-09-02
---

# Assumption graph — H1 (superseded, revivable)

H1 was superseded on 2026-09-02 when founder attention moved to H2. It was **not falsified**
— zero conversations were held against it, so every node below is still an open question and
may be revived intact if H2 dies.

These nodes moved out of the live `graph.md` for one reason: the generator ranks every node
in that file, and a parked hunch's nodes were outranking the active hunch's. Parking them
here keeps the ranking honest.

**H1A9-H1A12 remain allocated and must never be reissued to a different claim** — reviving
H1 means restoring these IDs with these meanings, per the burned-ID rule in CLAUDE.md.

assumptions:
  - id: H1A9
    assumption: >-
      A large enough share of discarded furniture is solid wood or metal frame — the only
      materials that can be restored to a sellable condition — rather than MDF or
      particleboard, which cannot be recycled into new board at all.
    hunch: H1
    category: market
    lens: feasibility
    validation_track: supply
    why_it_matters: >-
      This is the root and it gates everything. The sizing model's recoverable-share input
      swings gross profit more than any other number. At 15% there is a business; at 5% the
      same revenue needs three times the geography, and the logistics that killed Kaiyo get
      three times worse.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 5
    kill_power: 5
    test_cost: 1
    parent_assumptions: []
    child_assumptions: [H1A10, H1A11, H1A12]
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      Call five junk removal operators and ask one question: "of the furniture you pick up,
      roughly how much is real solid wood or metal versus the pressed-board flat-pack stuff?"
      Anyone who loads a truck knows this instantly. No pitch, no explanation.
    disconfirmation: >-
      If the median answer across five operators is below 10%, the addressable stream is too
      thin to build on and H1 needs a different input source or dies.
    stop_rule: "Stop after 8 operators or 1 week, whichever comes first."
    icp_segment: >-
      People who physically handle discarded furniture daily — junk removal crews and
      operators, and the movers who refer to them.
    icp_valid_tiers:
      - {name: junk_removal_operator, side: supply}
      - {name: home_mover, side: supply}
      - {name: municipal_waste, side: supply}
    domain_data_sources: []
    icp_valid_titles: [Owner, Franchisee, Operations Manager, Crew Lead, Dispatcher]
    icp_out_of_scope:
      - "furniture retailers (they see new goods, not the waste stream)"
      - "anyone estimating rather than handling — a guess from an office is not the number"

  - id: H1A10
    assumption: >-
      The input costs nothing or less than nothing — the people who currently hold this
      material are paid to take it away, and would hand it over rather than pay to dump it.
    hunch: H1
    category: willingness_to_pay
    lens: viability
    validation_track: supply
    why_it_matters: >-
      Negative-cost feedstock is what makes pallet recycling work and it is the single
      biggest lever on unit economics. If you have to pay for input, the margin math changes
      completely and you are competing with existing resale buyers.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 4
    kill_power: 4
    test_cost: 1
    parent_assumptions: [H1A9]
    child_assumptions: []
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      In the same calls: "do you charge to haul it away, and what does it cost you to dump
      it?" Both numbers, from the same person.
    disconfirmation: >-
      If operators say they already sell the good pieces to resale buyers at a price, the
      input is not free and someone is ahead of you in the queue.
    stop_rule: "Settled by the same calls as H1A9."
    icp_segment: "Junk removal operators and movers who currently charge for disposal."
    icp_valid_tiers:
      - {name: junk_removal_operator, side: supply}
      - {name: home_mover, side: supply}
    domain_data_sources: []
    icp_valid_titles: [Owner, Franchisee, Operations Manager]
    icp_out_of_scope: ["anyone who does not personally set or see the disposal price"]

  - id: H1A11
    assumption: >-
      A restored piece sold under our own brand, framed as reclaimed rather than secondhand
      and backed by a warranty, sells for materially more than a used piece — closer to the
      Restoration Hardware premium than the 80%-off remanufactured-office discount.
    hunch: H1
    category: willingness_to_pay
    lens: desirability
    validation_track: customer_adoption
    why_it_matters: >-
      This is the price ceiling, and the whole business lives or dies on it. At a used-goods
      price the contribution is roughly $45 a piece; at a branded reclaimed price it is
      $400-700. Nothing else in the model swings that far.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 5
    kill_power: 5
    test_cost: 2
    parent_assumptions: [H1A9]
    child_assumptions: []
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      Buy five solid-wood pieces off Facebook Marketplace or from a hauler. Restore them by
      hand or pay a local shop. Photograph and list them under a name, with a story, at a
      premium price. Record what they actually sell for and how long they take to sell.
    disconfirmation: >-
      If the five do not sell for at least twice what was paid for them, the premium framing
      does not hold and the model reverts to thin-margin used-goods resale — which is what
      Kaiyo died doing.
    stop_rule: "Stop after five pieces or three weeks. Do not buy a sixth to prove a point."
    icp_segment: >-
      Consumers buying furniture for a home they care about, at a price point above
      flat-pack — the people who currently buy reclaimed-look furniture at a premium.
    icp_valid_tiers:
      - {name: consumer_buyer, side: demand}
      - {name: interior_designer, side: demand}
    domain_data_sources: []
    icp_valid_titles: []
    icp_out_of_scope:
      - "bargain hunters on marketplace apps (they are buying the discount, not the object)"
      - "B2B procurement buyers (spec-for-spec comparison is exactly where the premium dies)"

  - id: H1A12
    assumption: >-
      Restoration takes few enough labour hours to bootstrap manually, and enough hours that
      automating it later is worth doing.
    hunch: H1
    category: technical
    lens: feasibility
    validation_track: operations
    why_it_matters: >-
      Both bounds matter. Above about four hours a piece you cannot run the manual version
      long enough to reach automation. Below about ninety minutes there is nothing for a
      robot to remove and the technology thesis evaporates.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 4
    kill_power: 3
    test_cost: 1
    parent_assumptions: [H1A9]
    child_assumptions: []
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      Time yourself on the five pieces. Log hours per piece, split by step: assess, strip,
      repair, sand, finish, photograph.
    disconfirmation: >-
      Over 4 hours a piece and manual bootstrapping does not work. Under 1.5 hours and the
      automation thesis has nothing to attack.
    stop_rule: "Settled by the same five pieces as H1A11."
    icp_segment: "Yourself, plus any restoration shop you pay to do it."
    icp_valid_tiers:
      - {name: restoration_shop, side: supply}
    domain_data_sources: []
    icp_valid_titles: [Owner, Restorer, Finisher]
    icp_out_of_scope: []
