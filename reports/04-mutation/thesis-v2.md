---
purpose: The V2 product thesis — how the trained V1 measurement model expands through parallel textile and horizontal-industry routes into multi-sensor attribution and verified operating recommendations.
idea: industrial-process-data-infrastructure
version: 2
date: 2026-09-15
previous_version_file: reports/04-mutation/thesis-v1.md

thesis: |
  The first product is not only an optical sensor. It is a trained measurement system that
  turns raw images into calibrated fibre counts, dimensions, cotton/polyester/unknown labels
  and uncertainty. V2 connects two or more of those measurement systems to the operating data
  around them. From that shared measurement core, two routes run in parallel. Matter is the
  textile route: measure before and after its filter, learn when performance changes, then
  use its mill access to place sensors at a source process, the ETP inlet and final discharge
  and close one wet-process loop at a time. CyFract is the horizontal-industry route: put the
  same performance layer around its separation product in each industry it enters, while each
  new water and buyer is calibrated and validated separately.

core_bet: "A trusted measurement at one point can become a control product when the same measurement is synchronized across a process and joined to the setting that produced the result."

what_changed_from_previous: >-
  V1 previously began at inline polymer identification as though the measurement already
  existed. V2 now includes the missing model-training layer: segmentation, geometry,
  cotton/polyester/unknown classification, calibration and uncertainty. The next product is
  defined as multi-sensor attribution and verified recommendations. Matter to textile mills
  and CyFract to other industries are parallel expansion routes from the same core, rather
  than successive stages or three undifferentiated customer segments.

evidence_that_caused_change:
  - founder_product_sequence_2026-09-15
  - E5
  - E6
  - E10

open_questions:
  - Can the V1 model distinguish cotton, polyester and unknown on independently sourced fibres and real wastewater, not only controlled standards?
  - Will Matter expose synchronized flow, pressure, filter state and intervention records alongside the sensor readings?
  - Which operating variable can Matter change often enough to learn a response curve: backwash timing, flow, pressure, cleaning or another setting?
  - Will CyFract provide paid or cost-covered pilots, data rights and access to operating conditions in each new industry?
  - How far do optical calibration and classification transfer between textile water and the other waters CyFract encounters?
  - At a textile mill, can source events be recovered after transport delay, dilution and mixing at the ETP?
  - Which first mill decision produces a measurable saving inside one pilot: rinse endpoint, treatment backwash or another operator-confirmed action?

assumptions_confirmed_so_far: []
assumptions_killed_so_far: []
---

# Thesis v2 — measurement to feedback

## 1. The shared core and two parallel routes

| Stage | Product | Model output | Buyer or partner | Gate to advance |
|---|---|---|---|---|
| V1A | Controlled imaging and labelled-data rig | Training examples with independent material labels | Internal development | Repeatable images and traceable labels from multiple material sources |
| V1B | One-point fibre measurement | Count, geometry, cotton/polyester/unknown probabilities, concentration and quality state | Filter companies and funded brand programmes | Held-out real samples meet an agreed error and rejection threshold |
| Textile T1 | Matter separation loop | Inlet/outlet removal by type and size, breakthrough or fouling event, verified intervention result | Matter | One operating change produces a repeatable measured effect |
| Textile T2 | Mill wet-process attribution | Source-to-ETP event attribution linked to batch, recipe, machine and treatment state | Textile mill, reached through Matter or a brand | One source event can be attributed after transport and mixing |
| Textile T3 | Mill process control | Human-approved, then controller-integrated set-point recommendation | Textile mill | One recommendation changes a paid operating outcome repeatedly |
| Horizontal H1 | CyFract separation loop | Inlet/outlet performance under a new water matrix and operating conditions | CyFract and its project customer | The water can be calibrated and the measured property matters to the buyer |
| Horizontal H2 | Industry-specific control | Verified recommendation for the separation decision in that application | Industrial site reached through CyFract | One operating change produces a repeatable paid outcome |

V1A and V1B are the shared trunk. After that, the routes are parallel. Matter supplies the
first paired textile-filter dataset and a route into mills, where multiple sources, transport
delays and treatment stages interact. CyFract supplies other industrial applications for the
same measurement and performance architecture. A CyFract deployment is not a prerequisite
for a textile-mill deployment, and a Matter deployment is not a prerequisite for CyFract.

## 2. The model stack

V2 does not require a foundation model. It is a stack of bounded models whose outputs can be
checked against physical measurements.

1. **Measurement model.** Instance segmentation finds fibres and particles. A small image
   classifier plus optical and geometric features predicts cotton, polyester or unknown.
   Calibration converts pixels and sampled volume into dimensions and concentration.
2. **Quality model.** Blur, obstruction, saturation, unfamiliar material and distribution
   shift cause a rejected or low-confidence reading rather than a forced label.
3. **Synchronization model.** Flow and residence time align an upstream event with the
   downstream sensor that sees it later.
4. **Performance model.** Mass balance calculates removal; change-point detection identifies
   breakthrough or fouling; regularized regression or gradient-boosted trees estimate how
   operating settings affect the result.
5. **Recommendation model.** Constrained search or Bayesian optimisation proposes the next
   setting to test inside limits supplied by the equipment owner. An operator approves it.

Reinforcement learning and autonomous actuation are not requirements for V2. They become
relevant only after repeated interventions establish a safe operating envelope and enough
data exists to evaluate a policy without learning dangerous behaviour on a live line.

## 3. The Matter loop

Minimum instrumentation:

- one synchronized measurement before the filter;
- one after the filter;
- flow and pressure or differential pressure;
- equipment state and every backwash, cleaning or setting change;
- a shared clock and a record of sampled volume and sensor quality.

The first deliverable is a performance record, not automatic control: removal efficiency by
size and cotton/polyester class, the unknown fraction, confidence, operating conditions and
the point at which performance changed. The first closed loop is complete when Matter changes
one setting or intervention in response, and the paired sensors verify what happened next.

Matter's existing offer of a pilot site and data access supports access to try this. It does
not establish a paid contract, a mill's consent, usable historian data or permission to retain
the resulting dataset. Those are gates in the agreement.

## 4. The CyFract loop

CyFract is the horizontal route. Its value is not merely another filter company; its horizontal
separation product can expose the measurement system to wastewater treatment, desalination,
mining, oil and gas, agriculture and other water matrices through projects it already pursues.

Each water is a separate calibration and market test. The three questions remain:

1. Does the optical system obtain a usable signal in that water?
2. Is the measured particle or fibre property relevant to the customer's decision?
3. Will someone pay to know it or change an operating decision because of it?

A successful CyFract pilot expands the model's robustness and proves that the V2 data contract
can sit around more than one separation technology. It does not gate the textile route, and it
does not, by itself, establish a market in every industry CyFract names.

## 5. The textile-mill loop

The minimum useful deployment is three synchronized locations:

1. a high-impact process drain, such as the first rinse from a dye machine or a garment washer;
2. the ETP influent or equalisation outlet;
3. the final discharge.

A fourth sensor before and after a treatment stage isolates that stage's performance. Each
observation must join to a facility, location, batch, recipe, machine, material, timestamp,
flow and sensor-quality record. The model then estimates which process event caused a later
load at the ETP after accounting for travel time, dilution and mixing.

The first commercial output is attribution: which batch or operation drove the load, whether
the treatment system removed it, and what left the facility. The first optimisation product
is one human-approved decision with a directly measurable result. Rinse endpoint and
condition-based filter backwash are candidates; operator evidence should select between them.

## 6. Commercial structure

### Brands and mills buy different outcomes

The commercial model is two-sided because the incentives are split. The mill pays the water,
energy, chemical, treatment and rework bills and therefore owns the direct operating return.
The brand does not receive those savings, but it owns value-chain targets, supplier engagement,
sourcing risk and the need for comparable primary data across facilities.

| Customer | Product bought | Budget logic |
|---|---|---|
| Brand | Supplier portfolio, verified baselines and reductions, intervention prioritisation, facility comparison and auditable exports | Scope 3 and water programmes, responsible sourcing, supplier development, sustainability data and innovation |
| Mill | Sensors, process attribution, operating recommendations and verified savings | Production, utilities, quality, ETP and capital-improvement budgets |

The recommended structure is that a brand pays an annual portfolio or programme fee and may
fund the first cohort or reduce the financing risk. Each mill pays for site hardware and the
optimisation service once the intervention demonstrates an acceptable payback. A lender,
programme or brand guarantee can fund the mill's upfront capital and be repaid from its
savings. Longer orders, preferred-supplier status or volume commitments can be more valuable
to the mill than a grant, but they count only when the brand puts them in an agreement.

This structure avoids asking a brand to subsidise another company's utility bill and avoids
asking a mill to pay for a brand's portfolio reporting. Brands sharing the same suppliers can
fund a pooled programme, while the mill retains one operational system rather than installing
a separate instrument for every customer.

Partner discounts or cost-covered pilots can be rational when they purchase capabilities and
access rather than being treated as lost revenue. A partner arrangement must state:

- who pays for hardware, installation, calibration, travel, maintenance and reference tests;
- the sites and operating data the partner will make available;
- whether the site owner has consented;
- Lattice's right to retain raw sensor data and derived model improvements;
- the introductions or deployment opportunities exchanged for any discount;
- who owns the customer relationship and whether Lattice may sell the measurement or
  optimisation layer directly at the site;
- a time limit and a conversion point from pilot terms to commercial terms.

Without those terms, free hardware buys hope rather than distribution. Matter and CyFract are
currently organisations in conversation; neither is recorded as a paying customer.

## 7. How V2 is sized

V2 revenue is not sized from the total savings of an efficiency programme. It is sized from
the specific loop the product closes.

Two programme results anchor the value pool:

- Apparel Impact Institute reports that 56 Clean by Design mills saved $22.3M in annual
  operating costs, or about $398,000 per participating mill, while reducing water use 11% and
  coal use 7% [S].
- Its later review of 67 wet-processing facilities reports average annual energy-efficiency
  savings of 12.6% and water savings of 11.5% [S].

Those are results from broader efficiency programmes, not savings caused by this product. If
the $398,000 average were generalized across the documented floor of 16,000 wet-processing
sites, the theoretical customer savings pool would be about $6.4B a year. This is the value
available to compete for, not company revenue and not a forecast that every site can attain it.

A "Clean by Design mill" is a participating Tier 2 wet-processing facility, not a mill type or
certification. The programme scans a facility, establishes resource baselines, identifies and
implements a portfolio of projects, and verifies the resulting savings. Its ten practices are
mostly factory-utility and infrastructure measures: water leaks and cleaning, cooling-water
reuse, condensate reuse, process-water reuse, heat recovery from hot water, boiler efficiency,
steam-system maintenance, insulation, heat recovery from hot air and compressed-air
optimisation. Many require physical works and capital in addition to better measurement.

The participating mills were selected or nominated into an improvement programme and differ
in size, baseline efficiency, production mix, geography and energy prices. The programme
figures therefore demonstrate that a large savings pool exists inside wet-processing plants;
they do not establish that the sensor platform causes $398,000 of savings at a representative
mill. The $6.4B extrapolation must not be presented as product TAM. Product-addressable value
is measured loop by loop: dye and rinse control, treatment dosing, aeration, backwash, reuse or
another decision where the system can verify the before-and-after result.

For separation partners:

`active deployments × hardware or deployment fee + monitored systems × annual software fee`

For mills:

`distinct paying sites × annual site price`, checked against
`measured annual saving from the chosen decision × capturable share`

Using 5–10% of the $398,000 programme result as a high-level pricing check gives roughly
$20,000–40,000 per site per year. That price becomes supportable only when the product controls
enough verified loops to create substantially more value than its fee. It is not supported by
the Clean by Design evidence alone. The resulting recurring-revenue sensitivity is:

| Share of the 16,000-site documented floor | Paying sites | At $20k/site/year | At $40k/site/year |
|---:|---:|---:|---:|
| 10% | 1,600 | $32M | $64M |
| 25% | 4,000 | $80M | $160M |
| 50% | 8,000 | $160M | $320M |
| 100% ceiling | 16,000 | $320M | $640M |

The nearer population is the current ZDHC footprint: 2,359 direct-discharge wastewater reports
analysed and 3,712 registered suppliers in its 2025 impact report [S]. At $20,000–40,000 per
site, that population represents a $47M–148M recurring-revenue ceiling before adoption,
eligibility, overlap and competition are applied.

Hardware is separate. The v1 assumption of $45,000–75,000 for a three-to-five-point site gives
a $720M–1.2B one-time full-installation ceiling across 16,000 sites. It remains an untested
price and cannot be added to ARR as though it recurred annually.

Brand supplier lists overlap, so sites are deduplicated before they enter the model. Partner
reach is counted only when an agreement grants an introduction or deployment right. Until the
first intervention has a measured saving, V2 pricing remains a sensitivity range rather than
a revenue forecast.

Sources for the programme anchors: Apparel Impact Institute, "What is Clean by Design"
(2019), https://apparelimpact.org/resources/what-is-clean-by-design/; Apparel Impact Institute,
"Efforts to Decarbonize the Apparel Sector" (2023),
https://apparelimpact.org/wp-content/uploads/2023/06/Aii_RoadmapReport-752.pdf; ZDHC Impact
Report 2025, https://www.roadmaptozero.com/impact-report-2025.

## 8. The immediate build and evidence gate

The next complete experiment is one paired separation run:

1. train and freeze a V1 measurement model on independently labelled samples;
2. measure a known mixed feed before and after one separation system;
3. synchronize readings with flow, pressure and equipment state;
4. trigger or wait for one controlled intervention;
5. predict the direction and magnitude of the next performance change;
6. verify the prediction with the paired sensors and an independent reference sample.

That experiment produces the first V2 dataset and settles whether the company has only a
sensor reading or the beginning of a feedback product.
