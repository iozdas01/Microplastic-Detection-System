---
purpose: The company registry — one entry per organisation on the demand or supply side of contaminant detection in industrial water, what it actually does, and where it sits on the declared map axes.
idea: Microplastic Detection System
schema_version: 3
last_updated: 2026-09-09
# ─── Map axes (proposed 2026-09-09, awaiting founder confirmation) ───────────────
# The question this registry has to answer is not "who does microplastics" but "which
# detection use-cases in industrial water exist, who has each one, and who already sells
# into it" — so microplastics can be compared against its neighbours instead of assumed.
#
# Demand side (map: client) is placed by WHERE in the plant the water is measured and
# WHAT JOB the measurement does for them, with the regulatory pressure behind it as depth.
# Supply side (map: startup) is placed by WHAT they detect and HOW (lab sample vs online
# sensor), coloured by WHAT THEY SELL (an instrument, a test, a monitoring outcome).
# Two honest readers of a company page should agree on every value; if a value needs a
# judgement call, it is recorded in the entry's notes and graded conservatively.
map_axes:
  client:
    x: water_stream
    y: driver
    z: regulatory_pressure
  startup:
    x: target
    y: measurement_mode
    colour: commercial_offer
    sells_to: sells_to
map_axis_labels:
  water_stream: "Water stream measured"
  driver: "Job the measurement does"
  regulatory_pressure: "Regulatory pressure"
  measurement_today: "How they measure today"
  target: "Contaminant detected"
  measurement_mode: "Measurement mode"
  commercial_offer: "What they sell"
  technology: "Technology"
  sells_to: "Sells to"
  stage: "Stage"
map_vocabularies:
  map: [client, startup, none]
  # Contaminant classes. `multi` is for analyser incumbents whose catalogue spans most of
  # the list; a company whose primary line is one class takes that class and lists the
  # rest under targets_all.
  target: [microplastics, microfibres, nanoplastics, pfas, heavy_metals, hydrocarbons, pathogens, nutrients, micropollutants, tss_turbidity, general_params, multi]
  # Where in the plant the sample is taken. Ordered upstream to downstream.
  water_stream: [intake, process, cooling, product_water, effluent, reuse, sludge, stormwater, distribution]
  # The job the measurement does for the buyer — what the number is FOR.
  driver: [research, treatment_optimisation, process_control, asset_protection, product_safety, disclosure, liability_defence, compliance]
  regulatory_pressure: [none, voluntary_standard, pending, enforced]
  measurement_today: [none, lab_grab, at_line, online]
  # How the vendor measures. Ordered from slowest (ship a sample) to continuous.
  measurement_mode: [lab_service, portable_field, at_line, online_continuous, data_platform]
  technology: [optical_imaging_ml, raman, ftir, light_scattering, fluorescence, flow_cytometry, electrochemical, mass_spec, thermal_pygcms, filtration_gravimetric, impedance, hyperspectral, other]
  # What is actually sold. Ordered from one-off to recurring outcome; the colour ramp runs
  # cold to warm along it, so a monitoring-as-a-service company reads warm.
  commercial_offer: [consulting, lab_testing_service, instrument_sale, compliance_data, monitoring_service]
  sells_to: [industrial_end_user, utility, lab, regulator, brand, research]
  stage: [pre_seed, seed, series_a, series_b, series_c, series_d_plus, private_established, public, incumbent_subsidiary]
  funding_source: [press, filing, self_stated, aggregator, unknown]
map_value_labels:
  target: {microplastics: "microplastics", microfibres: "microfibres", nanoplastics: "nanoplastics", pfas: "PFAS", heavy_metals: "heavy metals", hydrocarbons: "oil / hydrocarbons", pathogens: "pathogens", nutrients: "nutrients", micropollutants: "micropollutants", tss_turbidity: "TSS / turbidity", general_params: "general parameters", multi: "multi-parameter"}
  water_stream: {product_water: "product water", effluent: "effluent / discharge", reuse: "reuse / recycle"}
  driver: {treatment_optimisation: "treatment optimisation", process_control: "process control", asset_protection: "asset protection", product_safety: "product safety", disclosure: "ESG disclosure", liability_defence: "liability defence"}
  regulatory_pressure: {voluntary_standard: "voluntary standard"}
  measurement_mode: {lab_service: "lab sample", portable_field: "portable / field", at_line: "at-line", online_continuous: "online continuous", data_platform: "data platform only"}
  commercial_offer: {lab_testing_service: "testing service", instrument_sale: "instrument", compliance_data: "compliance data", monitoring_service: "monitoring service"}
  sells_to: {industrial_end_user: "industrial end user"}
  stage: {pre_seed: "pre-seed", series_a: "Series A", series_b: "Series B", series_c: "Series C", series_d_plus: "Series D+", private_established: "private, established", incumbent_subsidiary: "incumbent subsidiary"}
---

# Companies — contaminant detection in industrial water

Started 2026-09-09 from a blank registry. The first batch is the lab-testing-as-a-service
slice of the supply side (12 entries, every one from a page opened that day); the online
analyser incumbents, the monitoring-as-a-service startups, the dedicated microplastic
instrument makers and the whole demand side are still to be sourced. Until they are, the
maps show one column of one side and should be read as such.


## Eurofins Scientific

id: CO1
map: startup
tier_side: supply
tier: ""
canonical_name: Eurofins Scientific
country: LU
founded: 
stage: public
total_raised_usd: 
funding_source: unknown
headcount: 
sector: Lab testing — drinking water utilities, bottled water, food_beverage
target: microplastics
targets_all: [microplastics, pfas, heavy_metals, hydrocarbons, pathogens, nutrients, micropollutants, general_params, multi]
measurement_mode: lab_service
technology: raman
size_floor_um: 20
commercial_offer: lab_testing_service
sells_to: industrial_end_user
sells_to_all: [industrial_end_user, utility, regulator, brand, research]
industries_served: [drinking water utilities, bottled water, food_beverage, consumer products, municipal wastewater, environmental consultancies, textiles (microfibre shedding, Spain lab)]
water_streams: [intake, effluent, product_water, sludge, distribution]
makes_or_does: >
  Sells per-sample microplastics analysis through several regional labs with different methods: the US service (Eurofins SFA-origin) uses high-resolution visual microscopy plus Raman spectroscopy in a clean room and reports polymer ID, per-polymer counts and total count for 10 polymers (PA, PC, PE, PET, PMMA, PP, PU, PVC, PS, PTFE) over "20 µm to 500 µm" in treated drinking water, aqueous consumer products and non-potable environmental water; the Melbourne lab (est. 2019, NATA ISO/IEC 17025 for potable water late 2023 and all water matrices 2024) uses LDIR over "20 to 5,000 µm"; the European "Microplastics Competence Centre" sells accredited Pyr-GC/MS mass quantification of >10 polymers plus tyre-wear rubbers (NR, SBR, BR) reported in µg/L for drinking, waste, sea, clean and rinse water (sample: 2 x 1 L plus a blank per batch). No public price or turnaround; the corporate page header shows a listed share price (EUR 70.94), confirming public status. Also a full PFAS/general water-chemistry menu.
why_it_matters: >
  The world's largest lab group treats microplastics as one specialty line among dozens, bought sample-by-sample with a 20 µm floor for particle counting and mass-only py-GC/MS for dirty effluent, so it is a feature of a broad water-analytics catalogue rather than a standalone business, and it leaves sub-20 µm particle counting in effluent unserved.
source_url: https://www.eurofins.com/en-us/environment-testing/services/specialty-services/microplastics/
sources_note: "also read: https://www.eurofins.com/en-uk/water-hygiene-testing/microplastics-testing/ ; https://www.eurofins.com/en-au/environment-testing/speciality-analysis/microplastics/ ; https://www.eurofins.com/about-us/"
first_added: 2026-09-09
source_date: 2026-09-09

## SGS (SGS Institut Fresenius)

id: CO2
map: startup
tier_side: supply
tier: ""
canonical_name: SGS (SGS Institut Fresenius)
country: CH
founded: 
stage: public
total_raised_usd: 
funding_source: unknown
headcount: 
sector: Lab testing — bottled/mineral water, food_beverage (soft drinks, beer
target: microplastics
targets_all: [microplastics, pfas, heavy_metals, hydrocarbons, pathogens, micropollutants, general_params, multi]
measurement_mode: lab_service
technology: ftir
size_floor_um: 
commercial_offer: lab_testing_service
sells_to: industrial_end_user
sells_to_all: [industrial_end_user, utility, brand, research, regulator]
industries_served: [bottled/mineral water, food_beverage (soft drinks, beer, salt, tea bags), consumer appliances (kettles, coffee machines), packaging, water and waste management]
water_streams: [product_water, process, intake]
makes_or_does: >
  SGS Institut Fresenius (Dresden, DE) sells microplastics analysis by FT-IR spectroscopy, Raman microspectroscopy, SEM-EDX and optical microscopy for particle counting and size distribution, in "mineral water, spring water, and process water", soft drinks, beer, salt and consumer products, following "ISO 16094-2:2025 for determining microplastics in water samples". The page defines microplastics as 1 µm to 5 mm but does not state its own detection floor, price or turnaround; the group-level page (which per search results names Varna and Singapore labs with QCL-IR, FTIR-microscopy and pyr-GCMS across soil, sludge, water, biota, waste) returned 403 and is UNVERIFIED here. Stage "public" (SIX-listed) is common knowledge but not stated on the opened page: UNVERIFIED.
why_it_matters: >
  SGS positions microplastics as a niche "special analytics" line sold mainly to bottled-water, beverage and consumer-product brands, i.e. product-quality/reputation buyers rather than effluent compliance buyers, which says the industrial-effluent microplastics market is not yet where the big TIC firms see demand.
source_url: https://sgs-institut-fresenius.de/en/material-failure-analysis/special-analytics/microplastics
first_added: 2026-09-09
source_date: 2026-09-09

## ALS Global (incl. former WESSLING, now ALS Germany)

id: CO3
map: startup
tier_side: supply
tier: ""
canonical_name: ALS Global (incl. former WESSLING, now ALS Germany)
country: AU
founded: 
stage: public
total_raised_usd: 
funding_source: unknown
headcount: 
sector: Lab testing — surface water monitoring, drinking water, municipal wastewater
target: microplastics
targets_all: [microplastics, pfas, heavy_metals, hydrocarbons, pathogens, nutrients, micropollutants, general_params, multi]
measurement_mode: lab_service
technology: ftir
size_floor_um: 10
commercial_offer: lab_testing_service
sells_to: industrial_end_user
sells_to_all: [industrial_end_user, utility, regulator, research, brand]
industries_served: [surface water monitoring, drinking water, municipal wastewater, fisheries/biota, soil, environmental consultancies]
water_streams: [intake, effluent, product_water, distribution]
makes_or_does: >
  ALS sells three tiers of microplastics analysis for water: a Nile Red staining plus image-analysis count ("typically used to measure particles down to 100 µm"), ATR-FTIR ("down to 50 µm") and imaging µ-FTIR ("down to 10 µm"), with polymer ID; a 2023 corporate article adds pyrolysis-GCMS for mass quantification and says the Malaysia lab was seeking accreditation for wastewater, fish and soil, with river/marine water to follow, and that services also run in the US, Europe and Middle East. ALS Germany (WESSLING, rebranded "ALS Germany" on 2025-09-29 per its news feed) offers Raman microscopy, FT-IR microscopy and pyrolysis-GC/MS with full sample prep and detection for drinking water and environmental waters, defining particles as 1 µm to 5 mm. No public price or turnaround. Stage "public" (ASX-listed) not stated on opened pages: UNVERIFIED.
why_it_matters: >
  ALS's tiered menu (100 µm dye count, 50 µm ATR, 10 µm imaging FTIR) shows the lab market prices resolution as an upsell and that the WESSLING dedicated microplastics lab could not stay independent, absorbed into a full-service group, which argues microplastics is a feature inside a broad water-testing catalogue rather than a standalone market at lab-service scale.
source_url: https://www.alsglobal.com/en/water-industry/surface-water/microplastics
sources_note: "also read: https://www.alsglobal.com/en/news-and-publications/2023/10/the-growing-threat-of-microplastics-how-als-is-advancing-testing ; https://www.alsglobal.com/de/Deutschland/Mikroplastik ; http://www.alsglobal.com/Germany/en/services/microanalysis-and-nanoanalysis/microplastics/microplastics-in-the-environment"
first_added: 2026-09-09
source_date: 2026-09-09

## Intertek

id: CO4
map: startup
tier_side: supply
tier: ""
canonical_name: Intertek
country: GB
founded: 
stage: public
total_raised_usd: 
funding_source: unknown
headcount: 45000
sector: Lab testing — food_beverage (table water, drinking water, honey
target: microplastics
targets_all: [microplastics, pfas, heavy_metals, pathogens, general_params, multi]
measurement_mode: lab_service
technology: ftir
size_floor_um: 
commercial_offer: lab_testing_service
sells_to: brand
sells_to_all: [brand, industrial_end_user, research]
industries_served: [food_beverage (table water, drinking water, honey, salt, beer, spirits), consumer products]
water_streams: [product_water]
makes_or_does: >
  Intertek's food division sells "identification and quantification of microplastics in selected samples" using sample preparation, light microscopy, FTIR microscopy, Raman microscopy and SEM/EDX, aimed at "table water, drinking water, honey, table salt, drinks, beer, and spirits". The page states no size floor, turnaround, price or accreditation. Separate PFAS and general water lines exist elsewhere in the group.
why_it_matters: >
  Intertek files microplastics under food testing, not environmental or industrial water, another signal that TIC incumbents currently see microplastic demand coming from product/brand reputation rather than from effluent or process-water compliance.
source_url: https://www.intertek.com/food/microplastics-testing/
sources_note: "also read: https://www.intertek.com/about/"
first_added: 2026-09-09
source_date: 2026-09-09

## Measurlabs (Measur Oy)

id: CO5
map: startup
tier_side: supply
tier: ""
canonical_name: Measurlabs (Measur Oy)
country: FI
founded: 2017
stage: seed
total_raised_usd: 
funding_source: unknown
headcount: 28
sector: Lab testing — bottled water, drinking water, municipal wastewater
target: microplastics
targets_all: [microplastics, pfas, heavy_metals, micropollutants, general_params, multi]
measurement_mode: lab_service
technology: raman
size_floor_um: 1
commercial_offer: lab_testing_service
sells_to: industrial_end_user
sells_to_all: [industrial_end_user, brand, research, utility]
industries_served: [bottled water, drinking water, municipal wastewater, industrial process water, packaging, cosmetics, food_beverage, materials R&D]
water_streams: [product_water, effluent, process, intake]
makes_or_does: >
  Measurlabs is a marketplace that routes samples to "several hundred" partner accredited labs through hubs in Helsinki, Cambridge and Palo Alto, and publishes list prices: clean-water microplastics by accredited µFTIR to ISO/DIS 16094-2 (10 to 5,000 µm) or accredited in-house µRaman (1 to 5,000 µm) at 190 EUR per 1 L sample plus 97 EUR order fee, 3-week turnaround; wastewater/natural water by µFTIR to ISO 24187 (10 µm floor, size bins 10-50/50-100/100-500/>500 µm) at 390 EUR per 500 mL sample plus 97 EUR fee, 4-week turnaround, with surcharges for "process water, industrial water, samples with very high particle loads or fibers"; plus TED-GC-MS and py-GC-MS mass methods. Raised EUR 2.5M seed (Sept 2023, led by VentureFriends with Lifeline Ventures, Tesi, Curus); the USD 4.91M total is an aggregator figure.
why_it_matters: >
  The only vendor with public prices puts a 1 µm-capable microplastics count at ~190-390 EUR and 3-4 weeks per sample, which is the cost/latency ceiling any online or at-line effluent monitor competes against, and its marketplace model (no own labs) shows microplastics demand is real but thin enough to be served by brokering spare capacity rather than dedicated labs.
source_url: https://measurlabs.com/products/microplastics-clean-water-u-raman/
sources_note: "also read: https://measurlabs.com/products/microplastics-in-water-and-wastewater-micro-raman/ ; https://measurlabs.com/about/ ; https://measurlabs.com/blog/measurlabs-seed-round/"
first_added: 2026-09-09
source_date: 2026-09-09

## Brooks Applied Labs (an IEH company)

id: CO6
map: startup
tier_side: supply
tier: ""
canonical_name: Brooks Applied Labs (an IEH company)
country: US
founded: 
stage: incumbent_subsidiary
total_raised_usd: 
funding_source: unknown
headcount: 
sector: Lab testing — food_beverage (infant formula, baby food, meats
target: microplastics
targets_all: [microplastics, heavy_metals, multi]
measurement_mode: lab_service
technology: ftir
size_floor_um: 
commercial_offer: lab_testing_service
sells_to: industrial_end_user
sells_to_all: [industrial_end_user, brand, research, regulator]
industries_served: [food_beverage (infant formula, baby food, meats, fish, coffee, tea, beer, soft drinks), supplements, pharma, chemicals and salts, surface water and sediment monitoring, drinking water]
water_streams: [intake, product_water, process]
makes_or_does: >
  A trace-metals speciation lab in Seattle, WA (ANAB ISO/IEC 17025, TNI NELAP) that added "high throughput" microplastics testing by LDIR (laser direct infrared imaging), reporting particle counts, polymer identification and particle size in one automated run, for surface water, sediment, drinking water, foods, beverages, supplements and pharmaceuticals, and pitched at monitoring changes "from source to finished products". Size floor, price and turnaround are not published. Parent IEH is stated on the page; no founding date or headcount given.
why_it_matters: >
  A specialty metals lab bolting LDIR microplastics onto its menu to serve food and pharma process-water monitoring shows the current paying buyer is product-quality QA in manufacturing, and that microplastics is being sold as an add-on to an existing lab relationship rather than as a standalone service.
source_url: https://brooksapplied.com/services/microplastics-testing-services/
sources_note: "also read: https://brooksapplied.com/"
first_added: 2026-09-09
source_date: 2026-09-09

## SimpleLab (Tap Score)

id: CO7
map: startup
tier_side: supply
tier: ""
canonical_name: SimpleLab (Tap Score)
country: US
founded: 
stage: unknown
total_raised_usd: 
funding_source: unknown
headcount: 
sector: Lab testing — residential drinking water, bottled water, small water systems
target: microplastics
targets_all: [microplastics, pfas, heavy_metals, pathogens, nutrients, micropollutants, general_params, multi]
measurement_mode: lab_service
technology: raman
size_floor_um: 1
commercial_offer: lab_testing_service
sells_to: industrial_end_user
sells_to_all: [industrial_end_user, brand, research]
industries_served: [residential drinking water, bottled water, small water systems, real estate, consumer brands]
water_streams: [distribution, product_water]
makes_or_does: >
  Sells a mail-in "Microplastics Drinking Water Test Kit" at USD 598 that reports presence/absence of particles between 1 and 10 µm and quantification down to 10 µm across six size bins (<10, 10-50, 50-100, 100-500, 500-1000, 1000-5000 µm), 12 business days lab turnaround plus 3-5 days reporting; polymer ID is sold separately as an "Advanced Microplastics" test. Restricted to tap or bottled water ("cannot be used to analyze marine or surface water"). Routes samples through "a nationwide network of 250+ certified, independent laboratories". Method (optical/polarised microscopy plus Raman) appears only in search snippets, not on the opened product page: UNVERIFIED. Funding figure is an aggregator number.
why_it_matters: >
  A consumer/prosumer broker charging USD 598 for a single 1 µm-sensitive count with no polymer ID sets the retail price point for microplastics in water and shows willingness to pay exists at the household level, but only for clean drinking water, not effluent.
source_url: https://mytapscore.com/products/microplastics-water-test
sources_note: "also read: https://mytapscore.com/pages/our-story"
first_added: 2026-09-09
source_date: 2026-09-09

## McCampbell Analytical

id: CO8
map: startup
tier_side: supply
tier: ""
canonical_name: McCampbell Analytical
country: US
founded: 1991
stage: private_established
total_raised_usd: 
funding_source: unknown
headcount: 
sector: Lab testing — drinking water utilities (California SWRCB monitoring), municipal wastewater, stormwater
target: microplastics
targets_all: [microplastics, pfas, heavy_metals, hydrocarbons, pathogens, nutrients, general_params, multi]
measurement_mode: lab_service
technology: ftir
size_floor_um: 
commercial_offer: lab_testing_service
sells_to: utility
sells_to_all: [utility, industrial_end_user, regulator, research]
industries_served: [drinking water utilities (California SWRCB monitoring), municipal wastewater, stormwater, environmental consultancies, soil and sediment]
water_streams: [intake, distribution, effluent, stormwater, product_water]
makes_or_does: >
  A Pittsburg, CA environmental lab ("Serving the Bay Area since 1991"; NELAP, ELAP, DoD, USDA, AIHA-LAP) that is CA ELAP-certified for microplastics in drinking water under the State Water Board method "SWB-MP1-rev1", using automated microFTIR with a focal-plane-array detector for small particles and single-particle ATR for larger ones, and offers wastewater and stormwater monitoring support. Cites the California definition of 1 to 5,000 µm but does not state its own reporting floor, price or microplastics turnaround (PFAS is quoted at 10-day standard / 5-day expedited).
why_it_matters: >
  The first US regulatory driver for microplastics in water (California drinking-water monitoring) is being served by an ordinary regional compliance lab adding a microFTIR line, which says regulation turns microplastics into a routine lab parameter, not a new market with new vendors.
source_url: https://www.mccampbell.com/microplastics.php
first_added: 2026-09-09
source_date: 2026-09-09

## Pace Analytical

id: CO9
map: startup
tier_side: supply
tier: ""
canonical_name: Pace Analytical
country: US
founded: 1978
stage: private_established
total_raised_usd: 
funding_source: unknown
headcount: 
sector: Lab testing — public water utilities, manufacturing, energy
target: pfas
targets_all: [pfas, heavy_metals, hydrocarbons, pathogens, nutrients, micropollutants, general_params, multi]
measurement_mode: lab_service
technology: mass_spec
size_floor_um: 
commercial_offer: lab_testing_service
sells_to: utility
sells_to_all: [utility, industrial_end_user, regulator, research]
industries_served: [public water utilities, manufacturing, energy, healthcare, government/DoD, landfills, firefighting foam users, wastewater treatment]
water_streams: [intake, distribution, effluent, sludge, stormwater, process]
makes_or_does: >
  "The largest American-owned laboratory network" (founded 1978) sells PFAS testing by LC-MS/MS and organic-fluorine methods across nine matrix categories: AFFF, air and emissions, biota, consumer/industrial products, drinking water, ground and surface water, landfill leachate, soil/sediment, and wastewater/sludge/biosolids, with "reporting limits at or below all program requirements", "PFAS RAPID TURNAROUND TIME SERVICES for every matrix", and certification by NELAC, ISO, DOD, DOE and every state PFAS program. No price or numeric limits published. No microplastics service is mentioned anywhere on the PFAS or company pages opened.
why_it_matters: >
  The biggest US environmental lab network has built a dedicated PFAS franchise with rapid turnaround and treatability studies but lists no microplastics service at all, which is the clearest sign that in the US lab market PFAS is a standalone regulated market while microplastics is not yet one.
source_url: https://www.pacelabs.com/analytical-environmental/pfas/
sources_note: "also read: https://www.pacelabs.com/company/"
first_added: 2026-09-09
source_date: 2026-09-09

## Element Materials Technology

id: CO10
map: startup
tier_side: supply
tier: ""
canonical_name: Element Materials Technology
country: GB
founded: 
stage: private_established
total_raised_usd: 
funding_source: unknown
headcount: 
sector: Lab testing — drinking water, industrial emissions, firefighting foam
target: pfas
targets_all: [pfas, heavy_metals, hydrocarbons, pathogens, nutrients, general_params, multi]
measurement_mode: lab_service
technology: mass_spec
size_floor_um: 
commercial_offer: lab_testing_service
sells_to: industrial_end_user
sells_to_all: [industrial_end_user, utility, regulator, brand]
industries_served: [drinking water, industrial emissions, firefighting foam, food, construction (concrete), consumer products, landfill leachate, biosolids]
water_streams: [intake, distribution, effluent, sludge]
makes_or_does: >
  Sells ISO/IEC 17025 PFAS analysis from dedicated labs in Deeside (UK) and Fort Wayne (US): EPA 533 and 537.1 Rev 2.0 for drinking water, EPA 1633A for soil, groundwater, surface water, leachate and biosolids, a TOP assay, a UK 53-substance target list covering the 20 PFAS in the EU Drinking Water Directive, "50+ PFAS compounds", detection to "parts per trillion" and "sub parts per trillion" on Agilent 1290/6495 triple-quad LC-MS/MS, and "standard turnaround at Element's Fort Wayne laboratory is 5-10 business days". No price. No microplastics service on the page. Ownership (Temasek) not stated on opened pages: UNVERIFIED.
why_it_matters: >
  A materials-testing group entered water contaminants specifically through PFAS with regulated methods and ppt limits, and skipped microplastics entirely, which confirms lab entrants follow regulation-defined analytes and that microplastics lacks the regulatory pull to justify a dedicated line.
source_url: https://www.element.com/environmental-testing/pfas-testing
first_added: 2026-09-09
source_date: 2026-09-09

## Onterris (formerly Montrose Environmental Group / Enthalpy Analytical)

id: CO11
map: startup
tier_side: supply
tier: ""
canonical_name: Onterris (formerly Montrose Environmental Group / Enthalpy Analytical)
country: US
founded: 
stage: public
total_raised_usd: 
funding_source: unknown
headcount: 
sector: Lab testing — chemical, energy, government
target: pfas
targets_all: [pfas, heavy_metals, hydrocarbons, micropollutants, general_params, multi]
measurement_mode: lab_service
technology: mass_spec
size_floor_um: 
commercial_offer: lab_testing_service
sells_to: industrial_end_user
sells_to_all: [industrial_end_user, utility, regulator]
industries_served: [chemical, energy, government, manufacturing, mining, solid waste/landfill, water utilities]
water_streams: [intake, distribution, effluent, stormwater, sludge]
makes_or_does: >
  Montrose Environmental Group "has rebranded as Onterris" and "Enthalpy Analytical is now Onterris, providing accredited environmental laboratory testing, data analysis, and regulatory support across a national network of labs" in the US, Canada and Australia. PFAS testing covers drinking water, non-potable water, solids, air and tissue using "established EPA methods", isotope dilution, Total Oxidizable Precursor Assay and adsorbable organic fluorine, sold alongside PFAS treatment and consulting. Opened pages give no detection limits, prices, turnaround or accreditation details (search snippets cite DoD 1633 accreditation at Wilmington NC and El Dorado Hills CA, Feb 2023: UNVERIFIED). Stage "public" (NYSE) not stated on opened pages: UNVERIFIED. No microplastics service mentioned.
why_it_matters: >
  A listed environmental-services roll-up bundles PFAS lab data with consulting and treatment into one "PFAS data" offer and does not mention microplastics, which says the lab-plus-treatment revenue model has formed around PFAS and has no microplastics counterpart yet.
source_url: https://www.onterris.com/treatment-technologies/pfas-testing-analysis
sources_note: "also read: https://www.onterris.com/who-we-are/montrose-environmental-group-is-now-onterris ; https://www.onterris.com/solutions/water-consulting-testing-and-treatment/water-treatment/pfas-data"
first_added: 2026-09-09
source_date: 2026-09-09

## Bureau Veritas (BV Laboratories, North America)

id: CO12
map: startup
tier_side: supply
tier: ""
canonical_name: Bureau Veritas (BV Laboratories, North America)
country: FR
founded: 
stage: public
total_raised_usd: 
funding_source: unknown
headcount: 
sector: Lab testing — textile and carpet manufacturing, food packaging, medical devices
target: pfas
targets_all: [pfas, heavy_metals, hydrocarbons, pathogens, nutrients, general_params, multi]
measurement_mode: lab_service
technology: mass_spec
size_floor_um: 
commercial_offer: lab_testing_service
sells_to: industrial_end_user
sells_to_all: [industrial_end_user, utility, regulator]
industries_served: [textile and carpet manufacturing, food packaging, medical devices, pharma, cosmetics, electronics, firefighting, wastewater treatment, oil_gas produced water]
water_streams: [intake, effluent, process, sludge]
makes_or_does: >
  BV's North American labs sell three PFAS approaches: targeted PFAS by LC/MS/MS ("all matrices"), a Total Oxidizable Precursor (TOPS) assay, and Total Organofluorine by combustion ion chromatography (TOF-CIC), with DoD ELAP accreditation "for EPA Draft Method 1633" covering "all 40 PFAS under EPA 1633 for water and solid matrices"; matrices named are water, tissue, landfill leachate and sediment. No detection limits, prices, turnaround or lab locations on the page; pricing is by fee schedule. No microplastics service found on BV's water pages. Stage "public" (Euronext) not stated on opened page: UNVERIFIED.
why_it_matters: >
  Another top-tier TIC group whose water lab menu goes deep on PFAS (three orthogonal methods) and has nothing on microplastics, reinforcing that microplastics is currently a feature offered by a subset of labs, not a market that every full-service lab feels it must be in.
source_url: https://www.bvna.com/pfas-testing
first_added: 2026-09-09
source_date: 2026-09-09
