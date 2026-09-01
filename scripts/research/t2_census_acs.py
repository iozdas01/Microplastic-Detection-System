"""Tier 2 — ACS: the Bay Area household denominator the TAM is built on.

Every Census API dataset now requires a key (free, instant, no cost):
    https://api.census.gov/data/key_signup.html  ->  set CENSUS_API_KEY in .env

Pulls, for the ten Bay Area counties, California and the US:
  households, tenure, median income, share of households above $200k,
  median home value, and one-year mover counts.

Movers matter more than the population count: moving is the largest single trigger of a
furniture purchase, so the mover count is the closest thing to an annual "at-bat" number.
"""
from __future__ import annotations

import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import ENV, census_rows, get, guard, log, record, save_csv, save_raw  # noqa: E402

SOURCE = "census-acs"
YEAR = 2023
BASE = f"https://api.census.gov/data/{YEAR}/acs/acs5"
BAY_AREA = {"001": "Alameda", "013": "Contra Costa", "041": "Marin", "055": "Napa",
            "075": "San Francisco", "081": "San Mateo", "085": "Santa Clara",
            "095": "Solano", "097": "Sonoma", "087": "Santa Cruz"}
VARS = {
    "B25003_001E": "households_occupied_units",
    "B25003_002E": "owner_occupied",
    "B25003_003E": "renter_occupied",
    "B19013_001E": "median_household_income",
    "B19001_017E": "households_income_200k_plus",
    "B19001_016E": "households_income_150_200k",
    "B25077_001E": "median_home_value",
    "B07003_001E": "population_1yr_plus",
    "B07003_004E": "movers_within_same_county",
    "B07003_007E": "movers_from_other_county_same_state",
    "B07003_010E": "movers_from_other_state",
}


def pull(geo: dict) -> list[dict]:
    params = {"get": "NAME," + ",".join(VARS), "key": ENV["CENSUS_API_KEY"], **geo}
    return census_rows(get(BASE, params=params, timeout=90).json())


def main() -> None:
    if not ENV.get("CENSUS_API_KEY"):
        log(f"→ {SOURCE}: SKIPPED — no CENSUS_API_KEY "
            "(free, instant: https://api.census.gov/data/key_signup.html)")
        record(SOURCE, "bay-area-households", BASE, 0,
               status="blocked_no_credential", note="CENSUS_API_KEY not set")
        return

    with guard(SOURCE, "bay-area-households", BASE):
        raw = {
            "counties": pull({"for": "county:" + ",".join(BAY_AREA), "in": "state:06"}),
            "california": pull({"for": "state:06"}),
            "us": pull({"for": "us:*"}),
        }
        save_raw(SOURCE, "bay-area-households", raw)

        rows = []
        for level, recs in raw.items():
            for r in recs:
                out = {"geo_level": level, "name": r.get("NAME", ""),
                       "county_fips": r.get("county", ""), "year": YEAR}
                for code, label in VARS.items():
                    try:
                        out[label] = float(r[code]) if r.get(code) not in (None, "") else None
                    except ValueError:
                        out[label] = None
                movers = sum(out[k] or 0 for k in
                             ("movers_within_same_county",
                              "movers_from_other_county_same_state",
                              "movers_from_other_state"))
                out["movers_total_1yr"] = movers
                hh = out["households_occupied_units"] or 0
                out["affluent_household_share"] = round(
                    ((out["households_income_200k_plus"] or 0)
                     + (out["households_income_150_200k"] or 0)) / hh, 4) if hh else None
                rows.append(out)

        save_csv("acs_bay_area_households", rows)
        record(SOURCE, "bay-area-households", BASE, len(rows), note=f"ACS 5-year {YEAR}")

        bay = [r for r in rows if r["geo_level"] == "counties"]
        log(f"  Bay Area (10 counties), ACS {YEAR} 5-year:")
        log(f"    households                {sum(r['households_occupied_units'] or 0 for r in bay):>12,.0f}")
        log(f"    households $150k+         {sum((r['households_income_200k_plus'] or 0)+(r['households_income_150_200k'] or 0) for r in bay):>12,.0f}")
        log(f"    movers in last 12 months  {sum(r['movers_total_1yr'] for r in bay):>12,.0f}")


if __name__ == "__main__":
    main()
