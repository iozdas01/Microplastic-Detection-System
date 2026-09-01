"""Tier 2 — County Business Patterns: who already makes this, and where.

The Economic Census / ASM API endpoints need a Census key. CBP is published as a keyless
bulk file and carries what matters most here: establishment counts, employment and annual
payroll by 6-digit NAICS by county. That gives the real competitor count inside the Bay
Area rather than a national abstraction.

NAICS 337122 (nonupholstered wood household furniture) and 337211 (wood office furniture)
are the two the brief names; the adjacent millwork and finish-carpentry codes are pulled
too because in practice that is who a custom table order actually competes with locally.
"""
from __future__ import annotations

import csv
import io
import sys
import zipfile

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import RAW, get, guard, log, record, save_csv  # noqa: E402

SOURCE = "census-cbp"
YEAR = 2022
CO_URL = f"https://www2.census.gov/programs-surveys/cbp/datasets/{YEAR}/cbp{YEAR%100}co.zip"
US_URL = f"https://www2.census.gov/programs-surveys/cbp/datasets/{YEAR}/cbp{YEAR%100}us.zip"

NAICS = {
    "337///": "Furniture and related product manufacturing",
    "3371//": "Household and institutional furniture",
    "33712/": "Household and institutional furniture (nonupholstered wood group)",
    "337122": "Nonupholstered wood household furniture",
    "337127": "Institutional furniture",
    "3372//": "Office furniture (incl. fixtures)",
    "337211": "Wood office furniture",
    "337110": "Wood kitchen cabinet and countertop manufacturing",
    "337212": "Custom architectural woodwork and millwork",
    "321918": "Other millwork (incl. flooring)",
    "238350": "Finish carpentry contractors",
    "236118": "Residential remodelers",
    "423210": "Furniture merchant wholesalers",
    "442110": "Furniture stores (retail)",
    "453310": "Used merchandise stores",
}

# The nine-county Bay Area, plus Santa Cruz which sits in the same delivery radius.
BAY_AREA = {
    "001": "Alameda", "013": "Contra Costa", "041": "Marin", "055": "Napa",
    "075": "San Francisco", "081": "San Mateo", "085": "Santa Clara",
    "095": "Solano", "097": "Sonoma", "087": "Santa Cruz",
}


def fetch(url: str, member_hint: str):
    d = RAW / SOURCE
    d.mkdir(parents=True, exist_ok=True)
    local = d / url.rsplit("/", 1)[-1]
    if not local.exists():
        local.write_bytes(get(url, timeout=300).content)
    with zipfile.ZipFile(local) as z:
        name = next(n for n in z.namelist() if n.endswith(".txt") and member_hint in n)
        return list(csv.DictReader(io.TextIOWrapper(z.open(name), encoding="latin-1")))


def num(v):
    try:
        return int(str(v).strip() or 0)
    except ValueError:
        return 0


def main() -> None:
    with guard(SOURCE, "establishments-by-naics", CO_URL):
        rows_out = []

        # The national file breaks each NAICS out by legal form of organization;
        # lfo "-" is the all-establishments row.
        national = {r["naics"]: r for r in fetch(US_URL, "us")
                    if r["naics"] in NAICS and r.get("lfo", "-") == "-"}
        for code, r in national.items():
            rows_out.append({"geo_level": "us", "fips": "00000", "county": "United States",
                             "naics": code, "naics_label": NAICS[code], "estab": num(r["est"]),
                             "employees": num(r["emp"]), "annual_payroll_k": num(r["ap"]),
                             "estab_under_5_emp": num(r.get("n<5"))})

        counties = fetch(CO_URL, "co")
        ca = [r for r in counties if r["fipstate"] == "06" and r["naics"] in NAICS]
        for r in ca:
            cty = r["fipscty"]
            level = "bay_area_county" if cty in BAY_AREA else "ca_other_county"
            rows_out.append({
                "geo_level": level, "fips": f"06{cty}",
                "county": BAY_AREA.get(cty, f"CA county {cty}"),
                "naics": r["naics"], "naics_label": NAICS[r["naics"]],
                "estab": num(r["est"]), "employees": num(r["emp"]),
                "annual_payroll_k": num(r["ap"]),
                "estab_under_5_emp": num(r.get("n<5")),
            })

        # California and Bay Area roll-ups, summed from the county rows.
        for label, level, keep in (("California", "ca_total", lambda r: True),
                                   ("Bay Area (10 counties)", "bay_area_total",
                                    lambda r: r["fipscty"] in BAY_AREA)):
            for code in NAICS:
                sub = [r for r in ca if r["naics"] == code and keep(r)]
                if not sub:
                    continue
                rows_out.append({
                    "geo_level": level, "fips": "06" if level == "ca_total" else "06BAY",
                    "county": label, "naics": code, "naics_label": NAICS[code],
                    "estab": sum(num(r["est"]) for r in sub),
                    "employees": sum(num(r["emp"]) for r in sub),
                    "annual_payroll_k": sum(num(r["ap"]) for r in sub),
                    "estab_under_5_emp": sum(num(r.get("n<5")) for r in sub),
                })

        save_csv("cbp_furniture_supply", rows_out)
        record(SOURCE, "establishments-by-naics", CO_URL, len(rows_out),
               note=f"CBP {YEAR}")

        log(f"  CBP {YEAR} establishments:")
        for code in ("337122", "337211", "337212", "442110"):
            def n(lvl):
                m = [r for r in rows_out if r["geo_level"] == lvl and r["naics"] == code]
                return m[0]["estab"] if m else 0
            log(f"    {code} {NAICS[code][:42]:<42} US {n('us'):>6,}  "
                f"CA {n('ca_total'):>5,}  Bay {n('bay_area_total'):>4,}")


if __name__ == "__main__":
    main()
