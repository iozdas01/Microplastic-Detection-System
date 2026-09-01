---
purpose: The assumption DAG for H1 — what must be true, ranked, each with the cheapest test that would settle it.
idea: custom-kitchen-cabinets
hunch_id: H1
belief_file: input-context/custom-kitchen-cabinets/belief.md
last_updated: 2026-08-31
active_assumption: H1A2
---

# Assumption graph — H1

Extracted from the belief and H1 on 2026-08-31, seeded from the measurement pipeline in
`research/` rather than from a shotgun run: that corpus already exists and already moved the
thesis once, from configurable furniture to fitted cabinetry.

Founder-market-fit nodes and technical build bets are deliberately absent, per the standing
rule in `memory/MEMORY.md` (2026-08-09): this graph holds only claims testable by talking to
people. The build gates — can the app engineer a real kitchen, will a subcontract shop cut to
our files — are kill conditions that run after demand is proven, and they live on the build
board in `reports/custom-kitchen-cabinets/pages/build-board.html`.

Every node below is `untested`. Everything currently in the ledger is desk measurement
graded 2/5; no buyer, dealer or shop has been asked anything yet. That is the whole reason
outreach is the next move.

assumptions:
  - id: H1A2
    assumption: >-
      Kitchen & bath dealers, interior designers and design-build remodelers regularly lose,
      discount or delay jobs that fall outside their catalogue cabinet sizes, and that loss
      costs them enough money to want a different supplier.
    hunch: H1
    category: pain
    lens: desirability
    validation_track: customer_adoption
    why_it_matters: >-
      This is the root. If out-of-catalogue jobs are rare, cheap, or already absorbed by the
      lines a dealer carries, there is no wedge and every node below it dissolves. It is also
      the cheapest thing in the graph to settle — ten phone calls, no product, no spend.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 5
    kill_power: 5
    test_cost: 1
    parent_assumptions: []
    child_assumptions: [H1A4, H1A5, H1A8]
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      Build a list of ~70 trade targets in one metro (NKBA directory, Houzz, Google Maps —
      not furniture stores, which sell freestanding rather than fitted), then call ten and ask
      one question: "when a job doesn't fit your catalogue sizes, what do you do?" Do not
      pitch. Write the answer down verbatim.
    disconfirmation: >-
      If 6 or more of 10 dealers say their existing line handles out-of-catalogue work, or
      that the situation arises less than a few times a year, reject the wedge and stop.
    stop_rule: >-
      Stop after 15 completed calls or 3 weeks, whichever comes first. Fewer than 8 completed
      calls in 3 weeks is itself a finding about channel reachability.
    icp_segment: >-
      Trade specifiers of fitted cabinetry in one US metro — the businesses that put cabinets
      into a customer's kitchen and carry the cost when a job does not fit the catalogue.
    icp_valid_tiers:
      - {name: dealer_showroom, side: demand}
      - {name: design_build_remodeler, side: demand}
      - {name: interior_designer, side: demand}
      - {name: custom_cabinet_shop, side: supply}
      - {name: cabinet_software_vendor, side: competitor}
      - {name: cabinet_industry_expert, side: expert}
    domain_data_sources: []
    icp_valid_titles: [Owner, Principal, Kitchen Designer, Design Consultant, Showroom Manager,
                       Sales Manager, Project Manager, Design-Build Owner, Interior Designer,
                       Kitchen and Bath Designer, Estimator]
    icp_out_of_scope:
      - "furniture stores and freestanding-furniture retailers (wrong product — they sell
         catalogue pieces, not fitted runs measured to a room)"
      - "big-box home improvement retail (the catalogue IS their product; out-of-catalogue is
         not a loss they carry)"
      - "general contractors with no cabinetry specification role (they install what someone
         else specified)"
      - "cabinet hardware and component vendors (sellers into the shop, not payers of the pain)"

  - id: H1A7
    assumption: >-
      Inside live custom cabinet shops, design and engineering really is around half the human
      labour per kitchen, and the designer — not the machines or the floor — is the constraint
      that caps how many kitchens the shop can take.
    hunch: H1
    category: pain
    lens: desirability
    validation_track: customer_adoption
    why_it_matters: >-
      The whole belief rests on this split. If the 13.5-hour design figure is an artefact of
      the founder's own build model rather than a fact about real shops, removing the designer
      does not move the price and the company has no reason to exist.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 4
    kill_power: 5
    test_cost: 1
    parent_assumptions: []
    child_assumptions: [H1A1]
    evidence_for: [E4, E5]
    evidence_against: []
    status: untested
    next_action: >-
      Ask three to five custom cabinet shop owners how many hours go into a kitchen before a
      sheet is cut, and what they already use to do it (2020 Design, Cabinet Vision, Mozaik).
      Ask what their bottleneck is without naming a candidate.
    disconfirmation: >-
      If 3 or more of 5 shops put design and engineering below 25% of labour per kitchen, or
      name the shop floor rather than the front office as their constraint, the mechanism is
      wrong.
    stop_rule: "Stop after 6 shop conversations or 4 weeks, whichever comes first."
    icp_segment: >-
      Owners and lead designers at small custom cabinet shops — the people who personally do
      or supervise the drawing, quoting and engineering of a one-off kitchen.
    icp_valid_tiers:
      - {name: custom_cabinet_shop, side: supply}
      - {name: cabinet_industry_expert, side: expert}
      - {name: cabinet_software_vendor, side: competitor}
    domain_data_sources: []
    icp_valid_titles: [Owner, Founder, Shop Owner, Lead Designer, CAD Technician,
                       Production Manager, Estimator, CNC Programmer]
    icp_out_of_scope:
      - "large cabinet manufacturers running catalogue lines (their design cost is amortised
         across thousands of identical boxes — a different economics)"
      - "installers with no shop (they do not carry design labour)"

  - id: H1A4
    assumption: >-
      The dealer or remodeler is the buyer for this — they will resell an engineered custom run
      at their own margin rather than insisting the homeowner buy direct.
    hunch: H1
    category: buyer
    lens: viability
    validation_track: customer_adoption
    why_it_matters: >-
      Decides the entire go-to-market. Trade channel means ~70 targets in one metro and a
      price list; homeowner-direct means a consumer configurator and paid acquisition, which
      the research pipeline could not size — ad budget spans $114k to $1.71m on a placeholder.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 4
    kill_power: 4
    test_cost: 1
    parent_assumptions: [H1A2]
    child_assumptions: []
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      In the same calls as H1A2, ask who currently signs off on a cabinet supplier change and
      what would have to be true for them to put a new name in front of a client.
    disconfirmation: >-
      If dealers say they will only specify a line they can show in a showroom or have used
      for years, and none of ten will trial a new supplier on a single job, the trade channel
      is closed and the homeowner-direct door has to be opened instead.
    stop_rule: "Settled by the same 15 calls as H1A2; no separate budget."
    icp_segment: >-
      The person inside a dealer or remodeler who decides which cabinet lines the business
      carries and specifies.
    icp_valid_tiers:
      - {name: dealer_showroom, side: demand}
      - {name: design_build_remodeler, side: demand}
      - {name: interior_designer, side: demand}
    domain_data_sources: []
    icp_valid_titles: [Owner, Principal, Showroom Manager, Sales Manager, Purchasing Manager,
                       Kitchen and Bath Designer]
    icp_out_of_scope:
      - "homeowners (a different buyer and a different assumption — do not mix them into this
         node's evidence)"

  - id: H1A5
    assumption: >-
      A dealer will pay around $650 per linear foot for an engineered custom run — roughly
      $17,550 for a 27-foot kitchen — and resell it at a ~35% margin, because the alternative
      quote from a local shop is both higher and eight to twelve weeks out.
    hunch: H1
    category: willingness_to_pay
    lens: viability
    validation_track: customer_adoption
    why_it_matters: >-
      The unit economics in the plan sit entirely on this number. At $650/lf the variable cost
      of $5,831 leaves $11,719 of contribution; the whole break-even of 34 kitchens a year
      moves with it. It has never been quoted to anyone.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 5
    kill_power: 4
    test_cost: 2
    parent_assumptions: [H1A2]
    child_assumptions: []
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      Once a dealer describes a real out-of-catalogue job, ask what they paid or quoted for it
      and how long it took. Collect prices before naming one — a stated price anchors every
      answer after it.
    disconfirmation: >-
      If the prices dealers report paying for comparable custom runs cluster below $450 per
      linear foot, the contribution assumed in the plan is not there.
    stop_rule: "Stop after 10 dealers have named a real price for a real past job, or 4 weeks."
    icp_segment: >-
      Dealers and remodelers who have bought a one-off custom cabinet run in the last year and
      can name what it cost and how long it took.
    icp_valid_tiers:
      - {name: dealer_showroom, side: demand}
      - {name: design_build_remodeler, side: demand}
      - {name: custom_cabinet_shop, side: supply}
    domain_data_sources: []
    icp_valid_titles: [Owner, Principal, Purchasing Manager, Estimator, Project Manager]
    icp_out_of_scope:
      - "anyone quoting a catalogue price rather than a job they actually bought"

  - id: H1A8
    assumption: >-
      Nobody currently serving this channel can return a firm, engineered, machine-ready price
      for a one-off kitchen in under a day — so a ten-minute quote is a difference dealers
      can feel, not a marginal improvement.
    hunch: H1
    category: competition
    lens: viability
    validation_track: customer_adoption
    why_it_matters: >-
      The live demo — pricing a job the dealer is quoting right now, in front of them — is the
      entire pitch. If their existing supplier already turns a quote around same-day, there is
      no moment to sell.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 3
    kill_power: 3
    test_cost: 1
    parent_assumptions: [H1A2]
    child_assumptions: []
    evidence_for: [E3]
    evidence_against: []
    status: untested
    next_action: >-
      Ask each dealer how long a custom quote currently takes and how many revisions it goes
      through. Separately, check what 2020 Design, Cabinet Vision and Mozaik already automate.
    disconfirmation: >-
      If dealers report same-day or next-day firm quotes as normal, the wedge is speed-neutral
      and the pitch has to move to price or lead time instead.
    stop_rule: "Settled by the same 15 calls as H1A2, plus one afternoon on the software."
    icp_segment: >-
      Dealers who buy custom runs today, and the shops and software vendors who serve them.
    icp_valid_tiers:
      - {name: dealer_showroom, side: demand}
      - {name: custom_cabinet_shop, side: supply}
      - {name: cabinet_software_vendor, side: competitor}
      - {name: cabinet_industry_expert, side: expert}
    domain_data_sources: []
    icp_valid_titles: [Owner, Principal, Estimator, Kitchen Designer, Product Manager]
    icp_out_of_scope:
      - "vendors selling into unrelated trades"

  - id: H1A6
    assumption: >-
      The measured appetite for custom cabinets — 7.61% of "kitchen cabinets" search, with
      commercial-intent queries attached — reflects demand that would grow, not shrink, if the
      custom premium and the wait came down.
    hunch: H1
    category: market
    lens: viability
    validation_track: customer_adoption
    why_it_matters: >-
      The 7.61% is who wants custom at today's premium and today's lead time. The business
      sells custom at close to semi-custom price. Whether that widens the pool or merely
      redistributes it is the difference between a $182.9m SAM and a much smaller one, and no
      available dataset can settle it.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 4
    kill_power: 4
    test_cost: 2
    parent_assumptions: []
    child_assumptions: []
    evidence_for: [E1, E2, E6]
    evidence_against: []
    status: untested
    next_action: >-
      Ask dealers what share of their jobs would have gone custom if custom had cost 20% more
      than catalogue instead of 200% more, and had shipped in three weeks. Ask about past
      jobs, not hypothetical ones, wherever they can name one.
    disconfirmation: >-
      If dealers say the constraint on custom is the customer's taste or the design effort
      rather than price and lead time, then removing price and lead time does not widen the
      pool.
    stop_rule: "Settled by the same 15 calls as H1A2."
    icp_segment: >-
      Dealers and designers who can compare what a customer asked for against what they
      actually specified, on real past jobs.
    icp_valid_tiers:
      - {name: dealer_showroom, side: demand}
      - {name: design_build_remodeler, side: demand}
      - {name: interior_designer, side: demand}
    domain_data_sources: []
    icp_valid_titles: [Owner, Kitchen Designer, Design Consultant, Interior Designer,
                       Showroom Manager]
    icp_out_of_scope:
      - "anyone answering about cabinets they have never specified or sold"

  - id: H1A1
    assumption: >-
      What changed in the last 12-36 months is that a language model plus a constraint solver
      can take a homeowner-taken laser measurement and a description in plain words to an
      engineered, code-compliant, machine-ready cabinet run without a designer in the loop —
      and shops know their existing software does not do this.
    hunch: H1
    category: timing
    lens: feasibility
    validation_track: customer_adoption
    why_it_matters: >-
      Timing failures are the most common death for companies with a correct market thesis.
      If the incumbent CAD packages already close this gap, the window claimed here does not
      exist and the advantage is a few months of engineering, not a business.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 3
    kill_power: 4
    test_cost: 2
    parent_assumptions: [H1A7]
    child_assumptions: []
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      Ask shops and designers what their current software automates and where it still hands
      the job back to a person. The gap they describe unprompted is the answer; a gap we name
      first is not.
    disconfirmation: >-
      If shops report that their current package already generates layouts, quotes and CNC
      programs with only light human review, the timing claim is false.
    stop_rule: "Stop after 5 shop conversations plus one afternoon of vendor documentation."
    icp_segment: >-
      People who run the design software daily — shop designers, CAD technicians, CNC
      programmers — plus the vendors who sell it.
    icp_valid_tiers:
      - {name: custom_cabinet_shop, side: supply}
      - {name: cabinet_software_vendor, side: competitor}
      - {name: cabinet_industry_expert, side: expert}
    domain_data_sources: []
    icp_valid_titles: [Lead Designer, CAD Technician, CNC Programmer, Production Manager,
                       Owner, Product Manager]
    icp_out_of_scope:
      - "people who have never operated cabinet design software (out of competence — an
         out-of-competence answer enters the ledger as durable wrong evidence)"
