"""Tier 2 — Census ARTS: how much of retail actually happens online, by kind of business.

Collected to settle one number that was being quoted from memory. A "16% of window covering
sales happen online" figure was recalled as prior research; it is not in this repo, and the
closest thing to it — `online_addressable_share` in the cabinet TAM — is declared an
ASSUMPTION in REPORT.md, is about custom cabinets, and was never measured. This collector
fetches the measured figure so the two cannot be confused again.

WHAT THIS MEASURES, AND WHAT IT DOES NOT. ARTS reports e-commerce by the SELLER's kind of
business, not by merchandise line. "Furniture and home furnishings stores sell 3.3% online"
does NOT mean 3.3% of furniture is bought online — a sofa bought on Wayfair is counted under
nonstore retailers (454), not under 442. So this table gives channel STRUCTURE, and it cannot
give the online share of any single product category.

There is no keyless source for the online share of window coverings specifically. Merchandise
-line detail lives in the Economic Census, whose API returns HTTP 302 without a key. Until
that key exists, the category's online share is an OPEN QUESTION, not a known number — which
is precisely why the H3 statement asserts that the measuring step caps the online share
without claiming what the share is.
"""
from __future__ import annotations

import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import RAW, get, guard, log, record, save_csv  # noqa: E402

SOURCE = "census-arts"
YEAR = 2022
URL = f"https://www2.census.gov/programs-surveys/arts/tables/{YEAR}/ecommerce.xlsx"


def main() -> None:
    with guard(SOURCE, "retail-ecommerce-share", "www2.census.gov"):
        import openpyxl

        dest = RAW / SOURCE / f"arts-ecommerce-{YEAR}.xlsx"
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            log(f"  downloading {URL}")
            dest.write_bytes(get(URL).content)
        log(f"  {dest.name} ({dest.stat().st_size:,} bytes)")

        wb = openpyxl.load_workbook(dest, read_only=True, data_only=True)
        ws = wb[wb.sheetnames[0]]
        rows = []
        for r in ws.iter_rows(values_only=True):
            cells = list(r)
            if len(cells) < 3:
                continue
            code = str(cells[0]).strip() if cells[0] is not None else ""
            label = str(cells[1]).strip().rstrip(". ") if cells[1] is not None else ""
            total, ecom = cells[2], cells[3] if len(cells) > 3 else None
            if not label or not isinstance(total, (int, float)):
                # the "Total Retail Trade" row carries its label in column B with no code
                if isinstance(cells[1], (int, float)) and code.startswith("Total"):
                    label, total, ecom = code, cells[1], cells[2]
                else:
                    continue
            # 'D' withheld, 'S' below publication standard — kept as a flag, never as 0
            flag = ecom if isinstance(ecom, str) else ""
            ecom_val = ecom if isinstance(ecom, (int, float)) else None
            rows.append({
                "naics": code if code and not code.startswith("Total") else "",
                "kind_of_business": label,
                "total_sales_usd_m": total,
                "ecommerce_sales_usd_m": ecom_val,
                "suppression_flag": flag,
                "ecommerce_share": (round(ecom_val / total, 4)
                                    if ecom_val and total else None),
            })

        save_csv("retail_ecommerce_share", rows)
        record(SOURCE, "retail-ecommerce-share", URL, len(rows),
               note=f"ARTS {YEAR} e-commerce by kind of business — by SELLER type, "
                    f"not by merchandise line")

        log("")
        log(f"  US retail e-commerce share, {YEAR} (by kind of business):")
        for r in rows:
            if r["ecommerce_share"] is None:
                continue
            log(f"    {(r['naics'] or '—'):<6}{r['kind_of_business'][:46]:<48}"
                f"{r['ecommerce_share']:>7.1%}")


if __name__ == "__main__":
    main()
