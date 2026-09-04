"""Tier 2 — Economic Census: the real industry denominator.

NAICS 337122 (nonupholstered wood household furniture) and 337211 (wood office
furniture): shipment value, establishment count, employment and payroll, nationally and
for California. This is the denominator to quote instead of a syndicated
"global furniture market" number.

Requires CENSUS_API_KEY (free, instant: https://api.census.gov/data/key_signup.html).
CBP (scripts/t2_cbp_supply.py) already provides establishment and employment counts with
no key; what this adds is RCPTOT — the revenue the establishments actually book.
"""
from __future__ import annotations

import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import ENV, census_rows, get, guard, log, record, save_csv, save_raw  # noqa: E402

SOURCE = "census-econ"
YEAR = 2022
BASE = f"https://api.census.gov/data/{YEAR}/ecnbasic"
NAICS = {"337920": "Blind and shade manufacturing",
         "337122": "Nonupholstered wood household furniture manufacturing",
         "337211": "Wood office furniture manufacturing",
         "337212": "Custom architectural woodwork and millwork",
         "3371": "Household and institutional furniture manufacturing",
         "337": "Furniture and related product manufacturing"}
FIELDS = "NAME,NAICS2022,NAICS2022_LABEL,ESTAB,RCPTOT,PAYANN,EMP"


def main() -> None:
    if not ENV.get("CENSUS_API_KEY"):
        log(f"→ {SOURCE}: SKIPPED — no CENSUS_API_KEY "
            "(free, instant: https://api.census.gov/data/key_signup.html)")
        record(SOURCE, "industry-shipments", BASE, 0,
               status="blocked_no_credential", note="CENSUS_API_KEY not set")
        return

    with guard(SOURCE, "industry-shipments", BASE):
        rows, raw = [], {}
        for code in NAICS:
            for geo_label, geo in (("us", {"for": "us:*"}), ("california", {"for": "state:06"})):
                params = {"get": FIELDS, "NAICS2022": code,
                          "key": ENV["CENSUS_API_KEY"], **geo}
                try:
                    recs = census_rows(get(BASE, params=params, timeout=90).json())
                except Exception as exc:  # noqa: BLE001 — suppressed cells are normal
                    log(f"    {code}/{geo_label}: {str(exc)[:80]}")
                    continue
                raw[f"{code}-{geo_label}"] = recs
                for r in recs:
                    def n(k):
                        try:
                            return float(r.get(k) or 0)
                        except ValueError:
                            return 0.0
                    rows.append({
                        "geo": geo_label, "name": r.get("NAME", ""), "naics": code,
                        "naics_label": NAICS[code], "year": YEAR,
                        "establishments": n("ESTAB"), "employees": n("EMP"),
                        "receipts_kusd": n("RCPTOT"), "payroll_kusd": n("PAYANN"),
                    })
        save_raw(SOURCE, "industry-shipments", raw)
        save_csv("econ_census_industry", rows)
        record(SOURCE, "industry-shipments", BASE, len(rows), note=f"Economic Census {YEAR}")

        log(f"  Economic Census {YEAR} receipts:")
        for r in rows:
            if r["receipts_kusd"]:
                log(f"    {r['naics']} {r['geo']:<11} ${r['receipts_kusd']*1000/1e9:>7.2f}bn  "
                    f"{r['establishments']:>6,.0f} estab")


if __name__ == "__main__":
    main()
