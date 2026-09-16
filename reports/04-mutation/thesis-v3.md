---
purpose: The locked fashion-first strategy, design-partner economics, three-month product target, founder market ceiling and the validation gates required before each claim can be made externally.
idea: industrial-process-data-infrastructure
version: 3
date: 2026-09-15
previous_version_file: reports/04-mutation/thesis-v2.md

thesis: |
  Build the prototype and inline polymer-identification measurement system in three months,
  use it to convert funded fashion-brand microfibre programmes into the first recurring
  revenue, and use Matter as a cost-covered design partner and route into textile mills.
  Once the measurement system and brand demand are proved, add synchronized sensors for
  chemical, dye, water and energy use and close one paid wet-process optimization loop at a
  time. In parallel, CyFract and alternative horizontal-separation partners can carry the
  measurement and feedback architecture into other industries after their deployments
  mature. The fashion route does not depend on CyFract.

core_bet: "Inline polymer identification is the entry product; verified wet-process savings are the expansion product."

what_changed_from_previous: >-
  This version fixes the commercial order and partner economics. Matter and CyFract are
  design partners, not clients. Matter is expected to cover direct costs and product R&D in
  exchange for co-development and access, with no margin assumed. CyFract is treated as a
  later horizontal route with an approximately one-year maturity assumption and an explicit
  requirement to recruit alternatives. Fashion is the near-term revenue wedge. The founder's
  35% savings shorthand and $20B fashion-manufacturing wedge are recorded as ceilings that
  require bottom-up validation, not as sourced market facts.

evidence_that_caused_change:
  - founder_strategy_lock_2026-09-15
  - founder_product_sequence_2026-09-15
  - E5
  - E6
  - E10

open_questions:
  - Can the measurement system meet a buyer-agreed polymer classification and concentration threshold on real wastewater within three months?
  - Will a working prototype convert a funded brand programme at $25k, $50k or $100k per year?
  - Will Matter sign terms covering direct costs, R&D, site access, operating data, data rights and introductions?
  - Which mill decision is the first controllable paid loop: rinse endpoint, dye dosing, treatment dosing, aeration or filter backwash?
  - What is the actual annual energy, water, dye, chemical, rework and treatment spend of the reachable mill population?
  - What portion of that spend can the product influence and verify without double counting?
  - What milestones would make CyFract deployment-ready, and which alternative horizontal partners remove the dependency?

assumptions_confirmed_so_far: []
assumptions_killed_so_far: []
---

# Thesis v3: fashion first, then verified process control

## 1. The locked sequence

| Horizon | Product and route | Economic purpose | Gate before advancing |
|---|---|---|---|
| 0-3 months | Prototype plus inline polymer identification: calibrated count, concentration, cotton/polyester/unknown probabilities and uncertainty | Convert funded fashion-brand microfibre programmes; create the shared measurement core | Independently held-out real wastewater meets buyer-agreed error, latency and rejection thresholds; at least one brand enters a paid pilot or procurement path |
| First design deployment | Paired sensors around Matter's filter, synchronized with flow, pressure, equipment state and interventions | Let Matter fund direct costs and R&D; prove a closed performance loop; gain textile-mill access | Signed terms cover cost reimbursement, site consent, data access, data rights, intervention records and introductions |
| Fashion expansion | Sensors at selected mill wet processes, the ETP inlet and final discharge, joined to batch, recipe, machine, chemical, water and energy data | Attribute loss to a process and sell one verified optimization outcome to the mill while the brand buys portfolio visibility | One human-approved recommendation repeatedly changes a paid operating outcome without harming quality or throughput |
| Fashion platform | Broader chemical, dye, water and energy sensor kit across multiple loops | Expand site value and recurring revenue across wet processing | Measured savings exceed the combined hardware, integration and service cost with an acceptable mill payback |
| Parallel horizontal route | CyFract plus alternative separation partners enter wastewater, desalination, mining, oil and gas and agriculture | Reuse the measurement and feedback architecture in other industries | Each water, measured property, buyer and willingness to pay passes a separate test; no expansion depends on one partner |

This sequence is a strategy, not a forecast. Three months and one year are founder-set targets.
Both require dated milestones and evidence. Fashion can proceed through brands and Matter while
CyFract matures. CyFract is not on the critical path to fashion revenue.

## 2. What is evidence, and what is a ceiling

| Claim | Status | What it means |
|---|---|---|
| Clean by Design participants averaged 12.6% energy-efficiency savings | Sourced programme result | Apparel Impact Institute's review covered 67 participating wet-processing facilities. It demonstrates an energy-efficiency value pool, not product-attributable savings. |
| The same group averaged 11.5% water savings | Sourced programme result | It demonstrates a water value pool across a broad improvement programme. |
| The same group averaged a 10.8% GHG reduction | Sourced programme result | It is an environmental result with a different denominator from water and energy. |
| "35% savings" | Founder shorthand and ceiling assumption | 12.6 + 11.5 + 10.8 = 34.9, but those percentages cannot be added into a valid cost-saving rate. They measure different outcomes. Use 10-35% only as a scenario range until savings are rebuilt by cost line. |
| "$20B fashion-manufacturing wedge" | Founder-defined market ceiling | This is the ambition for the total fashion wet-process value pool the full platform could address. It is not yet TAM, revenue or customer savings. It needs a bottom-up model. |
| Other industries add billions | Founder direction, unsized | Wastewater, desalination, mining, oil and gas and agriculture remain later options. No market value is claimed yet. |

A defensible market model must keep four quantities separate:

1. **Customer spend:** annual mill expenditure on energy, water, dyes, chemicals, treatment,
   rework and waste.
2. **Influenceable spend:** the portion controlled by decisions the sensor and model can change.
3. **Verified customer savings:** the measured before-and-after improvement attributable to
   those decisions.
4. **Company revenue:** hardware, software and programme fees that customers will pay from
   that value.

The $20B ceiling becomes a market claim only when the company defines which of those four it
represents, deduplicates the reachable mill population and supports the spend and savings for
each line item.

## 3. The product that can unlock the first revenue

The three-month target is a trained measurement system, not a foundation model. It combines:

- instance segmentation for fibres and particles;
- a compact image classifier plus optical and geometric features for
  cotton/polyester/unknown probabilities;
- calibration from pixels and sampled volume to dimensions and concentration;
- quality detection for blur, obstruction, saturation and unfamiliar materials;
- explicit low-confidence rejection rather than a forced label;
- a report that exposes the result, confidence, sample conditions and traceability.

The prototype is revenue-ready only when it works on independently sourced fibres and real
wastewater, not only clean standards. The exact accuracy threshold is not invented internally;
it is agreed with the first buying brand and Matter against the decision each needs to make.

The current commercial hypothesis is 20-50 funded brand microfibre programmes paying roughly
$25,000-$100,000 a year, with $50,000 as the working price. At 20-50 programmes and $50,000,
the early recurring-revenue sensitivity is $1.0M-$2.5M a year. Brand count, budget ownership,
procurement route, proof threshold and willingness to pay remain assumptions.

## 4. Matter and CyFract are design partners

Neither company is a client or a source of recognized revenue today.

### Matter: fashion route

The intended exchange is that Matter covers direct hardware, installation, testing and R&D
costs while the parties build the paired-sensor filter system. No margin is assumed from
Matter. The economic return to Lattice is the trained product, operating data and access to
brands and textile mills. That exchange is rational only if an agreement states:

- which direct and R&D costs Matter pays and on what schedule;
- which filter sites and mill sites are available, with site-owner consent;
- access to synchronized flow, pressure, filter state, cleaning and intervention records;
- rights to retain raw sensor data and improve derived models;
- agreed reference tests and success criteria;
- introductions to named brands or mills and permission for direct commercial relationships;
- ownership of hardware, maintenance obligations, confidentiality and a time limit;
- whether any exclusivity exists and what consideration is received for it.

Cost coverage without data rights or customer access is contract manufacturing. Access without
a signed site and data commitment is not consideration.

### CyFract: horizontal route

The founder expects CyFract to need approximately one year to mature into a useful deployment
channel. The year is a planning assumption, not evidence. It should be replaced by milestones:
funding, a named industrial site, an installation date, an operating-data owner and a customer
decision the paired measurement can improve.

The company should recruit 3-5 other horizontal separation partners so CyFract never becomes
a dependency. Every new vertical must separately prove optical compatibility, relevance of the
measured property, access to operating data and a buyer with a budget.

## 5. The wet-process expansion

The broader kit is assembled around the first valuable decision rather than sold as an
undifferentiated sensor bundle. Candidate inputs include fibre imaging, colour or absorbance,
turbidity, pH, conductivity, oxidation-reduction potential, temperature, flow, pressure and
machine state. Energy and water meters may already exist and should be integrated when they do.

The first loops to compare are:

| Loop | Decision | Direct value | Main proof risk |
|---|---|---|---|
| Rinse endpoint | Stop or continue a rinse | Water, heat, cycle time and wastewater load | Quality must remain inside specification across recipes and fabrics |
| Dye dosing and exhaustion | Adjust dye, salt, alkali, temperature or time | Dye and chemical cost, first-pass quality, less rework | Inline signal must predict shade and fixation better than the current control method |
| Treatment chemical dosing | Adjust coagulant, oxidant, acid or alkali | Chemical cost and discharge performance | The controlled variable must respond within the process residence time |
| Aeration | Adjust blower or dissolved-oxygen set point | Electricity and treatment stability | Energy savings cannot create treatment failure |
| Filter backwash or cleaning | Trigger maintenance from measured performance | Water, energy, uptime and media life | Paired sensors must detect a repeatable change before failure |

Each loop needs a baseline, one intervention, a counterfactual or control, independent quality
checks and a measured financial result. Recommendations remain human-approved until repeated
trials establish safe operating limits.

## 6. Who pays

Brands and mills buy different products because they receive different value.

| Buyer | Pays for | Why the budget can exist |
|---|---|---|
| Brand | Supplier portfolio, verified baseline and reduction data, intervention prioritization, facility comparison and auditable exports | Scope 3 and water programmes, responsible sourcing, supplier development, sustainability data and innovation |
| Mill | Sensors, integrations, process attribution, recommendations and verified savings | Production, utilities, quality, dyehouse, ETP and capital-improvement budgets |
| Matter | Direct build and R&D costs under a design-partner agreement | Filter performance evidence, product improvement and commercial proof |
| CyFract or a peer | Later cost-covered industry validation, if agreed | Separation-performance evidence and a reusable measurement layer |

The brand can fund the first supplier cohort or guarantee adoption. The mill should adopt the
site system when verified savings justify its fee and payback. Shared suppliers must be
deduplicated so several brands do not create several copies of one site in the market model.

## 7. Validation register

### A. Three-month build

| Assumption to validate | Cheapest decisive evidence | Pass condition before the next claim |
|---|---|---|
| Cotton, polyester and unknown can be separated optically | Blind, independently labelled holdout set from multiple material sources | Buyer-agreed precision, recall, unknown rejection and concentration error |
| Static performance transfers inline | Recirculating rig followed by one live wastewater line | Stable readings across flow, bubbles, fouling, turbidity and realistic concentration |
| Concentration is calibrated | Known spike and recovery series with sampled-volume traceability | Error and repeatability remain inside the decision threshold |
| The system is usable at a site | Timed installation, cleaning and maintenance trial | Agreed uptime, latency, cleaning interval and bill of materials |
| Three months is achievable | Week-by-week build plan with owners and dependency dates | Critical-path parts, labelled data, reference testing and pilot site are all committed |

### B. Matter design partnership

| Assumption to validate | Cheapest decisive evidence | Pass condition before the next claim |
|---|---|---|
| Matter will cover direct costs and R&D | Written term sheet with cost categories and payment timing | No unfunded build obligation |
| Matter can supply the needed site and operating data | Site data map plus owner approval | Inlet/outlet, flow, pressure, filter state and intervention records share a clock |
| The partnership creates distribution | Named introduction and commercial-rights clause | Lattice can pursue brands and mills directly after the pilot |
| The loop can be changed and measured | One controlled operating intervention | Paired sensors verify a repeatable before-and-after change |

### C. Brand revenue

| Assumption to validate | Cheapest decisive evidence | Pass condition before the next claim |
|---|---|---|
| 20-50 brands have funded microfibre programmes | Named census with programme owner and current activity | Each counted organisation has a live budget or funded workstream |
| A prototype unlocks purchase | Five prototype reviews with real budget owners | At least one paid pilot or procurement path with dated next step |
| $50,000 per year is viable | Price test at $25k, $50k and $100k against a defined deliverable | Buyer chooses a level or supplies a budget boundary and approval route |
| Portfolio data is the brand product | Workflow review using the brand's current report and supplier process | Proposed output replaces or advances a real recurring task |
| Regulation is not required for demand | Budget evidence tied to an existing programme | Purchase case stands without a new legal mandate |

### D. First mill optimization loop

| Assumption to validate | Cheapest decisive evidence | Pass condition before the next claim |
|---|---|---|
| The mill has enough controllable spend | Twelve-month utility, chemical, dye, quality and ETP ledger for one site | Baseline by process and batch is complete enough to price one loop |
| A specific decision causes waste | Operator interviews plus synchronized process data | One repeatable loss event maps to one adjustable variable |
| The sensor kit observes that decision | Short instrumented trial | Signal changes early enough and reliably enough to guide action |
| Savings are attributable | Controlled intervention or matched-batch comparison | Quality and throughput hold while one cost line falls |
| The mill will pay | Proposal based on measured annual value | Accepted pilot price and target payback from the operational budget owner |

### E. $20B fashion ceiling

| Assumption to validate | Cheapest decisive evidence | Pass condition before the next claim |
|---|---|---|
| The number means one defined thing | Market-model definition signed off internally | It is labelled customer spend, influenceable spend, savings or company revenue |
| Site population is real and deduplicated | Merge brand lists, ZDHC footprint and mill databases by facility | Reachable sites have geography, process type and ownership |
| Spend per site is supportable | Representative mill ledgers by size, process and country | Low, base and high annual spend distributions by cost line |
| 10-35% is plausible | Loop-level studies and measured pilots | Savings are calculated by line item and never added across different denominators |
| Revenue can be captured | Willingness-to-pay and adoption model | Price, adoption, competition, gross margin and implementation capacity are included |

### F. CyFract and other industries

| Assumption to validate | Cheapest decisive evidence | Pass condition before the next claim |
|---|---|---|
| CyFract will be deployment-ready in about one year | Milestone plan confirmed by CyFract | Funding, site, date, data owner and buyer decision are named |
| The architecture transfers | One representative sample and bench run per water matrix | Usable signal at realistic turbidity, salinity, oil and solids conditions |
| The measured property has economic value | Buyer workflow and loss interview in each vertical | A named owner changes a paid decision from the result |
| The route is not partner-dependent | Census and outreach to 3-5 alternatives | At least two credible routes can provide sites and operating data |

## 8. Go or stop gates

1. **Measurement gate:** do not sell polymer identification until blind real-water results and
   rejection behavior meet a buyer-agreed threshold.
2. **Revenue gate:** do not call the 20-50 brand population a market until named budgets,
   procurement paths and at least one paid commitment exist.
3. **Partner gate:** do not build bespoke Matter hardware until cost coverage, data rights,
   site access and introductions are written.
4. **Optimization gate:** do not promise water, energy, dye or chemical savings until one
   controlled mill intervention produces an attributable result.
5. **Market gate:** do not present 35% as a combined saving or $20B as TAM until the bottom-up
   model defines and supports them.
6. **Expansion gate:** do not allocate core product capacity to another industry until its
   water matrix, buyer, decision and willingness to pay are independently validated.

## 9. The story that is supportable now

Lattice is building an inline polymer-identification system for funded fashion microfibre
programmes. The three-month objective is to turn that measurement into the first paid brand
deployment. Matter and CyFract are design partners, not clients: Matter is the near-term
fashion route and is expected to cover direct build and R&D costs; CyFract is a later parallel
route into other industries and must be de-risked with alternatives. The expansion product is
a multi-sensor system that attributes wet-process loss and verifies one optimization decision
at a time. Industry programmes show material headroom, including average reductions of 12.6%
in energy use, 11.5% in water use and 10.8% in GHG emissions across 67 facilities. They prove
the value pool exists, but not that this product captures it. The founder's $20B fashion wedge
is the ceiling the company will now test from mill-level spend upward.

Sources for the programme anchors: Apparel Impact Institute, "Efforts to Decarbonize the
Apparel Sector" (2023), https://apparelimpact.org/wp-content/uploads/2023/06/Aii_RoadmapReport-752.pdf;
Apparel Impact Institute, "What is Clean by Design" (2019),
https://apparelimpact.org/resources/what-is-clean-by-design/; ZDHC Impact Report 2025,
https://www.roadmaptozero.com/impact-report-2025.
