"""Tier 2 — Census Population Estimates: Bay Area size and net migration, keyless.

ACS needs a key; the Population Estimates program publishes the same county vintage as a
plain CSV that needs none. Two things come out of it:

  population share  -> scales national CEX spend down to the Bay Area
  net migration     -> people arriving, i.e. households about to furnish a home

Net domestic migration in the Bay Area has been strongly negative since 2020, which is a
demand headwind the national furniture numbers hide.
"""
from __future__ import annotations

import csv
import io
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import get, guard, log, record, save_csv, save_raw  # noqa: E402

SOURCE = "census-popest"
URL = ("https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/"
       "counties/totals/co-est2024-alldata.csv")
BAY_AREA = {"001": "Alameda", "013": "Contra Costa", "041": "Marin", "055": "Napa",
            "075": "San Francisco", "081": "San Mateo", "085": "Santa Clara",
            "095": "Solano", "097": "Sonoma", "087": "Santa Cruz"}
YEARS = [2020, 2021, 2022, 2023, 2024]


def main() -> None:
    with guard(SOURCE, "county-population-migration", URL):
        text = get(URL, timeout=180).content.decode("latin-1")
        recs = list(csv.DictReader(io.StringIO(text)))
        save_raw(SOURCE, "county-population-migration", {"rows": len(recs), "url": URL})

        def num(r, k):
            try:
                return float(r.get(k) or 0)
            except ValueError:
                return 0.0

        rows = []
        # The county vintage carries state (SUMLEV 040) and county (050) rows but no
        # national row; sum the states for the US denominator.
        states = [r for r in recs if r["SUMLEV"] == "040"]
        for y in YEARS:
            rows.append({"geo_level": "us", "name": "United States", "fips": "00000",
                         "year": y,
                         "population": sum(num(r, f"POPESTIMATE{y}") for r in states),
                         "net_migration": sum(num(r, f"NETMIG{y}") for r in states),
                         "domestic_migration": sum(num(r, f"DOMESTICMIG{y}") for r in states),
                         "international_migration": sum(num(r, f"INTERNATIONALMIG{y}") for r in states)})

        ca_counties = [r for r in recs if r["SUMLEV"] == "050" and r["STATE"] == "06"]
        for r in ca_counties:
            cty = r["COUNTY"]
            if cty not in BAY_AREA:
                continue
            for y in YEARS:
                rows.append({"geo_level": "bay_area_county", "name": BAY_AREA[cty],
                             "fips": f"06{cty}", "year": y,
                             "population": num(r, f"POPESTIMATE{y}"),
                             "net_migration": num(r, f"NETMIG{y}"),
                             "domestic_migration": num(r, f"DOMESTICMIG{y}"),
                             "international_migration": num(r, f"INTERNATIONALMIG{y}")})

        for y in YEARS:
            sub = [x for x in rows if x["geo_level"] == "bay_area_county" and x["year"] == y]
            rows.append({"geo_level": "bay_area_total", "name": "Bay Area (10 counties)",
                         "fips": "06BAY", "year": y,
                         "population": sum(x["population"] for x in sub),
                         "net_migration": sum(x["net_migration"] for x in sub),
                         "domestic_migration": sum(x["domestic_migration"] for x in sub),
                         "international_migration": sum(x["international_migration"] for x in sub)})

        save_csv("bay_area_population", rows)
        record(SOURCE, "county-population-migration", URL, len(rows), note="vintage 2024")

        log("  Bay Area population and migration:")
        for y in YEARS:
            b = next(x for x in rows if x["geo_level"] == "bay_area_total" and x["year"] == y)
            u = next(x for x in rows if x["geo_level"] == "us" and x["year"] == y)
            log(f"    {y}: pop {b['population']:>10,.0f}  ({b['population']/u['population']*100:.2f}% of US)"
                f"   net mig {b['net_migration']:>+9,.0f}"
                f"   (domestic {b['domestic_migration']:>+9,.0f})")


if __name__ == "__main__":
    main()
