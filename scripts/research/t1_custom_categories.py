"""Tier 1 — which furniture categories people actually want customised.

The main Trends collector anchors on "dining table" to size one category. This one
anchors on "custom furniture" and sweeps the categories underneath it, to answer a
different question: given that someone wants something custom-made, what is it?

Also pulls top and rising related queries for every category, per term — which is what
reveals the language and the specific objects behind each category.
"""
from __future__ import annotations

import json
import sys
import time

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import guard, log, record, save_csv, save_raw  # noqa: E402
from t1_google_trends import GEO, TIMEFRAME, Trends  # noqa: E402

SOURCE = "google-trends"
ANCHOR = "custom furniture"
CATEGORIES = [
    "custom closet", "custom cabinets", "custom built ins", "custom kitchen island",
    "custom dining table", "custom desk", "custom bookshelf", "custom headboard",
    "custom coffee table", "custom bed frame", "custom vanity", "custom shelving",
    "custom conference table", "custom bench", "custom wardrobe", "custom sofa",
    "custom outdoor furniture", "custom nightstand", "custom mantel", "custom bar",
    "custom dining chair", "custom chair", "custom stool", "custom console table",
]


def main() -> None:
    with guard(SOURCE, "custom-furniture-categories", "trends.google.com"):
        tr = Trends()
        batches = [CATEGORIES[i:i + 4] for i in range(0, len(CATEGORIES), 4)]
        rows, related, raw, timeline = [], [], {}, []

        for bi, batch in enumerate(batches):
            terms = [ANCHOR] + batch
            log(f"  batch {bi+1}/{len(batches)}: {', '.join(batch)}")
            try:
                widgets = tr.widgets(terms)
            except Exception as exc:  # noqa: BLE001
                log(f"    !! explore failed: {str(exc)[:90]}")
                continue

            try:
                ts = tr.widget_data(widgets["TIMESERIES"], "multiline")
                raw[f"batch{bi}-ts"] = ts
                points = ts["default"]["timelineData"]
                anchor_mean = sum(p["value"][0] for p in points) / max(len(points), 1) or 1
                sums = [0.0] * len(terms)
                for p in points:
                    for ti in range(len(terms)):
                        sums[ti] += p["value"][ti]
                # Keep the weekly series as well as the mean. Without it there is no way
                # to say whether a category is rising, and "most in demand right now" is
                # a question about direction as much as level.
                for ti, term in enumerate(terms):
                    if ti == 0 and bi > 0:
                        continue
                    for p in points:
                        timeline.append({
                            "keyword": term, "batch": bi,
                            "timestamp": int(p["time"]),
                            "raw_index": p["value"][ti],
                            "vs_anchor": round(p["value"][ti] / anchor_mean, 5),
                        })
                for ti, term in enumerate(terms):
                    if ti == 0 and bi > 0:
                        continue  # the anchor only needs recording once
                    rows.append({
                        "keyword": term,
                        "is_anchor": ti == 0,
                        "mean_index": round(sums[ti] / len(points), 3),
                        "vs_custom_furniture": round(
                            (sums[ti] / len(points)) / anchor_mean, 4),
                        "batch": bi,
                    })
            except Exception as exc:  # noqa: BLE001
                log(f"    timeseries unavailable: {str(exc)[:80]}")

            for ti, term in enumerate(terms):
                if ti == 0 and bi > 0:
                    continue
                wid = f"RELATED_QUERIES_{ti}"
                if wid not in widgets:
                    continue
                try:
                    rq = tr.widget_data(widgets[wid], "relatedsearches")
                except Exception as exc:  # noqa: BLE001
                    log(f"    related for '{term}': {str(exc)[:60]}")
                    continue
                raw[f"batch{bi}-related-{ti}"] = rq
                for li, block in enumerate(rq.get("default", {}).get("rankedList", [])):
                    kind = "top" if li == 0 else "rising"
                    for item in block.get("rankedKeyword", []):
                        related.append({"seed_term": term, "kind": kind,
                                        "query": item.get("query", ""),
                                        "value": item.get("value"),
                                        "formatted_value": item.get("formattedValue", "")})
                time.sleep(1.5)
            time.sleep(3)

        rows.sort(key=lambda r: -r["vs_custom_furniture"])
        save_raw(SOURCE, "custom-furniture-categories", raw)
        save_csv("trends_custom_categories", rows)
        save_csv("trends_custom_timeline", timeline)
        save_csv("trends_custom_related", related)
        record(SOURCE, "custom-furniture-categories", "trends.google.com",
               len(rows) + len(related),
               note=f"anchor='{ANCHOR}' geo={GEO} timeframe={TIMEFRAME}")

        log("")
        log(f"  Interest relative to '{ANCHOR}' = 1.000 (United States, 5 years):")
        for r in rows:
            mark = "  <- anchor" if r["is_anchor"] else ""
            log(f"    {r['keyword']:<28} {r['vs_custom_furniture']:>7.3f}{mark}")


if __name__ == "__main__":
    main()
