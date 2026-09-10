---
purpose: The assumption DAG for this idea — what must be true, ranked, each with the cheapest test that would settle it. Holds the active hunch's nodes plus any belief-level (H0) node that outlives whichever hunch is current.
idea: industrial-process-data-infrastructure
hunch_id: H1
belief_level_prefix: H0
belief_file: input-context/belief.md
last_updated: 2026-09-09
active_assumption: H1A2
---

# Assumption graph — H1

Started 2026-09-09 in the same session that wrote belief v4 and H1. No shotgun report
exists yet, so drafts are drawn from the H1 lineage entry and `belief.md` and say so; the
shotgun's initial-test run will add or contradict them.

# Idea-owned ICP tier vocabulary, declared 2026-09-09 with the first graph. `side` is
# the only thing the pipeline routes on; names are this market's own.
#   textile_mill          demand  — wet-processing (dyeing, washing, finishing) manufacturer
#   brand                 demand  — apparel/textile brand that reports the number
#   wastewater_operator   demand  — effluent treatment plant receiving mill water
#   lab_testing_provider  supply  — runs ISO 4484 / TMC methods on samples
#   sensor_vendor         competitor — inline particle / process instrumentation vendor
#   consortium_expert     expert  — TMC, standards bodies, academics on microfibers
#
# Read in order: H1A2 (are mills being asked for the number, and does it cost them) is
# the root; H1A3, H1A4 and H1A6 sit under it. H1A1 and H1A5 are independent roots.
# H1A7-H1A9 wait on H1A2. H1A10 is the belief's own pain claim asked of any line;
# it was first written as belief-level H0A1 and re-homed under H1 the same day at
# the founder's call (every node under the hunch). The id H0A1 is burned.
# Drafted 2026-09-09 without a shotgun run; each node says what it was drawn from.

# Active hunch H1 (confirmed 2026-09-09)
# In the fashion industry there are no sensors to detect microplastics, so a textile
# manufacturer cannot see or act on the microfibers their process releases; a real-time
# sensor with a feedback loop is the first product, and the first sensor feedback loop is
# the beachhead.


assumptions:

  - id: H1A1
    assumption: >-
      A standard test method for microfibers from textiles (ISO 4484, 2023) and incoming EU
      ecodesign requirements for textiles (delegated acts 2026, digital product passport
      2027) have turned microfiber release into a number a brand can be asked for, and that
      demand reaches the manufacturer within 24 months.
    hunch: H1
    category: timing
    lens: feasibility
    validation_track: customer_adoption
    test_method: agent
    why_it_matters: >-
      If nothing has changed, a mill has no new reason to want the number and H1 is early
      rather than wrong. Drawn from the 2026-09-09 desk check: ISO 4484-1/2/3 (2023), part 4
      in draft (2026), ESPR textiles delegated acts due 2026, DPP July 2027. Open question the
      founder has not answered: whether the pull is product rules on the brand or effluent
      rules on the mill — the desk check found only the former.
    importance: high
    quadrant: known_important
    uncertainty_score: 2
    kill_power: 4
    test_cost: 1
    parent_assumptions: []
    child_assumptions: [H1A7]
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      One afternoon: date the ESPR textile delegated acts and say which party they bind and
      whether microfiber release is in them; check whether any effluent rule (EU Urban
      Wastewater Directive recast, national textile BAT) names microfibers at the mill.
    disconfirmation: >-
      If the delegated acts do not name microfiber release, and no effluent rule binds the
      mill on it, there is no regulatory pull before 2028 and the why-now rests on brand
      voluntarism alone.
    stop_rule: "One afternoon of desk research or one week, whichever first."

  - id: H1A2
    assumption: >-
      Textile wet-processing mills are already being asked for a microfiber number by a
      brand, an auditor or a regulator, cannot produce one without an external lab, and
      that costs them orders, fees or time.
    hunch: H1
    category: pain
    lens: desirability
    validation_track: customer_adoption
    test_method: founder
    why_it_matters: >-
      The root. If no one is asking the mill for the number, there is no pain, no buyer and
      no reason for a sensor; every node beneath dissolves. Drawn from H1's problem clause
      ("cannot see or act on the microfibers their process releases") and its own note that
      the pain may only be felt once a brand or regulator demands the number.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 4
    kill_power: 5
    test_cost: 1
    parent_assumptions: []
    child_assumptions: [H1A3, H1A4, H1A6, H1A7, H1A8, H1A9]
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      Ten conversations with people who run wet processing at textile mills. One question
      first: "the last time someone asked you for a microfiber figure — who was it, what did
      you do, and what did it cost you?"
    disconfirmation: >-
      If fewer than four of ten can name anyone asking them for a microfiber number in the
      last year, or name one and report it cost nothing material, the pain is not there.
    stop_rule: "Ten conversations or one week, whichever first."
    icp_segment: >-
      Textile manufacturers running wet processing (dyeing, washing, finishing) who supply
      brands, and the people inside them who answer a brand's or auditor's technical request.
    icp_valid_tiers:
      - {name: textile_mill, side: demand}
      - {name: brand, side: demand}
      - {name: lab_testing_provider, side: supply}
      - {name: consortium_expert, side: expert}
    domain_data_sources: []
    icp_valid_titles: [Plant Manager, Production Manager, Dyehouse Manager, Head of Wet Processing,
                       Quality Manager, Compliance Manager, Sustainability Manager, Technical Director,
                       Environmental Manager, Owner, General Manager]
    icp_out_of_scope: ["garment assembly only (no wet processing)",
                       "sensor or instrumentation vendors",
                       "retailers with no manufacturing"]

  - id: H1A3
    assumption: >-
      The mill, not the brand and not the wastewater operator, holds both the obligation to
      produce the microfiber number and the budget to pay for producing it.
    hunch: H1
    category: buyer
    lens: desirability
    validation_track: customer_adoption
    test_method: founder
    why_it_matters: >-
      H1 sells to the manufacturer. If the brand pays for the lab and owns the result, the
      buyer is the brand and the product is a reporting tool, not a process monitor. Drawn
      from H1's "plausible buyer: unknown" line.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 4
    kill_power: 4
    test_cost: 1
    parent_assumptions: [H1A2]
    child_assumptions: [H1A6]
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      In the same H1A2 calls: "who paid for the last test, and whose problem was the
      result?" Then one call to a brand sustainability lead asking the mirror question.
    disconfirmation: >-
      If in six or more of ten cases the brand paid and kept the result, the mill is not
      the buyer.
    stop_rule: "Settled by the H1A2 conversations plus three brand calls; one week."
    icp_segment: "Whoever paid for the last microfiber test on a mill's output, and whoever received the result."
    icp_valid_tiers:
      - {name: textile_mill, side: demand}
      - {name: brand, side: demand}
      - {name: wastewater_operator, side: demand}
    domain_data_sources: []
    icp_valid_titles: [Plant Manager, Sustainability Manager, Compliance Manager, Sourcing Manager,
                       Head of Sustainability, Supplier Quality Manager, Environmental Manager]
    icp_out_of_scope: ["anyone without sight of who paid for testing"]

  - id: H1A4
    assumption: >-
      A real-time reading would change something the mill does during the run — dose,
      temperature, cycle, filtration — so an inline number is worth more to them than a
      lab report after the fact.
    hunch: H1
    category: pain
    lens: desirability
    validation_track: customer_adoption
    test_method: founder
    why_it_matters: >-
      This is the "feedback loop" in H1 and the belief's interpretation clause in one node.
      If no adjustment exists, detection alone is the product and it competes with a lab
      sample, not with nothing. Drawn from H1's mechanism and the belief's "adjust" language.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 4
    kill_power: 4
    test_cost: 2
    parent_assumptions: [H1A2]
    child_assumptions: []
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      Ask each H1A2 contact: "if you had that number live during the run, what would you
      change?" A named adjustment counts; "we'd know" does not.
    disconfirmation: >-
      If fewer than three of ten name a specific mid-run adjustment they would make, the
      loop has nothing to close and H1 is a detection product.
    stop_rule: "Same ten conversations; one week."
    icp_segment: "People who set process parameters in wet processing and could change them mid-run."
    icp_valid_tiers:
      - {name: textile_mill, side: demand}
      - {name: consortium_expert, side: expert}
    domain_data_sources: []
    icp_valid_titles: [Dyehouse Manager, Process Engineer, Head of Wet Processing, Production Manager,
                       Technical Director, Plant Manager]
    icp_out_of_scope: ["sustainability or compliance roles with no control over process settings"]

  - id: H1A5
    assumption: >-
      Nothing good enough exists: mills consider lab sampling and effluent filtration
      insufficient for the question being asked of them, and no inline microfiber sensor is
      in use at any of them.
    hunch: H1
    category: competition
    lens: viability
    validation_track: customer_adoption
    test_method: founder
    why_it_matters: >-
      The desk check found inline particle counters (Mettler Toledo ParticleTrack, Malvern
      Insitec Wet) and lab methods (ISO 4484, TMC); it found no inline microfiber identifier.
      Whether a mill regards what exists as enough is the half only a mill can answer.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 3
    kill_power: 4
    test_cost: 1
    parent_assumptions: []
    child_assumptions: []
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      Agent: one pass over instrumentation vendors and TMC signatories for any inline
      microfiber product or pilot. Founder, in the H1A2 calls: "what do you use today to
      answer that question, and is it enough?"
    disconfirmation: >-
      If any vendor sells an inline microfiber identifier that a mill in the pool uses, or
      if seven of ten mills say lab sampling answers the question adequately, this dies.
    stop_rule: "One afternoon of desk work plus the same ten conversations; one week."
    icp_segment: "Mills already answering the microfiber question by some means, and the vendors serving them."
    icp_valid_tiers:
      - {name: textile_mill, side: demand}
      - {name: sensor_vendor, side: competitor}
      - {name: lab_testing_provider, side: supply}
    domain_data_sources: []
    icp_valid_titles: [Quality Manager, Environmental Manager, Plant Manager, Technical Director,
                       Product Manager, Application Engineer]
    icp_out_of_scope: ["mills with no wet processing"]

  - id: H1A6
    assumption: >-
      A mill will commit money to a pilot before the sensor is proven, at a level that makes
      a hardware unit economic.
    hunch: H1
    category: buyer
    lens: viability
    validation_track: customer_adoption
    test_method: founder
    why_it_matters: >-
      Pain that nobody will pay to remove is not a business. The pilot is the proxy for the
      sale. Drawn from H1's unknown buyer and the belief's own counterweight: who signs the
      first cheque and why.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 5
    kill_power: 4
    test_cost: 2
    parent_assumptions: [H1A2, H1A3]
    child_assumptions: []
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      Once three mills have confirmed H1A2, put a paid pilot in front of each with a number
      on it and ask for a signature or a written no.
    disconfirmation: >-
      If none of three mills that confirmed the pain will sign a paid pilot at any price,
      willingness to pay is absent at the mill.
    stop_rule: "Three pilot asks or two weeks after H1A2 is confirmed; one week of asking."
    icp_segment: "Mills that confirmed H1A2 and hold the budget per H1A3."
    icp_valid_tiers:
      - {name: textile_mill, side: demand}
    domain_data_sources: []
    icp_valid_titles: [Owner, General Manager, Plant Manager, Managing Director, CFO, Technical Director]
    icp_out_of_scope: ["anyone who cannot sign for spend"]

  - id: H1A7
    assumption: >-
      Enough wet-processing sites supply EU-bound brands to matter, and they cluster in
      geographies the founders can reach.
    hunch: H1
    category: market
    lens: viability
    validation_track: investor_thesis
    test_method: agent
    why_it_matters: >-
      A wedge of forty mills is a consultancy. Sizing decides whether textile is the
      beachhead or just the first experiment. Drawn from H1's unknown segment size.
    importance: medium
    quadrant: known_important
    uncertainty_score: 2
    kill_power: 3
    test_cost: 1
    parent_assumptions: [H1A1, H1A2]
    child_assumptions: []
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      Count wet-processing establishments by country from trade and industry statistics,
      then cut to those supplying EU brands (TMC signatory supplier lists, brand supplier
      disclosures).
    disconfirmation: >-
      If fewer than 500 reachable sites carry EU brand exposure, the wedge cannot carry a
      hardware company and textile is an experiment, not a beachhead.
    stop_rule: "Two afternoons of desk work; one week."

  - id: H1A8
    assumption: >-
      Brands or The Microfibre Consortium will introduce us to their mills, because the
      number is theirs to report.
    hunch: H1
    category: distribution
    lens: viability
    validation_track: strategic_partnership
    test_method: founder
    why_it_matters: >-
      Mills are hard to reach cold; if the brand routes the intro, the channel is the brand.
      If not, distribution is one mill at a time.
    importance: medium
    quadrant: uncertain_minor
    uncertainty_score: 4
    kill_power: 3
    test_cost: 2
    parent_assumptions: [H1A2]
    child_assumptions: []
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      Three brand sustainability leads: "would you send this to your suppliers, and which
      ones?" A named supplier is a yes.
    disconfirmation: >-
      If none of three brands will name a supplier to introduce, the brand is not a channel.
    stop_rule: "Three brand conversations or one week."
    icp_segment: "Sustainability and sourcing leads at brands that report microfiber figures or signed the TMC 2030 commitment."
    icp_valid_tiers:
      - {name: brand, side: demand}
      - {name: consortium_expert, side: expert}
    domain_data_sources: []
    icp_valid_titles: [Head of Sustainability, Sustainability Manager, Sourcing Director,
                       Supplier Engagement Manager, Materials Innovation Lead]
    icp_out_of_scope: ["brands with no synthetic textile lines"]

  - id: H1A9
    assumption: >-
      A mill will let an instrument into its process water and act on a number it did not
      generate itself.
    hunch: H1
    category: trust
    lens: feasibility
    validation_track: customer_adoption
    test_method: founder
    why_it_matters: >-
      Access to the line and trust in the reading are what turn a sensor into a feedback
      loop. If mills refuse either, the product is a lab in a box.
    importance: medium
    quadrant: uncertain_minor
    uncertainty_score: 3
    kill_power: 3
    test_cost: 2
    parent_assumptions: [H1A2]
    child_assumptions: []
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      In the H1A2 calls: "who else has put an instrument in your line, what did it take to
      get it in, and did you change anything because of what it said?"
    disconfirmation: >-
      If mills describe past instruments as installed and ignored, or refuse access on
      principle, the loop cannot close on site.
    stop_rule: "Same ten conversations; one week."
    icp_segment: "Mill staff who decide what goes into the process line and who act on readings."
    icp_valid_tiers:
      - {name: textile_mill, side: demand}
    domain_data_sources: []
    icp_valid_titles: [Plant Manager, Maintenance Manager, Process Engineer, Dyehouse Manager, Technical Director]
    icp_out_of_scope: ["head-office roles with no site authority"]

  - id: H1A10
    assumption: >-
      People running a production line can name a recent case where a measured number sat
      waiting for a person to interpret it before anything was adjusted, and can say what
      the wait cost.
    hunch: H1
    category: pain
    lens: desirability
    validation_track: customer_adoption
    test_method: founder
    why_it_matters: >-
      This is belief v4's "numbers with no identity or meaning attached" turned
      into something an operator can answer. If nobody can name the case, the belief has no
      pain under it, and neither does H1.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 3
    kill_power: 5
    test_cost: 1
    parent_assumptions: []
    child_assumptions: []
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      Ask five people who run any high-mix production line, before any mention of sensors
      or software: "the last time a reading came off the line and someone had to decide
      what to do with it — what was it, who decided, and how long did the line wait?"
    disconfirmation: >-
      If four of five cannot name such a case, or name one and say the wait cost nothing
      material, the interpretation gap is not felt by the people who carry it.
    stop_rule: "Five conversations or one week, whichever first."
    icp_segment: "People who run or supervise a production line where readings are taken during the run."
    icp_valid_tiers:
      - {name: textile_mill, side: demand}
      - {name: consortium_expert, side: expert}
    domain_data_sources: []
    icp_valid_titles: [Production Manager, Plant Manager, Process Engineer, Quality Manager,
                       Operations Manager, Shift Supervisor, Head of Production]
    icp_out_of_scope: ["software or instrumentation vendors (supply side, not the pain)",
                       "consultants describing other people's lines"]
