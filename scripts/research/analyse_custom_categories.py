"""Separate genuine custom-furniture demand from lookalike accessory demand.

A raw Trends score for "custom desk" counts everyone searching for a custom desk *mat*.
Those are print-on-demand accessories, not furniture, and they inflate exactly the
categories a furniture maker would be most tempted by.

For each category this reads its top related queries, scores what share of that related
volume carries an accessory modifier rather than an object, and discounts the category's
headline index by the remainder. The modifier list is explicit and editable; the
per-category evidence is written out so any classification can be checked by hand.
"""
from __future__ import annotations

import csv
import sys
from collections import defaultdict

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import log, read_csv, record, save_csv  # noqa: E402

# Words that turn a furniture query into an accessory, print or jewellery query.
ACCESSORY = [
    "mat", "mats", "pad", "pads", "sign", "signs", "necklace", "sticker", "decal",
    "cover", "covers", "cushion", "cushions", "slipcover", "desktop", "wallpaper",
    "shirt", "mug", "topper", "cloth", "runner", "protector", "skin", "engraved",
    "plate", "plates",   # "custom vanity plates" is a licence plate, not a vanity
    "mirror", "mirrors",
]
# Words that confirm a real purchase of the object itself.
COMMERCIAL = ["near me", "cost", "price", "companies", "designer", "builder",
              "installation", "quote", "contractor", "maker", "custom made"]


def classify(query: str) -> str:
    q = query.lower()
    if any(f" {w}" in f" {q}" or q.endswith(f" {w}") for w in ACCESSORY):
        return "accessory"
    return "furniture"


def main() -> None:
    cats = read_csv("trends_custom_categories")
    related = read_csv("trends_custom_related")
    if not cats or not related:
        log("analyse_custom_categories: run t1_custom_categories.py first")
        return

    top = defaultdict(list)
    for r in related:
        if r["kind"] == "top" and r["value"]:
            top[r["seed_term"]].append(r)

    rows = []
    for c in cats:
        term = c["keyword"]
        items = top.get(term, [])
        total = sum(float(i["value"]) for i in items) or 0.0
        acc = sum(float(i["value"]) for i in items if classify(i["query"]) == "accessory")
        furn_share = (1 - acc / total) if total else None
        commercial = sum(1 for i in items
                         if any(w in i["query"].lower() for w in COMMERCIAL))
        raw_index = float(c["vs_custom_furniture"])
        rows.append({
            "keyword": term,
            "raw_vs_custom_furniture": raw_index,
            "related_queries_seen": len(items),
            "furniture_share_of_related": round(furn_share, 3) if furn_share is not None else "",
            "adjusted_index": round(raw_index * furn_share, 4) if furn_share is not None else "",
            "commercial_intent_queries": commercial,
            "top_related": " | ".join(i["query"] for i in items[:5]),
        })

    scored = [r for r in rows if r["adjusted_index"] != ""]
    scored.sort(key=lambda r: -r["adjusted_index"])
    unscored = [r for r in rows if r["adjusted_index"] == ""]
    out = scored + unscored
    save_csv("custom_categories_adjusted", out)
    record("analysis", "custom-category-adjustment", "derived", len(out),
           note="raw Trends index discounted by the furniture share of related queries")

    log("  Custom furniture demand, accessory-adjusted (California, 5 years)")
    log("  " + "-" * 78)
    log(f"  {'category':<26}{'raw':>7}{'furn%':>8}{'adj':>8}{'commercial':>12}")
    for r in out:
        if r["keyword"] == "custom furniture":
            continue
        fs = f"{r['furniture_share_of_related']*100:.0f}%" if r["furniture_share_of_related"] != "" else "n/a"
        adj = f"{r['adjusted_index']:.3f}" if r["adjusted_index"] != "" else "  —"
        log(f"  {r['keyword']:<26}{r['raw_vs_custom_furniture']:>7.3f}{fs:>8}{adj:>8}"
            f"{r['commercial_intent_queries']:>12}")
    log("")
    log("  'commercial' counts related queries containing near me / cost / price /")
    log("  companies / designer / installation — i.e. someone shopping, not browsing.")


if __name__ == "__main__":
    main()
