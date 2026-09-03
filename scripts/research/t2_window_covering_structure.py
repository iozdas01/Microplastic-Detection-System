"""Size distribution of the US window-covering trade, from Census CBP the repo already holds.

Written 2026-09-03 to replace an unsourced figure. The window-coverings recon asserted
"484 establishments, ~$2.4-2.5bn revenue, NAICS 337920, 2025" with no URL and no manifest
entry. CBP 2022 — the file already in `data/raw/census-cbp/` — puts 337920 at 329
establishments. Revenue is not a CBP variable at all, so that figure cannot have come from
here and remains unsourced.

The structural finding matters more than the correction. Three NAICS codes touch this trade
and they have very different shapes, which is what decides whether there is an enterprise
buyer:

    337920  blind & shade manufacturing      — who MAKES the product
    442291  window treatment stores          — who MEASURES and sells it
    238390  other building finishing         — who INSTALLS it

The measure visit is a dealer cost, so sizing it off the manufacturing code sizes the wrong
population.

    python scripts/research/t2_window_covering_structure.py
"""
from __future__ import annotations

import csv
import io
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "reports/high-mix-manufacturing/research/data/raw/census-cbp/cbp22us.zip"
OUT = ROOT / "reports/high-mix-manufacturing/research/data/processed/window_covering_structure.csv"

CODES = {
    "337920": "Blind and shade manufacturing",
    "442291": "Window treatment stores (retail)",
    "238390": "Other building finishing contractors",
}
BANDS = [("n<5", "<5"), ("n5_9", "5-9"), ("n10_19", "10-19"), ("n20_49", "20-49"),
         ("n50_99", "50-99"), ("n100_249", "100-249"), ("n250_499", "250-499"),
         ("n500_999", "500-999"), ("n1000", "1000+")]


def _int(v: str) -> int:
    """CBP suppresses small cells with letter flags; those are zero establishments here."""
    try:
        return int(v)
    except (TypeError, ValueError):
        return 0


def main() -> int:
    with zipfile.ZipFile(RAW) as z:
        name = z.namelist()[0]
        rows = list(csv.DictReader(io.TextIOWrapper(z.open(name), encoding="latin-1")))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["naics", "label", "band", "establishments", "share_of_establishments",
                    "total_establishments", "total_employees", "annual_payroll_usd"])
        for code, label in CODES.items():
            r = next((x for x in rows if x["naics"] == code and x["lfo"] == "-"), None)
            if r is None:
                print(f"[warn] {code} absent from CBP 2022 national file")
                continue
            est, emp, ap = _int(r["est"]), _int(r["emp"]), _int(r["ap"]) * 1000
            print(f"{code} {label}: {est:,} establishments · {emp:,} employees · ${ap/1e6:,.0f}m payroll")
            for key, band in BANDS:
                n = _int(r[key])
                if not n:
                    continue
                w.writerow([code, label, band, n, round(n / est, 4), est, emp, ap])
                print(f"    {band:>9} employees : {n:>5}  ({n/est*100:4.1f}%)")
    print(f"\n[ok] wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
