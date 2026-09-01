"""Tier 2 — Census Population Estimates by metro: how far an in-home service can reach.

An in-home assembly crew is not a national product on day one. It is a van, and a van
covers a metro. So the question the service tier has to answer is: if you stand up crews
in the largest N metros, what share of US households can you actually sell that tier to?

This collects the CBSA population vintage (keyless, same programme as the county file)
and builds the cumulative curve — top 5, 10, 25, 50, 100 metros as a share of the US.
That replaces a guessed "serviceable share" in the model with a measured one.
"""
from __future__ import annotations

import csv
import io
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import get, guard, log, record, save_csv, save_raw  # noqa: E402

SOURCE = "census-popest"
URL = ("https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/"
       "metro/totals/cbsa-est2024-alldata.csv")
YEAR = 2024
CUTS = [5, 10, 25, 50, 100, 200]


def main() -> None:
    with guard(SOURCE, "metro-coverage", URL):
        text = get(URL, timeout=180).content.decode("latin-1")
        recs = list(csv.DictReader(io.StringIO(text)))
        save_raw(SOURCE, "metro-coverage", {"rows": len(recs), "url": URL})

        def num(r, k):
            try:
                return float(r.get(k) or 0)
            except ValueError:
                return 0.0

        # Metro areas only. Micropolitan areas and the county rows nested underneath
        # each CBSA would double-count, and metropolitan divisions subdivide the big
        # ones — all three are excluded.
        metros = [r for r in recs if r["LSAD"] == "Metropolitan Statistical Area"]
        metros.sort(key=lambda r: -num(r, f"POPESTIMATE{YEAR}"))

        # The US denominator: the county file has no national row either, so sum the
        # state rows from the same vintage rather than mixing sources.
        state_url = ("https://www2.census.gov/programs-surveys/popest/datasets/"
                     "2020-2024/counties/totals/co-est2024-alldata.csv")
        st = list(csv.DictReader(io.StringIO(
            get(state_url, timeout=180).content.decode("latin-1"))))
        us_pop = sum(num(r, f"POPESTIMATE{YEAR}") for r in st if r["SUMLEV"] == "040")

        rows, cum = [], 0.0
        for i, r in enumerate(metros, start=1):
            cum += num(r, f"POPESTIMATE{YEAR}")
            rows.append({
                "rank": i, "cbsa": r["CBSA"], "name": r["NAME"], "year": YEAR,
                "population": num(r, f"POPESTIMATE{YEAR}"),
                "cumulative_population": cum,
                "cumulative_share_of_us": round(cum / us_pop, 5) if us_pop else None,
            })
        save_csv("metro_coverage", rows)
        record(SOURCE, "metro-coverage", URL, len(rows),
               note=f"{len(metros)} MSAs, vintage {YEAR}, US pop {us_pop:,.0f}")

        log(f"  US population reachable by standing up crews in the top N metros "
            f"(vintage {YEAR}):")
        for n in CUTS:
            if n <= len(rows):
                log(f"    top {n:>3} metros  {rows[n - 1]['cumulative_share_of_us']:.1%}"
                    f"   ({rows[n - 1]['cumulative_population']:,.0f} people)")


if __name__ == "__main__":
    main()
