---
purpose: The market model for the inline polymer identification system — three channels, the staged product behind them, and every number the revenue rests on, graded sourced or assumed.
idea: industrial-process-data-infrastructure
version: 1
date: 2026-09-15
previous_version_file: null

thesis: |
  An inline sensor that identifies the polymer type of particles in process water, not just
  how many there are. The first buyers are the people already paying to find that out by
  hand: filtration companies proving their filters work, and brand microfibre programmes
  burning specialist days on FTIR microscopy. Textile wet-processing mills are the volume
  market, but nothing forces a mill to measure fibre, so they open only when the same probe
  also measures what they already check by hand and can be tied to water, heat and rework.
  Brands supply the mandate, mills supply the volume, filtration companies supply the first
  revenue and the hardest technical test.

core_bet: "What is in the water predicts something a mill or a brand will change a decision over — and polymer type predicts it better than particle count."

what_changed_from_previous: null
evidence_that_caused_change: []

open_questions:
  - Does polymer type map to a process step, or does everything mix in a common drain before it can be attributed?
  - What does a brand pay today, per year, for fibre identification work — the only real input to the programme price.
  - Will a mill pay for an instrument no regulation requires, when the brand mandates but does not fund it?
  - Which single decision can be closed-loop first: rinse endpoint, peroxide kill, or filter backwash?

assumptions_confirmed_so_far: []
assumptions_killed_so_far: []
---

# Thesis v1 — the number stack

Every figure below is marked **[S]** sourced or **[A]** assumed. Sources live in
`reports/03-validation/evidence.md` and the research notes behind the 2026-09-15 sizing
session. The open questions each figure depends on are numbered against
`reports/pages/discovery-questions.html`.

---

## 1. Who pays, and who mandates

The structural finding that sets the whole model: in every comparable programme the
**supplier funds the equipment and the brand supplies the obligation**. [S]

- Efficiency programme capital 2018–2025: $144.6M from facilities against $43.7M from the
  programme — facilities funded 77% [S]
- The Higg platform charges the facility $899/year, not the brand [S]
- ZDHC obliges the supplier to commission its own wastewater testing above 15 m³/day [S]
- The Clean by Design programme charged participating mills 25,000–35,000 RMB [S]

So the price has to fit a mill's cheque book, with the brand as the reason the cheque gets
signed. A brand-funded fleet purchase is not how this industry has ever bought.

---

## 2. Channel one — filtration companies

The only segment that has asked us to sell them this. Matter opened its call with it.

| Figure | Value | Grade |
|---|---|---|
| Companies building microfibre filtration worldwide | 20–40 | [A] q26 |
| Instrument price | $25,000 | [A] q23 |
| Units per company | 1–3 | [A] q22 |
| Reachable in 12–18 months | 3–8 customers | [A] |
| **Revenue now** | **$75k–250k** | [A] |
| Ceiling if every company buys 2 units | $1.0M–2.0M one-off | [A] |

Small and immediate. Its real value is not the revenue: it is a customer who already
benchmarks, a hard water sample, and access to the mills they are installing in. The risk is
that they want the sensor inside their product rather than beside it, which caps us as a
component and removes our name from the mill relationship. Settle it early — q24.

---

## 3. Channel two — brands

Brands do not buy the box. They buy the programme, and they mandate the box.

| Figure | Value | Grade |
|---|---|---|
| ZDHC signatory brands (64 signatory + 22 friend) | 86 | [S] |
| Brands that worked with the efficiency programme in 2025 | 78 | [S] |
| Cascale corporate full members | 195 | [S] |
| Microfibre consortium organisations (brand/supplier split unpublished) | 100+ | [S] |
| Brands with a *funded* microfibre programme | 20–50 | [A] |
| Programme price per brand per year | $50k–150k | [A] q18 |
| **Channel revenue at maturity** | **$1.0M–7.5M/yr** | [A] |

The $50k–150k is built, not sourced. Its two anchors: a brand running this work in house
pays roughly €60k–100k a year of loaded specialist cost (adidas has a full-time microfibre
lead who runs the FTIR herself, about one day per sample) [S], and European sustainability
reporting costs a company about €106,000 a year with another €24k–42k answering ESG
questionnaires [S]. Question 18 replaces this guess with a number.

Two brand positions on record, which is why the funded-programme count is the constraint:
H&M will not specify a measurement before regulation exists [S]; adidas chaired a twenty-brand
discussion on getting microfibre solutions into plants [S].

---

## 4. Channel three — mills

The volume market. No rule requires a mill to measure fibre, so this channel opens on
mandate first and on process value second.

### The populations

| Population | Count | Grade |
|---|---|---|
| Mills publishing wastewater test reports to ZDHC | ~2,450 | [S] |
| Sites a brand could plausibly mandate today | 2,400–3,700 | [S] |
| Facilities active in efficiency programmes, 2025 | 473 | [S] |
| Suppliers registered on ZDHC (organisation's own figures conflict: 3,712 in the 2025 report, 12,972 in the 2024 report — cite one, never average) | 3,712 / 12,972 | [S] |
| Facilities that have done a Higg FEM assessment | 18,000 | [S] |
| Documented wet-processing sites worldwide (EU ~10,000, China 1,804, Vietnam ~1,335, US 570, Bangladesh ~600, Pakistan ~360, Indian clusters ~2,500) | ~16,000 floor | [S] |
| True global figure, including India nationally, Türkiye and Indonesia | 25,000–45,000 | [A] q27 |

Wet-process suppliers per large brand, from published lists: adidas 138, Inditex 269 (476 if
finishing counts), Fast Retailing 108, C&A 104, Levi's 80+ [S]. Average about 140. Disclosure
understates it — PVH publishes 177 against a stated base of 1,853 [S].

### The revenue, by product stage

| Stage | Price basis | 2,400–3,700 sites | 16,000 sites |
|---|---|---|---|
| Identification, one point | $15k + $3k/yr [A] q34 | $36M–55M + $7M–11M/yr | $240M + $48M/yr |
| Multi-analyte, 3–5 points | $45k–75k/site [A] | $110M–275M | $720M–1.2B |
| Efficiency share | 5–10% of savings [A] q35 | $26M–175M/yr | $176M–1.17B/yr |

The efficiency row rests on sourced savings: an efficiency programme delivers $230,000–730,000
a year per mill for $110,000–300,000 of capital, paying back in 3–10 months [S]. The best
single result was $910,000 a year for $78,000 [S]. Anything sold to a mill competes with that
hurdle rate.

### What a mill spends today

| Line | Amount | Grade |
|---|---|---|
| All environmental platforms and schemes combined | $2,000–5,000/yr | [S] |
| Lab identification of microplastics | €190–390/sample, 3–4 weeks | [S] |
| ZDHC wastewater testing cadence | 2 samples/yr, price unpublished anywhere | [S] q8 |
| Effluent plant operating cost (Bangladesh mean) | ~$174,000/yr | [S] |
| Cost of poor right-first-time, 1,000 t/yr mill | ~$91,000/yr (2005) | [S] |
| Re-shaded / re-dyed share of production | ~20% / ~10% (2005) | [S] |

The compliance budget is $2k–5k. The waste is $230k–910k. Selling into the first is selling
into a rounding error; the second is not yet a purchased line item. That gap is the whole
commercial problem.

---

## 5. The staged product behind the channels

Each stage is what unlocks the next channel. The mills channel is not a third sales motion to
run now — it is the payoff for the tech work done while channels one and two pay.

1. **Identification.** Polymer type and count, one point, minutes instead of a lab's 3–4
   weeks or a specialist's day. Sells to filtration companies and funded brand programmes.
2. **Attribution.** Several points, so type maps to step, machine or fabric. Risk: if streams
   merge before the drain, attribution needs machine-level sampling and the hardware per site
   multiplies.
3. **Multi-analyte.** Peroxide, unfixed dye, salt and turbidity on the same optical path.
   These are things mills already check by hand, so it moves us into an existing quality
   budget rather than a new line.
4. **Control.** Close the loop on one decision. Rinse endpoint is the candidate: it is hot
   water straight off the fuel bill and it can be verified in a week.
5. **Optimisation.** Dosing and recipe control against right-first-time. The published
   analogue — automated chemical dosing — cut chemical cost 11.2% and reworks 17% for
   $150k–890k of capital [S]. We must beat that payback, not match it.
6. **Network.** Verified type data across thousands of sites, sold to brands now and
   regulators later. About 300 brand-side organisations at $30k–100k each [A] gives
   $9M–30M/yr — the smallest layer, not the largest.

---

## 6. Where the money is, in one view

| Horizon | Source | Revenue | Grade |
|---|---|---|---|
| Now (0–18 months) | Filtration companies + first brand programmes | $0.3M–2.5M/yr | [A] |
| Brand channel at maturity | 20–50 funded programmes | $1M–7.5M/yr | [A] |
| Mandated mills, identification only | 2,400–3,700 sites | $36M–55M one-off | [S] population, [A] price |
| All documented wet sites, multi-analyte | 16,000 sites | $720M–1.2B one-off | [A] |
| Efficiency share at scale | 16,000 sites | $176M–1.17B/yr | [A] |

Read down the grade column: the populations are sourced, the prices are not. Every figure
below the third row multiplies two assumptions together and should be treated as a shape, not
a forecast.

---

## 7. Two tailwinds and one wall

**Tailwind — the mandate hook already exists.** The ZDHC wastewater guidelines (v2.2, September
2024) already carry microfibre discharge monitoring, based on suspended solids, with corrective
actions uploaded to their platform [S]. That is live now, not in five years, and it is the
nearest thing to a regulatory pull in this market.

**Tailwind — nobody measures type.** The industry's microfibre test method is gravimetric,
first wash only, and identifies neither fibre nor polymer, across 1,500+ fabrics tested and 60+
accredited laboratories [S]. The whole existing test market is blind to the thing we sell.

**Wall — regulation is three to five years out** on the brand side's own reading [S], and no
rule anywhere requires a mill to measure fibre. Until then every sale is discretionary, which
is why the first two channels are people who already spend money on this question by hand.

---

## 8. Ruled out

**Paper mills.** No rule requires particle or microplastic monitoring and the EU wastewater
directive explicitly excludes them; mills' own treatment already removes >99% of microplastics
and researchers conclude they contribute minimally; their real pain is stickies, which are
defined by tackiness and therefore invisible to optical contrast, with the industry's own
association stating no reliable measurement method exists; inline optical particle counting is
already a sold category there; and white water sits past where turbidity instruments saturate,
so the optics need redesigning rather than recalibrating [S]. Revisit only with a tackiness
measurement, which is a different physical principle.

**Still untested, same three questions:** tanneries, garment laundries, man-made cellulosic
fibre plants, plastics recycling. Is anyone required or paid to know; is what we detect what
they care about; does the water break the optics.
