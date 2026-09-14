---
purpose: The evidence ledger — every graded claim that moves an assumption, each linked to the node it updates and the direction it moves it.
idea: industrial-process-data-infrastructure
last_updated: 2026-09-14
next_evidence_id: E3
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
```
