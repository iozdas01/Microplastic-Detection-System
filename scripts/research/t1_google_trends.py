"""Tier 1 — Google Trends: direction, seasonality and geography of purchase intent.

Trends only ever returns numbers relative to the peak of whatever set of terms you ask
about, so five terms queried separately are five incomparable series. This collector
therefore queries in batches of five with the SAME anchor term ("dining table") in every
batch, then rescales each batch by its anchor. That makes every keyword in the output
directly comparable to every other, across batches.

Pulls three widgets per batch:
  TIMESERIES      weekly interest over five years  -> direction and seasonality
  GEO_MAP         interest by US state          -> where the demand is
  RELATED_QUERIES top and rising related searches  -> the language buyers actually use

No credential required, but Google rate-limits hard; the collector backs off and records
partial results rather than failing the run.
"""
from __future__ import annotations

import json
import sys
import time

import requests

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import guard, log, record, save_csv, save_raw  # noqa: E402

SOURCE = "google-trends"
BASE = "https://trends.google.com/trends/api"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")

ANCHOR = "dining table"
# Generic/custom pairs across the furniture families a sheet-goods factory can make.
# The pair is the instrument: custom-share per family = custom term / generic term,
# both scaled by the same anchor, so families are comparable to each other.
KEYWORDS = [
    # generic demand, per family
    "sofa", "bed frame", "desk", "bookshelf", "dresser", "wardrobe",
    "coffee table", "nightstand", "tv stand", "kitchen cabinets", "closet organizer",
    # the custom framing of the same families
    "custom sofa", "custom bed frame", "custom desk", "custom bookshelf",
    "custom dresser", "custom wardrobe", "custom coffee table", "custom nightstand",
    "custom tv stand", "custom cabinets", "custom closet", "custom dining table",
    # seating and the remaining articles. Chairs were missing entirely, which meant the
    # dining family was being scored on the dining table's evidence alone.
    "dining chair", "custom dining chair", "accent chair", "custom accent chair",
    "bench", "custom bench", "console table", "custom console table",
    # the category words themselves
    "custom furniture", "made to order furniture", "modular furniture",
    "built in furniture",
]
GEO = "US"
# Anchoring makes the keywords comparable but flattens the geography: next to
# "dining table" every state rounds to 1. So the custom terms also get an
# unanchored pass whose only job is to resolve the state breakdown.
GEO_FOCUS = ["custom furniture", "custom cabinets", "custom closet",
             "custom dining table", "made to order furniture"]
TIMEFRAME = "today 5-y"


class Trends:
    def __init__(self) -> None:
        self.s = requests.Session()
        self.s.headers.update({"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
        # The explore endpoint only issues widget tokens to a session that already holds
        # the consent/NID cookies handed out by the HTML page.
        self.s.get("https://trends.google.com/trends/explore", timeout=30,
                   params={"geo": GEO, "q": ANCHOR})

    def _json(self, url: str, params: dict) -> dict:
        for attempt in range(1, 5):
            r = self.s.get(url, params=params, timeout=45,
                           headers={"Referer": "https://trends.google.com/"})
            if r.status_code == 200:
                return json.loads(r.text[r.text.find("{"):])
            time.sleep(6 * attempt)  # 429 is the normal case; wait it out
        raise RuntimeError(f"{url} -> HTTP {r.status_code}")

    def widgets(self, terms: list[str]) -> dict[str, dict]:
        req = {"comparisonItem": [{"keyword": t, "geo": GEO, "time": TIMEFRAME}
                                  for t in terms],
               "category": 0, "property": ""}
        data = self._json(f"{BASE}/explore",
                          {"hl": "en-US", "tz": "420", "req": json.dumps(req)})
        # Explore returns one RELATED_QUERIES_<i> widget per term. Keying them all as
        # "RELATED" keeps only the last term's list, which silently reports one
        # keyword's neighbours as if they were the whole batch's.
        return {w["id"]: w for w in data["widgets"]}

    def widget_data(self, widget: dict, endpoint: str) -> dict:
        return self._json(f"{BASE}/widgetdata/{endpoint}",
                          {"hl": "en-US", "tz": "420",
                           "req": json.dumps(widget["request"]),
                           "token": widget["token"]})


def main() -> None:
    with guard(SOURCE, "purchase-intent-terms", f"{BASE}/explore"):
        tr = Trends()
        batches = [KEYWORDS[i:i + 4] for i in range(0, len(KEYWORDS), 4)]
        timeseries, geo_rows, related_rows, raw = [], [], [], {}

        for bi, batch in enumerate(batches):
            terms = [ANCHOR] + batch
            log(f"  batch {bi+1}/{len(batches)}: {', '.join(batch)}")
            try:
                widgets = tr.widgets(terms)
            except Exception as exc:  # noqa: BLE001
                log(f"    !! explore failed: {str(exc)[:90]}")
                continue
            raw[f"batch{bi}-widgets"] = list(widgets)

            # --- interest over time, rescaled against the anchor -------------------
            try:
                ts = tr.widget_data(widgets["TIMESERIES"], "multiline")
                raw[f"batch{bi}-timeseries"] = ts
                points = ts["default"]["timelineData"]
                anchor_mean = sum(p["value"][0] for p in points) / max(len(points), 1) or 1
                for p in points:
                    for ti, term in enumerate(terms):
                        timeseries.append({
                            "keyword": term, "batch": bi, "is_anchor": ti == 0,
                            "date": p["formattedTime"], "timestamp": p["time"],
                            "raw_index": p["value"][ti],
                            "anchor_scaled": round(p["value"][ti] / anchor_mean, 4),
                        })
            except Exception as exc:  # noqa: BLE001
                log(f"    timeseries unavailable: {str(exc)[:80]}")

            # --- interest by US state      --------------------------------------
            try:
                gm = tr.widget_data(widgets["GEO_MAP"], "comparedgeo")
                raw[f"batch{bi}-geo"] = gm
                for g in gm["default"]["geoMapData"]:
                    for ti, term in enumerate(terms):
                        geo_rows.append({"keyword": term, "batch": bi,
                                         "geo_name": g["geoName"],
                                         "geo_code": g.get("geoCode", ""),
                                         "index": g["value"][ti]})
            except Exception as exc:  # noqa: BLE001
                log(f"    geo map unavailable: {str(exc)[:80]}")

            # --- related and rising queries, per seed term ---------------------------
            for ti, term in enumerate(terms):
                # The anchor rides in every batch; collect its neighbours once.
                if ti == 0 and bi > 0:
                    continue
                wid = f"RELATED_QUERIES_{ti}"
                if wid not in widgets:
                    continue
                try:
                    rq = tr.widget_data(widgets[wid], "relatedsearches")
                except Exception as exc:  # noqa: BLE001
                    log(f"    related for '{term}' unavailable: {str(exc)[:70]}")
                    continue
                raw[f"batch{bi}-related-{ti}"] = rq
                for li, block in enumerate(rq.get("default", {}).get("rankedList", [])):
                    kind = "top" if li == 0 else "rising"
                    for item in block.get("rankedKeyword", []):
                        related_rows.append({
                            "seed_term": term, "seed_batch": bi, "kind": kind,
                            "query": item.get("query", ""),
                            "value": item.get("value"),
                            "formatted_value": item.get("formattedValue", ""),
                        })
                time.sleep(1.5)

            time.sleep(4)

        # --- unanchored geo pass ---------------------------------------------------
        log("  geo pass (unanchored): " + ", ".join(GEO_FOCUS))
        try:
            widgets = tr.widgets(GEO_FOCUS)
            gm = tr.widget_data(widgets["GEO_MAP"], "comparedgeo")
            raw["geo-focus"] = gm
            for g in gm["default"]["geoMapData"]:
                for ti, term in enumerate(GEO_FOCUS):
                    geo_rows.append({"keyword": term, "batch": "geo_focus",
                                     "geo_name": g["geoName"],
                                     "geo_code": g.get("geoCode", ""),
                                     "index": g["value"][ti]})
        except Exception as exc:  # noqa: BLE001
            log(f"    geo focus unavailable: {str(exc)[:80]}")

        save_raw(SOURCE, "purchase-intent-terms", raw)
        save_csv("trends_interest_over_time", timeseries)
        save_csv("trends_by_metro", geo_rows)
        save_csv("trends_related_queries", related_rows)
        record(SOURCE, "purchase-intent-terms", f"{BASE}/explore",
               len(timeseries) + len(geo_rows) + len(related_rows),
               note=f"geo={GEO} timeframe={TIMEFRAME} anchor='{ANCHOR}'")

        focus = [r for r in geo_rows if r["batch"] == "geo_focus"
                 and r["keyword"] == "custom dining table"]
        if focus:
            log("  'custom dining table' by US state (unanchored, 100 = peak state):")
            for r in sorted(focus, key=lambda r: -r["index"])[:6]:
                log(f"    {r['geo_name'][:44]:<44} {r['index']:>3}")

        if timeseries:
            means: dict[str, float] = {}
            for r in timeseries:
                means.setdefault(r["keyword"], []).append(r["anchor_scaled"])
            log("  Mean interest, anchor-scaled (1.00 = 'dining table'):")
            for k, v in sorted(means.items(), key=lambda kv: -sum(kv[1]) / len(kv[1])):
                log(f"    {k:<30} {sum(v)/len(v):.3f}")


if __name__ == "__main__":
    main()
