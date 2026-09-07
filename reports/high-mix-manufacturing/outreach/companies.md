---
purpose: The company registry for this idea — one entry per organisation, its sector, what it actually makes, and why it is on the list.
idea: high-mix-manufacturing
schema_version: 2
map_vocabularies:
  # Per-idea map axes. Declared here so the map forms as companies go in: adding a
  # value creates a lane. A value NOT listed here lands in the unmapped lane and is
  # counted as missing data, so a typo shows up rather than inventing a position.
  chain_position: [oem, tier1, tier2, tier3]
  proveout_exposure: [none, low, medium, high]
  integration: [software_only, software_plus_service, equipment, operates_machines, owns_factory]
  # `assembly` added 2026-08-27 for Bright Machines. Not a typo and not a stretch of an
  # existing value: this axis was drawn from a CNC-machining thesis and had no lane for
  # putting parts together. Declaring it keeps the gap visible rather than filing an
  # assembly company under machine_execution, where it would read as a machining rival.
  # `tooling` added 2026-08-27 for Atomic Industries. Same reasoning as `assembly`:
  # the axis was drawn from a CNC-machining thesis and had no lane for making the tool
  # rather than making the part. Filing a mould maker under machine_execution would read
  # them as a production rival; they sit one step upstream, and a mould tryout is the
  # prove-out of a tool. Declaring it keeps that distinction on the map.
  # `spec_capture` added 2026-09-03 for SiVIEW. The axis was drawn from a CNC-machining
  # thesis, where the spec arrives as a CAD file and the open jobs all sit downstream of it.
  # H3 is about the step BEFORE that: turning a physical thing into the numbers the job runs
  # on. Filing a measurement company under quoting or inspection_qa would read them as
  # downstream of a spec that, in made-to-measure, does not exist yet. Declaring it keeps
  # the empty lane visible — it is the lane H3 is entering.
  job_covered: [spec_capture, quoting, cam_programming, program_verification, setup_workholding, tooling, machine_execution, assembly, inspection_qa, scheduling_ops]
  sells_to: [shop, oem_buyer, machine_builder, none_yet]
  revenue_source: [filing, self_stated, estimate, unknown]
  # Capability axes for the window-covering software matrix, declared 2026-09-03. These are
  # the jobs the trade's own software does or does not do, ordered by where they sit in the
  # pipeline. `remote_capture` and `cross_shop_routing` are here specifically so the matrix
  # can render those columns EMPTY — that emptiness is the finding H3 rests on, and a column
  # nobody occupies only shows up if it is declared.
  # How each company stands to this idea, declared 2026-09-03 after the capability matrix
  # was read as a competitor table and was not one. Capability answers "what do they do";
  # this answers "what are they to us", and the two are independent — the most capable
  # company on the matrix (BlindMatrix) is rails, and the only true competitor
  # (Windowmaker) ships fewer capabilities than it does.
  #   rails         — owns the stage after ours; our Order goes into them
  #   competitor    — same job, same buyer, same budget line
  #   platform_risk — not competing today, but owns distribution and could bundle
  #   analogue      — different trade; proof the shape works, not a rival
  #   floor         — marks the category baseline, not a player
  relationship: [rails, competitor, platform_risk, analogue, floor]
  capability: [remote_capture, onsite_measure_app, quoting, dealer_orders, deductions_cutlist, machine_file_out, production_scheduling, inventory, machine_readback, cross_shop_routing]
  map: [client, startup, none]
  # `window_layer` added 2026-09-04. Every axis above was drawn from the CNC/prove-out
  # thesis and none of them can say WHERE in the window-covering trade a company sits, which
  # is the only question H3's maps ask. Values are the seven layers declared in
  # scripts/research/build_players_page.py — that file is the author of what each layer means;
  # this axis only records which one a company is in. `unpinned` is for a company the founder
  # spoke to but could not name.
  window_layer: [1, 2, 3, 4, 5, 6, 7, unpinned]
  # Geography is recorded only where a company has a real street presence that could be
  # visited. `lat`/`lon` are approximate, derived from the public address for plotting, and
  # are never a verification that the founder has been there.
  geo_status: [mapped, off_map, unknown]
  # Startup-map-only axes. Added 2026-08-27 when the startup scene was split onto its
  # own page. `liability_taken` is the belief's own axis: the claim under test is that
  # nobody sells into the prove-out job while carrying the first-run risk, so the map
  # has to be able to render that column empty.
  # part_guarantee vs owns_outcome, decided 2026-08-27 after two sessions graded
  # factory-owning suppliers differently on the same day. Owning a factory is NOT
  # the test — SendCutSend and OSH Cut own theirs and are part_guarantee.
  #   part_guarantee = commits to the part inside a PUBLISHED, BOUNDED envelope
  #     (a tolerance table, a process catalogue, a standard part class).
  #   owns_outcome   = commits to a custom part with no published envelope, where
  #     scoping the job is itself part of what they carry.
  # When neither is evidenced in writing, grade DOWN and say so in liability_notes.
  liability_taken: [none, warranty, rework_credit, part_guarantee, owns_outcome]
  stage: [pre_seed, seed, series_a, series_b, series_c, series_d_plus, public, incumbent_subsidiary]
  funding_source: [press, filing, self_stated, aggregator, unknown]
  touches_proveout: [none, adjacent, direct]
last_updated: 2026-09-03
migrated_from: Assumption-Lab/reports/manufacturing-execution-layer/outreach/companies.md
migration_note: >-
  Carried over whole on 2026-09-03, unedited, from the manufacturing-execution-layer idea in
  the predecessor repo. Same founder, same belief, and that idea is this one's ancestor, so
  the research is not another idea's state being borrowed — it is this lineage's own back
  catalogue arriving late.
  READ THIS BEFORE USING THE MAP: every axis here was drawn from a CNC-machining and
  prove-out thesis. `job_covered`, `touches_proveout` and `liability_taken` are all shaped by
  that question. The active hunch is now H3, made-to-measure window coverings, and NOT ONE of
  the 171 entries is a window-covering company. That is the gap, not a defect in the map, and
  it is what continuing this map means.
---

# Companies — manufacturing-execution-layer

**Pruned 2026-09-04 (founder decision).** 149 entries were deleted: every demand-side company
sourced for H1 and H2 (CNC job shops, precision and aerospace suppliers, semicap, the four CAM
incumbents, and the 2026-08-20 UniMaaS grant scrape that was never targeted or contacted). None
carried an interview or an assumption, and H3 does not buy from any of them. Their CO-ids are
burned and must never be reassigned; git holds the entries if an H1 or H2 revival needs them.

What remains is 34: the 16 supply-side startups, which are landscape intelligence rather than
outreach targets and were explicitly left untouched; the 6 window-covering trade software
vendors and 7 remote-measurement analogues that the H3 capability matrix reads; and the 5
window-covering sellers on the demand side.

## Cyncly

id: CO173
map: startup
canonical_name: Cyncly (Compusoft Group)
also_known_as: [Cyncly, Compusoft, 2020 Technologies, FeneVision]
country: GB
tier_side: supply
tier: ""
sector: Design, quoting and ERP software for kitchens, bath, furniture, windows and doors
relationship: platform_risk
job_covered: quoting
integration: software_only
sells_to: shop
liability_taken: none
touches_proveout: none
stage: incumbent_subsidiary
total_raised_usd: 0
funding_source: press
revenue_usd: 420100000
revenue_source: estimate
founded: 2021
headcount: 2300
headcount_source: "company statement at merger; an aggregator says 3,965 - treat as a wide band"
capabilities_have: quoting, dealer_orders, production_scheduling, inventory
capabilities_partial: onsite_measure_app, deductions_cutlist, machine_file_out
capability_source: "company product pages, 2026-09-03"
source_url: https://www.cyncly.com/industries/windows-doors-glass
sources_note: >
  Swept 2026-09-03 from company and investor material. Revenue is a single aggregator figure
  with no filing behind it and the headcount sources disagree by 70% - both are held loosely.
services:
  - "End-to-end design, visualisation, configuration, pricing, quoting, ERP and manufacturing"
  - "FeneVision - dealer and distributor quote, order and track"
  - "Windows, doors and glass vertical alongside kitchen, bath and furniture"
makes_or_does: >
  The consolidator. Formed 2021 by merging Compusoft (TA Associates) and 2020 Technologies
  (Genstar Capital), then bolted on further acquisitions. Company statement at merger: 2,300+
  employees, 70,000+ customers, 100+ countries. Sells the whole dealer-to-factory chain across
  several made-to-order home trades, of which windows and doors is one.
funding_notes: >
  Private-equity owned, not venture funded - `total_raised_usd: 0` means not-venture-raised.
  TA Associates invested in Compusoft 2018; Genstar held 2020 Technologies; the two merged 2021.
hmlv_relevance: >
  The scale answer to "is there money in this trade's software". Whatever the exact revenue,
  this is a multi-hundred-million business built entirely on quoting and ordering for
  made-to-order home products - and not one line of it measures anything. It is the ceiling
  and the shape of the incumbent at once.
liability_notes: >
  None evidenced.
map_note: >
  `touches_proveout: none` - axis does not transfer.


## BlindMatrix

id: CO174
map: startup
canonical_name: BlindMatrix Ltd
also_known_as: [BlindMatrix, Blind Matrix, BlindMatrix Private Limited]
country: GB
tier_side: supply
tier: ""
sector: End-to-end ERP for blinds, curtains, awnings and shutters
relationship: rails
job_covered: deductions_cutlist
integration: software_only
sells_to: shop
liability_taken: none
touches_proveout: none
stage: incumbent_subsidiary
total_raised_usd: 0
funding_source: unknown
revenue_usd: 22000000
revenue_source: estimate
founded: 2002
headcount: 125
headcount_source: "aggregator band 51-200; midpoint used"
capabilities_have: onsite_measure_app, quoting, dealer_orders, deductions_cutlist, machine_file_out, production_scheduling, inventory
capabilities_partial: ""
capability_source: "blindmatrix.com/erp-for-manufacturers, 2026-09-03"
source_url: https://blindmatrix.com/erp-for-manufacturers/
sources_note: >
  Swept 2026-09-03 from the company's own manufacturer ERP page. Sources give founding as
  2002 or 2003; the earlier is used. Revenue is an aggregator estimate with no filing behind
  it. HQ Bletchley, Milton Keynes, with a development arm registered in Tamil Nadu.
services:
  - "BM Sales - appointment through measurement to installation"
  - "Production management - plan, schedule and track manufacturing"
  - "Cut sheets, allowances and manufacturing calculations"
  - "Cut lengths pushed to integrated cutting tables via XML or CSV"
  - "Work orders and barcode labels"
  - "Dealer pricing, orders and tracking; inventory; franchise management"
makes_or_does: >
  The most complete fulfilment stack in this trade, and the entry that closed the compiler
  wedge. Their own copy states the software will "generate the cut sheets, allowances, and
  manufacturing calculations" and "send the information about the cut lengths after adding or
  deducting the allowances" to integrated cutting tables via XML or CSV, plus barcode work
  orders. Claims 1,000+ businesses across UK, US, AU, CA, NZ and ZA.
funding_notes: >
  No venture funding found. Appears founder-owned and bootstrapped over twenty years.
hmlv_relevance: >
  Directly occupies phases 0, 1 and 3 of the proposed architecture: order intake, deduction
  to cut list, and machine file out. Selling a compiler to a fabricator that already runs this
  is not a wedge. What it does NOT do is originate the measurement - it begins after a human
  has arrived at the window with numbers - and it does not route across shops or read anything
  back from a machine. Those are the two columns left open.
liability_notes: >
  None evidenced. Software licence.
map_note: >
  `touches_proveout: none` - axis does not transfer.


## Windowmaker Software

id: CO175
map: startup
canonical_name: Windowmaker Software Limited
also_known_as: [Windowmaker, Windowmaker Measure, Windowmaker Cloud]
country: GB
tier_side: supply
tier: ""
sector: Quoting, measuring and manufacturing software for windows and doors
relationship: competitor
job_covered: spec_capture
integration: software_only
sells_to: shop
liability_taken: none
touches_proveout: none
stage: incumbent_subsidiary
total_raised_usd: 0
funding_source: unknown
revenue_usd: 21800000
revenue_source: estimate
founded: 1983
headcount: 131
headcount_source: "aggregator, April 2026"
capabilities_have: onsite_measure_app, quoting, dealer_orders, production_scheduling
capabilities_partial: deductions_cutlist, machine_file_out
capability_source: "windowmaker.com/windomaker-measure, 2026-09-03"
source_url: https://windowmaker.com/windomaker-measure/
sources_note: >
  Swept 2026-09-03 from the product page. Revenue and headcount are aggregator figures.
  Windows and doors rather than window coverings - adjacent trade, same measurement job.
services:
  - "Windowmaker Measure - iOS and Android on-site measuring app"
  - "Pairs with laser measures for instant capture"
  - "Validates multiple measurements against each other"
  - "Computes frame sizes from configurable clearances"
  - "Quotes and measurement sheets on the spot"
makes_or_does: >
  Established 1983, London. The closest thing in either trade to measurement software - and
  the clearest demonstration of the gap. It pairs with a laser measure, cross-validates
  readings against each other, and derives frame sizes from clearances. Every one of those
  features assumes a person is standing at the opening.
funding_notes: >
  No venture funding found. Forty-three years old.
hmlv_relevance: >
  The single most useful competitor to have read, because it defines the boundary precisely.
  Windowmaker digitises the RECORDING - it makes the surveyor's number better, faster and
  checkable. It does not remove the surveyor. Forty-three years in the trade and the human is
  still on the ladder. That is either strong evidence the visit cannot be removed, or evidence
  that nobody with this distribution ever tried. The `deductions_cutlist` capability is graded
  partial: clearance-to-frame-size arithmetic is deduction logic, but no cut-list output was
  confirmed on the page swept.
liability_notes: >
  None evidenced.
map_note: >
  `touches_proveout: none` - axis does not transfer.


## BlinQ Software

id: CO176
map: startup
canonical_name: BlinQ Software Pty Ltd
also_known_as: [BlinQ, blindsapp]
country: AU
tier_side: supply
tier: ""
sector: Cloud quoting and CRM for window furnishings
relationship: rails
job_covered: quoting
integration: software_only
sells_to: shop
liability_taken: none
touches_proveout: none
stage: ""
total_raised_usd: 0
funding_source: unknown
revenue_usd: 0
revenue_source: unknown
founded: 0
headcount: ""
capabilities_have: quoting, dealer_orders, deductions_cutlist, inventory
capabilities_partial: onsite_measure_app
capability_source: "blinq.com.au product pages, 2026-09-03"
source_url: https://www.blinq.com.au/
sources_note: >
  Swept 2026-09-03. No founding date, revenue or headcount disclosed anywhere checked - the
  absence is recorded rather than estimated. States 1,000+ users, Australia-led but sold
  globally.
services:
  - "Cloud quoting, CRM and ecommerce for window furnishing businesses"
  - "Orders organised with detailed deductions and labels"
  - "Inventory management"
makes_or_does: >
  Australia-origin cloud platform for window covering retailers and makers - quoting, CRM,
  ecommerce and inventory, with order deductions and labelling. States over 1,000 users.
funding_notes: >
  None found. No disclosed round, no disclosed revenue.
hmlv_relevance: >
  Second confirmation that deduction logic is a commodity feature in this trade rather than a
  differentiator: a mid-sized regional player ships it too. Also confirms the geographic shape
  of the market - the trade's software is regional, with a different incumbent per continent,
  which is a distribution fact worth knowing before choosing where to sell.
liability_notes: >
  None evidenced.
map_note: >
  `touches_proveout: none` - axis does not transfer.


## Quoterite

id: CO177
map: startup
canonical_name: Retail Pro Pty Ltd
also_known_as: [Quoterite, Smartpad Pro]
country: AU
tier_side: supply
tier: ""
sector: Quoting and ordering automation for window furnishings
relationship: rails
job_covered: quoting
integration: software_only
sells_to: shop
liability_taken: none
touches_proveout: none
stage: ""
total_raised_usd: 0
funding_source: unknown
revenue_usd: 0
revenue_source: unknown
founded: 2016
headcount: ""
capabilities_have: quoting, dealer_orders
capabilities_partial: onsite_measure_app, deductions_cutlist
capability_source: "quoterite.com, 2026-09-03"
source_url: https://quoterite.com/
sources_note: >
  Swept 2026-09-03. Founded 2016 by Aaron and Renee LeCornu, who ran a window-covering retail
  business from 2002 - an operator-founded tool. Rebranded from Smartpad Pro. No revenue
  disclosed; the only financial figure found is a stated 1.3M investment into the product.
services:
  - "Quoting for indoor and outdoor blinds, awnings, shutters, curtains, security screens, films"
  - "Linked quoting and ordering with automations"
  - "Dealer portal"
makes_or_does: >
  Quoting automation across the full window furnishing product range, built by people who ran
  a window covering retail business first. Rebranded from Smartpad Pro with a revised platform.
funding_notes: >
  No external funding found. A stated 1.3M investment into expanding the software is the only
  financial figure in the public record checked.
hmlv_relevance: >
  Founder-operator origin is the notable fact: the trade's tools are built by people who sold
  blinds, not by software companies entering the trade. That is who a new entrant is selling
  against and, more usefully, who a new entrant should be talking to.
liability_notes: >
  None evidenced.
map_note: >
  `touches_proveout: none` - axis does not transfer.


## Measure Square

id: CO178
map: startup
canonical_name: Measure Square Corp.
also_known_as: [MeasureSquare, Measure Square Blinds Estimator]
country: US
tier_side: supply
tier: ""
sector: Estimating and takeoff software for flooring and window treatments
relationship: floor
job_covered: quoting
integration: software_only
sells_to: shop
liability_taken: none
touches_proveout: none
stage: ""
total_raised_usd: 0
funding_source: unknown
revenue_usd: 0
revenue_source: unknown
founded: 0
headcount: ""
capabilities_have: quoting
capabilities_partial: ""
capability_source: "measuresquare.com/tools/blinds-estimator, 2026-09-03"
source_url: https://measuresquare.com/tools/blinds-estimator/
sources_note: >
  Swept 2026-09-03. A free blinds estimator offered alongside a flooring takeoff business.
  No founding date or financials disclosed on the pages checked.
services:
  - "Free blinds estimator, metric and imperial"
  - "Flooring takeoff and estimating as the main business"
makes_or_does: >
  A free calculator that turns entered dimensions into a blind estimate, offered as a lead
  magnet beside a flooring takeoff product. Takes measurements as input; captures nothing.
hmlv_relevance: >
  Included as the floor of the category rather than as a competitor: it marks the point where
  "measurement software" in this trade means a calculator you type numbers into. Useful for
  showing how low the bar currently sits.
liability_notes: >
  None evidenced.
map_note: >
  `touches_proveout: none` - axis does not transfer.


## Hover

id: CO167
map: startup
canonical_name: Hover Inc.
also_known_as: [HOVER, hover.to]
country: US
tier_side: supply
tier: ""
sector: Phone-photo property measurement for exterior contractors and insurers
relationship: analogue
job_covered: spec_capture
integration: software_only
sells_to: shop
liability_taken: none
touches_proveout: none
stage: series_d_plus
total_raised_usd: 60000000
funding_source: press
founded: 2011
headcount: ""
capabilities_have: remote_capture, onsite_measure_app, quoting
capabilities_partial: 
capability_source: "company product pages, 2026-09-03; scored on the blinds pipeline for comparison only - this company is in a different trade"
source_url: https://hover.to/
sources_note: >
  Swept 2026-09-03 from company material and press coverage of the Series D. The raise figure
  is the disclosed Series D only - no verified lifetime total was found, so the field
  understates rather than guesses.
services:
  - "Homeowner or sales rep photographs the property on a phone"
  - "Photogrammetry returns a dimensioned 3D model"
  - "Roof, wall and sub-eave measurements, plus window and door openings"
  - "Visual estimates and proposals generated from the model"
makes_or_does: >
  A homeowner or a rep walks around a house taking phone photos; photogrammetry returns a 3D
  model carrying real dimensions, including window and door openings. Contractors quote and
  order from the model instead of driving out to measure. Independent data cited by the company
  puts the saving at 124 minutes per project on measure and takeoff.
funding_notes: >
  USD 60M Series D, November 2020, at a stated USD 490M post-money. Led by the insurance
  carriers themselves - Travelers, State Farm Ventures and Nationwide - with GV and Guidewire
  participating. Carriers funding the measurement layer is itself the finding: the party paying
  for remeasurement errors bought a stake in removing them.
hmlv_relevance: >
  The most directly transferable company on this map. Same capture technology H3 needs
  (phone photogrammetry, no special hardware), same buyer shape (the trade business that
  currently sends someone out), and it already measures window and door openings - one product
  step away from the H3 spec. It also proves the unit: the measurement itself is the thing
  sold, and the manufacturer is somebody else entirely.
liability_notes: >
  None evidenced. A measurement report with no published accuracy guarantee or rework credit
  found; graded down per schema rule.
map_note: >
  `touches_proveout: none` - that axis measures machining first-run exposure and does not
  transfer. Here for the spec_capture lane.


## EagleView

id: CO168
map: startup
canonical_name: EagleView Technologies, Inc.
also_known_as: [EagleView, Pictometry]
country: US
tier_side: supply
tier: ""
sector: Aerial property measurement reports for contractors, insurers and government
relationship: analogue
job_covered: spec_capture
integration: software_only
sells_to: shop
liability_taken: none
touches_proveout: none
stage: incumbent_subsidiary
total_raised_usd: 0
funding_source: press
founded: 2008
headcount: ""
capabilities_have: remote_capture
capabilities_partial: quoting
capability_source: "company product pages, 2026-09-03; scored on the blinds pipeline for comparison only - this company is in a different trade"
source_url: https://www.eagleview.com/
sources_note: >
  Swept 2026-09-03 from company material and acquisition coverage. `total_raised_usd: 0`
  because this is private-equity owned rather than venture funded - neither figure was
  disclosed, and zero here means not-venture-raised, not unfunded.
services:
  - "Aerial roof measurement reports, no site visit at all"
  - "Oblique and orthogonal aerial imagery library dating to 2001"
  - "Property data analytics for insurance carriers and government"
makes_or_does: >
  Sells measurement reports on a property from aerial imagery, with nobody ever going to the
  site. Founded 2008 by Chris Pershing and Dave Carlson; merged with Pictometry 2013. Holds a
  roughly sixty-petabyte imagery library and states capacity to process tens of thousands of
  roof measurement reports a day.
funding_notes: >
  Not a venture story. Acquired by Vista Equity Partners June 2015; Clearlake Capital came in
  as co-equal investor 2018. Included on the startup map as a business-model reference rather
  than as a peer.
hmlv_relevance: >
  The purest version of the model H3 would run: the measurement is the product, priced per
  unit, and the company touches no manufacturing at all. Published per-report residential
  pricing in 2026 spans roughly USD 9 to USD 87 depending on tier - which is the clearest
  outside read anyone has on what a trade will actually pay for one measurement. Set that
  against the USD 225 measured cost of a window-covering visit already on file.
liability_notes: >
  Not verified. Accuracy guarantees may exist in their contracts; none confirmed in this
  sweep, so graded down.
map_note: >
  `touches_proveout: none` - axis does not transfer. Here for the spec_capture lane.


## Volumental

id: CO169
map: startup
canonical_name: Volumental AB
also_known_as: [Volumental]
country: SE
tier_side: supply
tier: ""
sector: In-store 3D foot scanning and fit recommendation for footwear
relationship: analogue
job_covered: spec_capture
integration: equipment
sells_to: shop
liability_taken: none
touches_proveout: none
stage: series_b
total_raised_usd: 17700000
funding_source: aggregator
founded: 2012
headcount: ""
capabilities_have: onsite_measure_app
capabilities_partial: remote_capture
capability_source: "company product pages, 2026-09-03; scored on the blinds pipeline for comparison only - this company is in a different trade"
source_url: https://volumental.com/
sources_note: >
  Swept 2026-09-03 from company material; funding total is aggregator-sourced and should be
  treated as approximate.
services:
  - "3D foot scanner placed in the retail store"
  - "Fit and size recommendation from the scan"
  - "Scan data feeding customised product"
makes_or_does: >
  Places a physical 3D foot scanner in the shop and turns the scan into a fit recommendation.
  States presence in 3,000+ stores across 60+ countries. Stockholm, founded 2012.
funding_notes: >
  Roughly USD 17.7M across seven rounds per aggregators, including a USD 13M Series B in
  December 2021 led by CNI.
hmlv_relevance: >
  The counter-model to Hover, and the reason it is worth logging both: Volumental put hardware
  at the point of sale rather than an app in the customer's hand. That is the fork H3 faces -
  a phone the consumer holds, or an instrument the dealer carries. Their store count says the
  hardware route scales, but it scales through the retailer, never past them to the consumer.
liability_notes: >
  None evidenced. Fit recommendation, no published guarantee.
map_note: >
  `touches_proveout: none` - axis does not transfer. Here for the spec_capture lane.


## 3DLOOK

id: CO170
map: startup
canonical_name: 3DLOOK Inc.
also_known_as: [3DLOOK, 3dlook.ai]
country: US
tier_side: supply
tier: ""
sector: Mobile body scanning and fit for apparel brands
relationship: analogue
job_covered: spec_capture
integration: software_only
sells_to: shop
liability_taken: none
touches_proveout: none
stage: ""
total_raised_usd: 0
funding_source: unknown
founded: 2016
headcount: ""
capabilities_have: remote_capture
capabilities_partial: 
capability_source: "company product pages, 2026-09-03; scored on the blinds pipeline for comparison only - this company is in a different trade"
source_url: https://3dlook.ai/
sources_note: >
  Swept 2026-09-03 from company material. No funding figure found in this sweep; left at zero
  with `funding_source: unknown` rather than estimated.
services:
  - "3D body model from two photographs"
  - "80+ body measurements extracted per scan"
  - "Size recommendation and virtual try-on for apparel e-commerce"
makes_or_does: >
  Generates a 3D body model and states it extracts over 80 measurements from two photographs.
  Founded 2016. Sold to apparel brands and retailers, positioned against return rates.
funding_notes: >
  None disclosed in this sweep. The absence is recorded rather than filled.
hmlv_relevance: >
  The extreme end of the capture ladder: two ordinary photos, no depth sensor, no hardware,
  no trained operator. If 80 measurements off two photos is defensible, a window recess is a
  far easier target than a human body. Also note the metric they sell against - returns, which
  is the apparel word for a remake.
liability_notes: >
  None evidenced.
map_note: >
  `touches_proveout: none` - axis does not transfer. Here for the spec_capture lane.


## Dandy

id: CO171
map: startup
canonical_name: Dandy (Orthly, Inc.)
also_known_as: [Dandy, meetdandy, Orthly]
country: US
tier_side: supply
tier: ""
sector: Digital dental lab - intraoral scanning plus restoration manufacturing
relationship: analogue
job_covered: spec_capture
integration: owns_factory
sells_to: shop
liability_taken: none
touches_proveout: none
stage: series_c
total_raised_usd: 120000000
funding_source: aggregator
founded: 2016
headcount: ""
capabilities_have: onsite_measure_app, dealer_orders, deductions_cutlist, machine_file_out, production_scheduling, inventory
capabilities_partial: remote_capture
capability_source: "company product pages, 2026-09-03; scored on the blinds pipeline for comparison only - this company is in a different trade"
source_url: https://www.meetdandy.com/
sources_note: >
  Swept 2026-09-03 from company material and funding coverage. Totals differ across
  aggregators (USD 120M vs USD 250M+); the lower, better-attested figure is used.
services:
  - "Intraoral scanners placed with the practice, reportedly free"
  - "Digital impressions replacing physical putty impressions"
  - "CAD/CAM restoration manufacturing in their own labs"
makes_or_does: >
  Gives dental practices a scanner, takes the digital impression, and manufactures the
  restoration in its own lab. Founded 2016 by Daniel Hanover Katz and Toni Oloko, New York.
  The scan takes minutes and replaces the physical impression entirely.
funding_notes: >
  Around USD 120M across five rounds, most recently a USD 95M Series C in September 2025 led
  by General Catalyst, with Greenoaks, Addition, Inspired Capital and Primary Venture Partners.
hmlv_relevance: >
  The only entry in this lane that owns the manufacturing, which is exactly why it belongs
  next to the others. Dandy did not sell capture as a product - it gave the capture device away
  and monetised the order flow it unlocked, then made the part itself. That is the vertically
  integrated answer to the same question SiVIEW and Hover answered asset-light, and having all
  three on one map is what makes the map worth reading.
liability_notes: >
  None evidenced in writing. Dental labs commonly remake at their own cost, but no published
  guarantee was found in this sweep; graded down per schema rule.
map_note: >
  `touches_proveout: none` - axis does not transfer. Here for the spec_capture lane.


## SiVIEW

id: CO166
map: startup
canonical_name: SiVIEW SAS
also_known_as: [SiVIEW, SiviewExam, SiVIEW TeleOpto, SiVIEW SelfRef]
country: FR
tier_side: supply
tier: ""
sector: AI-assisted refraction software for opticians and ophthalmologists
relationship: analogue
job_covered: spec_capture
integration: software_only
sells_to: shop
liability_taken: none
touches_proveout: none
stage: series_a
total_raised_usd: 5800000
funding_source: press
founded: 2016
headcount: ""
headcount_source: ""
capabilities_have: remote_capture, onsite_measure_app
capabilities_partial: dealer_orders
capability_source: "company product pages, 2026-09-03; scored on the blinds pipeline for comparison only - this company is in a different trade"
source_url: https://siview.ai/en/
sources_note: >
  Swept 2026-09-03 from the company's own site (homepage, /en/news/, /en/the-story/) plus the
  investor's announcement at lbofrance.com. Company-authored material is positioning, not
  verified demand — founding date, founders, round size and named chains are treated as fact
  because a competitor or investor would correct them; the traction figures below are quoted
  as their claim, not asserted.
services:
  - "SiviewExam - AI-assisted refraction run by store staff"
  - "SiVIEW TeleOpto - remote examination by a practitioner elsewhere"
  - "SiVIEW SelfRef - autonomous patient-guided examination, no practitioner present"
  - "Connects to existing refraction equipment: Essilor, Nidek, Topcon and others"
makes_or_does: >
  Software that drives refraction equipment an optician already owns, and turns the eye exam
  into a guided procedure a non-specialist can run. Founded 2016 by Laure Pichereau and Jerome
  Perderiset; first algorithm took three years, first prototype Feb 2018, SiviewExam launched
  Oct 2019 after roughly six years of R&D. Their own positioning line is "a software revolution
  without changing your hardware". Three products form a ladder that removes progressively more
  of the human: staff-run, remote practitioner, then patient-guided with nobody present.
funding_notes: >
  EUR 5.5M capital increase led by LBO France's Digital Health 2 fund, December 2022, announced
  by the investor. Converted at the prevailing rate to roughly USD 5.8M; the EUR figure is the
  disclosed one. No later round found. No headcount disclosed anywhere checked.
hmlv_relevance: >
  The closest structural analogue on this map to H3, and it is not a manufacturing company.
  A prescription lens is made-to-measure: a measurement of a physical thing drives a custom
  manufactured product, the measurement has traditionally required a trained human in a room
  with the customer, and the failure mode is a remake. SiVIEW attacks exactly that step, sells
  software over equipment it does not own, and puts the remake rate on its own homepage as the
  headline metric. Their claim: over 1.1 million examinations performed, 1,000+ points of sale
  including Krys, Specsavers and Optical Center, exam in 5-10 minutes, and lens remanufacturing
  "below 1%". Those are the company's numbers, unverified here. What the entry establishes is
  that the shape works commercially and was fundable: capture the measurement, do not own the
  machine, and sell against the remake. SelfRef is the strongest single data point - a
  made-to-measure trade has already shipped a product with no practitioner in the room.
liability_notes: >
  None evidenced in writing. The sub-1% remanufacturing figure is a marketing claim on the
  homepage, not a published guarantee or a rework credit, so this is graded down to `none`
  per the schema rule. Worth re-checking against their contracts if the analogue is ever
  leaned on harder than as proof-of-shape.
map_note: >
  `touches_proveout: none` is correct rather than missing: that axis measures exposure to
  machining first-run risk and does not transfer to this company. The prove-out columns on the
  startup map were drawn for a different thesis, and SiVIEW is here as an analogue for the
  spec_capture lane, not as a machining rival.


## Smartex

id: CO172
map: startup
canonical_name: Smartex.AI
also_known_as: [Smartex, Smartex CORE, Smartex FACT]
country: PT
tier_side: supply
tier: ""
sector: In-line AI defect detection and machine control for circular-knitting textile mills
job_covered: inspection_qa
integration: equipment
sells_to: shop
liability_taken: none
touches_proveout: none
stage: series_a
total_raised_usd: 30200000
funding_source: aggregator
founded: ""
headcount: ""
headcount_source: ""
source_url: https://www.smartex.ai/blog
sources_note: >
  Swept 2026-09-03 from the company's own site (/grants-awards, /blog index, and the CORE/FACT
  announcement posts) plus TechCrunch 2022-11-03 for the round and Lightspeed's own post for
  the founder background. Company-authored material is positioning, not verified demand: the
  grant amounts, funders, product names and dated announcements are treated as fact because a
  funder or competitor would correct them; the waste and water figures are quoted as their
  claim. No customer is named anywhere on the site, no pricing, no installed-machine count —
  recorded as an absence that was checked, not one that went unmentioned.
services:
  - "CORE - AI hardware mounted on a circular knitting machine that detects fabric defects in real time and stops the machine"
  - "CORE Settings - remote change of production parameters and inspection protocols across Smartex-equipped machines"
  - "FACT - cloud and mobile platform: digital twin of every fabric roll, automatic roll grading, OEE, downtime/stop history, notifications"
  - "Automatic roll grading against a customer-defined defect point system, replacing manual final inspection"
makes_or_does: >
  Sells a sensor-and-compute unit that bolts onto knitting machines the mill already owns, watches
  the fabric as it is produced, and halts the machine when it sees a defect. Above it sits FACT,
  which grades every roll automatically and gives the mill a remote view of its own floor. Their
  own line is "the future of fabric quality control"; the FACT launch post calls it "a digital
  textile factory in your pocket". CEO Gilberto Loureiro has a masters in physics and started as
  a knitting machine operator and textile inspector in his family's clothing business (Lightspeed,
  2022). HQ Porto, Portugal; a fabric-labelling team was built in Pakistan (their own post,
  2024-11-07).
funding_notes: >
  USD 24.7M Series A announced 2022-11-03, co-led by Tony Fadell's Build Collective and Lightspeed
  Venture Partners (TechCrunch). Aggregators put lifetime funding at USD 30.2M over seven rounds
  including HAX/SOSV at the start; the Series A is the only round with a primary source read here,
  so `funding_source: aggregator` rather than `press`.
grant_notes: >
  Heavily grant-funded and it is public. Their own /grants-awards page lists EIC under Horizon 2020
  (GA 946915, EUR 1.03M incentive on EUR 1.46M, Feb 2020 - Sep 2021), DigiTVC (EUR 638k incentive),
  DefectFree (EUR 590k, to Aug 2026), TexQualis (EUR 491k, Nov 2025 - Oct 2027), Texia (EUR 570k),
  Smartexpand (EUR 297k) and Industria 4.0 (EUR 176k). They are also named participants in two
  Portuguese mobilising agendas whose totals are the CONSORTIUM's, not theirs: Produtech R3
  (EUR 167.3M investment) and TEXP@CT (EUR 45.8M). Do not read those two as money Smartex received
  - that misreading is the reason the distinction is written down here. Awards claimed: Forbes 30
  Under 30, LinkedIn Top Startups 2022, IRCAI Top 100, Innovation World Cup, WebSummit Pitch, ITMF,
  Altice International Innovation Award, Herois PME, SantanderX.
hmlv_relevance: >
  This is the founder's own architecture, already shipped and funded, in somebody else's industry -
  and the way it differs is the useful part.
  What it proves: you do not have to own the factory to own the loop. Smartex puts its own hardware
  on machines it does not own, takes control of those machines to the point of stopping them, and
  sells the layer above. That is the `supports_layer` answer to the belief's link 2, executed
  commercially rather than argued.
  What it does NOT prove, and this is the important half: circular knitting is continuous
  high-volume production, the opposite end of the belief's conditional. The integration cost was
  worth paying there precisely BECAUSE there is a production run to amortise it over - which is
  the belief's own mechanism working in Smartex's favour and against a batch-of-one version of the
  same play. Smartex also went one machine class deep, so nothing here carries to a different
  machine without being rebuilt; same `vendor_stack` shape the research map flags on the Chalmers
  ABB row.
  Third, worth noting on timing: CORE Settings is remote per-machine control built bespoke, machine
  class by machine class - exactly the work Anthropic's Model Hardware Standard proposes to
  standardise. Smartex is what that integration costs today.
  Not a competitor to H3. No window-covering exposure, no site-taken dimension, no made-to-measure
  step - they inspect a continuous web, they do not capture a spec. Filed as an analogue.
liability_notes: >
  None evidenced in writing. The "1 million kg of fabric prevented from waste" and "over 100 million
  litres of water" figures are their own blog claims with no methodology published, and no
  guarantee, rework credit or SLA appears anywhere on the site. Graded `none` per the schema rule.
map_note: >
  `integration: equipment` rather than `operates_machines`: they ship hardware onto a machine and
  can stop it, but the mill still runs its own production. The machine-stop is recorded here
  because it is the strongest single fact in the entry and the axis has no lane for it.
  `job_covered: inspection_qa` is the primary lane; the automatic roll grading also displaces a
  final-inspection labour step, which is closer to `spec_capture`'s inverse - grading an output
  rather than capturing an input - and does not belong in that lane.
  `touches_proveout: none` is correct rather than missing, for the same reason as SiVIEW: that axis
  measures machining first-run risk and does not transfer.



## CloudNC

id: CO146
map: startup
canonical_name: CloudNC Ltd
also_known_as: [CloudNC, CAM Assist]
country: GB
tier_side: supply
tier: ""
sector: AI CAM programming software
job_covered: cam_programming
integration: software_only
sells_to: shop
liability_taken: none
touches_proveout: adjacent
stage: series_b
total_raised_usd: 76000000
funding_source: press
founded: 2015
headcount: 123
headcount_source: "Revelio Labs, May 2026"
headcount_note: "Sources disagree within a narrow band: Revelio 123 (May 2026), company site ~115 across 4 continents (Apr 2026), PitchBook 114, GetLatka 136. The Revelio figure is used; treat it as +/- 15."
services:
  - "CAM Assist add-in for Autodesk Fusion"
  - "CAM Assist add-in for Mastercam"
  - "CAM Assist add-in for Siemens NX"
  - "AI milling strategy and toolpath generation from a 3D model"
  - "CAM Assist Partner Program for resellers"
makes_or_does: >
  CAM Assist — an AI add-in for Autodesk Fusion, Mastercam and Siemens NX that generates
  milling strategy and toolpaths from a 3D model. Sold as a seat to the shop's programmer;
  CloudNC does not touch the machine. Company states over 1,000 machine shops use it.
funding_notes: >
  $45M Series B (2022) led by Autodesk with Lockheed Martin and British Patient Capital,
  alongside Atomico and Episode 1. A further GBP 30M round in Feb 2026 including the NATO
  Innovation Fund and British Business Bank took total equity to GBP 60M (~$76M). An
  aggregator reports $72M over 4 rounds — consistent within rounding and FX; the GBP 60M
  self-stated figure is the one used here.
hmlv_relevance: >
  The most load-bearing competitor on this map and the reason H1A1 exists. Their own copy
  sells "80% of your CAM program in minutes" and concedes the tool "will rarely provide a
  perfect strategy first time" — the product explicitly stops at posted G-code and hands an
  unproven program to a human. That is the prove-out load H1 says is widening, admitted by
  the company generating it.
liability_notes: >
  None found. Software licence; no warranty on the part, no rework credit, no assumption of
  scrap or crash cost. The customer's machinist carries the first run.
source_url: https://www.cloudnc.com/
sources: >
  cloudnc.com (site fetch 2026-08-20, quoted in graph.md H1A1) ·
  cloudnc.com/blog/cloundnc-series-b-funding-lockheed-martin · tracxn.com/d/companies/cloudnc
first_added: 2026-08-27
status: mapped


## Toolpath

id: CO147
map: startup
canonical_name: Toolpath Technologies Inc.
also_known_as: [Toolpath, ToolPath]
country: US
tier_side: supply
tier: ""
sector: AI CAM automation and process planning software
job_covered: cam_programming
integration: software_only
sells_to: shop
liability_taken: none
touches_proveout: adjacent
stage: seed
total_raised_usd: 20000000
funding_source: press
founded: 2021
headcount: 26
headcount_source: "PitchBook, 2026"
services:
  - "Cloud CAM automation from an inbound 3D model"
  - "Automated quoting and cycle-time estimation"
  - "Process planning"
  - "Optimized G-code generation and posting"
makes_or_does: >
  Cloud CAM automation platform covering the arc from an inbound 3D model through quoting
  and process planning to optimized G-code. Atlanta, GA. Co-founded by Andy Powell
  (previously CallRail) and Justin Gray, PhD (ex-NASA optimization).
funding_notes: >
  $10M seed (Sept 2024) led by Leaders Fund with Tech Square Ventures, BLH Venture Partners
  and angels including Carl Bass (former Autodesk CEO) and John Saunders. A strategic round
  led by Kennametal with existing investor ModuleWorks (May 2025) took the total to $20M.
  No priced Series A announced — the strategic round is not labelled as one in the release.
hmlv_relevance: >
  Closest structural analogue to CloudNC and the second name the interviewed owner reached
  for. Their pitch reaches further down the chain than CloudNC's — quoting through posted
  G-code — which makes the gap they leave more informative: still nothing at the machine,
  still no liability. The interviewed owner knows their CEO personally (stated as context,
  no intro offered).
liability_notes: >
  None found. Software subscription; the shop still proves out.
source_url: https://toolpath.com/
sources: >
  toolpath.com/blog/toolpath-closes-10m-seed-round-to-transform-the-machining-business-with-applied-ai ·
  toolpath.com/blog/toolpath-closes-strategic-investment-round-led-by-kennametal ·
  leaders.vc/blog/our-investment-in-toolpath · crunchbase.com/organization/toolpath
first_added: 2026-08-27
status: mapped


## Paperless Parts

id: CO148
map: startup
canonical_name: Paperless Parts, Inc.
also_known_as: [Paperless Parts, Paperless]
country: US
tier_side: supply
tier: ""
sector: Quoting and estimating software for job shops
job_covered: quoting
integration: software_only
sells_to: shop
liability_taken: none
touches_proveout: none
stage: series_b
total_raised_usd: 45500000
funding_source: aggregator
founded: 2017
headcount: 139
headcount_source: "PitchBook / Tracxn, May 2026"
headcount_note: "Reported 130-142 across sources; 139 is the modal figure. Aggregator-stated annual revenue $27.3M (2026) is not recorded as a field: no filing backs it."
services:
  - "Quoting and estimating for CNC machining"
  - "Quoting for sheet metal and fabrication"
  - "3D-model-driven cycle-time estimation against the shop's tool library"
  - "Shop-specific rate and margin modelling"
  - "Quote delivery and customer portal"
makes_or_does: >
  Quoting and estimating platform for CNC machining, sheet metal and fabrication shops —
  takes a 3D model and produces an estimated cycle time and price against the shop's own
  tool library and rates. Boston, MA.
funding_notes: >
  $30M Series B (Sept 2021) led by OpenView Partners. Aggregator total of $45.5M over 5
  rounds (OpenView, Tinicum Venture Partners). No Series C found in public sources as of
  2026-08-27 — read the stage as "latest announced", not "current".
hmlv_relevance: >
  The first name the interviewed owner listed, and the clearest illustration of where the
  vendor landscape actually crowds: estimating. His words — "Estimating always. Thats a
  given. Lots of companies working on it." The map's value is the contrast between this
  dense lane at `quoting` and the empty one at `machine_execution` for anything sold to a shop.
liability_notes: >
  None. A quote is a number, not a commitment on the part.
source_url: https://www.paperlessparts.com/
sources: >
  businesswire.com/news/home/20210913005163 · tracxn.com/d/companies/paperless-parts ·
  clay.com/dossier/paperless-parts-funding
first_added: 2026-08-27
status: mapped


## Xometry

id: CO149
map: startup
map_kept_because: >
  Founder call 2026-08-27, asked directly when the incumbents came off: KEEP. Publicly traded since 2021, which is the same disqualifier applied to Hexagon and Autodesk, but Xometry is venture-born, still active in the scene the interviewed owner tracks, and holds the only part_guarantee position on the map that owns no machines. Do not re-propose removing it without new evidence.
canonical_name: Xometry, Inc.
also_known_as: [Xometry, XMTR]
country: US
tier_side: supply
tier: ""
sector: On-demand manufacturing marketplace (public)
job_covered: quoting
integration: software_plus_service
sells_to: oem_buyer
liability_taken: part_guarantee
touches_proveout: none
stage: public
funding_source: filing
founded: 2013
headcount: 1174
headcount_source: "company filing, 31 Dec 2025"
headcount_note: "Wikipedia lists 1,500 for 2026 and LeadIQ ~1.3K (Mar 2026); the filed 1,174 is used because it is the only figure with a reporting date behind it."
services:
  - "On-demand CNC machining marketplace"
  - "Sheet metal fabrication marketplace"
  - "Injection moulding marketplace"
  - "Additive manufacturing marketplace"
  - "AI instant pricing from an uploaded model"
  - "Supplier network sourcing and order placement"
makes_or_does: >
  AI-priced marketplace matching part buyers to a supplier network for CNC machining, sheet
  metal, injection moulding and additive. The buyer contracts with Xometry; Xometry places
  the work. NASDAQ: XMTR, Derwood MD.
funding_notes: >
  Public. Q2 2026 revenue $229.3M, up 41% YoY, of which $215M marketplace; FY2026 growth
  guided at 33-34%; FY2025 outlook raised to $678M. No revenue_usd is recorded on this entry:
  the only annual figure available would be a run-rate derived from one quarter, and a
  derived number in a filing-sourced field would read as a reported one.
hmlv_relevance: >
  Named by the interviewed owner in the estimating cluster, but structurally it is the
  demand-aggregation play, not a shop tool: it takes the buyer's order and routes it. Sits on
  this map as the ceiling case for "quoting automated at scale" and as the only entry
  carrying a real commercial guarantee to the buyer while owning no machines.
liability_notes: >
  Marketplace quality guarantee to the buyer — Xometry is the counterparty on the order, so a
  bad part is Xometry's commercial problem. Graded `part_guarantee`, not `owns_outcome`: the
  risk is passed through to the supplier shop, whose machinist still proves out.
source_url: https://www.xometry.com/
sources: >
  voxelmatters.com/xometry-reports-record-229-3-million-in-q2-2026-revenue-up-41-yoy ·
  stocktitan.net/news/XMTR · investing.com Q2 2026 slides
first_added: 2026-08-27
status: mapped


## Hadrian

id: CO150
map: startup
canonical_name: Hadrian Automation, Inc.
also_known_as: [Hadrian]
country: US
tier_side: supply
tier: ""
sector: Automated precision factories for aerospace and defense
job_covered: machine_execution
integration: owns_factory
sells_to: oem_buyer
liability_taken: owns_outcome
touches_proveout: direct
stage: series_d_plus
total_raised_usd: 2100000000
funding_source: press
founded: 2020
headcount: 407
headcount_source: "Revelio Labs, Mar 2026"
headcount_note: "Widest spread on this map: Revelio 407 (Mar 2026), PitchBook 346, Startup Intros 250, LeadIQ ~106 (May 2026). Revelio is used as the most recent full-workforce figure; the low LeadIQ number is a contact-database artefact, not a payroll count."
services:
  - "Precision CNC machining for aerospace primes"
  - "Precision CNC machining for defense and space primes"
  - "Factories-as-a-service capacity contracts"
  - "In-house automation software (not sold externally)"
makes_or_does: >
  Builds and operates highly automated machining factories ("factories as a service") making
  precision components for aerospace, defense and space primes. Los Angeles, CA. Sells parts,
  not software — the automation is internal.
funding_notes: >
  $260M Series C (July 2025) led by Founders Fund and Lux Capital with Morgan Stanley;
  $1.37B Series D (Aug 2026) at an $8B valuation. Aggregator total ~$2.1B over 10 rounds from
  32 investors; that total roughly coincides with the Series D announcement, so treat it as a
  floor rather than a settled figure.
hmlv_relevance: >
  The greenfield case in full. Named by the interviewed owner as "getting there", and
  separately in his notes as pairing every machinist with a software engineer — the honest
  read of what automating prove-out costs today: a second salaried person. Hadrian owns the
  outcome because it owns the factory. H1's bet is that the same liability can be carried
  WITHOUT owning the factory, inside brownfield shops.
liability_notes: >
  Owns the outcome by construction — its own machines, its own scrap, its own delivery
  commitment to the prime. Not a liability product sold to anyone; a consequence of vertical
  integration.
source_url: https://www.hadrian.co/
sources: >
  techcrunch.com/2026/08/06/defense-tech-hadrian-raises-1-37b-at-8b-valuation ·
  prnewswire.com Series D release · labusinessjournal.com Series C ·
  tracxn.com/d/companies/hadrian · interview 2026-08-25
first_added: 2026-08-27
status: mapped


## SendCutSend

id: CO151
map: startup
canonical_name: SendCutSend, LLC
also_known_as: [SendCutSend, SCS]
country: US
tier_side: supply
tier: ""
sector: Web-first on-demand sheet metal and cutting
job_covered: machine_execution
integration: owns_factory
sells_to: oem_buyer
liability_taken: part_guarantee
touches_proveout: direct
stage: series_a
total_raised_usd: 124000000
funding_source: press
founded: 2018
headcount: 500
headcount_source: "Nevada Business Magazine, Jun 2026 (stated as 'more than 500')"
headcount_note: "A floor, not a count — the June 2026 report says 'more than 500' during a fourth Reno facility opening. ZoomInfo still bands it 201-500."
services:
  - "Online laser cutting"
  - "Waterjet cutting"
  - "Sheet and plate cutting"
  - "Bending"
  - "Tapping and hardware insertion"
  - "CNC machining"
  - "Finishing and powder coat"
  - "Instant online quoting and instant buy"
makes_or_does: >
  Instant-quote, instant-buy online manufacturing — laser and waterjet cutting, bending,
  tapping, CNC machining and finishing from uploaded files, produced in its own plants.
  Reno, NV. Has announced a $1B commitment to US manufacturing capacity.
funding_notes: >
  $110M first institutional round (May 2026) co-led by Sequoia and Paradigm with Patrick and
  John Collison, at a valuation above $1B. Aggregator total $124M including Horizon Venture
  Capital. Bootstrapped until that round, which is why the stage label understates the company.
hmlv_relevance: >
  Named by the interviewed owner as "getting there", and he has personally run parts through
  them ("I did an experiment with them. Great experience"). The founder's live objection in
  that same thread — "sendcutsend seems like not so precise parts" — is the boundary worth
  holding: this is 2.5D cutting scaled by removing the human from the quote, not multi-axis
  first-run machining. It marks where automation succeeds because the geometry is simple.
liability_notes: >
  Guarantees the delivered part to the buyer within published tolerances. Made possible by a
  tightly constrained process envelope, not by solving prove-out.
source_url: https://sendcutsend.com/
sources: >
  crunchbase.com/organization/sendcutsend · pitchbook.com/profiles/company/462661-12 ·
  sendcutsend.com/blog/sendcutsend-is-building-americas-anything-factory ·
  thefabricator.com web-first manufacturing · interview 2026-08-25
first_added: 2026-08-27
status: mapped


## OSH Cut

id: CO152
map: startup
canonical_name: OSH Cut LLC
also_known_as: [OSH Cut, OshCut]
country: US
tier_side: supply
tier: ""
sector: On-demand laser cutting and sheet metal
job_covered: machine_execution
integration: owns_factory
sells_to: oem_buyer
liability_taken: part_guarantee
touches_proveout: direct
stage: seed
total_raised_usd: 3000000
funding_source: aggregator
founded: 2018
headcount: 22
headcount_source: "aggregator, Oct 2025"
headcount_note: "Reported 22-29 across sources, with LinkedIn banding 11-50. The smallest team on the owns-factory row by an order of magnitude."
services:
  - "Online laser cutting"
  - "Precision sheet metal and plate"
  - "Bending"
  - "Tapping"
  - "Deburring and edge rolling"
  - "Powder coating"
  - "Instant online quoting"
makes_or_does: >
  Precision sheet metal and plate on demand — laser cutting, bending, tapping, deburring,
  edge rolling, powder coat — quoted and bought online. Orem / Spanish Fork, UT. A second
  70,000 sq ft plant near Cincinnati is coming online on a $10M equipment investment.
funding_notes: >
  $3M raised per aggregator; no priced round announced publicly. The Cincinnati plant is a
  $10M capex commitment, not a raise — the two must not be added.
hmlv_relevance: >
  The direct SendCutSend comparator, and the interviewed owner trialled both. Useful here as
  the low-capital point on the `owns_factory` lane: $3M raised against SendCutSend's $124M
  and Hadrian's $2.1B at the same integration depth. Capital is not what separates these
  three; the tolerance envelope is.
liability_notes: >
  Delivered-part guarantee within a published process envelope, same shape as SendCutSend.
source_url: https://www.oshcut.com/
sources: >
  crunchbase.com/organization/osh-cut · pitchbook.com/profiles/company/499403-53 ·
  thefabricator.com/thefabricator/news/shopmanagement/osh-cut-to-open-second-us-factory ·
  interview 2026-08-25
first_added: 2026-08-27
status: mapped


## Isembard

id: CO153
map: startup
canonical_name: Isembard Ltd
also_known_as: [Isembard, MasonOS]
country: GB
tier_side: supply
tier: ""
sector: Software-run distributed precision manufacturing
job_covered: scheduling_ops
integration: owns_factory
sells_to: oem_buyer
liability_taken: owns_outcome
touches_proveout: direct
stage: series_a
total_raised_usd: 59000000
funding_source: press
founded: 2024
headcount: 14
headcount_source: "PitchBook, 2026"
headcount_note: "CONFLICTED: PitchBook 14 against Crunchbase's 51-100 band. A 2024-founded company that raised $50M in Mar 2026 and plans 25 factories by year end could plausibly be at either. Do not cite this figure without re-checking Companies House filing 15989684."
services:
  - "Precision CNC machining for aerospace"
  - "Precision CNC machining for defense and energy"
  - "Distributed small-factory network capacity"
  - "MasonOS factory platform: quoting, scheduling, production, quality (internal)"
makes_or_does: >
  Operates its own network of precision CNC factories for aerospace, defense and energy, run
  on MasonOS — its proprietary platform covering quoting, scheduling, production and quality.
  London, UK. Plans 25 factories by end of 2026 plus launches in Germany, France and Ukraine.
funding_notes: >
  ~$9M (GBP 6.7M) seed, then a $50M / GBP 37M / EUR 43-46.3M Series A (March 2026) led by
  Union Square Ventures, under twelve months later. Total $59M across 2 rounds. The euro,
  sterling and dollar figures in the press are the same round at different FX — do not sum them.
hmlv_relevance: >
  The founder's own named contrast case, verbatim in the 2026-08-25 thread: "not like
  isembard, not new tech from the ground up." This is what H1 is positioned AGAINST —
  Isembard gets a software-run factory by building the factory. If the brownfield thesis is
  right, `software_only` x `owns_outcome` should stay empty on this map for a long time, and
  Isembard is the reason that space keeps getting approached from the wrong direction.
liability_notes: >
  Owns the outcome — its own factories, its own quality sign-off to the customer.
source_url: https://www.isembard.com/
sources: >
  uktech.news/deep-tech/isembard-manufacturing-series-a-20260309 · eu-startups.com EUR 43M ·
  vestbee.com/insights/articles/isembard-raises-50-m ·
  isembard.com/blogs-and-articles/reshoring-the-future-of-manufacturing · interview 2026-08-25
first_added: 2026-08-27
status: mapped


## Anduril Industries

id: CO154
map: startup
map_kept_because: >
  Founder call 2026-08-27, asked directly when the incumbents came off: KEEP. Anduril is 8,372 people and $61B, so it fails a size test, but it is venture-track rather than a legacy incumbent, the interviewed owner named it first in his 'getting there' list, and it is the extreme greenfield anchor the brownfield framing is positioned against. Do not re-propose removing it without new evidence.
canonical_name: Anduril Industries, Inc.
also_known_as: [Anduril, Arsenal-1]
country: US
tier_side: supply
tier: ""
sector: Defense products manufacturer with hyperscale in-house production
job_covered: machine_execution
integration: owns_factory
sells_to: ""
liability_taken: owns_outcome
touches_proveout: direct
stage: series_d_plus
total_raised_usd: 6820000000
funding_source: press
founded: 2017
headcount: 8372
headcount_source: "Revelio Labs, Mar 2026"
headcount_note: "Reported 7,000 (PitchBook, Wikipedia) to 8,372 (Revelio, Mar 2026). Company-wide, not Arsenal-1: that plant started at ~250 people and is projected at 4,000 within the decade."
services:
  - "Autonomous defense systems"
  - "YFQ-44A 'Fury' collaborative combat aircraft"
  - "Lattice autonomy software"
  - "Arsenal-1 hyperscale in-house production (not sold as a service)"
makes_or_does: >
  Autonomous defense systems, produced in its own hyperscale plant. Arsenal-1 in Ohio is a
  5M+ sq ft, ~$1B facility; serial production of the YFQ-44A "Fury" collaborative combat
  aircraft began there ahead of schedule. 2025 revenue $2.2B, ~$4.3B projected for 2026.
funding_notes: >
  $1.5B Series F earmarked for Arsenal-1; $5B Series H (May 2026) at a $61B post-money
  valuation; $6.82B total across eight rounds.
hmlv_relevance: >
  Named first by the interviewed owner in the "getting there" list. Deliberately mapped with
  `sells_to` LEFT BLANK rather than forced: Anduril sells finished defense systems to
  governments, which is not a value in this idea's `sells_to` vocabulary. It therefore sits
  in the unmapped lane on that axis, which is the correct reading — a reference point for
  what vertically integrated automated production looks like, not a vendor competing for the
  same buyer. Do not invent a position for it.
liability_notes: >
  Owns the outcome as a manufacturer of its own products. Not comparable to a vendor
  liability offer; included because the brownfield-vs-greenfield framing needs the extreme
  greenfield anchor visible.
source_url: https://www.anduril.com/
sources: >
  tectonicdefense.com/anduril-raises-5b-series-h-at-61b-valuation · govconwire.com Series F ·
  tectonicdefense.com/inside-arsenal-1 · interview 2026-08-25
first_added: 2026-08-27
status: mapped


## Harmoni

id: CO155
map: startup
canonical_name: Harmoni Solutions, Inc.
also_known_as: [Harmoni]
country: US
tier_side: supply
tier: ""
sector: Factory orchestration — machine data capture and shop-floor telemetry
job_covered: scheduling_ops
integration: equipment
sells_to: shop
liability_taken: none
touches_proveout: adjacent
stage: ""
funding_source: unknown
founded: 2020
headcount: 17
headcount_source: "PitchBook, 2026"
headcount_note: "Reported 17 (PitchBook) to 20 (RocketReach), LinkedIn band 11-50. The smallest team on this map and the one closest to the founder's own angle."
services:
  - "Long-range RFID edge device for operator and job detection"
  - "Real-time machine monitoring and OEE"
  - "Machine cycle-time and downtime data collection"
  - "Labour tracking into ERP"
  - "Shop-floor reporting and utilisation analytics"
  - "CNC and ERP system integration"
makes_or_does: >
  Factory orchestration layer for existing shops: a long-range RFID edge device that
  auto-detects operator and job, paired with machine cycle data and pushed into the shop's
  ERP. Connects Mazak, Haas, Fanuc, Heidenhain, Siemens, DMG MORI, Makino and Fadal without
  replacing machines; integrates Epicor, Infor Visual, JobBoss/JobBoss2, ABAS, ODOO.
  Akron OH and New York.
funding_notes: >
  NO PUBLIC FUNDING FIGURE FOUND as of 2026-08-27. A PitchBook profile exists but the round
  history is not public. Left blank deliberately — missing data, not zero.
hmlv_relevance: >
  The nearest competitor to the founder's own stated angle, and the only entry on this map
  doing brownfield retrofit rather than greenfield. The interviewed owner asked the founder
  directly: "Arre you trying to data gather like Harmoni" — this is the frame a target buyer
  reaches for unprompted, so the positioning has to survive it. The seam: Harmoni captures
  cycle time, uptime and utilisation, and the same owner names offsets entered at the machine
  as the expensive uncaptured thing with "nothing tried" against it. Harmoni records that the
  machine ran, not what the machinist changed.
liability_notes: >
  None. Monitoring and reporting; the shop keeps every consequence.
source_url: https://harmoni.io/
sources: >
  harmoni.io · prnewswire.com Harmoni CES 2026 · pitchbook.com/profiles/company/543919-33 ·
  linkedin.com/company/harmoni-solutions · interview 2026-08-25
first_added: 2026-08-27
status: mapped


## Normark

id: CO156
map: startup
canonical_name: "(unresolved — see identity_conflict)"
also_known_as: [Normark]
country: ""
tier_side: supply
tier: ""
sector: "(unresolved)"
job_covered: ""
integration: ""
sells_to: ""
liability_taken: ""
touches_proveout: ""
stage: ""
funding_source: unknown
makes_or_does: >
  UNRESOLVED. Named by the interviewed shop owner on 2026-08-25 inside a list of estimating
  vendors — "Paperless, cloudNC, toolpath, normark, xometry, etc. Taking 3d models and
  spitting out estimated time base on tool library" — so his usage implies a quoting or CAM
  software vendor.
identity_conflict: >
  The only "Normark" the 2026-08-27 public search surfaced in this space is Normark
  Manufacturing (normarkmfg.com), a job shop started in 2011 after its founder took on
  machining work — demand side, not a software vendor. Either the owner misremembered a name,
  or the vendor is too small or too new to be indexed, or the spelling differs. Every axis is
  LEFT BLANK so this lands in the unmapped lane rather than being guessed onto the map.
  Resolve by asking him directly at the next contact, then fill the axes or retire this id.
hmlv_relevance: >
  Low until resolved. Retained because a named vendor the founder cannot identify is itself a
  finding about how legible this market is, and because dropping the name would lose the
  question.
source_url: ""
sources: >
  interview 2026-08-25 (verbatim list) · normarkmfg.com/about (conflicting entity)
first_added: 2026-08-27
status: unresolved


## VulcanForms

id: CO161
map: startup
canonical_name: VulcanForms Inc.
also_known_as: [VulcanForms, Vulcan Forms, Arwood Machine, V2]
country: US
tier_side: supply
tier: ""
sector: Integrated digital metal manufacturing — additive plus precision machining
job_covered: machine_execution
integration: owns_factory
sells_to: oem_buyer
liability_taken: owns_outcome
touches_proveout: direct
stage: series_d_plus
total_raised_usd: 825000000
funding_source: press
founded: 2015
headcount: 358
headcount_source: "Revelio Labs, Mar 2026"
headcount_note: "358 as of March 2026, up 79 (+6.2%) year on year. One of the better-evidenced figures on this map — a single dated source with a stated delta rather than a spread across aggregators."
services:
  - "Proprietary laser powder bed fusion (LPBF) additive at production scale"
  - "High-precision CNC machining to tight tolerances"
  - "Integrated additive-plus-subtractive part production"
  - "Build preparation and slicing software"
  - "In-process monitoring and closed-loop process control"
  - "AI quality control"
  - "Prototyping, pilot runs and high-volume production"
makes_or_does: >
  Metal end-use parts made on its own machines, combining proprietary LPBF additive with
  in-house precision machining and AI software for build prep, in-process sensing and
  closed-loop control. Two Massachusetts plants: Newburyport (95 Parker Street) and Devens
  (112 Barnum Road). Titanium, Inconel, stainless, nickel superalloys — 12 alloys listed.
  Serves aerospace, defense, transportation, energy, equipment, consumer, medical and
  compute. ITAR registered; AS9100D, ISO 13485, ISO 9001.
funding_notes: >
  $220M Series D (Jan 2026) led by Eclipse and 1789 Capital with Washington Harbour,
  Fontinalis and IEQ Capital, at a stated $1B valuation. Aggregator total $825M across 3
  rounds — that round count is implausibly low against a $355M raise reported in 2022, so
  the $825M total is trustworthy but the round history is not; do not cite "3 rounds".
hmlv_relevance: >
  The most thesis-relevant entry added so far, and it cuts BOTH ways. VulcanForms is the one
  company on this map that went brownfield: it acquired Arwood Machine in Jan 2022, a
  60-year-old Newburyport machine shop, and runs it as "V2" alongside its additive plants.
  That is the founder's own stated route — start where the legacy machines are — executed by
  a company that then took the liability. But it took the liability by BUYING the shop, not
  by selling the shop anything. So it belongs with Hadrian and Isembard on the owns-factory
  row, and it sharpens rather than softens the question H1 has to answer: every route to
  carrying first-run risk on this map still runs through owning the floor.
  Second point worth tracking: their software stack is described as closed-loop — in-process
  sensing feeding control — which is the capability H1 would need, built internally and not
  sold. Watch for any sign they unbundle it.
liability_notes: >
  Owns the outcome. Delivers qualified end-use parts under AS9100D / ISO 13485 / ITAR from
  its own plants, so scrap, rework and conformance are its own cost.
source_url: https://www.vulcanforms.com/
sources: >
  vulcanforms.com (site fetch 2026-08-27) ·
  prnewswire.com VulcanForms $220M Series D (Jan 2026) ·
  3dprint.com/323605 · bloomberg.com 2026-01-30 · pitchbook.com/profiles/company/268366-51 ·
  reveliolabs.com/companies/vulcanforms/employees · metal-am.com $355M / 150-laser facility
first_added: 2026-08-27
status: mapped


## Bright Machines

id: CO162
map: startup
canonical_name: Bright Machines, Inc.
also_known_as: [Bright Machines, AutoLab AI, Brightware, Bright Robotic Cell, BRC]
country: US
tier_side: supply
tier: ""
sector: Software-defined assembly automation — robotic cells plus control software
job_covered: assembly
integration: equipment
sells_to: shop
liability_taken: none
touches_proveout: none
stage: series_c
total_raised_usd: 400000000
funding_source: self_stated
founded: 2018
headcount: 266
headcount_source: "company statement, Jul 2026 ('approximately 266 across 5 continents')"
services:
  - "Bright Machines Microfactory (integrated cells plus software)"
  - "Bright Robotic Cells (BRC) — modular, pre-integrated production-ready units"
  - "Brightware control and configuration software"
  - "Robotic assembly automation"
  - "Automated inspection stages"
  - "Computer vision and ML-driven adaptive robotics"
  - "Robotics-as-a-service commercial model"
makes_or_does: >
  Modular robotic assembly cells sold with the software that configures them. A Microfactory
  is Brightware software plus Bright Robotic Cells plus accessories, automating the assembly
  and inspection stages of production; the pitch is that a line can be configured, replicated
  and scaled in software rather than re-engineered, and deployed roughly twice as fast as a
  conventional assembly line. Available as-a-service as well as sold. Targets high-mix
  electronics and, increasingly, hyperscale AI-infrastructure assembly. Spun out of Flex as
  AutoLab AI; founded by Flex and Autodesk executives.
funding_notes: >
  CONFLICTED TOTAL. $126M Series C closed 25 Jun 2024 — $106M equity led by BlackRock with
  NVIDIA, Microsoft, Eclipse, Jabil and Shinhan Securities, plus $20M venture debt from
  J.P. Morgan — at which point the company stated total raised as "more than $400M". Tracxn
  reports $608.45M over 12 rounds. The conservative company-stated $400M floor is recorded;
  do not cite it as a precise total. Valuation $938M (Oct 2022); no post-Series-C valuation
  is public. Came out of stealth in 2018 on $179M. Note the strategic investor list: NVIDIA,
  Microsoft and Jabil are customers-adjacent, not financial investors.
hmlv_relevance: >
  On the map as an ANALOGUE, not a rival — and the distinction is the point.
  Bright Machines does not touch CNC prove-out; `touches_proveout` is graded `none` and
  `job_covered` needed a new `assembly` lane, because this axis was drawn from a machining
  thesis and had nowhere to put them. Filing them under machine_execution would have made
  them read as a Hadrian competitor, which they are not.
  What makes them worth tracking is structural: their whole pitch is getting a NEW product
  running on a reconfigurable cell WITHOUT the specialist who normally programs it by hand.
  That is the same shape as the prove-out problem, one domain over. Somebody raised $400M+
  attacking reconfiguration-without-the-expert in assembly, with NVIDIA, Microsoft and Jabil
  on the cap table — which is evidence the problem class is fundable, and a warning that the
  machining version is not unclaimed territory for long.
  Second read worth holding: assembly is the easier half. Cells are repeatable, geometry is
  known, and a misplaced screw is not a crashed spindle on a titanium billet. If Bright
  Machines has needed eight years and $400M for the tractable version, that is a data point
  about how hard the machining version is, and it cuts against H1's timeline, not for it.
liability_notes: >
  None found at the part level. The robotics-as-a-service model shifts CAPEX risk off the
  customer's balance sheet, which is a real commercial risk transfer, but no public evidence
  says Bright Machines carries the cost of a bad unit coming off the cell. Graded `none`
  rather than `warranty` on that basis — upgrade it only if a service-level commitment on
  output is found in writing.
source_url: https://www.brightmachines.com/
sources: >
  brightmachines.com/news/bright-machines-raises-126m-series-c-funding (site fetch blocked
  403 on 2026-08-27; read via press mirrors) · prnewswire.com Series C 302181151 ·
  crunchbase.com/funding_round/bright-machines-series-c · tracxn.com/d/companies/bright-machines ·
  therobotreport.com/bright-machines-plans-microfactory-innovations-126m-funding ·
  automate.org/products/bright-machines/bright-machines-microfactory ·
  businesswire.com 20190626005163 (first Microfactory) · semafor.com 2024-09-26 (new CEO) ·
  techcrunch.com 2018-10-23 ($179M out of stealth) · caplight.com (Oct 2022 valuation)
first_added: 2026-08-27
status: mapped


## Atomic Industries

id: CO163
map: startup
canonical_name: Atomic Industries, Inc.
also_known_as: [Atomic Industries, Atomic]
country: US
tier_side: supply
tier: ""
sector: AI-native tool and die — mould design, mould making and injection moulding production
job_covered: tooling
integration: owns_factory
sells_to: oem_buyer
liability_taken: part_guarantee
touches_proveout: direct
stage: series_a
total_raised_usd: 45200000
funding_source: aggregator
founded: 2021
headcount: 60
headcount_source: "Y Combinator company profile (team size 60); YC profile still lists Cleveland OH while the company's own site and job postings are Detroit / Shelby Township / Warren MI, so treat the profile as lagging"
services:
  - "AI-driven mould design and tool and die making"
  - "Multi-physics simulation (molten plastic flow, thermal, structural) ahead of cutting metal"
  - "Design-for-manufacturability analysis with human review"
  - "Injection moulding production on 1000T / 1400T / 2000T presses"
  - "Metal 3D printed conformal cooling channels (Velo3D Sapphire)"
  - "Real-time adaptive process control and intelligent moulding trials"
  - "Quoting through final quality check on one software backbone"
makes_or_does: >
  A vertically integrated plastics supplier that treats the mould as the product its AI makes.
  Their own framing: "Our superpower is mold making, and our entire operation is AI-native",
  with the goal of moving customers "from design to production faster than anyone on earth".
  The software models molten plastic flow, thermal behaviour and structural response "before
  metal is cut", feeds that into tooling and cooling design, and takes production outcomes back
  into the models. They then run the parts themselves in Detroit on heavy-tonnage presses —
  1000T, 1400T and 2000T, aimed at large-format automotive body panels and defence components —
  with Velo3D Sapphire printers producing conformal cooling channels in the moulds. Stated
  markets are automotive, consumer, industrial, aerospace and defence; stated customer types are
  OEMs and Tier 1 suppliers. Founded 2021 by Aaron Slodov (CEO), YC W21; he also co-founded the
  Reindustrialize Summit. Team described as computational physicists, veteran toolmakers, and
  engineers out of SpaceX, Google and Detroit's manufacturing floor.
funding_notes: >
  Two disclosed rounds. $17M seed announced 4 Dec 2023, led by Narya Capital, co-led by 8090
  Industries and Acequia Capital New Industrials, with Porsche Ventures, Yamaha Motor Ventures,
  Toyota Ventures and Impatient Ventures. $25M Series A announced 23 Sep 2025, led by MaC
  Venture Capital and DTX Ventures, with the University of Michigan, S&A, Calm Ventures,
  Blackwing and Narya. Total of $45.2M across 3 rounds is aggregator-derived (Crunchbase), not
  company-stated — the third round is not separately identified, so treat the total as
  approximate and the two named rounds as the hard floor. Note the strategic investor list:
  Porsche, Yamaha and Toyota are all vehicle OEMs, which is the buyer they sell to.
hmlv_relevance: >
  The most direct challenge on this map to the belief's second clause, and it should be read as
  such rather than filed as a neighbour.
  A mould tryout IS a prove-out: a never-made tool, a first shot, and a named toolmaker who eats
  it when the part comes out wrong. Atomic's entire pitch is compressing that with simulation
  ahead of cutting metal, which is why `touches_proveout` is graded `direct` and why the map
  needed a `tooling` lane rather than filing them under machine_execution.
  What they have NOT done is sell prove-out risk to somebody else's shop. They took the
  liability by becoming the manufacturer — owning the factory, quoting the part, and putting
  tooling cost at $0 to the customer. That is the vertical-integration answer to the liability
  problem, and it is the expensive one: $45M and five years to carry risk for parts they make
  on their own presses. H1's wedge is the other answer — carrying the risk for a shop that keeps
  its own machines. Atomic is evidence the problem is fundable and that OEM buyers will pay for
  someone else to hold first-run risk; it is not evidence that anyone has solved it for the
  installed base of HMLV shops, which is the population H1 is about.
  Two further reads worth holding. First, plastics, not chips: their process is injection
  moulding, so nothing here transfers directly to a CNC prove-out, and their absence from the
  machining lane is a fact about scope rather than a gap they left open. Second, and sharper —
  their own site says DFM output is delivered "with human review where required". The
  best-funded AI-native toolmaker in the country still has a human signing off. That is a
  self-published, dated data point ON the H1 mechanism, and it cuts both ways: it confirms the
  human-in-the-loop constraint is real, and it shows a company can build a fundable business
  without removing it.
  What is NOT on their public record, checked 2026-08-27: no named customers (markets and
  customer types only), no pricing, no part or programme counts, no lead time in weeks beyond
  the relative "40-60% faster" claim, and no press-utilisation or deployment numbers. Several
  homepage statistics render as animated counters that did not resolve, so clamping force, max
  shot size, machine count and material-grade count are recorded nowhere here rather than
  guessed, and the /news and /research pages returned no text on either fetch path — re-read
  them on the next refresh.
liability_notes: >
  Graded `part_guarantee`, deliberately one notch below `owns_outcome`, on the same conservative
  basis used for Bright Machines (CO162). What is publicly stated is commercial, not
  contractual: their own comparison table puts tooling at "$0 Tooling Cost" against an industry
  "$50K+", which moves tooling CAPEX off the customer's balance sheet, and as a parts supplier
  selling into OEM and Tier 1 programmes they carry ordinary conforming-part liability. No
  public document commits them to a first-shot or tryout outcome, and none names a remedy.
  Upgrade to `owns_outcome` only if a written commitment on tryout or first-article outcomes is
  found — a supply agreement, a published SLA, or a direct statement from the company.
source_url: https://atomic.industries/
sources: >
  atomic.industries homepage, browser read 2026-08-27 (WebFetch returned the company name only —
  JS-rendered; /news and /research returned no text on either path) ·
  capabilities.atomic.industries (equipment specs, not fetched) ·
  ycombinator.com/companies/atomic-industries (W21, founded 2021, team 60, founder Aaron Slodov) ·
  techcrunch.com 2023-12-04 ($17M seed, Narya lead) ·
  pulse2.com/atomic-industries-25-million-secured-to-advance-ai-based-manufacturing ($25M Series A,
  2025-09-23) · startuphub.ai Series A writeup · crunchbase.com/organization/atomic-industries
  ($45.2M / 3 rounds, aggregator) · detroitchamber.com/bios/aaron-slodov ·
  plasticsnews.com "Atomic adds AI to the mold making process"
first_added: 2026-08-27
status: mapped


## Senra Systems

id: CO164
map: startup
canonical_name: Senra Systems, Inc.
also_known_as: [Senra Systems, Senra]
country: US
tier_side: supply
tier: ""
sector: Automated aerospace and defense wire harness manufacturing
job_covered: assembly
integration: owns_factory
sells_to: oem_buyer
liability_taken: owns_outcome
touches_proveout: direct
stage: series_a
total_raised_usd: 25000000
funding_source: press
founded: 2023
headcount: 99
headcount_source: "PitchBook / CB Insights, 2026"
headcount_note: "99 for a company founded in 2023 on $25M — the fastest headcount build per dollar on this map. Worth re-checking: a single aggregator figure with no stated date, unlike the dated Revelio numbers elsewhere here."
services:
  # Manufacturing, design and operations lines below are the published catalogue at
  # senrasystems.us/services (fetched 2026-08-28), not a paraphrase of the about page.
  - "Aerospace and defense wire harness manufacture (own framing: we design & build wire harnesses)"
  - "Complex cable assemblies"
  - "Formboard assemblies"
  - "Hi-pot testing"
  - "36-2 AWG wiring"
  - "Heat-shrink tubing, overwraps, epoxy potting"
  - "Automated label printing"
  - "Automated work instructions"
  - "Smart machine utilization"
  - "Design: digital-twin conversion"
  - "Design: sketches converted to formal designs"
  - "Design: design-for-manufacturability (DFM) support"
  - "Design: 3D/2D formboard creation"
  - "Design: creation and first-article testing of hi-pot code"
  - "Design: supply-chain advice for piece parts"
  - "Operations: inventory management"
  - "Operations: configuration management"
  - "Operations: real-time project status"
  - "Operations: web-based work instructions"
  - "Operations: component traceability (COC)"
  - "Operations: internal IPC/NASA trainers"
  - "Proprietary harness design software"
  - "Assembly-as-a-service (design, procurement and production as one service)"
makes_or_does: >
  Builds aerospace and defense wire harnesses in its own 15,000 sq ft plant in Redondo Beach,
  CA, on an integrated stack of machinery, software control and in-house engineering. Sells
  proprietary design software alongside an assembly-as-a-service model covering design,
  procurement and production. States it compresses harness lead times from months to weeks
  at aerospace quality. Founded 2023 by former SpaceX engineers Jordan Black and Benjamin
  Shanahan; team includes numerous ex-SpaceX engineers.
  A second facility of 80,000 sq ft in Cypress, CA is stated as coming online in 2026 — 6.3x
  the current footprint inside three years of founding, and the loudest published signal on
  this map that a liability-taking model is being scaled rather than piloted.
  Certified or registered to AS9100, IPC/WHMA-A-620, NASA-STD-8739.4 and DDTC ITAR, with
  IPC/NASA trainers held in-house rather than bought in.
funding_notes: >
  $25M Series A co-led by Dylan Field (Figma CEO) and CIV, with General Catalyst, Sequoia,
  Founders Fund, Andreessen Horowitz, 8VC and Pax. An unusually dense investor list for a
  Series A of this size — read it as signal about the thesis rather than about the round.
  No seed is separately reported; $25M is the total on record, so treat it as "raised to
  date per press", not as a confirmed lifetime total.
  Non-dilutive on top of that: SBIR Phase 1 awarded and Phase 2 selected (self-stated on the
  services page). No dollar values published, so `total_raised_usd` excludes them.
hmlv_relevance: >
  The closest thing on this map to H1's own shape executed in a neighbouring material.
  Wire harnesses are genuinely HMLV — every airframe variant needs a different one, volumes
  are low, and the work has historically been manual, skilled and slow. Senra automated it,
  took the liability by owning the plant, and sells the OUTCOME (a delivered harness) rather
  than a tool. That is the fourth independent instance on this map of the same pattern: the
  route to carrying first-run risk runs through owning the floor.
  Two specifics worth acting on. First, they supply Anduril, which is CO154 on this same map
  — a supplier relationship between two mapped entries, and the only one recorded so far.
  Second, ex-SpaceX founders building HMLV automation in Redondo Beach are the single most
  interviewable population on this map for H1A2: they have lived the prove-out problem inside
  SpaceX and then chosen to solve the assembly version of it commercially. They are not
  buyers, so this is expert evidence, not demand evidence — grade any interview accordingly.
  Counter-reading to hold: harnesses have no spindle to crash. The failure mode is a
  mis-terminated pin found at test, not a scrapped titanium billet, so their liability is
  cheaper to carry than the machining equivalent. Do not read their success as proof the
  machining version prices the same way.
  Third specific, from the published service catalogue: Senra sells its own execution layer.
  Automated and web-based work instructions, configuration management, real-time project
  status and component traceability are listed as CUSTOMER-FACING operations services, not
  described as internal tooling. A company that took the liability built that layer itself
  rather than buying one — the strongest instance on this map of the belief's own premise.
  It cuts both ways, and the cut against is the sharper one: it is equally evidence that the
  layer may not be sellable apart from the factory that runs it, since the one team that
  built it kept it inside and sells the harness.
liability_notes: >
  Owns the outcome. Delivers finished aerospace-grade harnesses from its own plant under an
  assembly-as-a-service contract, so rework, scrap and schedule are its own cost. The
  as-a-service framing here is stronger than Bright Machines' equivalent: Senra is selling
  the finished part, not the means of making it.
proveout_notes: >
  Graded `direct` where Bright Machines is graded `none`, and the difference is deliberate.
  Senra runs production itself, so a never-built harness variant means a genuine first
  article inside its own four walls — the Hadrian and VulcanForms shape. Bright Machines
  sells cells and does not run the line, so its customers, not it, meet the first run.
  As of the services-page read the grade is published rather than inferred: "Creation +
  First-Article Testing of Hi-Pot Code" is a listed design service. They sell the first
  article of a never-built harness as a line item — the only entry on this map that puts
  prove-out on its own price list.
  The asymmetry that stops this being a precedent for H1: hi-pot is a non-destructive
  electrical test, cheap to run and cheap to fail, so the first article can be tested before
  it is trusted. Machining prove-out has no such test — the first run IS the test, and
  failing it consumes the billet. Senra found a way to test prove-out; H1 is about a job
  where nobody can.
source_url: https://www.senrasystems.us/
sources: >
  senrasystems.us/about (site fetch 2026-08-27) · senrasystems.us/media/announcing-our-series-a ·
  aviationweek.com Senra Systems raises $25M for A&D wire harnesses ·
  omm.com O'Melveny advises Senra on $25M Series A · app.dealroom.co Senra $25M ·
  pitchbook.com/profiles/company/521616-07 · cbinsights.com/company/senra-systems ·
  senrasystems.us/services (site fetch 2026-08-28)
first_added: 2026-08-27
status: mapped


## Tensr

id: CO165
map: startup
canonical_name: Tensr, Inc.
also_known_as: [Tensr, Tensør]
country: US
tier_side: supply
tier: ""
sector: Autonomous robotic contract manufacturing
job_covered: machine_execution
integration: owns_factory
sells_to: oem_buyer
liability_taken: owns_outcome
touches_proveout: direct
stage: pre_seed
total_raised_usd: 500000
funding_source: aggregator
founded: 2025
headcount: 3
headcount_source: "Y Combinator company page, fetched 2026-08-28"
headcount_note: "Three founders and no fourth employee; the YC page lists 0 open roles. Crunchbase-derived aggregators say 1-10, which is the same fact in a band. The smallest headcount on this map by an order of magnitude — Senra (CO164) has 99 on $25M, Tensr claims a running factory on 3 people and $500K."
services:
  - "On-demand contract manufacture of robots and robotic systems"
  - "Robots dispatched to operate industrial machinery, package and ship"
  - "Automated retooling between designs"
  - "Automated quality inspection"
  - "Automated supply chain management and logistics"
  - "Stated 24-hour order-to-shipment cycle"
makes_or_does: >
  Operates a 12,000 sq ft factory in the Bay Area, California, in which robots run the
  industrial machinery rather than people. Takes on-demand customer orders, dispatches robots
  to make the part, then packages and ships it — the company states in under 24 hours. The
  automation spans supply chain, design, retooling, quality inspection and logistics, and is
  not sold as software: Tensr sells the finished hardware. Founded 2025 by three UC Berkeley
  robotics researchers out of Berkeley AI Research — Eric Berndt (CEO, MS/BS EECS), Adith
  Sundram (CTO, MS/BS ME) and C.K. Wolfe (PhD AI and robotics, formerly Technical Program
  Manager at BAIR, credited with securing $17M+ in DARPA and industry sponsorship). The three
  ran Berkeley's autonomous IndyCar team at 160mph. Press adds operating background from
  Rockwell Automation, aerospace manufacturing and FDA-regulated medical device production,
  though it does not say which founder carries which.
funding_notes: >
  $500K on record, investors Y Combinator, Güil Mobility Ventures and Symphony Ventures
  (California). Aggregator-grade only — no funding announcement exists on the company's own
  site and no press release was found, so `funding_source: aggregator` rather than press.
  Two aggregator disagreements worth carrying rather than resolving: one hub page is titled
  "$1M" while its own body says $500K, and that same page assigns batch F25 where the YC
  company page itself says Summer 2026. The YC page is the primary source and is used here.
  One aggregator also lists a "Bruno De Deken, Founder & Partner" who appears in no other
  source and is not treated as a founder in this entry.
hmlv_relevance: >
  The fifth instance on this map of the same pattern, and the one that tests it hardest.
  Hadrian (CO150), VulcanForms (CO161), Isembard (CO153) and Senra (CO164) all carry first-run
  risk by owning the floor — but each did it with hundreds of people and eight or nine figures
  of capital, which is exactly the counter-argument to H1: taking the liability looks like it
  costs a factory. Tensr claims the same liability shape on three people and $500K. If that
  holds, the "you must own the floor AND be huge" reading weakens; if it doesn't, it is
  evidence about how much the liability actually costs to carry.
  Their own positioning is H1's own claim in the competitor's mouth. "Factories that can
  manufacture NEW DESIGNS 24/7" and "manufacture one unit or one million at the same unit
  economics" is a direct assertion that changeover and first-run cost is the thing standing
  between HMLV and volume economics — which is what H1A2 is being interviewed on. The YC
  description goes further than any other entry on this map: their ML "learns from real-world
  manufacturing errors rather than human-generated training data." Prove-out failures as
  training signal is the nearest thing on this map to H1's own mechanism, and it is worth
  watching whether they ever sell it separately from the parts.
  Three counter-readings to hold. First, they manufacture ROBOTS — "robotic factories that
  build robots" — not the aerospace and defense parts the rest of this map serves. Whether
  robot assemblies present the same prove-out risk as a scrapped titanium billet is unproven;
  the Senra caveat applies with more force here. Second, greenfield again: a purpose-built
  12,000 sq ft floor with robots on the machines is not a brownfield shop with legacy machines
  and named machinists, which is where H1 has to work. Third, and most important, every claim
  in this entry that matters is self-published and 2026-fresh.
  Not a buyer. If interviewed, grade as expert evidence, not demand evidence.
liability_notes: >
  Graded `owns_outcome` on business shape, NOT on written commitment — read the grade with the
  caveat attached. They take custom orders and ship finished hardware from their own plant, so
  scrap, rework and schedule structurally land on them, the same construction as Hadrian and
  VulcanForms. But unlike those two there is no published envelope of any kind: no warranty
  language, no tolerance table, no process catalogue, no quality certifications named (no
  AS9100, no ISO, no ITAR), no pricing, and no customer named. Per the map's own grading rule
  this is a grade-down candidate; it is held at `owns_outcome` only because the delivered-part
  business model is asserted plainly and the alternative lanes fit worse. Revisit if the
  whitepaper turns out to publish an envelope, and drop the grade if the customer claim
  cannot be corroborated.
absence_notes: >
  Checked and not found, which is itself the finding for a company claiming a running factory:
  no customer is named; no unit, order or throughput count is given; no pricing; no quality
  certification; no funding announcement on their own site; no /about, /blog, /news or
  /careers page exists — the site is a single page plus a contact form. The whitepaper, which
  would be the first substantive disclosure, was not published as of 2026-08-28: the page is a
  countdown timer to 2026-08-31 with an email capture. Re-fetch it after that date; it is the
  cheapest scheduled intelligence on this map.
claims_notes: >
  Recorded as their claims, not as fact, per the self-published grading rule. Their own words:
  "NOW ONLINE · 12,000 SQFT FACTORY IN THE BAY AREA, CALIFORNIA"; "A robotic factory that
  builds robots"; "manufacture one unit or one million, at the same unit economics". Their YC
  page states they are "actively manufacturing customer orders for some of the largest
  robotics companies in the US and the International Space Station." That ISS claim is the
  single most checkable assertion attached to this company and nothing found so far
  corroborates it — no NASA, ISS National Lab or prime-contractor announcement names Tensr.
  Treat as unverified until it is.
known_contacts: []
source_url: https://www.tensr.com/
sources: >
  tensr.com (browser fetch 2026-08-28, homepage is the whole site) ·
  tensr.com/whitepaper (fetched 2026-08-28 — unreleased, countdown to 2026-08-31) ·
  ycombinator.com/companies/tensr (fetched 2026-08-28 — batch, headcount, self-description) ·
  thesanfranciscotribune.com/the-build-it-cohort-bay-area-startups-putting-ai-to-physical-work ·
  extruct.ai/hub/tensr-com · crunchbase.com/organization/tensr (403, aggregator data read
  via secondary sources) · pitchbook.com/profiles/company/1162050-40
first_added: 2026-08-28
status: mapped



## Stoneside Blinds & Shades

id: CO179
map: client
canonical_name: Stoneside Blinds & Shades
also_known_as: [Stoneside]
country: US
tier_side: demand
tier: ""
sector: Vertically integrated national custom window coverings — own factory, own measurers, own installers
window_layer: 4
geo_status: mapped
city: San Francisco, CA
address: 50 California St, Ste 1500, San Francisco, CA 94111
lat: 37.7932
lon: -122.3977
phone: "415-792-0787"
job_covered: spec_capture
integration: owns_factory
sells_to: none_yet
liability_taken: owns_outcome
touches_proveout: none
stage: incumbent_subsidiary
revenue_source: unknown
source_url: https://www.stoneside.com/office/san-francisco-california
sources_note: >
  Address and model from the company's own SF office page and its Yelp listing, checked
  2026-09-04. The behavioural claims below are from the founder's own phone call, not the site.
makes_or_does: >
  National custom window-covering business that owns every step: manufacturing, the measuring
  visit, and installation. The SF "office" is a suite in a shared building and appointment-only
  by their own description — the model is shop-at-home, so the showroom travels to the customer
  rather than the customer travelling to a showroom. Works through designers, architects and
  contractors as well as direct.
hmlv_relevance: >
  Layer 4, and the cleanest P&L in the trade to understand: because they own manufacturing,
  measuring and installation, they are the only layer that can attribute a remake to its true
  cause instead of billing it to somebody else. Measures free of charge, and moves liability
  onto the CUSTOMER when the customer supplies the dimensions — the enum in the Order schema
  that decides who eats a wrong number, observed in the wild. E7, E9, E11.
liability_notes: >
  owns_outcome on their own measurement: the visit is free and the remake is theirs. Flips to
  none the moment the customer self-measures, which they state explicitly.
known_contacts: [E7, E9, E11]
first_added: 2026-09-04
id_note: >
  Allocated CO173 on 2026-09-04 against a stale next-free number; that id
  was already held by a trade-software entry. Renumbered to CO179 on 2026-09-04.
  Nothing outside this file cited the colliding id, so no citation was orphaned.
status: mapped


## Art Shade Shop

id: CO180
map: client
canonical_name: Art Shade Shop
also_known_as: []
country: US
tier_side: demand
tier: ""
sector: Independent window-covering shop, San Francisco — established 1934
window_layer: 2
geo_status: mapped
city: San Francisco, CA
address: 698 14th St, San Francisco, CA 94114
lat: 37.7683
lon: -122.4275
phone: "415-431-5074"
job_covered: spec_capture
integration: software_plus_service
sells_to: none_yet
liability_taken: warranty
touches_proveout: none
stage: incumbent_subsidiary
revenue_source: unknown
source_url: https://www.bbb.org/us/ca/san-francisco/profile/window-shades/art-shade-shop-1116-914570
sources_note: >
  Address, phone, trading hours and the 1934 founding date from the BBB profile and Yelp
  listing, checked 2026-09-04. Nothing about their remake rate or job values is known.
makes_or_does: >
  A 90-year-old independent window-covering shop on 14th Street. Whether they fabricate
  in-house or only sell and fit is NOT established — that is the single fact that decides
  whether they sit on layer 1 or layer 2, and it is answerable by walking in.
hmlv_relevance: >
  One of the four dealers behind E9: measures by sending a human to the window, uses no
  software to capture or verify the dimension. The longevity is the interesting part — a
  business that has survived 90 years in this trade has seen every substitute for the
  measuring visit that has ever been tried, and can say why each failed.
liability_notes: >
  Not established. Graded warranty as the trade default and flagged rather than assumed.
known_contacts: [E9]
first_added: 2026-09-04
id_note: >
  Allocated CO174 on 2026-09-04 against a stale next-free number; that id
  was already held by a trade-software entry. Renumbered to CO180 on 2026-09-04.
  Nothing outside this file cited the colliding id, so no citation was orphaned.
status: mapped


## Susan Lind Chastain Inc.

id: CO181
map: client
canonical_name: Susan Lind Chastain Inc.
also_known_as: [Susan Lind Chastain, SLC2]
country: US
tier_side: demand
tier: ""
sector: Independent custom drapery and soft-treatment workroom, San Francisco
window_layer: 1
geo_status: mapped
city: San Francisco, CA
address: 1330 Natoma St, San Francisco, CA 94103
lat: 37.7692
lon: -122.4176
phone: "415-701-8898"
job_covered: spec_capture
integration: owns_factory
sells_to: none_yet
liability_taken: owns_outcome
touches_proveout: none
stage: incumbent_subsidiary
revenue_source: unknown
source_url: https://www.susanchastain.com/
sources_note: >
  Address, phone and service list from the company's own site and its Yelp listing, checked
  2026-09-04. 25+ years stated on their own site.
services:
  - "Fabrication of all window treatments — fabric shades, valances, lambrequins, curtains"
  - "Roman shades, woven shades, roller shades, curtain hardware"
  - "Bedding — pillows, duvets, coverlets, bedskirts, headboards"
makes_or_does: >
  A working soft-treatment workroom: they cut and sew the product themselves rather than
  ordering it in. Sells largely through interior designers, which is the classic workroom
  channel — the designer measures or specifies, the workroom fabricates to that number.
hmlv_relevance: >
  Layer 1, and the exact business the worked example in window-covering-players.html is built
  around: one P&L carries measuring, material and labour, so a remake costs it twice over.
  Also the most interesting liability case on the map — a workroom fabricating to a dimension
  a DESIGNER supplied is carrying somebody else's measurement error, which is the size_basis
  enum with a third party in the middle.
liability_notes: >
  owns_outcome on their own fabrication. Who carries a designer-supplied wrong dimension is
  unestablished and is the question worth asking them.
known_contacts: [E9]
first_added: 2026-09-04
id_note: >
  Allocated CO175 on 2026-09-04 against a stale next-free number; that id
  was already held by a trade-software entry. Renumbered to CO181 on 2026-09-04.
  Nothing outside this file cited the colliding id, so no citation was orphaned.
status: mapped


## Blinds.com

id: CO182
map: client
canonical_name: Global Custom Commerce, Inc.
also_known_as: [Blinds.com, "Blinds.com, a Home Depot company"]
country: US
tier_side: demand
tier: ""
sector: Online custom window coverings; owned by The Home Depot since January 2014
window_layer: 6
geo_status: off_map
city: Houston, TX
address: 10255 Richmond Ave, Ste 300, Houston, TX 77042
lat: 29.7370
lon: -95.5410
service_area_observed: San Francisco and Oakland serviced directly by own technicians
job_covered: spec_capture
integration: software_plus_service
sells_to: none_yet
liability_taken: part_guarantee
touches_proveout: none
stage: incumbent_subsidiary
revenue_source: unknown
source_url: https://ir.homedepot.com/news-releases/2014/01-23-2014-014522229
sources_note: >
  Ownership and acquisition date from The Home Depot's own investor-relations release,
  23 January 2014. HQ address from company directories, checked 2026-09-04. Revenue figures
  circulating on data aggregators are unsourced and are NOT recorded here. The operating
  behaviour below is first-hand: the founder booked a real in-home appointment for six windows.
makes_or_does: >
  Sells custom window coverings online and disperses orders to a range of manufacturing
  vendors rather than making anything itself. Straddles two layers: nominally layer 6, where
  the customer self-measures and a fit guarantee absorbs their error, but it runs its OWN
  measure-and-fit service in San Francisco and Oakland, which is layer 5 behaviour on a
  layer 6 business.
hmlv_relevance: >
  The most evidenced company on this map and the only one observed in person. Its measure
  technician put wrong-size orders at roughly 50/50 between his own error and the factory's —
  half the errors survive a trained person standing at the window, which is the single most
  load-bearing data point H3 has (E15). It covers all rework when its own technician took the
  measurement and the cost sits in its own P&L; when the customer measured, the guarantee
  still pays (E16). Orders outside SF and Oakland are routed elsewhere (E17).
liability_notes: >
  part_guarantee — a published, bounded fit guarantee that pays for the customer's own
  measurement error. Evidenced in the founder's appointment and on the public product pages.
known_contacts: [E15, E16, E17]
first_added: 2026-09-04
id_note: >
  Allocated CO176 on 2026-09-04 against a stale next-free number; that id
  was already held by a trade-software entry. Renumbered to CO182 on 2026-09-04.
  Nothing outside this file cited the colliding id, so no citation was orphaned.
status: mapped


## Unidentified national blinds retailer ($225 visit)

id: CO183
map: client
canonical_name: ""
also_known_as: ["the national blinds guys"]
country: US
tier_side: demand
tier: ""
sector: National blinds retailer — exact legal entity not established
window_layer: unpinned
geo_status: unknown
city: ""
address: ""
job_covered: spec_capture
integration: software_plus_service
sells_to: none_yet
liability_taken: none
touches_proveout: none
stage: incumbent_subsidiary
revenue_source: unknown
source_url: ""
sources_note: >
  Deliberately entered UNNAMED rather than left out. E8 is the source of $225 — the sharpest
  costed number in this market and the one the layer-1 worked example is built on — and the
  company it came from was recorded in the founder's notes only as "the national blinds guys".
  An entry with an empty name keeps that gap visible; leaving it out would let the number
  circulate with no company behind it.
makes_or_does: >
  Charges $225 to send someone out to measure, said that visit is "not accurate enough", and
  declines jobs outright when the drive is too far — so the cost of measuring physically caps
  their service radius.
hmlv_relevance: >
  Carries the load-bearing number in the entire H3 thesis and cannot currently be checked by
  anyone else. Pinning the entity is cheap and worth doing before $225 is quoted to an
  investor: it appears in the pitch, the players page and the market ladder.
liability_notes: >
  Not established.
known_contacts: [E8]
first_added: 2026-09-04
id_note: >
  Allocated CO177 on 2026-09-04 against a stale next-free number; that id
  was already held by a trade-software entry. Renumbered to CO183 on 2026-09-04.
  Nothing outside this file cited the colliding id, so no citation was orphaned.
status: unidentified
