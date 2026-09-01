"""Tier 2 — BLS price and employment series: input costs vs. output prices.

The gap between what hardwood costs and what finished wood furniture sells for is the
margin the business lives in. PCU337122337122 is the producer price index for the exact
NAICS the brief names, so it is the cleanest read on whether domestic makers have been
able to pass tariff-era input costs through.
"""
from __future__ import annotations

import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import ENV, guard, log, post, record, save_csv, save_raw  # noqa: E402

SOURCE = "bls-prices"
API = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
SERIES = {
    "CUUR0000SEHM":    ("CPI", "Furniture and bedding (US city average)"),
    "CUUR0000SEHM01":  ("CPI", "Living room, kitchen and dining room furniture"),
    "PCU337122337122": ("PPI", "Nonupholstered wood household furniture mfg (NAICS 337122)"),
    "WPU0812":         ("PPI", "Hardwood lumber"),
    "WPU0811":         ("PPI", "Softwood lumber"),
    "WPU083":          ("PPI", "Millwork"),
    "CEU3133700001":   ("CES", "All employees, furniture and related product mfg (000s)"),
    # Wages and panel costs — the two largest lines in a factory cost model, measured
    # rather than assumed.
    "CEU3133700008":   ("CES", "Average hourly earnings, production employees, furniture mfg"),
    "CEU3133700002":   ("CES", "Average weekly hours, production employees, furniture mfg"),
    "PCU321219321219": ("PPI", "Reconstituted wood products (particleboard and MDF)"),
    "PCU321211321211": ("PPI", "Hardwood plywood and veneer"),
    "PCU337110337110": ("PPI", "Wood kitchen cabinet and countertop mfg"),
}
START, END = 2017, 2026


def main() -> None:
    with guard(SOURCE, "prices-and-employment", API):
        key = ENV.get("BLS_API_KEY", "")
        body = {"seriesid": list(SERIES), "startyear": str(START), "endyear": str(END)}
        if key:
            body["registrationkey"] = key
        payload = post(API, body, headers={"Content-Type": "application/json"}).json()
        if payload.get("status") != "REQUEST_SUCCEEDED":
            raise RuntimeError(str(payload.get("message"))[:300])
        save_raw(SOURCE, "prices-and-employment", payload)

        rows = []
        for s in payload["Results"]["series"]:
            fam, label = SERIES[s["seriesID"]]
            for d in s.get("data", []):
                if not d["period"].startswith("M") or d["period"] == "M13":
                    continue
                try:
                    val = float(d["value"].replace(",", ""))
                except ValueError:
                    continue
                rows.append({"series_id": s["seriesID"], "family": fam, "label": label,
                             "year": int(d["year"]), "month": int(d["period"][1:]),
                             "period": f"{d['year']}-{int(d['period'][1:]):02d}",
                             "value": val})
        rows.sort(key=lambda r: (r["series_id"], r["period"]))
        save_csv("bls_prices", rows)
        record(SOURCE, "prices-and-employment", API, len(rows),
               note=f"{len(SERIES)} series {START}-{END}")

        log("  Index change, latest vs. Jan 2020:")
        for sid, (_fam, label) in SERIES.items():
            ser = [r for r in rows if r["series_id"] == sid]
            if not ser:
                log(f"    {label[:52]:<52} unavailable")
                continue
            base = next((r for r in ser if r["period"] == "2020-01"), ser[0])
            last = ser[-1]
            pct = (last["value"] / base["value"] - 1) * 100
            log(f"    {label[:52]:<52} {pct:+6.1f}%  (→ {last['period']})")


if __name__ == "__main__":
    main()
