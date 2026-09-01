"""Tier 2 — import exposure by HS code (USITC DataWeb substitute).

DataWeb needs an account token. UN Comtrade's public preview endpoint carries the same
underlying US import statistics with no credential, so that is what this pulls: annual
US imports for the wooden-furniture HS lines, by partner country.

Answers: how large is the tariff-exposed category, and how much of it is China/Vietnam —
i.e. how much of the domestic price umbrella is import-set.
"""
from __future__ import annotations

import sys
import time

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import get, guard, log, record, save_csv, save_raw  # noqa: E402

SOURCE = "un-comtrade"
BASE = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"
PARTNERS_URL = "https://comtradeapi.un.org/files/v1/app/reference/partnerAreas.json"
USA = 842

# The wooden-furniture lines. 940360 is the one that contains dining and occasional
# tables — the direct import substitute for a custom hardwood table.
HS = {
    "940330": "Wooden furniture — office",
    "940340": "Wooden furniture — kitchen",
    "940350": "Wooden furniture — bedroom",
    "940360": "Wooden furniture — other (incl. dining/living room tables)",
    "940391": "Furniture parts — of wood",
    "940161": "Seats with wooden frames — upholstered",
    "940169": "Seats with wooden frames — other",
}
YEARS = [2019, 2020, 2021, 2022, 2023, 2024, 2025]


def partner_names() -> dict[str, str]:
    try:
        payload = get(PARTNERS_URL, timeout=60).json()
        results = payload.get("results", payload if isinstance(payload, list) else [])
        return {str(p.get("id")): p.get("text", "") for p in results}
    except Exception as exc:  # noqa: BLE001
        log(f"  (partner names unavailable: {exc})")
        return {}


def main() -> None:
    with guard(SOURCE, "us-wood-furniture-imports", BASE):
        names = partner_names()
        rows, raw = [], {}
        for code, label in HS.items():
            for year in YEARS:
                try:
                    r = get(BASE, params={"reporterCode": USA, "period": year,
                                          "cmdCode": code, "flowCode": "M"}, timeout=90)
                    data = r.json().get("data") or []
                except Exception as exc:  # noqa: BLE001
                    log(f"  {code}/{year} skipped: {str(exc)[:90]}")
                    continue
                raw[f"{code}-{year}"] = data
                for d in data:
                    pcode = str(d.get("partnerCode"))
                    rows.append({
                        "hs_code": code,
                        "hs_label": label,
                        "year": year,
                        "partner_code": pcode,
                        "partner": d.get("partnerDesc") or names.get(pcode, pcode),
                        "value_usd": d.get("primaryValue"),
                        "net_weight_kg": d.get("netWgt"),
                        "is_aggregate": d.get("isAggregate"),
                    })
                time.sleep(0.6)  # public preview endpoint is unauthenticated; be polite
        save_raw(SOURCE, "us-wood-furniture-imports", raw)
        save_csv("imports_wood_furniture", rows)
        record(SOURCE, "us-wood-furniture-imports", BASE, len(rows))

        world = [r for r in rows if r["partner"] in ("World", "0") or r["partner_code"] == "0"]
        for y in YEARS:
            tot = sum(r["value_usd"] or 0 for r in world if r["year"] == y)
            if tot:
                log(f"  {y}: US wood-furniture imports (all listed HS) ${tot/1e9:.2f}bn")


if __name__ == "__main__":
    main()
