---
purpose: The evidence ledger — every graded claim that moves an assumption, each linked to the node it updates and the direction it moves it.
idea: industrial-process-data-infrastructure
last_updated: 2026-09-14
next_evidence_id: E5
---

# Evidence ledger

Started 2026-09-14 with the H3 timing desk check. Entries are appended, never renumbered; a retired ID is burned.

```yaml
entries:
  - id: E1
    date: 2026-09-14
    source: "State Water Resources Control Board, Division of Drinking Water — Hélène Baribeau, 'Legislative Requirements for Microplastics in Drinking Water', workshop slides 11/13 Feb 2025, slide 20 (timeline). https://ftp.sccwrp.org/pub/download/MICROPLASTICS_WORKSHOP_DRINKING_WATER/MPDW%20workshop%20materials/Presentation%20slides/1.%20MP%20Legislative%20Requirements_SWRCB-DDW.pdf"
    source_type: regulatory_document
    claim: "The Board's programme timeline shows 'Fall 2023 – Fall 2025: Phase I Monitoring' and 'Fall 2026 – Fall 2028: Phase II Monitoring'; sampling by ASTM D8332-20 or in-line filtration; analysis by Raman (≥20 µm) or FTIR (≥50 µm); no notification level ('insufficient evidence', Sept 2021)."
    assumption_linked: H3A1
    verdict: supports
    confidence: 4
    notes: "Phase II is on the regulator's own published timeline as of Feb 2025, which is stronger than the 2022 handbook's 'if it occurs'. Still a plan, not a monitoring order issued: the list of Phase II systems and the sampling frequency are not in the deck."
    next_question_raised: "Which systems receive Phase II monitoring orders, at what frequency, and has any order been issued yet?"
  - id: E2
    date: 2026-09-14
    source: "Same deck, slides 13-18 (Policy Handbook key points), and the Board's microplastics page (last updated 2025-12-26) https://www.waterboards.ca.gov/drinking_water/certlic/drinkingwater/microplastics.html"
    source_type: regulatory_document
    claim: "Monitoring runs through 'monitoring orders'; results are reported to DDW and 'positive detections in CCRs' (the utility's annual Consumer Confidence Report); surrogates (turbidity, TOC, TSS, TDS) are analysed alongside; the handbook requires 'public disclosure of those results'."
    assumption_linked: H3A1
    verdict: supports
    confidence: 4
    notes: "A duty attaches to a result beyond filing it: public disclosure in the CCR. That is the obligation H3A1's disconfirmation asked for. It says nothing about whether any utility experiences it as a cost or a decision — that is H3A2's question and needs a conversation."
    next_question_raised: "Has any Phase I system had to print a positive detection in its CCR, and what happened when it did?"
  - id: E3
    date: 2026-09-14
    source: "ZDHC Wastewater Guidelines Version 2.2, September 2024, Part C 'Microfibres/fibre fragmentation', pp. 79-80, incl. 'Requirements for monitoring microfibre discharge'. https://downloads.roadmaptozero.com/output/ZDHC-Wastewater-Guidelines (PDF read 2026-09-14)"
    source_type: industry_standard
    claim: "The guideline that H&M, Inditex and most brands make mills test against does address fibre fragmentation, but the only requirement is on TSS: 'Monitor the TSS results and ensure that it meets at least the Foundational Level ... If the values of TSS are higher than the Foundational Level, suppliers must undertake a RCA and upload a CAP to the ZDHC Gateway.' Microfibre counting itself is only recommended: 'Facilities should consider determining their own microfibre release profile using a Dynamic Image Analysis (DIA) method, after which TSS tests can be used to monitor microfibre releases.' It also states 'limits are likely to be revised downwards in future updates.'"
    assumption_linked: H1A2
    verdict: ambiguous
    confidence: 4
    notes: "Supports the half of H1A2 that says mills ARE being asked about fibre release by their brands' standard, and undercuts the half that says they cannot produce the number: the number they are asked for is TSS, which every mill already measures. A microfibre count is optional. This is the 'existing workaround' H1A5 asks about, stated in the industry's own rulebook."
    next_question_raised: "Has any mill actually run the recommended DIA release profile, and did a brand ever ask to see it?"
  - id: E4
    date: 2026-09-14
    source: "Inditex, 'Green to Wear 3.2 July 2026 — Sustainability Standard for wet process facilities (Pre-treatment, Dyeing, Printing, Finishing, Washing, Tanneries and Synthetic leather)', PDF created 2026-06-19, B-ranking non-compliance list. https://www.inditex.com/itxcomweb/api/media/9af42004-8584-4681-917f-eca403026167/GTW%202.1%20English%202023.pdf (URL serves the 3.2 text; read 2026-09-14)"
    source_type: industry_standard
    claim: "A wet-processing mill is rated 'B' rather than best-in-class 'A' if 'Fibers and microfibers are released into the environment without any internal control.' The same standard requires wastewater to be 'tested according to ZDHC Wastewater Guidelines twice a year', results disclosed on the ZDHC Gateway, and direct discharge to meet the ZDHC Progressive level."
    assumption_linked: H1A2
    verdict: supports
    confidence: 4
    notes: "The largest fashion buyer now writes fibre release into its supplier grading for dyeing, printing, finishing and washing plants, effective July 2026. It asks for 'internal control', not a measured number, and the rating cost of a B is not stated. A mill supplying Inditex is therefore asked about microfibres today; what answering costs, and whether anyone asks for a figure, is still the interview question."
    next_question_raised: "What does an Inditex-audited mill show the auditor as 'internal control' of fibre release, and did the B/A distinction ever cost it an order?"
```
