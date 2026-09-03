"""Tier 2 — SUSB: the window-coverings market as a ladder of business sizes.

The founder's question is not "how big is the market" but "size the smallest business, then
go one layer up, all the way to enterprise — and does enterprise even have this problem".
That is a question about market STRUCTURE, and Census SUSB answers it directly: it buckets
every firm in an industry by its own annual receipts and reports firms, establishments,
employment, payroll and receipts per bucket.

Two industries carry the US window-coverings trade:

  337920  Blind and Shade Manufacturing — who cuts to size
  442291  Window Treatment Stores       — who sells and usually measures

238390 (Other Building Finishing Contractors) is collected as CONTEXT ONLY and must never be
quoted as a window-coverings number: it is a catch-all that includes drywall finishers and
many other trades, so the blinds share of it is unknown and certainly a minority.

Keyless. The Economic Census `ecnbasic` API returns HTTP 302 without a CENSUS_API_KEY, so the
SUSB bulk workbook is the only free path to RECEIPTS by size class — and receipts, not
payroll, is what makes the layers comparable to each other.
"""
from __future__ import annotations

import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import RAW, get, guard, log, record, save_csv  # noqa: E402

SOURCE = "census-susb"
YEAR = 2022
URL = (f"https://www2.census.gov/programs-surveys/susb/tables/{YEAR}/"
       f"us_6digitnaics_rcptsize_{YEAR}.xlsx")

NAICS = {
    # ── the window-coverings trade itself ────────────────────────────────
    "337920": ("Blind and shade manufacturing", "manufacturer"),
    "442291": ("Window treatment stores", "retail_dealer"),
    "238390": ("Other building finishing contractors (CONTEXT ONLY — not blinds-specific)",
               "context_only"),
    # ── adjacent MADE-TO-MEASURE industries, collected to answer one
    #    question the blinds numbers cannot: does the measure-to-machine
    #    problem generalise, or is a blinds-only company the whole ceiling?
    #    Every one of these cuts a product to a dimension taken at a site.
    "337110": ("Wood kitchen cabinet and countertop manufacturing", "adjacent_mtm"),
    "321911": ("Wood window and door manufacturing", "adjacent_mtm"),
    "327991": ("Cut stone and stone product manufacturing", "adjacent_mtm"),
    "238350": ("Finish carpentry contractors", "adjacent_mtm"),
    "238150": ("Glass and glazing contractors", "adjacent_mtm"),
}


def main() -> None:
    with guard(SOURCE, "window-coverings-ladder", "www2.census.gov"):
        import openpyxl

        dest = RAW / SOURCE / f"us_6digitnaics_rcptsize_{YEAR}.xlsx"
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            log(f"  downloading {URL}")
            r = get(URL)
            dest.write_bytes(r.content)
        log(f"  {dest.name} ({dest.stat().st_size:,} bytes)")

        wb = openpyxl.load_workbook(dest, read_only=True, data_only=True)
        ws = wb["US 6-digit NAICS"]
        rows_iter = ws.iter_rows(values_only=True)
        for _ in range(3):
            next(rows_iter)  # title, source note, header

        out = []
        for r in rows_iter:
            code = str(r[0]).strip() if r[0] else ""
            if code not in NAICS:
                continue
            label, role = NAICS[code]
            bucket = str(r[2]).strip() if r[2] else ""
            # "01: Total", "02: <100", ... — keep the sort key and the human label apart
            order, _, band = bucket.partition(":")
            out.append({
                "naics": code,
                "industry": label,
                "role": role,
                "bucket_order": order.strip(),
                "receipts_band_usd_000": band.strip(),
                "firms": r[3],
                "establishments": r[4],
                "employment": r[5],
                "payroll_usd_000": r[7],
                "receipts_usd_000": r[9] if len(r) > 9 else None,
            })

        save_csv("market_ladder_susb", out)
        record(SOURCE, "window-coverings-ladder", URL, len(out),
               note=f"SUSB {YEAR} receipts-size ladder for "
                    f"{', '.join(sorted(NAICS))} — keyless bulk workbook")

        log("")
        for code in ("337920", "442291"):
            rows = [x for x in out if x["naics"] == code]
            tot = next((x for x in rows if x["bucket_order"] == "01"), None)
            if not tot:
                continue
            log(f"  {code} {NAICS[code][0]}")
            log(f"    {tot['firms']:,} firms · {tot['establishments']:,} establishments · "
                f"${(tot['receipts_usd_000'] or 0)/1e6:,.2f}bn receipts")
            for x in rows:
                if x["bucket_order"] == "01":
                    continue
                rc = (x["receipts_usd_000"] or 0) / 1000
                shr = (x["receipts_usd_000"] or 0) / (tot["receipts_usd_000"] or 1)
                log(f"      {x['receipts_band_usd_000']:<16}{x['firms']:>6} firms  "
                    f"${rc:>9,.1f}m  {shr:>6.1%}")


if __name__ == "__main__":
    main()
