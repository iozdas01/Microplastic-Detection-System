---
purpose: The assumption DAG for the active hunch — what must be true, ranked, each with the cheapest test that would settle it.
idea: high-mix-manufacturing
hunch_id: H3
belief_file: input-context/high-mix-manufacturing/belief.md
last_updated: 2026-09-03
active_assumption: H3A4

# Idea-owned market vocabulary. Bands are the OBSERVABLE proxy (LinkedIn company
# headcount) for the receipts ladder measured in
# research/data/processed/market_ladder_ranked.csv, which is sized on firm receipts
# — a number no profile shows. Headcount is what a sourcing pass can actually read,
# so it is what a contact is banded on; the receipts share each band maps to is the
# reason the band exists. Establishment shares are CBP 2022 (337920 / 442291).
size_bands:
  source: reports/high-mix-manufacturing/research/data/processed/market_ladder_ranked.csv
  observable_on: LinkedIn company page headcount range
  values:
    micro:      "<10 staff. 60% of blind makers, 92% of window-treatment stores, ~1% of receipts."
    small:      "10-49 staff. 27% of makers, 8% of stores."
    mid:        "50-249 staff. 10% of makers, 0.2% of stores."
    large:      "250-999 staff. 2.7% of makers, none in specialty retail."
    enterprise: >-
      1000+ staff, OR a national brand / retail channel selling made-to-measure at
      scale. The 10 largest makers hold 62.5% of manufacturing receipts and the 4
      largest specialty retailers 19.0% of retail receipts, so this band IS the
      market by value however few names are in it.
---

# Assumption graph — H3

Re-rooted 2026-09-03 when the hunch statement moved from remake cost to channel. The claim is
now that the measuring visit caps how much of the category can sell online, so the root is the
visit (H3A4), not the remake rate (H3A1).

Read in order: H3A4 asks whether the visit costs real money and real orders. H3A5 asks whether
measurement is actually why people do not buy online, rather than fabric, colour or
installation — the node most likely to kill the hunch. H3A6 asks whether a seller would
actually drop the visit, or whether it is load-bearing as a sales call.

H3A1-H3A3 are retained beneath the new root, un-falsified. H3A1 (remake rate) is now the
sharpest evidence that hand measurement cannot be trusted rather than the thing being sold
against. H3A3 is effectively answered: three linked entries contradict it and none support,
which is the record of why the remake framing carried no buyer.

**No percentage for the category's online share appears anywhere in this graph.** The
remembered "16%" was the all-retail e-commerce headline, not window coverings (E14). Nothing
keyless measures the real figure; the Economic Census product-line endpoint would, and needs a
free CENSUS_API_KEY.

assumptions:

  - id: H3A4
    assumption: >-
      The home measuring visit is a real, per-order cost that the seller carries, and it
      loses them business — they can name the fee and name orders they turned down because
      the visit was not worth making.
    hunch: H3
    category: pain
    lens: desirability
    validation_track: customer_adoption
    why_it_matters: >-
      This is the root under the restated hunch. If the visit is cheap and costs nobody a
      sale, the measuring step is an inconvenience rather than a constraint, and removing it
      buys nothing. E8 already has one national retailer at $225 a visit who declines jobs
      when the travel is too far — this asks whether that is one company or the category.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 3
    kill_power: 5
    test_cost: 1
    parent_assumptions: []
    child_assumptions: [H3A5, H3A6, H3A1]
    evidence_for: []
    evidence_against: []
    status: weakly_supported
    status_reason: >-
      E8 is one buyer naming both halves — a $225 fee and refused distant jobs — at
      confidence 4. One company is not a category, so this stays weak until it repeats.
      Set 2026-09-03 from the ledger.
    next_action: >-
      Two questions, in this order, before mentioning software at all: "what does it cost you
      to send someone out to measure?" then "when was the last time you turned a job down
      because it was too far to be worth the visit?" Let them volunteer the number.
    disconfirmation: >-
      If fewer than 4 of 10 can name a visit cost, or if the cost is absorbed with no
      lost orders behind it, the visit is not a constraint and the restated hunch fails at
      the root.
    stop_rule: "Stop after 10 conversations or 3 weeks, whichever comes first."
    icp_segment: >-
      People who decide whether a measuring visit is worth making, or who make it — the
      seller carrying the cost, not the customer receiving it.
    icp_valid_tiers:
      - {name: window_covering_manufacturer, side: demand}
      - {name: dealer_installer, side: demand}
      - {name: industry_software_vendor, side: expert}
    domain_data_sources: []
    icp_valid_titles: [Owner, General Manager, Plant Manager, Production Manager,
                       Operations Manager, Operations Director, Quality Manager,
                       Customer Service Manager, Continuous Improvement Manager,
                       Supply Chain Manager, Dealer Principal, Franchise Owner,
                       Install Manager, Sales Manager]
    icp_out_of_scope:
      - "consumers who bought blinds — they see the fee, never the economics behind it"
      - "anyone who has never priced or scheduled a measuring visit"

  - id: H3A5
    assumption: >-
      Measurement is the binding constraint on selling made-to-measure window coverings
      online — not fabric and colour choice, not installation, not the customer wanting to
      see the product first.
    hunch: H3
    category: market
    lens: desirability
    validation_track: customer_adoption
    why_it_matters: >-
      The sharpest node in the restated hunch and the one most likely to kill it. The
      category may sell offline for reasons that have nothing to do with dimensions —
      people want to feel the fabric, match a colour in their own light, or have someone
      else responsible for hanging it. If any of those dominate, solving measurement
      changes the channel not at all, and the whole statement collapses into a remake-cost
      story that H3A3 already shows nobody will pay for.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 5
    kill_power: 5
    test_cost: 2
    parent_assumptions: [H3A4]
    child_assumptions: [H3A6]
    evidence_for: []
    evidence_against: []
    status: untested
    next_action: >-
      Ask sellers who do both: "what makes someone buy in the showroom rather than on the
      site?" Rank what they say. Measurement has to come first or near it, unprompted. Then
      ask the online-only sellers the mirror question — what their customers get wrong, and
      whether it is dimensions or colour.
    disconfirmation: >-
      If sellers rank fabric, colour or installation above measurement as the reason people
      do not buy online, measurement is not the constraint and the hunch is wrong about
      channel even if it is right about cost.
    stop_rule: "Settled by the same conversations as H3A4, plus two online-only sellers."
    icp_segment: >-
      Sellers who see both channels — a dealer with a showroom and a website, or an
      online-only retailer who can say what their customers get wrong.
    icp_valid_tiers:
      - {name: window_covering_manufacturer, side: demand}
      - {name: dealer_installer, side: demand}
      - {name: industry_software_vendor, side: expert}
    domain_data_sources: []
    icp_valid_titles: [Owner, General Manager, Plant Manager, Production Manager,
                       Operations Manager, Operations Director, Quality Manager,
                       Customer Service Manager, Continuous Improvement Manager,
                       Supply Chain Manager, Dealer Principal, Franchise Owner,
                       Install Manager, Sales Manager]
    icp_out_of_scope:
      - "manufacturers with no direct retail channel — they never see why a consumer chose one"

  - id: H3A6
    assumption: >-
      A seller would drop the visit for an order if a remote measurement could be trusted —
      the visit is a workaround for unverifiable dimensions, not a sales tactic they want to
      keep.
    hunch: H3
    category: buyer
    lens: desirability
    validation_track: customer_adoption
    why_it_matters: >-
      The behaviour change the whole business depends on. The visit may be load-bearing for
      reasons beyond measuring: it is a sales call, an upsell, and the moment liability
      transfers. A seller who wants the visit for those reasons will not drop it however
      good the measurement gets, and then the product saves a cost nobody wanted saved.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 5
    kill_power: 5
    test_cost: 1
    parent_assumptions: [H3A4, H3A5]
    child_assumptions: []
    evidence_for: []
    evidence_against: []
    status: weakly_supported
    status_reason: >-
      E11 only, and it is weak by construction: a prompted hypothetical graded 2, flagged in
      the ledger as a Mom Test false positive. It is one person saying they would like such
      software to exist, which is not the same as dropping the visit. Set 2026-09-03.
    next_action: >-
      "If you could trust a measurement the customer sent you, would you still send someone
      out?" Then the real question: "what else does that visit do for you?" The second
      answer matters more than the first.
    disconfirmation: >-
      If sellers say the visit closes the sale or sets the price, they will keep it
      regardless of measurement accuracy, and the channel argument dies even with H3A4 and
      H3A5 intact.
    stop_rule: "Settled by the same conversations as H3A4."
    icp_segment: "Whoever decides that a visit happens — owner, sales manager, or dealer principal."
    icp_valid_tiers:
      - {name: window_covering_manufacturer, side: demand}
      - {name: dealer_installer, side: demand}
      - {name: industry_software_vendor, side: expert}
    domain_data_sources: []
    icp_valid_titles: [Owner, General Manager, Plant Manager, Production Manager,
                       Operations Manager, Operations Director, Quality Manager,
                       Customer Service Manager, Continuous Improvement Manager,
                       Supply Chain Manager, Dealer Principal, Franchise Owner,
                       Install Manager, Sales Manager]
    icp_out_of_scope:
      - "installers who attend visits but do not decide whether one is booked"

  - id: H3A1
    assumption: >-
      Remakes caused by wrong measurements are a material and tracked cost for made-to-measure
      window covering manufacturers — they can state a rate, and it is not trivial.
    hunch: H3
    category: pain
    lens: desirability
    validation_track: customer_adoption
    why_it_matters: >-
      NO LONGER THE ROOT (re-rooted 2026-09-03 when the statement moved from remake cost to
      channel). It is now the cleanest evidence that a measurement taken by hand cannot be
      trusted — a remake is that failure with a price on it. A material rate makes H3A5's case
      that measurement is the binding constraint; a trivial rate weakens it without killing it,
      because a seller can send someone out precisely so the rate STAYS low. That asymmetry is
      why this stopped being the root: a low remake rate is as consistent with the hunch as a
      high one. Order value remade still spans roughly $73m to $245m a year in US manufacturing
      alone across a 3% to 10% range.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 5
    kill_power: 5
    test_cost: 1
    parent_assumptions: [H3A4]
    child_assumptions: [H3A2, H3A3]
    evidence_for: []
    evidence_against: []
    status: untested
    status_reason: >-
      Back to `untested` on 2026-09-03. It briefly read `weakly_supported` on the strength of
      E8 and E11, but on re-reading, neither entry is about a remake RATE: E8 reports a
      measuring-visit fee and refused jobs (now linked to H3A4) and E11 is a prompted
      hypothetical about software (now H3A6). Nobody has given a rate, so nothing supports the
      claim this node actually makes.
    next_action: >-
      Ask manufacturers and dealers about the last remake they did before asking for a rate.
      "Walk me through the last remake. What went wrong, and where was the error made?" then
      "roughly what share of orders come back?" They track it monthly; it hits cost of goods.
      Then force the SPLIT, because the rate alone does not say which half of the pipeline is
      broken: "of the remakes you did last month, how many were a bad measurement at the
      window, and how many were a mistake made in the office after the order came in?" That
      one question decides whether capture or the office arithmetic is the product, and the
      answer is no longer symmetric — E24 records that deduction-to-cut-list is a commodity
      feature of this trade's ERP, sold to a claimed 1,000+ businesses. So a HIGH office share
      means either they do not run such a system or they run it and it is not trusted, and
      both of those are worth knowing. Follow with "which system do you run, and are your cut
      lengths calculated by the software or by a person?"
    disconfirmation: >-
      If the median reported rate across five manufacturers is under about 1% of orders, the
      pain is too thin to build on and H3 dies.
    stop_rule: "Stop after 8 manufacturer or dealer conversations, or 3 weeks."
    icp_segment: >-
      People inside made-to-measure window covering manufacturers and dealers who see the
      remake land — on a cost line, a production schedule, or their own margin.
    icp_valid_tiers:
      - {name: window_covering_manufacturer, side: demand}
      - {name: dealer_installer, side: demand}
      - {name: national_retail_channel, side: demand}
      - {name: industry_software_vendor, side: expert}
    domain_data_sources: []
    icp_valid_titles: [Owner, General Manager, Plant Manager, Production Manager,
                       Operations Manager, Operations Director, Quality Manager,
                       Customer Service Manager, Continuous Improvement Manager,
                       Supply Chain Manager, Dealer Principal, Franchise Owner,
                       Install Manager, Sales Manager,
                       # national_retail_channel — the people who own a fit guarantee
                       Category Manager, Merchandising Manager, Director of Merchandising,
                       Vendor Manager, Head of Customer Experience, Returns Manager,
                       Head of Quality, VP Operations]
    icp_out_of_scope:
      - "consumers who bought blinds — they see one event, never a rate"
      - "architects and interior designers who specify but never carry the remake cost"
      - >-
        commodity blind resellers who do not make to measure. This excludes stock-size
        retail; it does NOT exclude a national retailer's made-to-measure programme —
        Home Depot (Blinds.com), Wayfair, Lowe's and SelectBlinds all sell cut-to-size
        and all publish a customer-mismeasure remake guarantee, which makes them a
        party that has priced this exact failure. They are national_retail_channel.
      - "anyone at a national retailer working on stock-size or non-window categories"

  - id: H3A2
    assumption: >-
      The error originates at measurement capture, outside the factory, rather than in
      manufacturing tolerance or order entry.
    hunch: H3
    category: technical
    lens: feasibility
    validation_track: customer_adoption
    why_it_matters: >-
      This decides what the product even is. If windows are measured correctly and the factory
      cuts them wrong, a measurement tool is worthless and the answer is process control. The
      whole "own the capture and the machine" framing rests on this split.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 4
    kill_power: 5
    test_cost: 1
    parent_assumptions: [H3A1]
    child_assumptions: []
    evidence_for: []
    evidence_against: []
    status: weakly_supported
    status_reason: >-
      E9 aggregates four calls: every dealer sends a human to the window and none uses
      software to capture or verify. That supports the capture-side location of the error
      without isolating it from manufacturing tolerance. Set 2026-09-03 from the ledger.
    next_action: >-
      In the same conversations: "when one comes back, how do you work out whose number was
      wrong?" and "how often does it turn out to be the window itself, out of square?"
    disconfirmation: >-
      If manufacturers attribute most remakes to their own tolerance or to order entry rather
      than to the measurement, the mechanism is wrong and the product is not a measuring one.
    stop_rule: "Settled by the same conversations as H3A1."
    icp_segment: "The same people, weighted to whoever adjudicates a remake claim."
    icp_valid_tiers:
      - {name: window_covering_manufacturer, side: demand}
      - {name: dealer_installer, side: demand}
      - {name: national_retail_channel, side: demand}
      - {name: industry_software_vendor, side: expert}
    domain_data_sources: []
    icp_valid_titles: [Quality Manager, Production Manager, Plant Manager, Owner,
                       Customer Service Manager, Operations Manager,
                       Head of Quality, Returns Manager, Vendor Manager]
    icp_out_of_scope: ["anyone who never sees a remake investigated"]

  - id: H3A3
    assumption: >-
      The remake cost is concentrated on one party hard enough that they would pay to remove
      it, rather than being diffused across customers and absorbed as a cost of doing business.
    hunch: H3
    category: willingness_to_pay
    lens: viability
    validation_track: customer_adoption
    why_it_matters: >-
      SUPERSEDED IN PRACTICE by the re-rooting on 2026-09-03, and kept because its three
      contradicting entries are a finding rather than a gap. Under the remake framing this
      asked "would anyone pay to avoid a remake", and the answer kept coming back no — the
      cost is dispersed, dealers push it onto customers, and family-run owners were not
      enthusiastic. Under the channel framing the question is different and easier: would a
      seller pay to reach customers they currently drive to or turn away? That question now
      lives in H3A4 and H3A6. Do not spend conversations on this node; read it as the record
      of why the remake framing did not carry a buyer.
    importance: high
    quadrant: leap_of_faith
    uncertainty_score: 5
    kill_power: 4
    test_cost: 1
    parent_assumptions: [H3A1]
    child_assumptions: []
    evidence_for: []
    evidence_against: []
    status: contested
    status_reason: >-
      All three linked entries CONTRADICT and none support. E7: Stoneside shifts liability to
      the customer when the customer measured, so the cost is dispersed rather than
      concentrated. E10: family-run owners were not enthusiastic about a software fix. E12:
      the SUSB ladder shows the cost concentrated by FIRM SIZE — ten manufacturers carrying
      $4.6m-$15.5m each — rather than by role, which is a different shape from the one this
      assumption proposes. `contested` is generous: the vocabulary defines it as supporting
      AND contradicting evidence both present, and there is no supporting evidence here. It is
      not `killed` because nothing has falsified "someone would pay" — E12 arguably relocates
      the payer rather than removing them. One interview away from either. Set 2026-09-03.
    next_action: >-
      "When it is the customer's measurement, who ends up paying?" Then follow the money one
      more step: whoever they name, ask what it costs that party in a year.
    disconfirmation: >-
      If every party says someone else absorbs it, there is no buyer and H3 becomes a real
      problem with no customer.
    stop_rule: "Settled by the same conversations as H3A1."
    icp_segment: "The same people, plus whoever they name as bearing the cost."
    icp_valid_tiers:
      - {name: window_covering_manufacturer, side: demand}
      - {name: dealer_installer, side: demand}
      - {name: national_retail_channel, side: demand}
    domain_data_sources: []
    icp_valid_titles: [Owner, General Manager, Operations Director, Dealer Principal,
                       Franchise Owner, Sales Manager,
                       Category Manager, Merchandising Manager, Director of Merchandising,
                       Vendor Manager, Head of Customer Experience, Returns Manager]
    icp_out_of_scope: ["anyone without visibility of what a remake costs their business"]
