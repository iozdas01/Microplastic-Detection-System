"""Tier 1 — Semrush: which keywords actually drive competitor revenue.

Reverse-engineers organic search traffic for the custom/solid-wood furniture brands the
brief names plus the credible independents. The useful output is not "how much traffic" —
it is which specific queries carry the traffic, because that is the demand a new entrant
would have to take.

Requires SEMRUSH_API_KEY (paid; ~$130 for one month, then cancel — the brief's own plan).
The API is credit-metered: each row of domain_organic costs 10 units.
"""
from __future__ import annotations

import csv
import io
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import ENV, get, guard, log, record, save_csv  # noqa: E402

SOURCE = "semrush"
API = "https://api.semrush.com/"
DATABASE = "us"
LIMIT = 100
DOMAINS = [
    "roomandboard.com",       # named in the brief — custom dining programme
    "ethanallen.com",         # named in the brief — custom programme
    "arhaus.com",
    "thejoinery.com",         # independent hardwood, made to order
    "vermontwoodsstudios.com",
    "hardwoodartisans.com",
    "moderntimeschicago.com",
    "danielgeorgefurniture.com",
    "cbfurniture.com",
]
COLUMNS = "Ph,Po,Nq,Cp,Co,Tr,Tc,Ur"   # phrase, position, volume, CPC, competition, traffic%, cost%, url


def main() -> None:
    if not ENV.get("SEMRUSH_API_KEY"):
        log(f"→ {SOURCE}: SKIPPED — no SEMRUSH_API_KEY")
        record(SOURCE, "competitor-organic-keywords", API, 0,
               status="blocked_no_credential", note="SEMRUSH_API_KEY not set")
        return

    with guard(SOURCE, "competitor-organic-keywords", API):
        rows = []
        for domain in DOMAINS:
            try:
                text = get(API, params={
                    "type": "domain_organic", "key": ENV["SEMRUSH_API_KEY"],
                    "display_limit": LIMIT, "export_columns": COLUMNS,
                    "domain": domain, "database": DATABASE}, timeout=90).text
            except Exception as exc:  # noqa: BLE001
                log(f"    {domain}: {str(exc)[:80]}")
                continue
            if text.startswith("ERROR"):
                log(f"    {domain}: {text.strip()[:90]}")
                continue
            for r in csv.DictReader(io.StringIO(text), delimiter=";"):
                rows.append({
                    "domain": domain,
                    "keyword": r.get("Keyword", ""),
                    "position": r.get("Position", ""),
                    "search_volume": r.get("Search Volume", ""),
                    "cpc_usd": r.get("CPC", ""),
                    "competition": r.get("Competition", ""),
                    "traffic_pct": r.get("Traffic (%)", ""),
                    "traffic_cost_pct": r.get("Traffic Cost (%)", ""),
                    "url": r.get("Url", ""),
                })
        save_csv("semrush_competitor_keywords", rows)
        record(SOURCE, "competitor-organic-keywords", API, len(rows),
               note=f"{len(DOMAINS)} domains, top {LIMIT} organic keywords each")
        log(f"  {len(rows)} keyword rows across {len({r['domain'] for r in rows})} domains")


if __name__ == "__main__":
    main()
