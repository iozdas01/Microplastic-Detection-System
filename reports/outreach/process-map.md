---
purpose: The wet-process map — one entry per textile wet-processing step and effluent-treatment stage, what enters it (water, chemicals), what leaves it (the wastewater stream), which production data can be joined to it, and where a measurement would have to sit to attribute a contaminant to its source; plus the routes by mill type, how water actually flows, the placement logic, the data model and what the record can evidence for Higg FEM.
idea: Microplastic Detection System
title: "Wet processing: process, water, wastewater, measurement point"
schema_version: 2
last_updated: 2026-09-15
# ─── Vocabulary (founder's structure, 2026-09-15) ────────────────────────────
# `phase` is exactly the founder's four blocks of wet processing; every step files under one.
# `lane` says which routes the step sits on (`all` = every mill type). `fibre_release` keeps the published grading of what a step sheds
# into water; it colours the chips and is the only field carried from the 2026-09-11 map.
map_vocabularies:
  phase: [pretreatment, coloration, finishing, effluent]
  lane: [all, cotton, synthetic, laundry, effluent]
  wet_or_dry: [dry, wet, rinse_only]
  fibre_release: [none, low, medium, high]
  fibre_created: [none, low, medium, high]
map_value_labels:
  phase: {pretreatment: "1. Preparation / pretreatment", coloration: "2. Coloration", finishing: "3. Finishing", effluent: "4. Wastewater treatment (ETP)"}
  lane: {all: "all routes", cotton: "cotton routes", synthetic: "synthetic routes", laundry: "garment laundry / denim", effluent: "effluent"}
  wet_or_dry: {dry: "dry", wet: "wet", rinse_only: "rinse only"}
  fibre_release: {none: "none", low: "low", medium: "medium", high: "high"}
  fibre_created: {none: "none", low: "low", medium: "medium", high: "high"}
map_contaminants:
  fibre_syn:
    label: Synthetic fibre (polyester, polyamide, elastane)
    colour: '#e11d48'
  fibre_cell:
    label: Cellulosic fibre (cotton, viscose)
    colour: '#f472b6'
  fibre:
    label: Fibre, type depends on the route
    colour: '#be185d'
    legend: false
  colour:
    label: Colour and unfixed dye
    colour: '#9333ea'
  salt:
    label: Salt and dissolved solids
    colour: '#0ea5e9'
  organic:
    label: Sizes, oils, waxes, organics
    colour: '#b45309'
  surfactant:
    label: Surfactants and detergents
    colour: '#65a30d'
  polymer:
    label: Resins, binders, silicones
    colour: '#0d9488'
  redox:
    label: Oxidants and reducing agents
    colour: '#d97706'
  alkali:
    label: 'pH load: caustic and acid'
    colour: '#7c3aed'
  solids:
    label: Settled solids and sludge
    colour: '#78716c'
  mixed:
    label: Mixed effluent
    colour: '#94a3b8'
    legend: false
map_routes:
  cotton_knit:
    label: Cotton knit dyehouse
    note: Knits carry no size, so desizing is skipped. Jet or soft-flow machines, batch by batch, rinse-heavy.
  cotton_woven:
    label: Cotton woven mill
    note: Sized warp, so desizing runs. Often open-width and continuous, with less water per kg than knit.
  polyester:
    label: Polyester or synthetic mill
    note: Disperse dyeing at 130 C, then a reduction clear. Heat setting is dry. No mercerizing. This is the route where the
      shed fibre is plastic.
  printing:
    label: Printing house
    note: Print, steam, wash off. Screen and blanket washing is a side stream of events.
  denim_laundry:
    label: Denim mill or garment laundry
    note: Finished garments, not fabric. Highest and most variable fibre load in the industry.
map_nodes:
- id: src-fresh
  label: Fresh water
  kind: source
  col: 0
  slot: 1
  note: Mains, borehole or surface abstraction. Metered per source for FEM water tracking.
- id: src-reuse
  label: Reclaimed water
  kind: source
  col: 0
  slot: 2
  note: Returned from the reuse loop. Whatever it still carries re-enters the process.
- id: hdr-pre
  label: Pretreatment header
  kind: header
  col: 2
  slot: 1
  note: Desize, scour, bleach and mercerizer rinses combine here. Alkaline and organic.
- id: hdr-dye
  label: Dyehouse header
  kind: header
  col: 2
  slot: 2
  note: Every dye machine drain. The largest volume and the largest fibre load in a fabric mill.
- id: hdr-print
  label: Printing header
  kind: header
  col: 2
  slot: 3
  note: Wash-off and screen washing.
- id: hdr-laundry
  label: Laundry header
  kind: header
  col: 2
  slot: 4
  note: Every washer drain in a garment laundry.
- id: hdr-fin
  label: Finishing header
  kind: header
  col: 2
  slot: 5
  note: Trough dumps and washdown. Small volume, high concentration.
- id: caustic-rec
  label: Caustic recovery
  kind: output
  col: 2
  slot: 6
  note: 'Not effluent: the weak caustic is evaporated back to strength and returned to the mercerizer.'
- id: out-discharge
  label: Final discharge
  kind: output
  col: 8
  slot: 1
  note: To sewer or surface water. The permit and ZDHC sample point.
- id: out-reuse
  label: Water back to process
  kind: output
  col: 8
  slot: 2
  note: Reclaimed water returning to the mill.
- id: out-reject
  label: RO reject / ZLD
  kind: output
  col: 8
  slot: 3
  note: To the evaporator and crystalliser, or to disposal.
- id: out-sludge
  label: Sludge
  kind: output
  col: 8
  slot: 4
  note: Where the removed fibre and solids actually end up. Weighed and manifested for FEM.
map_columns:
  '0': Water in
  '1': Process
  '2': Headers
  '3': Equalisation
  '4': Clarifier
  '5': Biological
  '6': Tertiary
  '7': Reuse
  '8': Out
map_fem:
  water-5:
    section: Water
    level: 1
    label: Domestic and production water tracked separately
    needs: Separate tracking records by use category
  water-13:
    section: Water
    level: 2
    label: Water balance identifying which processes use the most
    needs: Water balance report, processes ranked by consumption
  water-15:
    section: Water
    level: 2
    label: Target for increasing reused (grey) water
    needs: Recycling system evaluation and target calculation
  water-19:
    section: Water
    level: 2
    label: Reused water improved against baseline
    needs: Grey water tracking records
  ww-1:
    section: Wastewater
    level: 1
    label: Volume of wastewater discharged is tracked
    needs: Metering records or a stated estimation method
  ww-2:
    section: Wastewater
    level: 1
    label: BOD5 monitoring
    needs: Sampling reports or onsite monitoring records
  ww-3:
    section: Wastewater
    level: 1
    label: No stormwater mixing
    needs: Facility drainage diagram and inspection records
  ww-5:
    section: Wastewater
    level: 1
    label: Treatment plant operates to its design parameters
    needs: Design specs, operating procedures, process monitoring records
  ww-7:
    section: Wastewater
    level: 1
    label: No leaking; flows are known
    needs: Wastewater flow and piping diagram, volume monitoring records
  ww-8:
    section: Wastewater
    level: 1
    label: Sludge sources and solids content
    needs: Sludge inventory and analysis
  ww-9:
    section: Wastewater
    level: 1
    label: Sludge quantity reported
    needs: Tracking records, manifests, weighing records
map_sensor_layers:
  source:
    label: Source layer
    note: 'One high-impact process stream. Highest attribution: batch, recipe, material, machine.'
  treatment:
    label: Treatment layer
    note: ETP influent and across a treatment stage. Shows whether the plant is removing what arrives.
  outcome:
    label: Outcome layer
    note: Final treated effluent plus flow. Strongest link to discharge evidence, weakest to source.
map_phase_notes:
  pretreatment: "Make the greige textile clean and chemically ready. Steps: desizing, scouring, bleaching, mercerizing."
  coloration: "Put colour in and wash the excess out. Steps: dyeing, printing, reduction clearing (polyester), soaping and rinsing, equipment cleaning between shades."
  finishing: "Modify feel, appearance, stability, performance or functionality. Steps: chemical and mechanical finishing; garment laundry and denim wash for garments."
  effluent: "Collect and clean the combined effluent before discharge, reuse or ZLD. Steps: equalisation, clarifier, biological, tertiary and discharge, ZLD and reuse."
---

# Wet-process map

Rewritten 2026-09-15 to the founder's structure; the 2026-09-11 fibre-to-T-shirt lineage
(ginning, spinning, knitting, garment assembly) is retired because dry stages do not drain.
Each stage links the step to its water and chemical inputs, the wastewater it creates, the
production data that can be joined to it, and a candidate measurement point. It is a data-model
placement map, not a sensor specification. Water figures marked BAT are yearly-average
indicative levels from the EU Textiles BAT Conclusions (Decision 2022/2508, Table 1.1; m³/t
equals L/kg); fibre-release grades cite the paper they come from.

Each stage below declares what enters it, the wastewater streams that leave it (`streams:`,
one per drain, with litres per kilogram, what it carries and where it goes), which mill routes
it belongs to (`routes:`), which measurement layer its measurement point would sit in
(`sensor_layer:`), and which Higg FEM questions a measurement there could evidence (`fem:`).
The control room draws the flow map from exactly those fields, so the diagram cannot drift from
this file.

Textile wet processing is four blocks, and every step below files under one of them:

1. **Preparation / pretreatment:** desizing, scouring, bleaching, mercerizing.
2. **Coloration:** dyeing or printing, the polyester reduction clear, soaping and rinsing, machine cleaning between shades.
3. **Finishing:** chemical and mechanical finishing; for garments, laundry and denim wash.
4. **Wastewater treatment (ETP):** equalisation, clarifier, biological, tertiary and discharge, ZLD and reuse.

The route through the blocks differs by material:

- **Woven or knitted fabric mill:** yarn or fabric → pretreatment → dyeing or printing → washing → finishing → ETP.
- **Denim mill:** cotton yarn → indigo dyeing → weaving → washing and finishing → ETP.
- **Garment laundry:** completed garments → desizing, bleaching, enzyme, stone washing, distressing, rinsing, softening → ETP.
- **Yarn-dyeing facility:** yarn → scouring or prewash → dyeing → rinsing and soaping → drying → ETP.
- **Synthetic fabric mill:** polyester or nylon fabric → scouring → heat setting, dyeing → reduction clearing and rinsing → finishing → ETP.

Conventional wet processing uses substantial water, dyestuffs, salts and auxiliaries across
preparation, coloration, washing and finishing, so wastewater carries mixtures of dyes, salts,
surfactants, organics, suspended solids and process-specific residues.

## Desizing

id: P1
order: 1
phase: pretreatment
lane: all
short: Desizing
what_happens: >
  Removes the sizing applied to warp yarn before weaving, usually from the fabric before
  dyeing. Enzymatic or oxidative on continuous ranges or in the same batch machine as scouring.
machines: [desizing range, jigger, batch scour-desize in the dyeing machine]
vendors: []
wet_or_dry: wet
water_l_per_kg: 12
water_note: "BAT: pretreatment of woven fabric 10-40 L/kg for the whole desize-scour-bleach sequence."
inputs: "Water; enzymes or oxidants; wetting agents; detergents."
chemicals: [amylase or oxidant, wetting agent, detergent]
wastewater: "Starch, PVA or CMC sizes, waxes, suspended solids, high organic load (a large share of the pretreatment COD)."
data_link: "Fabric construction, sizing type, batch, recipe, machine."
measurement_point: "Desize-machine drain; combined pretreatment drain."
fibre_release: low
fibre_created: low
release_mechanism: >
  Warm water and enzyme loosen size and short fibre ends from the yarn surface; mechanical
  action is mild compared with dyeing.
release_evidence: "No stage-level fibre count published; graded low by analogy with scouring (Wang 2023 attributes 95% of wet-process release to dyeing)."
measured_today: pH, temperature, sometimes iodine test for residual starch
fibre_measured_today: false
drain: pretreatment header
sensor_note: "Hot, alkaline or enzymatic, high starch load; the pretreatment header is the practical point."
sources:
  - https://doi.org/10.1021/acs.est.3c06210
routes:
- cotton_woven
- polyester
sensor_layer: source
fem:
- water-13
- ww-7
streams:
- id: p1-liquor
  name: Desize liquor drop
  l_per_kg: 4
  to: hdr-pre
  dominant: organic
  carries:
  - organic
  - surfactant
  when: One dump per batch, or continuous from the range
  note: Most of the pretreatment organic load leaves in this one drop.
- id: p1-rinse
  name: Rinse
  l_per_kg: 8
  to: hdr-pre
  dominant: organic
  carries:
  - organic
  - fibre
  - surfactant
  when: After the liquor drop
  note: Carries dissolved size plus the first loose fibre off the woven surface.
fibre_types:
  cotton_woven: cellulosic
  polyester: synthetic
also_measurable: Flow, temperature, turbidity. Dosing enzyme against size actually removed would save
  a rinse.
first_added: 2026-09-15

## Scouring

id: P2
order: 2
phase: pretreatment
lane: all
short: Scouring
what_happens: >
  Cleans natural oils, waxes, pectin, dirt, seed fragments and spinning or knitting oils so the
  textile wets evenly. Hot caustic for cotton; milder detergent scour for polyester and nylon.
machines: [jet or soft-flow machine, continuous scouring range, jigger]
vendors: []
wet_or_dry: wet
water_l_per_kg: 12
water_note: "BAT: pretreatment of knitted fabric 10-40 L/kg; Shibly metered scouring at about 7 L/kg first fill plus rinses."
inputs: "Hot water, sodium hydroxide, surfactants, detergents, chelants."
chemicals: [NaOH, surfactant, detergent, chelant]
wastewater: "High pH, fats and oils, pectin, waxes, surfactants, suspended solids, high COD."
data_link: "Fibre type, greige source, batch, caustic recipe, wash time and temperature."
measurement_point: "Scourer outlet; pretreatment header."
fibre_release: medium
fibre_created: low
release_mechanism: >
  Hot alkali swells cotton and strips the knitting oil that held loose fibre to the fabric, so
  fly from spinning and knitting washes out here.
release_evidence: "Badruddin 2026 and Wang 2023 count pretreatment well below dyeing; loose fibre carried in from dry stages is the main source."
measured_today: pH, temperature, sometimes wetting test
fibre_measured_today: false
drain: pretreatment header
sensor_note: "95 °C, pH 13, oil and wax: the hardest pretreatment sample. Measure the header, not the drop."
sources:
  - https://doi.org/10.1021/acs.est.3c06210
  - https://doi.org/10.1093/etojnl/vgag200
routes:
- cotton_knit
- cotton_woven
- polyester
sensor_layer: source
fem:
- water-13
- ww-7
streams:
- id: p2-drop
  name: Scour bath drop
  l_per_kg: 5
  to: hdr-pre
  dominant: alkali
  carries:
  - alkali
  - organic
  - surfactant
  when: End of the scour, one dump
  note: 95 C, pH 13, oils and waxes. The hardest pretreatment sample to instrument.
- id: p2-rinse
  name: Scour rinse
  l_per_kg: 7
  to: hdr-pre
  dominant: fibre
  carries:
  - fibre
  - alkali
  - surfactant
  when: Two or three rinses after the drop
  note: Where the fly carried in from spinning and knitting finally washes out.
fibre_types:
  cotton_knit: cellulosic
  cotton_woven: cellulosic
  polyester: synthetic
also_measurable: Flow, temperature, pH, conductivity. Caustic dosing and a rinse end point; every rinse
  skipped is about 7 L/kg and the heat in it.
first_added: 2026-09-15

## Bleaching

id: P3
order: 3
phase: pretreatment
lane: all
short: Bleaching
what_happens: >
  Removes natural colour and raises whiteness before dyeing pale shades or selling white.
  Hydrogen peroxide in alkali, then a peroxide kill and rinse.
machines: [batch machine, continuous bleaching range]
vendors: []
wet_or_dry: wet
water_l_per_kg: 10
water_note: "Within the BAT pretreatment range; the peroxide kill and rinses are most of it."
inputs: "Water, hydrogen peroxide, sodium hydroxide, stabilisers, chelants."
chemicals: [H2O2, NaOH, stabiliser, chelant, peroxide killer]
wastewater: "Residual peroxide, alkaline wastewater, suspended solids, organic matter."
data_link: "Fabric or yarn type, whiteness target, peroxide dosage, bath temperature."
measurement_point: "Bleach rinse drain; pretreatment header."
fibre_release: low
fibre_created: low
release_mechanism: "Oxidative damage weakens cotton slightly; release is small next to dyeing."
release_evidence: "No stage-level count; graded low with pretreatment overall."
measured_today: residual peroxide (test strip), pH, whiteness
fibre_measured_today: false
drain: pretreatment header
sensor_note: "Oxidising, alkaline; the rinse drain is measurable, the bath drop is not."
sources: []
routes:
- cotton_knit
- cotton_woven
sensor_layer: source
fem:
- water-13
- ww-7
streams:
- id: p3-drop
  name: Bleach bath drop
  l_per_kg: 3
  to: hdr-pre
  dominant: redox
  carries:
  - redox
  - alkali
  when: End of the bleach
  note: Residual peroxide; a peroxide kill usually follows before dyeing.
- id: p3-rinse
  name: Bleach rinse
  l_per_kg: 7
  to: hdr-pre
  dominant: redox
  carries:
  - redox
  - fibre
  - alkali
  when: After the drop and the peroxide kill
  note: ''
fibre_types:
  cotton_knit: cellulosic
  cotton_woven: cellulosic
also_measurable: Flow, temperature, redox. Peroxide dose and the kill end point.
first_added: 2026-09-15

## Mercerizing

id: P4
order: 4
phase: pretreatment
lane: cotton
short: Mercerizing
what_happens: >
  Treats cotton under tension with strong caustic soda to change lustre, strength and dye
  uptake. Optional; mostly wovens and premium knits. Caustic is usually recovered.
machines: [chain or chainless mercerizer, caustic recovery evaporator]
vendors: []
wet_or_dry: wet
water_l_per_kg: 8
water_note: "Rinse water only; the caustic itself is recycled through recovery."
inputs: "Concentrated NaOH, water, wetting agents; often caustic recovery."
chemicals: [NaOH 20-30%, wetting agent, acetic acid for neutralising]
wastewater: "Very high pH and sodium or alkalinity in the rinse water; weak caustic if recovery is absent."
data_link: "Cotton lot, NaOH concentration, recovery rate, line speed."
measurement_point: "Mercerizer rinse or caustic-recovery stream; keep as a separated drain."
fibre_release: low
fibre_created: none
release_mechanism: "Fabric is held under tension; little mechanical action."
release_evidence: "No stage-level count."
measured_today: caustic concentration (Baumé), line speed
fibre_measured_today: false
drain: separated caustic drain, then equalisation
sensor_note: "Concentrated caustic; avoid."
sources: []
routes:
- cotton_woven
- cotton_knit
sensor_layer: none
fem:
- water-13
- water-15
streams:
- id: p4-weak
  name: Weak caustic to recovery
  l_per_kg: 3
  to: caustic-rec
  dominant: alkali
  carries:
  - alkali
  when: Continuous, from the stabilising boxes
  note: 'Kept out of the effluent on purpose: the caustic is evaporated back to strength and reused.'
- id: p4-rinse
  name: Mercerizer rinse
  l_per_kg: 5
  to: hdr-pre
  dominant: alkali
  carries:
  - alkali
  - salt
  when: Continuous
  note: High pH and sodium; neutralised before it reaches equalisation.
also_measurable: Caustic concentration and flow. Recovery efficiency, which is the whole economics of
  mercerizing.
first_added: 2026-09-15

## Dyeing

id: P5
order: 5
phase: coloration
lane: all
short: Dyeing
what_happens: >
  Applies colour to yarn, fabric or garments in batch (jet, soft-flow, airflow, package, jigger)
  or continuous (pad-batch, pad-steam, indigo rope or slasher) machines. Cotton takes reactive
  dyes with 40-80 g/L salt and alkali; polyester takes disperse dyes at 130 °C; denim warp takes
  indigo in repeated dips.
machines: [jet / soft-flow / airflow dyeing machine, package dyeing machine, jigger, pad-batch range, indigo rope or slasher range]
vendors:
  - {name: Thies (iMaster H2O, Luft-roto), url: https://www.thiestextilmaschinen.com/product-portfolio/fabric-dyeing/luft-roto-plus-sii-family/}
  - {name: Fong's (THEN Smartflow, Supratec LTM), url: https://www.fongs.eu/solutions/synthetic-fibres-knitwear-pes-pa-etc/ltm/}
  - {name: "Sedo Treepoint (SedoMaster, machine controllers)", url: https://www.sedo-treepoint.com/products/software/mes-systems/sedomaster/}
wet_or_dry: wet
water_l_per_kg: 8
water_note: "BAT: batch dyeing of fabric 10-150 L/kg for the whole cycle. Shibly: the dye bath alone is about 4 L/kg per fill at 1:7; scour-to-unload 60 L/kg for a light shade, 81 for a deep one, most of it rinses."
inputs: "Water and steam; dyes; sodium chloride or sodium sulfate; alkali or acids; dispersants; levelling agents; detergents; carriers or reducing agents depending on fibre and dye."
chemicals: [reactive or disperse or indigo dyes, NaCl or Na2SO4, Na2CO3 or acetic acid, dispersant, levelling agent, hydrosulphite for indigo]
wastewater: "Colour, unfixed dye, salts, surfactants, pH swings, high TDS, COD; potentially metals or dye-specific residues."
data_link: "Batch ID, substrate composition, dye class, shade, recipe, liquor ratio, temperature profile, fixation and rinse stages."
measurement_point: "Dye-bath dump and first-rinse drain; dye-house header."
fibre_release: high
fibre_created: medium
release_mechanism: >
  The longest mechanical exposure of the route: hours of nozzle shear and rope-to-rope rubbing
  at high temperature while alkali and heat swell cotton and soften polyester.
release_evidence: "Wang 2023: dyeing is 95% of wet-process release; release falls with white shades, lower temperature and shorter time. Badruddin 2026: about 800 fibres per gram, the largest stage. Zhou 2020: up to 54,100 fibres/L in printing-and-dyeing effluent."
measured_today: shade (spectrophotometer, delta E), pH, conductivity or salt, temperature profile, bath exhaustion; nothing fibre-related
fibre_measured_today: false
drain: machine drain to dye-house header and equalisation, hot drops sometimes through a heat exchanger
sensor_note: "Fibre-rich but coloured, 60-130 °C, salt to 80 g/L, foam. The dye-bath drop is the hardest sample; the first rinse that follows is easier and still fibre-rich."
sources:
  - https://doi.org/10.1021/acs.est.3c06210
  - https://doi.org/10.1093/etojnl/vgag200
  - https://doi.org/10.1016/j.scitotenv.2020.140329
routes:
- cotton_knit
- cotton_woven
- polyester
- denim_laundry
sensor_layer: source
fem:
- water-13
- water-5
- ww-7
streams:
- id: p5-bath
  name: Dye bath drop
  l_per_kg: 8
  to: hdr-dye
  dominant: colour
  carries:
  - colour
  - salt
  - fibre
  - surfactant
  when: End of the dyeing cycle, one dump per batch
  note: 'The most contaminated single stream in the mill and the hardest to measure: 60-130 C, salt to
    80 g/L, full shade depth, foam.'
fibre_types:
  cotton_knit: cellulosic
  cotton_woven: cellulosic
  polyester: synthetic
  denim_laundry: cellulosic
also_measurable: 'Flow, temperature, conductivity, colour. Bath exhaustion read live is the largest single
  lever in the mill: fewer re-dyes, shorter cycles, less steam.'
first_added: 2026-09-15

## Soaping, washing and rinsing

id: P6
order: 6
phase: coloration
lane: all
short: Washing / rinsing
what_happens: >
  Removes unfixed dye, printing paste, loose fibres, chemicals and residues after dyeing or
  printing. Several rinses and a hot soap in the batch machine, or an open-width washing range.
machines: [batch machine rinse cycles, open-width washing range, rope washer]
vendors: []
wet_or_dry: wet
water_l_per_kg: 40
water_note: "The largest water consumer: Shibly metered a 10-minute overflow rinse at about 19 L/kg and several rinses per batch; most of the 60-81 L/kg cycle is rinsing."
inputs: "Water, detergents, soaping agents, surfactants, sometimes reducing or oxidising agents."
chemicals: [soaping agent, detergent, acetic acid, sometimes oxidant]
wastewater: "Coloured wastewater, surfactants, salts, loosened lint and fibres, variable COD and TSS."
data_link: "Batch ID, wash recipe, number of rinses, water volume, line or machine."
measurement_point: "First rinse separately; wash header. High-priority source stream."
fibre_release: high
fibre_created: low
release_mechanism: >
  Everything the dyeing cycle loosened leaves with the rinses: the first rinse after the dye
  bath carries the peak fibre load at a temperature and colour a sensor can tolerate.
release_evidence: "Wang 2023 samples rinse and soap drops as the fibre-rich fraction of the dyeing cycle."
measured_today: water volume where metered, sometimes conductivity for rinse end-point
fibre_measured_today: false
drain: wash header to equalisation
sensor_note: "The single best source point: 40-70 °C, lower colour and salt than the bath, high fibre count, repeatable per batch."
sources:
  - https://doi.org/10.1021/acs.est.3c06210
routes:
- cotton_knit
- cotton_woven
- polyester
- printing
sensor_layer: source
fem:
- water-13
- water-5
- ww-7
streams:
- id: p6-first
  name: First rinse after the dye bath
  l_per_kg: 12
  to: hdr-dye
  dominant: fibre
  carries:
  - fibre
  - colour
  - salt
  when: Immediately after the bath drop, once per batch
  note: 'The best source point in the mill: peak fibre load, 40-70 C, much less colour and salt than the
    bath, and it repeats identically every batch.'
- id: p6-soap
  name: Hot soaping
  l_per_kg: 8
  to: hdr-dye
  dominant: colour
  carries:
  - colour
  - surfactant
  - fibre
  when: After the first rinse, 90-95 C
  note: Strips hydrolysed dye; colour peaks again here.
- id: p6-later
  name: Later rinses
  l_per_kg: 20
  to: hdr-dye
  dominant: salt
  carries:
  - salt
  - fibre
  - colour
  when: Two to four rinses to the end point
  note: Most of the mill's water volume. Dilute, so a concentration reading here needs flow to mean anything.
fibre_types:
  cotton_knit: cellulosic
  cotton_woven: cellulosic
  polyester: synthetic
  printing:
  - cellulosic
  - synthetic
fibre_note: On a blend the rinse carries both at once. Which of the two is leaving, and in what proportion,
  is the number a brand cannot get today.
also_measurable: Flow, temperature, conductivity, colour, fibre. Rinse end point detection is the biggest
  water and energy saving available, because rinses are most of the volume.
first_added: 2026-09-15

## Printing

id: P7
order: 7
phase: coloration
lane: all
short: Printing
what_happens: >
  Applies colour or pattern through screen, rotary, pigment, reactive, disperse or digital
  systems, then fixes and washes off. Screen and blanket washing is a continuous side stream.
machines: [rotary screen printer, flat-bed screen printer, digital printer, steamer, print washer]
vendors: []
wet_or_dry: wet
water_l_per_kg: 25
water_note: "BAT: printing 5-40 L/kg including wash-off; digital pigment printing far lower."
inputs: "Printing paste; dyes or pigments; urea; thickeners; binders; solvents; screen-wash water."
chemicals: [pigment or reactive or disperse dye, urea, alginate or synthetic thickener, acrylic binder, solvent]
wastewater: "Colour, pigment and binder particles, urea, solvents, surfactants, thickener residues, high COD."
data_link: "Print design or run, ink or paste recipe, fabric type, screen-cleaning event."
measurement_point: "Print-wash or screen-cleaning drain; printing header."
fibre_release: medium
fibre_created: low
release_mechanism: "Wash-off after steaming loosens fibre raised by the print blanket and squeegee; binder particles confound counts."
release_evidence: "Zhou 2020 sampled a printing-and-dyeing park at up to 54,100 fibres/L; the claimed 1.39 million fibres/L screen-printing figure has no locatable source."
measured_today: paste viscosity, colour match, wash-off water volume where metered
fibre_measured_today: false
drain: printing header to equalisation
sensor_note: "Pigment and binder particles look like fibres to a mass or turbidity method; needs shape or polymer discrimination."
sources:
  - https://doi.org/10.1016/j.scitotenv.2020.140329
routes:
- printing
sensor_layer: source
fem:
- water-13
- ww-7
streams:
- id: p7-washoff
  name: Print wash-off
  l_per_kg: 18
  to: hdr-print
  dominant: colour
  carries:
  - colour
  - organic
  - polymer
  - fibre
  when: Continuous, after steaming
  note: Urea and thickener come off with the unfixed dye.
- id: p7-screen
  name: Screen and blanket washing
  l_per_kg: 7
  to: hdr-print
  dominant: polymer
  carries:
  - polymer
  - colour
  when: Between designs, an event not a flow
  note: Pigment and binder particles here read like fibres to any shape-blind method.
fibre_types:
  printing:
  - cellulosic
  - synthetic
also_measurable: Flow, colour, solids. Wash-off end point and screen-wash events.
first_added: 2026-09-15

## Reduction clearing

id: P8
order: 8
phase: coloration
lane: synthetic
short: Reduction clearing
what_happens: >
  Polyester post-dye treatment that strips unfixed disperse dye from the fibre surface with
  hydrosulphite and caustic, then rinses; needed for deep shades and fastness.
machines: [same batch dyeing machine]
vendors: []
wet_or_dry: wet
water_l_per_kg: 10
water_note: "One bath plus rinses inside the dyeing cycle."
inputs: "Water, sodium hydrosulphite, sodium hydroxide, detergents."
chemicals: [Na2S2O4, NaOH, detergent]
wastewater: "High pH, sulphur-containing reducing residues, disperse dye, surfactants, colour and COD."
data_link: "Polyester batch, dye class, clearing recipe, duration and temperature."
measurement_point: "Reduction-clearing drain; dye-house header."
fibre_release: medium
fibre_created: low
release_mechanism: "Hot alkaline bath at 70-80 °C with continued rope circulation after the 130 °C dyeing has softened the polyester."
release_evidence: "No stage-level count; polyester dyeing cycles as a whole are the highest synthetic release (Wang 2023)."
measured_today: pH, temperature, sometimes redox
fibre_measured_today: false
drain: dye-house header
sensor_note: "Reducing, alkaline, sulphur odour; the rinse after the clear is the sample."
sources:
  - https://doi.org/10.1021/acs.est.3c06210
routes:
- polyester
sensor_layer: source
fem:
- water-13
- ww-7
streams:
- id: p8-bath
  name: Clearing bath drop
  l_per_kg: 4
  to: hdr-dye
  dominant: redox
  carries:
  - redox
  - colour
  - alkali
  when: After disperse dyeing, deep shades
  note: Hydrosulphite and caustic at 70-80 C.
- id: p8-rinse
  name: Clearing rinse
  l_per_kg: 6
  to: hdr-dye
  dominant: fibre
  carries:
  - fibre
  - colour
  when: After the clearing bath
  note: Polyester softened by the 130 C cycle sheds into this rinse.
fibre_types:
  polyester: synthetic
fibre_note: Polyester only, so everything shed here is plastic.
also_measurable: Flow, temperature, redox. Clearing end point instead of a fixed time.
first_added: 2026-09-15

## Garment laundry and denim wash

id: P9
order: 11
phase: finishing
lane: laundry
short: Garment / denim wash
what_happens: >
  Creates look, softness, fading, distressing, cleanliness or finish after garment assembly:
  desizing, enzyme and stone washing, bleaching, tinting, softening, sometimes permanganate
  spray or laser and ozone as dry alternatives.
machines: [front-loading garment washer, tumble dryer, laser, ozone cabinet]
vendors:
  - {name: Jeanologia (laser, G2 ozone, e-Flow), url: https://www.jeanologia.com/}
  - {name: Tonello, url: https://www.tonello.com/}
wet_or_dry: wet
water_l_per_kg: 30
water_note: "BAT: garment washing 20-80 L/kg; laser and ozone routes cut it sharply."
inputs: "Water; enzymes; detergents; bleach or oxidants; pumice stones; softeners; resins; sometimes permanganate."
chemicals: [cellulase, detergent, NaOCl or H2O2, KMnO4, softener, resin]
wastewater: "Lint and fibres, indigo or dye colour, pumice fines, enzymes, surfactants, oxidants, high TSS and COD."
data_link: "Garment style, fabric blend, wash recipe, machine, cycle phase, stones and load, order."
measurement_point: "Individual washer drain, laundry header, and ETP influent."
fibre_release: high
fibre_created: high
release_mechanism: >
  Cellulase and pumice deliberately abrade the fabric surface to fade it; the lint is the
  product's look leaving as effluent. Cut edges and seams shed more than fabric.
release_evidence: "Wang 2023 and the TMC/ZDHC Phase 2 design both name denim and laundry as priority fibre sources."
measured_today: load weight, cycle programme, sometimes TSS at the laundry ETP
fibre_measured_today: false
drain: washer drain to laundry header, then equalisation
sensor_note: "Highest and most variable fibre load, moderate temperature, indigo colour and pumice fines; the washer drain gives batch attribution, the header gives the daily picture."
sources:
  - https://doi.org/10.1021/acs.est.3c06210
  - https://www.textileworld.com/textile-world/fiber-world/2026/04/the-microfibre-consortium-and-zdhc-advance-joint-research-to-strengthen-wastewater-monitoring-of-fibre-fragmentation/
routes:
- denim_laundry
sensor_layer: source
fem:
- water-13
- water-5
- ww-7
streams:
- id: p9-desize
  name: Desize and enzyme drop
  l_per_kg: 8
  to: hdr-laundry
  dominant: fibre
  carries:
  - fibre
  - organic
  - colour
  when: First baths of the wash recipe
  note: Cellulase is abrading the fabric on purpose; the lint is the look leaving as effluent.
- id: p9-stone
  name: Stone wash drop
  l_per_kg: 7
  to: hdr-laundry
  dominant: fibre
  carries:
  - fibre
  - solids
  - colour
  when: Stone or combined enzyme-stone cycle
  note: Pumice fines sit alongside the fibre and confound a gravimetric method.
- id: p9-bleach
  name: Bleach or tint drop
  l_per_kg: 4
  to: hdr-laundry
  dominant: redox
  carries:
  - redox
  - colour
  when: Where the look needs it
  note: ''
- id: p9-rinse
  name: Rinses
  l_per_kg: 8
  to: hdr-laundry
  dominant: fibre
  carries:
  - fibre
  - colour
  when: Between and after every chemical step
  note: ''
- id: p9-soft
  name: Softener drop
  l_per_kg: 3
  to: hdr-laundry
  dominant: polymer
  carries:
  - polymer
  - surfactant
  when: Last bath
  note: ''
fibre_types:
  denim_laundry:
  - cellulosic
  - synthetic
fibre_note: Denim is cotton, so the shed fibre is cellulosic, except where the stretch yarn adds elastane.
  A blend sheds both and no current method separates them.
also_measurable: Flow, temperature, turbidity, fibre. Cycle end point per recipe, and stone and enzyme
  dose against the fade actually achieved.
first_added: 2026-09-15

## Finishing

id: P10
order: 10
phase: finishing
lane: all
short: Finishing
what_happens: >
  Alters hand feel, shrinkage, crease resistance, water repellency, antimicrobial behaviour,
  coating or softness. Chemicals are padded or exhausted, then the fabric is dried and cured on
  a stenter; mechanical finishes (raising, sueding, compacting) are dry.
machines: [padder, stenter, compactor, coating line, raising or sueding machine]
vendors:
  - {name: Monforts, url: https://www.monforts.de/}
  - {name: Brückner, url: https://www.brueckner-textile.com/}
wet_or_dry: wet
water_l_per_kg: 3
water_note: "Padding uses little water; the load is trough dumps and washdown, not volume."
inputs: "Water; softeners; resins; binders; waxes; silicones; crosslinkers; functional finishes; solvents depending on process."
chemicals: [silicone or cationic softener, DMDHEU resin, acrylic binder, wax, fluorine-free repellent, crosslinker]
wastewater: "Finishing chemical residues, suspended solids, surfactants, resin, wax and silicone residues, potentially VOC-related materials."
data_link: "Finish recipe, application method, add-on target, fabric composition, stenter or coating line."
measurement_point: "Finishing washdown or cleanup drain; finishing header."
fibre_release: low
fibre_created: high
release_mechanism: >
  Raising, sueding and compacting create loose fibre mechanically but dry; it leaves as fly and
  lint waste, or washes out in a later garment wash. The wet pad itself sheds little.
release_evidence: "Cai 2020/2021: mechanical finishes raise later release 5-30x; the wet finishing stage itself is not a measured source."
measured_today: pick-up percentage, stenter temperature, add-on
fibre_measured_today: false
drain: finishing header to equalisation
sensor_note: "Silicone films and tiny volumes; a poor sensor point. Track the lint waste from raising and sueding as solid waste instead."
sources:
  - https://doi.org/10.3390/w17040574
routes:
- cotton_knit
- cotton_woven
- polyester
- printing
sensor_layer: none
fem:
- water-13
- ww-7
streams:
- id: p10-trough
  name: Pad trough dump
  l_per_kg: 1
  to: hdr-fin
  dominant: polymer
  carries:
  - polymer
  when: Recipe change or shift end
  note: Small volume, very high concentration of softener, resin and silicone.
- id: p10-wash
  name: Washdown and cleanup
  l_per_kg: 2
  to: hdr-fin
  dominant: polymer
  carries:
  - polymer
  - surfactant
  when: Cleaning the padder and stenter
  note: Silicone films make this a poor place to put an optical instrument.
fibre_types:
  cotton_knit: cellulosic
  cotton_woven: cellulosic
  polyester: synthetic
  printing:
  - cellulosic
  - synthetic
also_measurable: Flow and add-on. Trough dumps at recipe change are pure loss.
first_added: 2026-09-15

## Equipment cleaning

id: P11
order: 9
phase: coloration
lane: all
short: Equipment cleaning
what_happens: >
  Cleans dye machines, tanks, lines, screens, filters and chemical containers between batches
  and shades; also the lint-filter cleaning on dyeing machines.
machines: [machine CIP cycle, screen washer, lint filter]
vendors: []
wet_or_dry: wet
water_l_per_kg: 2
water_note: "Small volume, high concentration; not normalised per kg of product."
inputs: "Water; caustic or acid cleaners; detergents; solvents; oxidants or reductants."
chemicals: [NaOH, acid cleaner, detergent, solvent, oxidant or hydrosulphite]
wastewater: "Short, concentrated chemical shock loads; colour, pH swings, surfactants, residues; the lint-filter flush is a concentrated fibre slug."
data_link: "CIP or cleaning event, machine ID, prior recipe or batch, cleaning chemical, volume."
measurement_point: "CIP drain; keep as a distinct tagged stream."
fibre_release: medium
fibre_created: none
release_mechanism: "Lint filters on dyeing machines collect the batch's fibre; flushing them sends it to drain in one slug."
release_evidence: "No published count; mill practice (lint filter cleaning frequency) is an interview question."
measured_today: nothing; cleaning is logged by the operator if at all
fibre_measured_today: false
drain: machine drain to header
sensor_note: "Events, not a steady stream; tag them so they do not pollute the batch attribution of the machine's next cycle."
sources: []
routes:
- cotton_knit
- cotton_woven
- polyester
- printing
- denim_laundry
sensor_layer: none
fem:
- ww-7
streams:
- id: p11-cip
  name: Machine clean between shades
  l_per_kg: 1.5
  to: hdr-dye
  dominant: alkali
  carries:
  - alkali
  - colour
  - surfactant
  when: Shade change, an event
  note: A concentrated shock load that belongs to no batch. Tag it or it corrupts the attribution of the
    next cycle.
- id: p11-lint
  name: Lint filter flush
  l_per_kg: 0.5
  to: hdr-dye
  dominant: fibre
  carries:
  - fibre
  when: Every one to several batches, by mill practice
  note: The batch's captured fibre going to drain in one slug. How often this happens is an interview
    question, not a published figure.
fibre_types:
  cotton_knit: cellulosic
  cotton_woven: cellulosic
  polyester: synthetic
  printing: &id001
  - cellulosic
  - synthetic
  denim_laundry: *id001
also_measurable: Event detection. How often lint filters are really cleaned, which nobody logs.
first_added: 2026-09-15

## ETP: equalisation

id: P12
order: 12
phase: effluent
lane: effluent
short: Equalisation
what_happens: >
  Screens and mixes the varying wastewater streams in a balancing tank to smooth flow, pH,
  temperature and load before treatment.
machines: [bar screen, equalisation tank, pH correction dosing]
vendors: []
wet_or_dry: wet
water_l_per_kg:
water_note: "Whole-site flow; the TMC/ZDHC Phase 2 study samples here."
inputs: "Combined wastewater; sometimes pH correction."
chemicals: [acid or alkali for pH]
wastewater: "Mixed, time-smoothed influent."
data_link: "Facility-wide inputs, timestamp, incoming flow and process events."
measurement_point: "ETP influent and equalisation tank inlet or outlet."
fibre_release: none
fibre_created: none
release_mechanism: "Carries what the process stages released; mixing loses batch attribution."
release_evidence: "Zhou 2020 measured influent at a centralised park WWTP; TMC/ZDHC Phase 2 samples balancing tanks."
measured_today: flow, pH, temperature, sometimes COD and TSS by lab
fibre_measured_today: false
drain: to primary treatment
sensor_note: "Cool, mixed, moderate colour; the easiest fibre-rich sample and the compliance influent, but source-blind."
sources:
  - https://doi.org/10.1016/j.scitotenv.2020.140329
  - https://www.textileworld.com/textile-world/fiber-world/2026/04/the-microfibre-consortium-and-zdhc-advance-joint-research-to-strengthen-wastewater-monitoring-of-fibre-fragmentation/
routes: []
sensor_layer: treatment
fem:
- ww-1
- ww-5
- ww-7
- ww-3
streams:
- id: p12-out
  name: Equalised influent
  to: P13
  dominant: mixed
  share: 1.0
  carries:
  - mixed
  - fibre
  - solids
  when: Continuous
  note: Everything the mill released, mixed and smoothed. The compliance influent, and source-blind.
also_measurable: Flow, pH, temperature, TSS. Load balancing and a shock warning to the plant before it
  arrives.
first_added: 2026-09-15

## ETP: coagulation, flocculation and clarification

id: P13
order: 13
phase: effluent
lane: effluent
short: Clarifier
what_happens: >
  Aggregates and settles suspended matter, colour, dyes and particles with coagulant and
  flocculant; primary clarifier or dissolved-air flotation.
machines: [coagulation tank, flocculation tank, primary clarifier or DAF]
vendors: []
wet_or_dry: wet
water_l_per_kg:
water_note: ""
inputs: "Coagulants, flocculants, pH chemicals."
chemicals: [ferric chloride or alum or PAC, polyelectrolyte, lime or acid]
wastewater: "Clarified water plus particle- and chemical-rich sludge."
data_link: "Chemical dose, turbidity or TSS change, sludge produced."
measurement_point: "Before and after the clarifier; sludge stream."
fibre_release: none
fibre_created: none
release_mechanism: "Removes fibre into sludge; the transfer is invisible if only the discharge is measured."
release_evidence: "TMC/ZDHC 2024 and Phase 2 treat TSS removal here as the fibre removal step."
measured_today: turbidity, TSS by lab, coagulant dose, sludge volume
fibre_measured_today: false
drain: to biological treatment; sludge to dewatering
sensor_note: "Before-and-after pair gives the removal efficiency; the sludge line is where the fibre goes."
sources: []
routes: []
sensor_layer: treatment
fem:
- ww-5
- ww-8
- ww-9
streams:
- id: p13-out
  name: Clarified water
  to: P14
  dominant: mixed
  share: 0.97
  carries:
  - mixed
  - fibre
  when: Continuous
  note: ''
- id: p13-sludge
  name: Primary sludge
  to: out-sludge
  dominant: solids
  share: 0.03
  carries:
  - solids
  - fibre
  - colour
  when: Continuous or batched
  note: Where the fibre actually goes. Measure only the discharge and this transfer is invisible.
also_measurable: TSS in and out, coagulant dose, sludge mass. Dosing against real load rather than a fixed
  rate.
first_added: 2026-09-15

## ETP: biological treatment

id: P14
order: 14
phase: effluent
lane: effluent
short: Biological
what_happens: >
  Activated sludge or MBBR uses microbes to reduce biodegradable organic load; secondary
  clarifier returns sludge.
machines: [aeration basin, MBBR, secondary clarifier, blowers]
vendors: []
wet_or_dry: wet
water_l_per_kg:
water_note: ""
inputs: "Aeration; sometimes nutrients and pH adjustment."
chemicals: [urea or DAP nutrients, antifoam]
wastewater: "Biological solids, residual COD and BOD, possible sludge."
data_link: "Dissolved oxygen, aeration, pH, loading, residence time."
measurement_point: "Aeration basin influent and effluent."
fibre_release: none
fibre_created: none
release_mechanism: "Synthetic fibre is not degraded; it partitions into biological sludge or passes through."
release_evidence: "No mill-scale fibre balance across biological treatment published."
measured_today: DO, MLSS, pH, COD and BOD by lab
fibre_measured_today: false
drain: to tertiary treatment
sensor_note: "Low colour, cool; a clean sample but fibre count is low after clarification."
sources: []
routes: []
sensor_layer: treatment
fem:
- ww-5
streams:
- id: p14-out
  name: Secondary effluent
  to: P15
  dominant: mixed
  share: 0.98
  carries:
  - mixed
  - fibre
  when: Continuous
  note: ''
- id: p14-sludge
  name: Waste activated sludge
  to: out-sludge
  dominant: solids
  share: 0.02
  carries:
  - solids
  - fibre
  when: Continuous
  note: Synthetic fibre is not degraded here; it partitions into the sludge or passes through.
also_measurable: Dissolved oxygen, mixed liquor solids, load. Aeration is the treatment plant's largest
  power consumer.
first_added: 2026-09-15

## ETP: tertiary treatment and discharge

id: P15
order: 15
phase: effluent
lane: effluent
short: Tertiary / discharge
what_happens: >
  Polishing via sand filters, activated carbon, ultrafiltration or RO, then final discharge to
  sewer or surface water, or to the reuse loop.
machines: [sand filter, activated carbon filter, ultrafiltration, disc filter]
vendors: []
wet_or_dry: wet
water_l_per_kg:
water_note: ""
inputs: "Backwash water; sometimes additional treatment chemicals."
chemicals: [chlorine or ozone for colour, antiscalant]
wastewater: "Filter backwash, concentrate or reject stream, final effluent."
data_link: "Filter pressure and run time, backwash event, membrane condition."
measurement_point: "Before and after the filter; final treated discharge; reject stream."
fibre_release: none
fibre_created: none
release_mechanism: "Backwash returns captured fibre to the head of the plant or to sludge."
release_evidence: "ZDHC Wastewater Guidelines V2.2 Part C sets the TSS levels the discharge must meet."
measured_today: flow, pH, TSS, COD, colour by lab twice a year for ZDHC; online flow and pH where permitted
fibre_measured_today: false
drain: outfall, sewer, or reuse loop
sensor_note: "The compliance point: strongest link to discharge evidence, weakest to source."
sources:
  - https://downloads.roadmaptozero.com/output/ZDHC-Wastewater-Guidelines
routes: []
sensor_layer: outcome
fem:
- ww-1
- ww-2
- ww-5
streams:
- id: p15-discharge
  name: Final discharge
  to: out-discharge
  dominant: mixed
  share: 0.55
  carries:
  - mixed
  - fibre
  when: Continuous
  note: What actually leaves the site, and the ZDHC and permit sample point. Whether residual
    fibre is still in it is exactly the number nobody can produce today.
- id: p15-ro
  name: Feed to reuse
  to: P16
  dominant: mixed
  share: 0.43
  carries:
  - mixed
  - fibre
  when: Continuous
  note: Fibre reaching the RO feed is what shortens membrane life.
- id: p15-backwash
  name: Filter backwash
  to: P12
  dominant: solids
  share: 0.02
  back: true
  carries:
  - solids
  - fibre
  when: Every filter run, an event
  note: Returns captured solids to the head of the plant. A loop, not an output.
also_measurable: Flow, TSS, differential pressure. Backwash on condition rather than on a timer.
first_added: 2026-09-15

## ZLD and reuse loop

id: P16
order: 16
phase: effluent
lane: effluent
short: ZLD / reuse
what_happens: >
  Recovers water through RO for reuse in the process; the concentrate goes to an evaporator and
  crystalliser (zero liquid discharge) or is disposed of separately. Mandated in parts of India
  and increasingly asked for by brands.
machines: [RO train, multiple-effect evaporator, crystalliser]
vendors: []
wet_or_dry: wet
water_l_per_kg:
water_note: "Recovery of 70-95% of treated effluent where run."
inputs: "Reverse osmosis, evaporator and crystalliser inputs."
chemicals: [antiscalant, cleaning acid and alkali for membranes]
wastewater: "RO reject, evaporator concentrate, salts and sludge; reclaimed water."
data_link: "Recovery percentage, reuse volume, reject handling."
measurement_point: "RO feed, permeate and reject; reuse-water loop."
fibre_release: none
fibre_created: none
release_mechanism: "Fibre reaching the RO feed fouls the membrane; the reuse loop can carry it back to the process."
release_evidence: "No published fibre balance; membrane fouling by fibre is the H5 hunch's question."
measured_today: conductivity, flow, differential pressure, recovery
fibre_measured_today: false
drain: permeate to process; reject to evaporator
sensor_note: "Clean water with low fibre count; the RO feed is where fibre would matter for membrane life."
sources: []
routes: []
sensor_layer: none
fem:
- water-15
- water-19
streams:
- id: p16-permeate
  name: Reclaimed water
  to: out-reuse
  dominant: mixed
  share: 0.75
  carries:
  - mixed
  - fibre
  when: Continuous
  note: Goes back into the process; whatever it still carries re-enters the mill.
- id: p16-reject
  name: RO reject
  to: out-reject
  dominant: salt
  share: 0.25
  carries:
  - salt
  - colour
  when: Continuous
  note: To the evaporator and crystalliser where ZLD is run.
also_measurable: Flow, conductivity, differential pressure. Fibre in the feed is what shortens membrane
  life.
first_added: 2026-09-15

## How water actually flows

Dated 2026-09-15. Not a stage (no `id:`), so the generators skip it.

The water path is rarely one clean pipe per machine, which is why the map is the first asset:

```
freshwater or recycled water
  → wet machine bath
  → batch drain plus rinse drains
  → local trench or header
  → dye-house, pretreatment, printing or laundry header
  → equalisation tank
  → ETP
  → final discharge | reuse water | RO reject or ZLD concentrate
```

Five things make the mapping matter:

- A machine drain is a short, concentrated batch dump. It gives attribution but is not representative of daily discharge.
- A department header mixes several machines. It is more representative and loses some batch-level attribution.
- The ETP influent gives the total factory incoming load.
- The final discharge gives what leaves the factory after treatment.
- Sludge and filter backwash hold what was removed from the water. Measuring only the discharge misses a transfer from water to sludge.

Higg FEM verification checks whether a facility tracks wastewater volume, monitors BOD5, holds
discharge compliance documents, and monitors whether its treatment plant runs to design
parameters: volume, flow rate, and influent and effluent quality.

## Sensor-placement logic

Dated 2026-09-15. A data-model placement strategy, not a claim that one instrument works at every point.

| Measurement location | What it lets you know | Attribution value | Higg FEM / operating value |
|---|---|---|---|
| Individual high-impact machine drain | What a particular dye, wash, printing or finishing cycle releases | Very high | Links environmental intensity to batch, recipe, material, operator and machine |
| Department header | Combined load from dye house, laundry, printing or finishing | Medium | Identifies which department needs intervention |
| ETP influent / equalisation inlet | Total untreated factory wastewater load | Low for source, high for facility total | Treatment loading, flow and treatment-performance monitoring |
| Before / after a clarifier, filter or membrane | Whether a treatment stage removes a contaminant, or fails or bypasses | Medium | ETP design-parameter monitoring and corrective action |
| Final treated effluent / outfall | What is actually discharged or sent for reuse | Low for source, highest for outcome | Strongest link to discharge evidence and the compliance workflow |
| Filter backwash / sludge line | Where captured solids and contaminants go after removal | Medium | Waste and sludge accounting; avoids "removal" claims that ignore transfer |

**Deployment sequence.** Three measurement layers, so no single point has to be chosen forever:

1. Outcome layer: final treated effluent plus flow.
2. Treatment layer: ETP influent and, where relevant, before and after tertiary filtration.
3. Source layer: one high-impact process, such as a garment laundry washer, a dye-bath and first-rinse drain, or a printing washdown stream.

That is the minimum structure that answers the three useful questions: what is leaving the site, is the ETP removing it, and which operation is driving it.

## How many sensors, and where

Dated 2026-09-15. Counts are the minimum that answers all three questions (what leaves, is the
plant removing it, which operation drives it), not a recommendation to sell that many.

| Route | Minimum units | Where they sit |
|---|---|---|
| Cotton knit dyehouse | 3 | One dye machine's first rinse, the equalisation outlet, the final discharge |
| Cotton woven mill | 3 | Same three, with the pretreatment header preferred over a single machine if desizing dominates |
| Polyester or synthetic mill | 4 | Dye-machine first rinse, the reduction-clearing rinse where the plastic fibre peaks, equalisation outlet, final discharge |
| Printing house | 3 | Wash-off line, equalisation outlet, final discharge |
| Denim or garment laundry | 4 | One washer drain, the laundry header, equalisation outlet, final discharge |

A fourth or fifth unit across the clarifier turns "we discharge X" into "the plant removes Y",
which is the claim a filtration vendor and an auditor both want and neither can make today.

**How the count grows with the product, not with the pitch.**

1. **Three units, compliance.** A dated, flow-normalised record at the outfall and the influent.
   Evidences the FEM wastewater questions and answers the Inditex fibre-control clause with a
   number rather than a procedure.
2. **One unit per high-impact machine, attribution.** Now a reading belongs to a batch, a recipe
   and a fabric. This is where a twenty-machine dyehouse becomes twenty source units, and where
   the fabric-level shedding figure that brands ask a lab for starts to come off the line instead.
3. **Joined to machine data, control.** The `also_measurable` field on each stage is the list:
   flow, temperature, conductivity, colour, pressure. Rinse end-point detection is the largest
   single water and energy saving in a dyehouse because rinsing is most of the volume and most of
   the heat. Bath exhaustion read live cuts re-dyes. Backwash on condition rather than on a timer
   cuts both water and pumping.
4. **Joined across sites, the platform.** Dye-machine controllers already speak OPC UA and MQTT
   through the mill's own MES, so the missing piece is not a protocol, it is that no effluent
   instrument publishes into it. A brand-side view is the same records rolled up by facility.

## Data model before sensors

Dated 2026-09-15. The data contract comes before the hardware specification. Every observation links five objects.

| Data object | Example fields |
|---|---|
| Facility | Facility ID, location, Higg or Worldly facility identifier, discharge type, ETP configuration, permit limits |
| Process and machine | Department, process family, machine ID, machine type, capacity, drain or header ID, operating state |
| Production batch | Batch or order ID, material and fibre composition, weight, fabric construction, supplier or material lot, start and end time |
| Chemical recipe | Chemical product ID, SDS and MRSL status, chemical family, dosage, bath volume, temperature and pH profile, supplier |
| Water-quality observation | Timestamp, location ID, wastewater flow, concentration or index, sample or measurement method, calibration and QC state, event ID |
| Treatment operation | ETP stage, chemical dose, filter status, pump and aerator state, sludge amount, bypass or maintenance status |
| Evidence and reporting record | Monitoring log, lab report, permit result, corrective action, reviewer and approver, reporting year, Higg FEM evidence link |

The optimisation layer exists only when those objects are joined in time. Worked example: on
12 March, machine D-07 ran a 500 kg polyester-elastane batch on a disperse-dye recipe. The
first-rinse drain showed an abnormal particulate and fibre index. Forty minutes later the
dye-house header rose, then the ETP influent load. The tertiary filter differential pressure
rose too. Final discharge stayed inside the facility's normal range, but sludge mass increased.
The system flags the batch and recipe and recommends checking rinse volume, filter maintenance
and dosing conditions. That is an industrial intelligence product, not a sensor dashboard.

## What maps to Higg FEM

Dated 2026-09-15. The system does not submit the whole Higg FEM 4.0. It supports selected evidence and metric workflows:

| Higg FEM area | What the record can contribute |
|---|---|
| Water | Meter data by source and process; consumption by process; recycling and reuse volume; intensity denominators from production volume |
| Wastewater | Volume discharged; discharge flow; wastewater-source map; treatment-process records; ETP influent and effluent monitoring; data-quality and calibration logs; exception and bypass records |
| Chemical management | Chemical inventory and recipe metadata; MRSL documentation links; consumption by process; release-event traceability, not full hazardous-chemical analytical compliance |
| Energy and GHG | Later: machine and process energy and steam tied to batches, water heating, ETP aeration, pumping and treatment intensity |
| Waste and sludge | Sludge and filter waste quantities, disposal route, removal-event evidence |
| Environmental management | Targets, baseline, corrective actions, operating procedures, trend reports, auditable evidence records |

Higg FEM's water and wastewater requirements include water-source tracking, wastewater-volume
tracking, treatment information, BOD5 monitoring, discharge documentation, and verification of
ETP performance against design parameters (volume, flow rate, input and output quality).

## Where to begin

Dated 2026-09-15. The next deliverable is a wet-process and wastewater data map for one
facility, not a product spec and not a generic Higg summary. Choose one facility category first,
ideally a synthetic-blend dyeing and finishing mill or a denim or garment laundry with an onsite
ETP, and build in a spreadsheet or diagram:

1. List every wet machine and its process step.
2. For each, capture its drain or header and whether it is separate or mixed.
3. List inputs: water, steam, dyes, salts, acids and alkalis, surfactants, softeners, resins, cleaning chemicals.
4. List outputs: bath dump, first rinse, later rinses, washdown, filter backwash, sludge.
5. Trace every output pipe to a department header, equalisation tank, ETP stage, reuse loop, outfall or sludge route.
6. Add the existing sensors, lab samples, manual logs and meters at each point.
7. Add the production, batch and recipe data source that can be joined to each machine and timestamp.
8. Mark three candidate observation points: one source stream, ETP influent, final effluent.

Only after that map exists can the product requirement be written in one sentence, for example:
"For polyester dyeing mills, provide a time-resolved, flow-normalised contaminant and
fibre-release record from dye-bath and rinse events through the ETP, linked to batch, recipe and
treatment operations, with auditable exports that support FEM wastewater evidence." That is the
bridge from the core IP to factory optimisation to the Higg FEM record.
