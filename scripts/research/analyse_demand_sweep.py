"""Rank where "make me this" demand actually lands — corrected for what the words also mean.

`analyse_custom_demand.py` ranks furniture articles against each other. This ranks whole
FAMILIES against each other, across every material, and it exists because the raw sweep
index is wrong in a way that would send outreach at the wrong people:

  "custom wheels"        1.522 raw — but its top related queries are `hot wheels custom
                         wheels` (a die-cast toy) and `rimtyme custom wheels and tires`
                         (a tire retail chain). Almost none of it is manufacture-to-order.
  "machine shop near me" 0.459 raw — but `sewing machine shop near me`, `washing machine
                         shop near me` and `diesel machine shop near me` are appliance and
                         engine repair. The machining share is a minority of the term.

So every term is discounted by the share of its own related queries that are actually
about having something made. That share is measured off the related-query list Google
returns for the term, against a declared off-topic vocabulary — auditable, and visible in
the output rather than buried in a coefficient.

Three columns carry the answer, and they are deliberately not collapsed into one number:

  adjusted     level of demand, contamination removed         — how many people
  commercial   share of related queries with buying intent    — how ready they are
  resolved     whether the index measured anything at all     — whether to believe it

A term that is THIN is not a small market. It is an unmeasured one: Google's index
quantises to integers, so a term that sits at 0 or 1 for most weeks has no recoverable
ordering. Reporting those as "low demand" is the mistake this column exists to prevent.
"""
from __future__ import annotations

import sys
from collections import defaultdict

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import log, read_csv, record, save_csv  # noqa: E402

# Off-topic vocabulary, per seed term. Each entry is a substring that, when it appears in
# a related query, means the searcher wants something OTHER than a thing manufactured to
# order. Declared per-term rather than globally because the same word is contamination in
# one family and the product itself in another ("tires" pollutes custom wheels; "acrylic"
# is the product in plastics).
OFF_TOPIC: dict[str, list[str]] = {
    # die-cast toys and tire-and-rim retail chains, not wheel manufacture
    "custom wheels": ["hot wheels", "rimtyme", "tire", "tires", "and tires"],
    # domestic appliance and engine repair shops share the words "machine shop"
    "machine shop near me": ["sewing", "washing", "auto ", "automotive", "car ",
                             "diesel", "engine"],
    # nail salons; "custom acrylic nails" is a manicure
    "custom acrylic": ["nail", "nails"],
    # the toy again, plus apparel printing that is not fabrication
    "custom car parts": ["hot wheels", "diecast"],
    # printing a flat sheet is not machining it; kept separate so the sign family can be
    # split into "printed" and "fabricated" downstream rather than scored as one thing
    "custom signs": [],
    # a salary search is a jobseeker, not a buyer
    "precision machining": ["salary", "jobs", "job ", "career", "technology",
                            "training", "school"],
    "cnc machining service": ["salary", "jobs", "course"],
    "3d printing service": ["printer", "printers", "salary", "jobs"],
}

# Related queries that signal someone about to transact rather than browse.
COMMERCIAL = ["near me", "cost", "price", "pricing", "quote", "company", "companies",
              "service", "services", "shop", "maker", "builder", "for sale",
              "custom made", "made to order", "online", "supplier", "manufacturer"]

# Jobseeker / student / hobbyist markers — present in a related list, they mean the
# audience is not a buyer even when the term itself looks commercial.
NON_BUYER = ["salary", "jobs", "job ", "career", "training", "school", "course",
             "certification", "apprentice", "reddit", "diy", "how to"]

RESOLUTION_LIMIT = 0.50   # share of weeks at index <= 1 above which nothing is measured
CALIBRATION_FAMILY = "soft_goods_cal"


def contains_any(text: str, needles: list[str]) -> bool:
    return any(n in text for n in needles)


def main() -> None:
    sweep = read_csv("demand_sweep")
    related = read_csv("demand_sweep_related")
    if not sweep:
        log("analyse_demand_sweep: run t1_demand_sweep.py first")
        return

    by_seed: dict[str, list[dict]] = defaultdict(list)
    for r in related:
        by_seed[r["seed_term"]].append(r)

    rows = []
    for s in sweep:
        term = s["keyword"]
        rel = by_seed.get(term, [])
        tops = [r for r in rel if r["kind"] == "top"]
        off = OFF_TOPIC.get(term, [])

        on_topic = [r for r in tops if not contains_any(r["query"].lower(), off)]
        # No related queries at all is itself a measurement: Google generates them from
        # co-occurring searches, so an empty list means the term is below the volume where
        # co-occurrence is stable. Scored as unmeasured, not as clean.
        if tops:
            on_topic_share = round(len(on_topic) / len(tops), 3)
        else:
            on_topic_share = None

        commercial_n = sum(1 for r in on_topic
                           if contains_any(r["query"].lower(), COMMERCIAL))
        non_buyer_n = sum(1 for r in tops
                          if contains_any(r["query"].lower(), NON_BUYER))
        commercial_share = (round(commercial_n / len(on_topic), 3)
                            if on_topic else None)

        raw = float(s["vs_anchor"])
        adjusted = round(raw * on_topic_share, 4) if on_topic_share is not None else None
        resolved = s["resolved"] in ("True", "true", True)

        rows.append({
            "keyword": term,
            "family": s["family"],
            "buyer": s["buyer"],
            "vocabulary": s["vocabulary"],
            "raw_vs_anchor": raw,
            "on_topic_share": on_topic_share,
            "adjusted_vs_anchor": adjusted,
            "related_top_n": len(tops),
            "commercial_share": commercial_share,
            "non_buyer_signals": non_buyer_n,
            "momentum_yoy": s["momentum_yoy"] or None,
            "weeks_at_or_below_1": float(s["weeks_at_or_below_1"]),
            "resolved": resolved,
            "verdict": (
                "unmeasured" if not resolved else
                "contaminated" if (on_topic_share is not None and on_topic_share < 0.5)
                else "measured"
            ),
        })

    rows.sort(key=lambda r: -(r["adjusted_vs_anchor"] or -1))
    save_csv("demand_sweep_ranking", rows)

    # Family rollup — the founder's question is which FAMILY to point a website at, and a
    # family can win on one strong term or on several mediocre ones. Both are reported:
    # `family_adjusted` sums the measured terms, `best_term` names the single entry point.
    fam = defaultdict(lambda: {"adjusted": 0.0, "terms": 0, "measured": 0,
                               "best": None, "best_v": -1.0, "buyers": set()})
    for r in rows:
        f = fam[r["family"]]
        f["terms"] += 1
        f["buyers"].add(r["buyer"])
        if r["verdict"] == "measured" and r["adjusted_vs_anchor"]:
            f["adjusted"] += r["adjusted_vs_anchor"]
            f["measured"] += 1
            if r["adjusted_vs_anchor"] > f["best_v"]:
                f["best_v"] = r["adjusted_vs_anchor"]
                f["best"] = r["keyword"]

    fam_rows = [{
        "family": k,
        "family_adjusted": round(v["adjusted"], 4),
        "terms_swept": v["terms"],
        "terms_measured": v["measured"],
        "best_term": v["best"] or "—",
        "best_term_adjusted": round(v["best_v"], 4) if v["best_v"] >= 0 else None,
        "buyer_mix": "/".join(sorted(v["buyers"])),
        "calibration_only": k == CALIBRATION_FAMILY,
    } for k, v in fam.items()]
    fam_rows.sort(key=lambda r: -r["family_adjusted"])
    save_csv("demand_sweep_families", fam_rows)

    record("google-trends", "demand-sweep-ranking", "derived", len(rows),
           note=f"{sum(1 for r in rows if r['verdict'] == 'measured')} measured, "
                f"{sum(1 for r in rows if r['verdict'] == 'contaminated')} contaminated, "
                f"{sum(1 for r in rows if r['verdict'] == 'unmeasured')} unmeasured")

    log("")
    log("  TERM RANKING — adjusted for contamination (US, 5y, vs 'custom furniture'=1.0)")
    log(f"    {'keyword':<27}{'family':<15}{'buyer':<9}{'raw':>6}{'adj':>7}"
        f"{'ontop':>7}{'comm':>6}  verdict")
    for r in rows:
        adj = f"{r['adjusted_vs_anchor']:.3f}" if r["adjusted_vs_anchor"] is not None else "   —"
        ot = f"{r['on_topic_share']:.2f}" if r["on_topic_share"] is not None else "  —"
        cm = f"{r['commercial_share']:.2f}" if r["commercial_share"] is not None else "  —"
        log(f"    {r['keyword']:<27}{r['family']:<15}{r['buyer']:<9}"
            f"{r['raw_vs_anchor']:>6.2f}{adj:>7}{ot:>7}{cm:>6}  {r['verdict']}")

    log("")
    log("  FAMILY ROLLUP — measured terms only")
    log(f"    {'family':<16}{'adj':>7}{'meas':>6}{'swept':>7}  {'buyers':<18}best term")
    for r in fam_rows:
        tag = "  (calibration)" if r["calibration_only"] else ""
        log(f"    {r['family']:<16}{r['family_adjusted']:>7.3f}{r['terms_measured']:>6}"
            f"{r['terms_swept']:>7}  {r['buyer_mix']:<18}{r['best_term']}{tag}")


if __name__ == "__main__":
    main()
