---
purpose: The evidence ledger for this idea — every graded claim, linked to the assumption it moves and the direction it moves it.
idea: custom-kitchen-cabinets
last_updated: 2026-08-31
---

# Evidence ledger — custom-kitchen-cabinets

Everything below is desk measurement carried in from the pipeline in `research/`. Every entry
is `our_observation` at confidence 2, which is the correct grade for a number we computed
ourselves from public data: it is reproducible, it moved the thesis once, and it is not buyer
evidence. No dealer, remodeler or shop has been asked anything yet — which is why every
assumption in the graph still reads `untested`.

Provenance for every figure: `research/data/MANIFEST.jsonl` carries one line per fetch with
url, time, row count and status. Nothing here quotes a number without one.

```yaml
entries:
  - id: E1
    date: 2026-08-28
    source: >-
      research/data/processed/custom_categories_adjusted.csv — Google Trends, anchored
      custom/generic keyword pairs across 24 furniture and joinery categories
    source_type: our_observation
    claim: >-
      "custom cabinets" runs at 7.61% of "kitchen cabinets" search volume — an order of
      magnitude above any furniture article, where the median custom/generic pair is 0.55%
      and every pair is under 1%.
    assumption_linked: H1A6
    verdict: supports
    confidence: 2
    notes: >-
      Anchored measurement: every Trends batch carries the same anchor term and is rescaled
      by it, so the categories are comparable to each other. This is a floor on appetite, not
      an estimate of it — it measures who wants custom at today's premium and today's wait.
      Graded 2 because it is our own computation from a public source, not buyer testimony.
    next_question_raised: >-
      Does the pool widen when the premium and the lead time come down, or does the same set
      of buyers simply pay less?

  - id: E2
    date: 2026-08-28
    source: >-
      research/data/processed/trends_custom_related.csv — Google Trends related queries for
      the custom/generic pairs
    source_type: our_observation
    claim: >-
      Cabinets are the only one of the 24 categories where the related queries carry
      commercial intent — "custom cabinets near me", "custom cabinets cost", "custom
      cabinetry" — five such queries against zero for every furniture term tested.
    assumption_linked: H1A6
    verdict: supports
    confidence: 2
    notes: >-
      For most furniture terms a large share of related traffic resolves to accessories
      (chair covers, table protectors) rather than the product. Intent, not just volume, is
      what separates cabinets here.
    next_question_raised: >-
      Is that intent the homeowner's or the trade's? The queries cannot tell them apart, and
      the two imply different go-to-markets.

  - id: E3
    date: 2026-08-28
    source: >-
      research/data/processed/cabinet_tam_model.json — US Census County Business Patterns,
      NAICS 337110 wood kitchen cabinet and countertop manufacturing
    source_type: our_observation
    claim: >-
      The US industry is 6,118 establishments sharing roughly $16.02bn of revenue, built up
      from $4.85bn of payroll — overwhelmingly small shops, with no firm large enough to
      carry a serious software budget.
    assumption_linked: H1A8
    verdict: supports
    confidence: 2
    notes: >-
      Built from Census payroll upward rather than from a market report downward. The
      fragmentation is the load-bearing part: it is why nobody in the industry has removed
      their own design bottleneck, and it is also why no single incumbent can be displaced.
    next_question_raised: >-
      What do these shops actually run today, and how much of the design job does it already
      do for them?

  - id: E4
    date: 2026-08-28
    source: >-
      research/scripts/build_cabinet_factory.py — station cycle times and labour model for a
      27-linear-foot frameless kitchen
    source_type: our_observation
    claim: >-
      Design and engineering accounts for 13.5 hours per kitchen against 12.2 hours across all
      six shop-floor steps — 52% of human labour happens before a sheet is cut.
    assumption_linked: H1A7
    verdict: supports
    confidence: 2
    notes: >-
      GRADED DOWN in substance even at 2: this is derived from our own build model using
      published cycle times, not observed inside a live shop. It is the single number the
      whole belief rests on and it has never been checked against a real business. Treat it
      as a hypothesis to test in H1A7, not as support for it.
    next_question_raised: >-
      How many hours do real shop owners say go into a kitchen before cutting, and does the
      split survive contact with one?

  - id: E5
    date: 2026-08-28
    source: research/scripts/build_cabinet_factory.py — constraint analysis over the same model
    source_type: our_observation
    claim: >-
      Annual capacity by station: machines 228 kitchens, shop floor with two people 306, front
      office with one designer 138. The front office binds; the machines idle at roughly 60%.
    assumption_linked: H1A7
    verdict: supports
    confidence: 2
    notes: >-
      Same caveat as E4 — derived, not observed. The conclusion it drives is what makes the
      company a software company rather than a robotics one: automating the shop floor would
      be automating the station that already has 40% spare capacity.
    next_question_raised: >-
      Do shop owners name the front office as their constraint when asked without being
      offered the answer?

  - id: E6
    date: 2026-08-28
    source: research/REPORT.md — CEX article scorecard and anchored custom-share measurement
    source_type: our_observation
    claim: >-
      Across all nine CEX furniture lines the custom framing runs well under 1% of the generic
      term, median 0.55% for the best-scoring article. The furniture version of this thesis
      buys against a ceiling roughly fourteen times thinner than cabinets.
    assumption_linked: H1A6
    verdict: supports
    confidence: 2
    notes: >-
      This is the measurement that moved the idea from configurable furniture to fitted
      cabinetry. It is evidence about where NOT to go, which is why it is logged: without it,
      the cabinet framing looks like a preference rather than a result.
    next_question_raised: >-
      Is there anything in fitted joinery adjacent to kitchens — closets, built-ins, vanities
      — that carries the same commercial intent?
```
