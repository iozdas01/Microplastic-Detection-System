"""Tier 2 — BLS Consumer Expenditure Survey: furniture spend per household.

This is what the bottom-up TAM is built on. Every article line under Furniture is
collected, not just one, because which article to build is an output of the model rather
than an input to it:

  290110..290440  the nine article lines       <- the per-article US spend pool
  FURNITUR Furniture (all)                     <- the wider basket, and the sum check
  HHFURNSH Household furnishings and equipment <- the widest defensible denominator

each cut two ways: by income quintile (LB01) and by census region (LB11, West = 05).
CONSUNIT gives the count of consumer units in each cell, which is what turns an average
annual expenditure into an aggregate dollar pool.

Runs against the BLS public API unregistered (25 series/query, 10 years, 25 queries/day).
Set BLS_API_KEY to lift that to 50 series and 20 years.
"""
from __future__ import annotations

import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import ENV, guard, log, post, record, save_csv, save_raw  # noqa: E402

SOURCE = "bls-cex"
API = "https://api.bls.gov/publicAPI/v2/timeseries/data/"

ITEMS = {
    # The nine article lines under Furniture. They sum exactly to FURNITUR ($648 per
    # consumer unit in 2024), which is the check that the set is complete and that the
    # code-to-label mapping below is right: 290410 is confirmed by the published series
    # name, the rest follow the CEX hierarchy (2901 bedroom, 2902 sofas, 2903 living
    # room, 2904 other) and reconcile to the total with no residual.
    "290110": "Mattresses and springs",
    "290120": "Other bedroom furniture",
    "290210": "Sofas",
    "290310": "Living room chairs",
    "290320": "Living room tables",
    "290410": "Kitchen and dining room furniture",
    "290420": "Infants' furniture",
    "290430": "Outdoor furniture",
    "290440": "Wall units, cabinets and other occasional furniture",
    "FURNITUR": "Furniture",
    "HHFURNSH": "Household furnishings and equipment",
    "CONSUNIT": "Number of consumer units (thousands)",
    "INCBEFTX": "Income before taxes",
}
CUTS = {
    "LB01": {"01": "All consumer units", "02": "Q1 lowest 20%", "03": "Q2", "04": "Q3",
             "05": "Q4", "06": "Q5 highest 20%"},
    "LB11": {"01": "All consumer units", "02": "Northeast", "03": "Midwest",
             "04": "South", "05": "West"},
}
START, END = 2015, 2024


def series_ids() -> dict[str, dict]:
    out = {}
    for item in ITEMS:
        pad = item  # series IDs use the item code verbatim, no padding
        for cut, chars in CUTS.items():
            for ch, label in chars.items():
                sid = f"CXU{pad}{cut}{ch}M"
                out[sid] = {"item_code": item, "item": ITEMS[item], "cut": cut,
                            "cut_label": {"LB01": "income quintile",
                                          "LB11": "census region"}[cut],
                            "group": label}
    return out


def main() -> None:
    with guard(SOURCE, "furniture-expenditure", API):
        meta = series_ids()
        ids = list(meta)
        key = ENV.get("BLS_API_KEY", "")
        batch = 50 if key else 25
        rows, raw = [], {}
        for i in range(0, len(ids), batch):
            chunk = ids[i:i + batch]
            body = {"seriesid": chunk, "startyear": str(START), "endyear": str(END)}
            if key:
                body["registrationkey"] = key
            payload = post(API, body, headers={"Content-Type": "application/json"}).json()
            if payload.get("status") != "REQUEST_SUCCEEDED":
                raise RuntimeError(f"BLS: {payload.get('status')} {payload.get('message')}")
            raw[f"batch{i//batch}"] = payload
            for s in payload["Results"]["series"]:
                sid = s["seriesID"]
                for d in s.get("data", []):
                    try:
                        val = float(str(d["value"]).replace(",", ""))
                    except ValueError:
                        continue
                    rows.append({**meta[sid], "series_id": sid, "year": int(d["year"]),
                                 "value": val})
        save_raw(SOURCE, "furniture-expenditure", raw)
        rows.sort(key=lambda r: (r["item_code"], r["cut"], r["group"], r["year"]))
        save_csv("cex_furniture_expenditure", rows)
        record(SOURCE, "furniture-expenditure", API, len(rows),
               note=f"{len(ids)} series, {START}-{END}, "
                    f"{'registered' if key else 'unregistered'}")

        latest = max(r["year"] for r in rows)
        log(f"  CEX {latest}, kitchen & dining room furniture, avg annual $/consumer unit:")
        for r in sorted([r for r in rows if r["item_code"] == "290410"
                         and r["cut"] == "LB01" and r["year"] == latest],
                        key=lambda r: r["group"]):
            log(f"    {r['group']:<18} ${r['value']:,.0f}")
        west = [r for r in rows if r["item_code"] == "290410" and r["cut"] == "LB11"
                and r["year"] == latest and r["group"] == "West"]
        if west:
            log(f"    West region        ${west[0]['value']:,.0f}")


if __name__ == "__main__":
    main()
