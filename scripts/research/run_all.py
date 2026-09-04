"""Run every collector, then the model, then the report.

Collectors are independent: one failing or being blocked on a credential never stops the
others. The run ends with a status table showing what landed and what is still gated.

    .venv/bin/python scripts/run_all.py            # everything
    .venv/bin/python scripts/run_all.py --tier2    # only the free government sources
"""
from __future__ import annotations

import importlib
import json
import sys
import traceback

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import MANIFEST, log  # noqa: E402

TIER1 = ["t1_google_trends", "t1_custom_categories", "t1_google_ads_keywords",
         "t1_semrush", "t1_etsy_supply"]
TIER2 = ["t2_census_mrts", "t2_bls_cex", "t2_bls_prices", "t2_cbp_supply",
         "t2_permits", "t2_popest", "t2_metro_coverage", "t2_trade_imports",
         "t2_census_acs", "t2_census_econ",
         # ARTS before merchline: merchline reads the all-retail benchmark ARTS writes.
         "t2_census_arts_ecommerce", "t2_census_merchline_window"]


def main() -> None:
    args = set(sys.argv[1:])
    mods = []
    if not args or "--tier1" in args:
        mods += TIER1
    if not args or "--tier2" in args:
        mods += TIER2
    if "--tier1" in args and "--tier2" not in args:
        mods = TIER1
    if "--tier2" in args and "--tier1" not in args:
        mods = TIER2

    start = MANIFEST.stat().st_size if MANIFEST.exists() else 0

    for name in mods:
        try:
            importlib.import_module(name).main()
        except Exception:  # noqa: BLE001 — a broken collector must not stop the run
            log(f"!! {name} raised:\n{traceback.format_exc(limit=3)}")

    # The US model is the default chain. The Bay Area / dining-table chain
    # (build_tam, build_report) is still runnable directly for the local view;
    # its last output is kept in reports/archive/.
    # build_factory runs first: it derives capacity and cost from cycle times, and
    # build_tam_us consumes both. The dependency runs supply -> demand, not the reverse.
    for name in ("analyse_custom_categories", "analyse_custom_demand",
                 "build_cabinet_tam", "build_factory", "build_tam_us",
                 "build_report_us"):
        try:
            importlib.import_module(name).main()
        except Exception:  # noqa: BLE001
            log(f"!! {name} raised:\n{traceback.format_exc(limit=3)}")

    log("")
    log("  SOURCE STATUS")
    log("  " + "-" * 74)
    if MANIFEST.exists():
        with MANIFEST.open() as fh:
            fh.seek(start)
            seen = {}
            for line in fh:
                try:
                    e = json.loads(line)
                except json.JSONDecodeError:
                    continue
                seen[(e["source"], e["dataset"])] = e
        for (src, ds), e in sorted(seen.items()):
            mark = {"ok": "✓", "failed": "✗"}.get(e["status"], "·")
            log(f"  {mark} {src:<16} {ds:<30} {e['rows']:>6,} rows  {e['status']}")


if __name__ == "__main__":
    main()
