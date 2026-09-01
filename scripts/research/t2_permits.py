"""Tier 2 — Census Building Permits Survey: Bay Area household formation.

Moving is the single largest furniture purchase trigger, and a permitted new unit is a
household that will furnish a dining room within roughly a year of completion. The BPS
county files are published keyless as fixed-format CSV, one per month, with a
year-to-date variant (`y`) and a current-month variant (`c`).

This pulls December year-to-date for each completed year plus the latest month available
in the current year, for the ten Bay Area counties.
"""
from __future__ import annotations

import csv
import datetime as dt
import io
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import get, guard, log, record, save_csv, save_raw  # noqa: E402

SOURCE = "census-bps"
BASE = "https://www2.census.gov/econ/bps/County"
BAY_AREA = {
    "001": "Alameda", "013": "Contra Costa", "041": "Marin", "055": "Napa",
    "075": "San Francisco", "081": "San Mateo", "085": "Santa Clara",
    "095": "Solano", "097": "Sonoma", "087": "Santa Cruz",
}
# Column layout: two header rows, then Date,State,County,Region,Division,Name, then
# (bldgs, units, value) triplets for 1-unit, 2-unit, 3-4 unit, 5+ unit.
UNIT_GROUPS = [("1_unit", 6), ("2_units", 9), ("3_4_units", 12), ("5plus_units", 15)]


def fetch_period(yy: int, mm: int, kind: str) -> list[list[str]] | None:
    url = f"{BASE}/co{yy:02d}{mm:02d}{kind}.txt"
    try:
        text = get(url, timeout=90).text
    except Exception:  # noqa: BLE001 - a month that is not published yet is not an error
        return None
    rows = list(csv.reader(io.StringIO(text)))
    return [r for r in rows[2:] if len(r) > 18 and r[0].strip().isdigit()]


def main() -> None:
    with guard(SOURCE, "bay-area-permits", BASE):
        out, raw = [], {}
        today = dt.date.today()
        periods = [(yy, 12, "y") for yy in range(15, today.year % 100)]
        # Latest published month of the current year, walking back from this month.
        for mm in range(today.month, 0, -1):
            if fetch_period(today.year % 100, mm, "y") is not None:
                periods.append((today.year % 100, mm, "y"))
                break

        for yy, mm, kind in periods:
            rows = fetch_period(yy, mm, kind)
            if rows is None:
                continue
            raw[f"20{yy:02d}-{mm:02d}"] = len(rows)
            for r in rows:
                state, cty = r[1].strip(), r[2].strip()
                if state != "06" or cty not in BAY_AREA:
                    continue
                rec = {"year": 2000 + yy, "through_month": mm,
                       "ytd": kind == "y", "county": BAY_AREA[cty], "fips": f"06{cty}"}
                total = 0
                for label, idx in UNIT_GROUPS:
                    units = int(r[idx + 1] or 0)
                    rec[f"{label}_units"] = units
                    rec[f"{label}_value_usd"] = int(r[idx + 2] or 0)
                    total += units
                rec["total_units"] = total
                out.append(rec)

        out.sort(key=lambda r: (r["county"], r["year"]))
        save_raw(SOURCE, "bay-area-permits", raw)
        save_csv("bay_area_building_permits", out)
        record(SOURCE, "bay-area-permits", BASE, len(out),
               note=f"{len(raw)} periods, 10 counties")

        by_year: dict[int, int] = {}
        for r in out:
            by_year[r["year"]] = by_year.get(r["year"], 0) + r["total_units"]
        log("  Bay Area permitted housing units:")
        for y in sorted(by_year)[-6:]:
            partial = " (YTD)" if y == max(r["year"] for r in out) and \
                max(r["through_month"] for r in out if r["year"] == y) < 12 else ""
            log(f"    {y}: {by_year[y]:>7,}{partial}")


if __name__ == "__main__":
    main()
