---
purpose: The process map — one entry per stage of textile manufacturing from raw fibre to finished T-shirt, whether the stage touches water, how much fibre it sheds into that water, what the mill measures there today, and where the water goes.
idea: Microplastic Detection System
title: "Textiles: raw fibre in, T-shirt out"
schema_version: 1
last_updated: 2026-09-11
# ─── Vocabulary (proposed 2026-09-11, awaiting founder confirmation) ─────────────
# `order` is the position in the real process sequence; two lanes (cotton, polyester) run in
# parallel until knitting, `shared` is everything after, `effluent` is the treatment train
# every wet stage drains to. `fibre_release` grades what a stage sheds INTO WATER, from
# published measurements where they exist; a dry stage that creates loose fibre washed out
# later is graded low here and says so in release_mechanism.
map_vocabularies:
  phase: [fibre, yarn, fabric, pretreatment, dyeing, finishing, garment, effluent]
  lane: [cotton, polyester, shared, effluent]
  wet_or_dry: [dry, wet, rinse_only]
  fibre_release: [none, low, medium, high]
  fibre_created: [none, low, medium, high]
map_value_labels:
  phase: {fibre: "Fibre", yarn: "Yarn", fabric: "Fabric", pretreatment: "Pretreatment", dyeing: "Dyeing", finishing: "Finishing", garment: "Garment", effluent: "Effluent treatment"}
  lane: {cotton: "cotton", polyester: "polyester", shared: "shared", effluent: "effluent"}
  wet_or_dry: {dry: "dry", wet: "wet", rinse_only: "rinse only"}
  fibre_release: {none: "none", low: "low", medium: "medium", high: "high"}
  fibre_created: {none: "none", low: "low", medium: "medium", high: "high"}
map_phase_notes:
  fibre: "Where the raw material comes from. Cotton is ginned from the boll; polyester is polymerised from PTA and MEG (or recycled PET) and melt-spun into filament or cut into staple."
  yarn: "Loose fibre becomes yarn. Dry, mechanical, and the source of most of the fly and loose fibre that later washes out."
  fabric: "Yarn becomes fabric. T-shirts are circular-knit jersey; knitting oil goes on here and has to come off in scouring."
  pretreatment: "The first wet contact. Oils, waxes and sizing come off, the fabric is bleached, and cotton may be mercerised; polyester is heat-set dry."
  dyeing: "Colour goes in. Jet or soft-flow machines tumble the fabric in hot liquor for hours, then rinse and soap it; the largest share of wet-process fibre release measured."
  finishing: "Hand, softness and shape. Padding of softeners and resins, stenter drying, compacting; brushing, sueding and enzyme washes deliberately remove or raise fibre."
  garment: "Cut, sew, print, wash, pack. Mostly dry; printing and garment washing are the wet exceptions."
  effluent: "Where every wet stage's water ends up before it leaves the site."
---

# Process map — textiles, raw fibre to T-shirt

Written 2026-09-11 from one desk batch. Water figures marked BAT are yearly-average indicative
levels from the EU Textiles BAT Conclusions (Decision 2022/2508, Table 1.1; m³/t equals L/kg);
figures marked Shibly are metered batches in a Bangladesh knit dye house on 1:7 liquor-ratio
machines (each fill about 4 L/kg, first fill about 7, a 10-minute overflow rinse about 19). The
`water_l_per_kg` number on each stage is one representative figure for the diagram; the range
and its source sit in `water_note`. Stages graded from one or two papers say so in
`release_evidence`. Two claims from earlier notes did not survive checking and are recorded as
such: the "1.39 million fibres/L screen-printing" figure has no locatable source, and the
"cutting, tumbling, sueding 5-30×" numbers belong to two different Cai papers (2020 and 2021).

## Ginning

id: P1
order: 1
phase: fibre
lane: cotton
short: Ginning
what_happens: >
  Seed cotton goes in; saw or roller gins strip the lint from the seed and lint cleaners remove
  trash. Out come lint bales of about 225 kg plus seed and motes.
machines: [saw gins, lint cleaners]
vendors:
  - {name: Lummus, url: ""}
  - {name: Continental Eagle, url: ""}
wet_or_dry: dry
water_l_per_kg: 0
chemicals: [none (moisture conditioning only)]
fibre_release: none
fibre_created: low
release_mechanism: Dry; creates cotton dust and short fibre, all to air and solid waste, not water.
release_evidence: none found
measured_today: bale moisture, trash, HVI fibre length, strength and micronaire
fibre_measured_today: false
drain: none
sensor_note: Nothing to see; no water.
sources: []
first_added: 2026-09-11

## Cotton spinning

id: P2
order: 2
phase: yarn
lane: cotton
short: Spinning
what_happens: >
  Bales are opened, cleaned, carded into a sliver, doubled, drafted and twisted into yarn on ring,
  rotor or air-jet frames, then wound to cones. Blends with polyester staple are made at the
  blowroom or draw frame.
machines: [blowroom, card, draw frame, comber, roving frame, ring / rotor / air-jet spinning frame, winder]
vendors:
  - {name: Trützschler, url: https://www.truetzschler.com/en/spinning/products/card/}
  - {name: Rieter, url: https://www.rieter.com/products/systems/ring-spinning-machines}
wet_or_dry: dry
water_l_per_kg: 0
water_note: humidification air only
chemicals: [none on cotton, spin finish already on polyester staple]
fibre_release: low
fibre_created: high
release_mechanism: >
  Heavy fly and short-fibre generation, captured by filters and air; the loose fibre that stays
  in the yarn washes out at first wet contact. Rotor yarn carries about twenty times the
  extractable fragments of ring yarn.
release_evidence: "Cai 2020 (J Cleaner Prod): rotor yarn 4,310 fragments per gram vs 160-230 for other yarns; filament 15 per gram."
measured_today: yarn count, evenness (Uster), hairiness, imperfections, strength
fibre_measured_today: false
drain: none
sensor_note: No water, but yarn type (rotor vs ring, hairiness) is a strong upstream predictor of what a downstream sensor will see.
sources:
  - https://doi.org/10.1016/j.jclepro.2020.121970
first_added: 2026-09-11

## Polyester melt spinning and texturing

id: P3
order: 3
phase: fibre
lane: polyester
short: PET melt spinning
what_happens: >
  Dried PET chips (virgin, or recycled pellets from bottle flake) are melted, extruded through
  spinnerets, quenched, spin-finished and wound as filament, then draw-textured, or cut to staple
  for blending with cotton. Recycled PET is about 12% of polyester and nearly all of it is
  bottle-derived.
machines: [POY / FDY filament lines, draw-texturing machines, staple lines]
vendors:
  - {name: Oerlikon Barmag, url: https://www.barmag.com/en/}
wet_or_dry: dry
water_l_per_kg: 
water_note: unknown at the fibre plant; outside the textile BAT scope
chemicals: [spin finish (oils, antistats), TiO2 delustrant, oligomers]
fibre_release: none
fibre_created: none
release_mechanism: Continuous filament sheds almost nothing; staple cutting creates ends but dry. Filament carries 15 extractable fragments per gram, the lowest of 18 products tested.
release_evidence: "Cai 2020: filament 15 fragments per gram."
measured_today: denier, tenacity, elongation, dye uptake, oligomer, intrinsic viscosity
fibre_measured_today: false
drain: none in the textile mill; the fibre plant has its own
sensor_note: Not a sensor site; spin finish and oligomer are washed off later in scouring and heat-setting.
sources:
  - https://www.textileexchange.org/knowledge-center/reports/materials-market-report-2025/
  - https://doi.org/10.1016/j.jclepro.2020.121970
first_added: 2026-09-11

## Circular knitting

id: P4
order: 4
phase: fabric
lane: shared
short: Knitting
what_happens: >
  Cones of cotton, polyester or blended yarn feed a circular machine that loops them into
  tubular greige fabric (single jersey, rib, interlock). Needles and sinkers run in knitting
  oil, and lint is blown off continuously.
machines: [circular knitting machines]
vendors:
  - {name: Mayer & Cie, url: https://www.mayercie.com/en/products/circular-knitting-machines}
  - {name: Terrot, url: ""}
  - {name: Pai Lung, url: ""}
wet_or_dry: dry
water_l_per_kg: 0
chemicals: [knitting oil (water-emulsifiable), wax on yarn]
fibre_release: low
fibre_created: high
release_mechanism: Needle abrasion frees fibre and creates fly; it is trapped in the oily fabric and released at the first wet bath.
release_evidence: "Badruddin 2026: dry-processing average about 700 fibres per gram across dry stages; Wang 2023 flags knit structure as a lever."
measured_today: GSM, courses and wales, faults, oil %, width
fibre_measured_today: false
drain: none
sensor_note: Dry; the oil and lint carried in greige fabric define the load the first wet drain will show.
sources:
  - https://doi.org/10.1093/etojnl/vgag200
  - https://doi.org/10.1021/acs.est.3c06210
first_added: 2026-09-11

## Pre-heat-setting (polyester and blends)

id: P5
order: 5
phase: pretreatment
lane: polyester
short: Heat-setting
what_happens: >
  Greige polyester knit runs open-width through a stenter at 180-200 °C for 30-60 s to fix
  stitch geometry and stop shrinkage and crease marks in the jet. Spin finish and oligomer
  volatilise to the exhaust. Optional; can also be done after dyeing.
machines: [stenter]
vendors:
  - {name: Brückner, url: https://www.brueckner-textile.com/en/products/stenters.html}
  - {name: Monforts, url: https://www.monforts.de/en/products/stenters/}
wet_or_dry: dry
water_l_per_kg: 0
chemicals: [none; exhaust air carries oil aerosol]
fibre_release: none
fibre_created: none
release_mechanism: Thermal only; no abrasion.
release_evidence: none found
measured_today: width, shrinkage, oven temperature, dwell
fibre_measured_today: false
drain: none (exhaust scrubber water if fitted)
sensor_note: Not a sensor site.
sources:
  - https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022D2508
first_added: 2026-09-11

## Scouring

id: P6
order: 6
phase: pretreatment
lane: shared
short: Scouring
what_happens: >
  The knit tube is loaded into a jet or soft-flow machine and boiled at about 98 °C for about
  50 minutes in caustic, wetting agent and sequestrant; for knits scouring and bleaching are
  usually one combined bath. Out come knitting oil, waxes, pectin, dirt, and the loose fibre
  from spinning and knitting.
machines: [jet / soft-flow / airflow dyeing machine, spun-oil washer for polyester]
vendors:
  - {name: Thies, url: https://www.thiestextilmaschinen.com/product-portfolio/fabric-dyeing/}
  - {name: Fong's (THEN Smartflow), url: https://www.fongs.eu/solutions/cellulosic-fibres-knitwear/tsf-1/}
  - {name: Goller Sintensa, url: https://www.fongs.eu/solutions/synthetic-fibres-knitwear-pes-pa-etc/goller-sintensa-spun-oil-washing-example/}
wet_or_dry: wet
water_l_per_kg: 10
water_note: "BAT: scouring batch 5-15; combined scour-bleach-desize 9-20; washing of synthetics 5-20. Shibly: first fill about 7 L/kg plus hot wash about 4. Older literature 10-80 L/kg."
chemicals: [NaOH, non-ionic or anionic surfactant, sequestrant, H2O2 and stabiliser if combined]
fibre_release: high
fibre_created: low
release_mechanism: >
  First wet contact. Hot alkali and 60-100 minutes of rope circulation through the nozzle wash
  out every loose fibre created in spinning, knitting and cutting.
release_evidence: "No scouring-only number found. Badruddin 2026: wet stages average about 1,300 fibres per gram vs about 700 for dry."
measured_today: absorbency (drop test), residual oil, pH, whiteness after bleach
fibre_measured_today: false
drain: machine drain, sometimes via hot-water recovery, to the equalisation tank
sensor_note: >
  Highest expected fibre load of any drain, but the worst matrix: about 95 °C, pH 12-13,
  emulsified oil and foam. A sensor here must survive caustic and grease.
sources:
  - https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022D2508
  - https://doi.org/10.15406/jteft.2020.06.00232
  - https://doi.org/10.1093/etojnl/vgag200
first_added: 2026-09-11

## Peroxide bleaching and peroxide kill

id: P7
order: 7
phase: pretreatment
lane: cotton
short: Bleaching
what_happens: >
  Alkaline hydrogen peroxide at about 98 °C whitens cotton (needed for whites and pale shades;
  polyester is not bleached). The bath is dropped, rinsed hot, then a peroxide-killer bath
  (catalase enzyme or a reducing agent at 55-65 °C) removes residual peroxide before reactive
  dyeing.
machines: [the same jet / soft-flow machine as scouring]
vendors: []
wet_or_dry: wet
water_l_per_kg: 15
water_note: "BAT: bleaching batch 10-32, continuous 3-8. Shibly: kill bath about 4 L/kg plus hot wash about 4."
chemicals: [H2O2, NaOH, stabiliser (silicate or organic), catalase or sodium bisulphite, optical brightener for whites]
fibre_release: medium
fibre_created: low
release_mechanism: Continued rope circulation and nozzle shear on already-clean fabric; the oxidative bath weakens surface fibre ends.
release_evidence: none stage-specific found
measured_today: whiteness (CIE), residual peroxide (test strip), pH
fibre_measured_today: false
drain: machine drain to equalisation
sensor_note: Still about 90 °C and alkaline; residual peroxide attacks optics and electrodes unless the sensor sits after the kill bath.
sources:
  - https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022D2508
  - https://doi.org/10.15406/jteft.2020.06.00232
first_added: 2026-09-11

## Mercerising (optional)

id: P8
order: 8
phase: pretreatment
lane: cotton
short: Mercerising
what_happens: >
  Fabric runs open-width or tubular under tension through 20-25% caustic soda for 30-60 s, then
  is washed counter-current to strip the caustic; lustre, strength and dye yield rise. Most
  T-shirt mills skip it.
machines: [tubular or open-width merceriser, caustic recovery evaporator]
vendors:
  - {name: Dornier, url: ""}
  - {name: Lafer (liquid-ammonia alternative), url: https://www.laferspa.com/en/liquid-ammonia-mercerizing}
wet_or_dry: wet
water_l_per_kg: 8
water_note: "BAT: 2-13"
chemicals: [NaOH 250-300 g/L, wetting agent, acid for neutralisation]
fibre_release: low
fibre_created: none
release_mechanism: Little mechanical action; the wash-off water passes screens or microfiltration before caustic evaporation, which itself removes fibre.
release_evidence: none found
measured_today: barium activity number, residual alkali, caustic concentration
fibre_measured_today: false
drain: wash water to caustic recovery (75-95% recovered), residual to equalisation
sensor_note: Concentrated caustic; not a sensor site.
sources:
  - https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022D2508
first_added: 2026-09-11

## Enzyme bio-polishing

id: P9
order: 9
phase: pretreatment
lane: cotton
short: Bio-polishing
what_happens: >
  A cellulase bath at about 55 °C for about 60 minutes hydrolyses protruding cotton fibre ends;
  the jet's nozzle shear knocks the weakened fuzz off, giving a clean, pill-resistant face.
  Increasingly combined with the peroxide-kill bath.
machines: [the same dyeing machine]
vendors: []
wet_or_dry: wet
water_l_per_kg: 8
water_note: "Shibly: enzyme bath about 4 L/kg plus normal wash about 4."
chemicals: [acid cellulase, acetic acid or buffer to pH 4.5-5.5, non-ionic wetter]
fibre_release: high
fibre_created: high
release_mechanism: This stage exists to remove surface fibre into the water, by enzymatic cutting plus abrasion. No published count found; graded high from what the step is for.
release_evidence: unknown; no stage-specific study located
measured_today: weight loss (1-3%), pilling grade, strength loss, pH, temperature
fibre_measured_today: false
drain: machine drain to equalisation
sensor_note: >
  Cotton fibre (not plastic), mildly acidic, 55 °C: chemically the gentlest wet drain and
  probably the fibre-richest per litre on a cotton line. A good calibration point, and the
  control that shows what a sensor does with non-plastic fibre.
sources:
  - https://doi.org/10.15406/jteft.2020.06.00232
first_added: 2026-09-11

## Exhaust dyeing

id: P10
order: 10
phase: dyeing
lane: shared
short: Dyeing
what_happens: >
  Fabric ropes circulate through a nozzle for 1-4 hours while dye and auxiliaries are dosed.
  Cotton takes reactive dyes at 60 °C with 40-80 g/L salt then soda ash, and classical reactive
  dyes fix only 60-70%, so 30-40% goes to drain. Polyester takes disperse dyes at 130 °C under
  pressure, then a reduction clear. Blends run two baths or one bath in two steps. Some cotton
  knits are pad-batch dyed instead.
machines: [jet / soft-flow / airflow dyeing machine]
vendors:
  - {name: Thies (iMaster H2O, Luft-roto), url: https://www.thiestextilmaschinen.com/product-portfolio/fabric-dyeing/luft-roto-plus-sii-family/}
  - {name: Fong's (THEN Smartflow, Supratec LTM), url: https://www.fongs.eu/solutions/synthetic-fibres-knitwear-pes-pa-etc/ltm/}
  - {name: "Tong Geng, Dilmenler (common in Bangladesh)", url: ""}
wet_or_dry: wet
water_l_per_kg: 8
water_note: "BAT: batch dyeing of fabric 10-150 for the whole cycle. Shibly: the dye bath alone is about 4 L/kg per fill at 1:7; the whole scour-to-unload cycle is 60 L/kg for a light shade and 81 for a deep one, most of it rinses (see the next stage)."
chemicals: [reactive or disperse dyes, NaCl or Na2SO4, Na2CO3, levelling or dispersing agents, acetic acid, hydrosulphite]
fibre_release: high
fibre_created: medium
release_mechanism: >
  The longest mechanical exposure of the whole route: hours of nozzle shear and rope-to-rope
  rubbing at high temperature, while alkali and heat swell cotton and soften polyester.
release_evidence: "Wang 2023: dyeing is 95% of wet-process release; release falls with white shades, lower temperature and shorter time. Badruddin 2026: dyeing about 800 fibres per gram, the largest stage. Zhou 2020: up to 54,100 fibres/L in printing-and-dyeing wastewater. Zhu 2025: three printing-and-dyeing lines were the plant's source."
measured_today: shade (spectrophotometer, delta E), pH, conductivity or salt, temperature profile, bath exhaustion; nothing fibre-related
fibre_measured_today: false
drain: machine drain to equalisation, hot drops sometimes through a heat exchanger
sensor_note: >
  Fibre-rich but dye-coloured, 60-130 °C, salt to 80 g/L, foam. The dye-bath drop is the
  hardest sample of all; the rinse drops that follow are easier and still fibre-rich.
sources:
  - https://doi.org/10.1021/acs.est.3c06210
  - https://doi.org/10.1093/etojnl/vgag200
  - https://doi.org/10.1016/j.scitotenv.2020.140329
  - https://doi.org/10.3390/w17040574
  - https://doi.org/10.15406/jteft.2020.06.00232
first_added: 2026-09-11

## Post-dye rinsing and soaping

id: P11
order: 11
phase: dyeing
lane: shared
short: Rinsing & soaping
what_happens: >
  Five to ten sequential fill-and-drop baths: cold rinse, acid neutralise, 90 °C soaping to
  strip unfixed dye, hot and cold washes, until the water runs clear (plus a reduction clear
  for polyester). This is where most of the cycle's water goes.
machines: [the same dyeing machine]
vendors: []
wet_or_dry: rinse_only
water_l_per_kg: 50
water_note: "Shibly: 5-10 baths at about 4 L/kg each plus overflow rinses at about 19 L/kg each; 6 of 9 baths (light shade) and 8 of 10 (deep) are rinses. 50 is the balance of the 60-81 L/kg cycle after the dye bath."
chemicals: [acetic acid, soaping agent, NaOH and hydrosulphite for polyester, residual dye and salt]
fibre_release: medium
fibre_created: low
release_mechanism: Fibre freed during dyeing keeps washing out; hot soaping adds further shear time.
release_evidence: none stage-specific; the Badruddin 2026 wet average applies
measured_today: wash-fastness, pH of the final bath, colour of the drop water by eye
fibre_measured_today: false
drain: machine drain to equalisation; counter-current or last-rinse reuse in better mills
sensor_note: >
  Later rinses are cool, near-neutral, lightly coloured, low foam: the cleanest matrix that
  still carries the dye-stage fibre, one drain per machine, batch-discharged, so a count per
  drop maps to a batch and a recipe. Prime candidate.
sources:
  - https://doi.org/10.15406/jteft.2020.06.00232
  - https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022D2508
first_added: 2026-09-11

## Dewatering and softener padding

id: P12
order: 12
phase: finishing
lane: shared
short: Softener padding
what_happens: >
  The wet rope is opened, slit (or kept tubular), squeezed to 60-80% pick-up and padded with
  softener or resin from a trough; alternatively softener is exhausted in the last dye-machine
  bath. Out comes damp, chemically loaded fabric ready for the dryer.
machines: [squeezer or balloon padder, slitter, padding trough]
vendors:
  - {name: Santex Rimar (Sperotto Rimar Compas), url: https://www.santexrimar.com/brands/sperotto-rimar/machinery/compas/}
  - {name: Monforts padders, url: https://www.monforts.de/en/products/dyeing-ranges/}
wet_or_dry: wet
water_l_per_kg: 1
water_note: unknown; trough make-up only, of the order of 1 L/kg
chemicals: [cationic or silicone softeners, wetting agent, acetic acid, resin and catalyst on some]
fibre_release: medium
fibre_created: low
release_mechanism: Squeeze rolls and nip pressure strip loose fibre into the trough and the squeezed-out liquor.
release_evidence: "Akyildiz 2024: the drain at the exit of a softening machine carried 0.058-0.251 g/L of microfibre (acrylic and cotton), the only machine-exit measurement found."
measured_today: pick-up %, trough pH and concentration, hand-feel
fibre_measured_today: false
drain: squeeze liquor and trough dumps to equalisation
sensor_note: Low volume, high fibre mass per litre, near-neutral, about 40 °C; silicone emulsion may film optics.
sources:
  - https://doi.org/10.2339/politeknik.1310805
first_added: 2026-09-11

## Stenter drying and final heat-setting

id: P13
order: 13
phase: finishing
lane: shared
short: Stenter drying
what_happens: >
  Fabric is pinned or clipped and dried at 120-160 °C (or heat-set at 180-200 °C for polyester);
  width and GSM are set and the softener cures. Relaxation dryers tumble tubular cotton knits
  loosely to pre-shrink them.
machines: [stenter, relaxation dryer]
vendors:
  - {name: Brückner, url: https://www.brueckner-textile.com/en/products/relaxation-dryers.html}
  - {name: Monforts, url: https://www.monforts.de/en/products/relaxation-dryers/}
  - {name: Santex Rimar (Santashrink), url: https://www.santexrimar.com/}
wet_or_dry: dry
water_l_per_kg: 0
chemicals: [none new; softener and resin cure, exhaust fumes]
fibre_release: none
fibre_created: low
release_mechanism: Fly to exhaust filters only.
release_evidence: none found
measured_today: width, GSM, residual moisture, shrinkage, exhaust temperature
fibre_measured_today: false
drain: none (exhaust scrubber if fitted)
sensor_note: Not a sensor site.
sources: []
first_added: 2026-09-11

## Compacting

id: P14
order: 14
phase: finishing
lane: shared
short: Compacting
what_happens: >
  Steamed fabric is over-fed into a felt or shoe compactor that mechanically shrinks it
  lengthwise to the residual-shrinkage spec (5% or less) and calenders it flat. Out comes
  finished roll fabric.
machines: [tubular or open-width felt compactor]
vendors:
  - {name: Lafer, url: https://www.laferspa.com/en/tubular-knit-fabric-felt-compacting}
  - {name: Santex Rimar, url: https://www.santexrimar.com/}
  - {name: Tubetex, url: ""}
wet_or_dry: dry
water_l_per_kg: 0
water_note: steam condensate only
chemicals: [none]
fibre_release: none
fibre_created: low
release_mechanism: Felt friction creates lint to the machine housing and later to garment wash if any; not to water here.
release_evidence: none found
measured_today: residual shrinkage, GSM, width, skew
fibre_measured_today: false
drain: condensate
sensor_note: Not a sensor site.
sources: []
first_added: 2026-09-11

## Raising, brushing and sueding (not all T-shirts)

id: P15
order: 15
phase: finishing
lane: shared
short: Raising / sueding
what_happens: >
  Wire rollers or abrasive sleeves tear fibre ends out of the fabric face to make a nap (fleece,
  peach-skin); shearing then trims it. Almost all this fibre goes to dust extraction, but the
  fabric carries a fibril-rich surface into every later wash.
machines: [sueding machine, raising machine, shearing machine]
vendors:
  - {name: Lafer, url: https://www.laferspa.com/en/sueding-machines-knitted-woven-fabrics}
wet_or_dry: dry
water_l_per_kg: 0
chemicals: [none]
fibre_release: low
fibre_created: high
release_mechanism: >
  Deliberate abrasion. Processed-surface fabrics carry five times the extractable fragments;
  abrasion multiplies fragments 5-30 times and fibrils (2-5 µm wide, 30-150 µm long) more than
  200 times. The dominant creator of fibre released downstream.
release_evidence: "Cai 2020 (J Cleaner Prod) and Cai 2021 (Environ Sci Technol)."
measured_today: pile height, hand, weight loss, pilling grade
fibre_measured_today: false
drain: none (dust collectors)
sensor_note: Dry; but if a mill sueds before garment wash, that wash drain is the place to look.
sources:
  - https://doi.org/10.1016/j.jclepro.2020.121970
  - https://doi.org/10.1021/acs.est.1c00650
first_added: 2026-09-11

## Cutting and sewing

id: P16
order: 16
phase: garment
lane: shared
short: Cut & sew
what_happens: >
  Fabric is spread in plies and cut by straight-knife, band-knife or automatic cutter; panels
  are overlocked and cover-stitched into T-shirts; loose threads are trimmed.
machines: [automatic cutter, straight-knife cutter, overlock and cover-stitch machines]
vendors:
  - {name: "Gerber / Lectra (cutters)", url: ""}
  - {name: "Juki, Brother, Pegasus (sewing)", url: ""}
wet_or_dry: dry
water_l_per_kg: 0
chemicals: [none; sewing thread lubricant]
fibre_release: low
fibre_created: high
release_mechanism: >
  Cut edges and needle penetration. Scissor- or knife-cut edges carry 3-31 times the fragments
  of laser-cut edges; a cutting floor sheds 2.9 million fibres per m² per day to the air, and
  one garment can carry a million fibres, about fifty times a laundry cycle.
release_evidence: "Cai 2020; Raja Balasaraswathi and Rathinamoorthy 2025 (Emerging Contaminants)."
measured_today: measurement to spec, seam strength, defects; nothing fibre-related
fibre_measured_today: false
drain: none
sensor_note: Dry; the release shows up in garment wash or the consumer's first wash.
sources:
  - https://doi.org/10.1016/j.jclepro.2020.121970
  - https://doi.org/10.1016/j.emcon.2025.100559
first_added: 2026-09-11

## Printing

id: P17
order: 17
phase: garment
lane: shared
short: Printing
what_happens: >
  Pigment paste is screened onto fabric or garment and cured dry; reactive or disperse prints
  need steaming and a wash-off line to remove thickener and unfixed dye. Direct-to-garment
  printers lay pre-treatment and water-based ink on finished T-shirts and cure with heat;
  screens and squeegees are washed between jobs.
machines: [rotary or flat screen press, carousel garment press, DTG printer, print wash-off range]
vendors:
  - {name: "MHM, M&R (carousels)", url: ""}
  - {name: Kornit (DTG), url: https://www.kornit.com/printer/kornit-atlas-max-plus/}
  - {name: Goller Print Wash, url: https://www.fongs.eu/solutions/cellulosic-fibres-knitwear/goller-print-wash/}
wet_or_dry: wet
water_l_per_kg: 10
water_note: "unknown for garments; a print wash-off range is comparable to continuous washing (BAT 5-20 L/kg for synthetics); pigment and DTG printing are dry apart from screen washing"
chemicals: [pigment binder, urea, alginate or synthetic thickener, reactive or disperse dyes, cationic DTG pre-treatment, screen-wash solvents]
fibre_release: medium
fibre_created: low
release_mechanism: Wash-off ranges scrub the printed face; screen washing rinses fibre off screens and pallets.
release_evidence: "The '1.39 million fibres/L' screen-printing figure could not be sourced and is unverified. Zhou 2020 and Zhu 2025 bundle printing with dyeing lines."
measured_today: print registration, colour, wash-fastness, cure temperature
fibre_measured_today: false
drain: wash-off range and screen-wash sink to equalisation
sensor_note: Screen-wash sinks are intermittent, low-flow and thickener-laden; a print wash-off range is continuous and cool, so feasible.
sources:
  - https://doi.org/10.1016/j.scitotenv.2020.140329
  - https://doi.org/10.3390/w17040574
first_added: 2026-09-11

## Garment wash and garment dye (where used)

id: P18
order: 18
phase: garment
lane: shared
short: Garment wash
what_happens: >
  Finished T-shirts tumble in a front-loading drum washer with enzyme, silicone softener or
  dye for 30-60 minutes at 40-60 °C, then are hydro-extracted and tumble-dried. Used for
  vintage looks, garment-dyed colours and softness.
machines: [industrial drum washer, hydro-extractor, tumble dryer]
vendors:
  - {name: Tonello, url: https://tonello.com/en/products/}
  - {name: Jeanologia (laser, ozone), url: ""}
wet_or_dry: wet
water_l_per_kg: 
water_note: unknown from primary sources; garment washers typically run 1:5-1:10 per bath over several baths
chemicals: [cellulase, silicone softener, reactive or pigment dyes, salt, soda ash, acetic acid]
fibre_release: high
fibre_created: medium
release_mechanism: >
  Drum tumbling of cut, sewn and possibly sueded garments; every edge and seam abrades. This is
  functionally the garment's first laundry, at 25-50 times the release of a consumer wash.
release_evidence: "Wang 2023; Raja Balasaraswathi and Rathinamoorthy 2025."
measured_today: shade, hand-feel, shrinkage, pH; lint filters emptied by hand
fibre_measured_today: false
drain: washer drain to equalisation, often a separate small treatment plant in garment factories
sensor_note: Moderate temperature, coloured only in dye cycles, silicone can film optics; one drain per machine, batch discharge, easy to instrument.
sources:
  - https://doi.org/10.1021/acs.est.3c06210
  - https://doi.org/10.1016/j.emcon.2025.100559
first_added: 2026-09-11

## Pressing, inspection and packing

id: P19
order: 19
phase: garment
lane: shared
short: Press & pack
what_happens: Garments are steam-pressed, inspected, folded, bagged and cartoned.
machines: [steam press, tunnel finisher]
vendors: []
wet_or_dry: dry
water_l_per_kg: 0
chemicals: [none]
fibre_release: none
fibre_created: none
release_mechanism: none
release_evidence: n/a
measured_today: AQL inspection
fibre_measured_today: false
drain: none
sensor_note: Not a sensor site.
sources: []
first_added: 2026-09-11

## Effluent: screening, equalisation, coagulation and primary settling

id: P20
order: 20
phase: effluent
lane: effluent
short: Equalisation
what_happens: >
  All machine drains combine in a bar-screened sump and an equalisation tank with hours of
  retention that averages temperature, pH and colour; alum, ferric or polymer is dosed and
  flocs settle or are floated off.
machines: [bar screen, equalisation tank, dissolved-air flotation, lamella clarifier]
vendors: []
wet_or_dry: wet
water_l_per_kg: 
water_note: "whole-mill totals: EU BAT indicative sum for a knit dye house about 20-60 L/kg at best practice; Bangladesh metered 60-81 L/kg on the dye machine alone (Shibly); older winch mills 100-450 L/kg"
chemicals: [alum or FeCl3, polyelectrolyte, lime or acid for pH]
fibre_release: none
fibre_created: none
release_mechanism: "A removal stage: primary settling captures 38.8% of particles (Prantor 2026); coagulation and sedimentation was the single most effective stage for PET (Zhu 2025)."
release_evidence: "Prantor 2026; Zhu 2025."
measured_today: flow, pH, temperature, TSS, COD, colour; online pH and flow are common, TSS by grab or online turbidity; TMC/ZDHC found TSS correlates with microfibre concentration
fibre_measured_today: false
drain: to the biological stage
sensor_note: >
  The equalisation outlet is the most stable matrix in the mill (35-40 °C, pH 7-9, blended
  colour) and the only point that integrates all stages, but concentrations are diluted 5-50
  times against a machine drain (54,100 fibres/L raw vs 334-1,730 at plant inlets). A
  compliance sensor, not a process sensor.
sources:
  - https://www.microfibreconsortium.com/manufacturing
  - https://doi.org/10.1016/j.scitotenv.2020.140329
  - https://doi.org/10.2166/wst.2018.476
  - https://doi.org/10.1016/j.jes.2026.03.002
  - https://doi.org/10.3390/w17040574
first_added: 2026-09-11

## Effluent: biological treatment and secondary clarifier

id: P21
order: 21
phase: effluent
lane: effluent
short: Biological
what_happens: >
  Bacteria consume dissolved organics and partly decolourise; fibres are enmeshed in
  biological floc and settle with the sludge.
machines: [anaerobic or hydrolysis tank, activated-sludge basin or MBBR, secondary clarifier]
vendors: []
wet_or_dry: wet
water_l_per_kg: 
chemicals: [nutrients (urea, DAP), antifoam]
fibre_release: none
fibre_created: none
release_mechanism: "A removal stage: secondary treatment adds a further 36.8% removal, 71.8% cumulative (Prantor 2026); aerobic tank, sand filter and BAF showed low removal in Zhu 2025."
release_evidence: "Prantor 2026; Zhu 2025."
measured_today: MLSS, dissolved oxygen, SVI, COD and BOD in and out
fibre_measured_today: false
drain: to tertiary or discharge; sludge to thickening
sensor_note: The clarifier outlet is clean and stable but fibre counts are already 70-90% down; good for compliance, poor for process feedback.
sources:
  - https://doi.org/10.1016/j.jes.2026.03.002
  - https://doi.org/10.3390/w17040574
first_added: 2026-09-11

## Effluent: tertiary polishing, discharge and sludge

id: P22
order: 22
phase: effluent
lane: effluent
short: Tertiary
what_happens: >
  Filters and membranes polish suspended solids and colour; zero-liquid-discharge mills push
  RO reject to evaporators. Captured fibres concentrate in dewatered sludge, which goes to
  landfill, incineration or brick-making.
machines: [sand or disc filter, ozone or Fenton for colour, UF / RO skid for reuse, filter press]
vendors: []
wet_or_dry: wet
water_l_per_kg: 
chemicals: [ozone, H2O2 and iron, antiscalant, polymer for dewatering]
fibre_release: none
fibre_created: none
release_mechanism: "A removal stage: tertiary raises removal to 95.6%, under 28 particles/L (Prantor 2026); 95.1% overall at Xu 2018; over 85% at Zhou 2020 but effluent still 537.5 fibres/L, enriched in small and coloured fibres; 99% by number but only 67.7% by mass at Zhu 2025."
release_evidence: "Prantor 2026; Xu 2018; Zhou 2020; Zhu 2025."
measured_today: TSS, COD, BOD, colour (ADMI or 436/525/620 nm), pH, temperature, flow, plus permit metals and AOX; no fibre parameter anywhere
fibre_measured_today: false
drain: receiving water or reuse; sludge off-site
sensor_note: Final effluent is the regulatory point and where a TSS-correlated fibre reading would first be demanded; concentrations are lowest here.
sources:
  - https://doi.org/10.2166/wst.2018.476
  - https://doi.org/10.1016/j.scitotenv.2020.140329
  - https://doi.org/10.1016/j.jes.2026.03.002
  - https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022D2508
first_added: 2026-09-11

## Mill types, and who owns which stages

Dated 2026-09-11. Not a stage (no `id:`), so the generators skip it.

- **Vertically integrated composite (spinning to garment):** owns every stage 1-22 and one
  effluent plant receives all wet drains, so the sensor buyer and the polluter are the same
  company. Fakir Group, Narayanganj (FKL Spinning, Fakir Knitwears); Yeşim, Bursa (knitting
  115 t/day, dyeing 125 t/day, 400,000 garments/day, five sites).
- **Knit-and-dye fabric mill (stages 4-15):** buys yarn, sells finished fabric to garment
  factories. Tintex, Vila Nova de Cerveira, treating all wastewater on site.
- **Commission dye house (stages 6-13):** dyes customer-owned greige for a fee; common in
  Bursa, Denizli, Vale do Ave and Shaoxing/Keqiao, where the industrial park often runs a
  centralised WWTP (the one Zhou 2020 sampled). Separates the polluter from the treatment owner.
- **Garment factory only (stages 16-19):** has water only if it runs a garment-wash unit.

Where the evidence says a sensor should sit, in order: the dyeing-machine rinse drops (stage
11), not the dye-bath drop; the bio-polishing drop on cotton lines (stage 9); the equalisation
outlet (stage 20) as a compliance point; garment-wash drains (stage 18) where the mill has
them. Avoid the scouring drop (95 °C, pH 13, oil), the dye-bath drop (130 °C, colour, salt),
mercerising (concentrated caustic) and the softener trough (silicone films, tiny volume).
