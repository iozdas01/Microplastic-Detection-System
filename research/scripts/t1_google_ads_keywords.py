"""Tier 1 — Google Keyword Planner: search volume and, more importantly, CPC.

The brief is right that CPC is the valuable half. `high_top_of_page_bid` is what an
advertiser must pay for a click at the top of the page; divide it by a realistic
site conversion rate and you have the customer-acquisition-cost floor for buying this
demand, before a dollar is spent.

Requires a Google Ads account (free to create; no spend needed for Keyword Planner) and
a developer token. Set in .env:
    GOOGLE_ADS_DEVELOPER_TOKEN, GOOGLE_ADS_CLIENT_ID, GOOGLE_ADS_CLIENT_SECRET,
    GOOGLE_ADS_REFRESH_TOKEN, GOOGLE_ADS_CUSTOMER_ID   (login customer id, digits only)
See docs/CREDENTIALS.md for how to get each one.
"""
from __future__ import annotations

import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import ENV, guard, log, record, save_csv, save_raw  # noqa: E402

SOURCE = "google-ads"
UNITED_STATES = "geoTargetConstants/2840"
CALIFORNIA = "geoTargetConstants/21137"
SF_BAY_DMA = "geoTargetConstants/200807"   # San Francisco-Oakland-San Jose DMA
ENGLISH = "languageConstants/1000"

SEEDS = [
    # the term the whole thesis rests on, and its buying-intent tail
    "custom cabinets", "custom kitchen cabinets", "custom cabinets near me",
    "custom cabinets cost", "custom cabinet makers", "custom cabinetry",
    # the semi-custom band a configurator actually competes in
    "semi custom cabinets", "kitchen cabinets custom size", "frameless cabinets",
    "european kitchen cabinets", "rta kitchen cabinets",
    # the wider purchase this sits inside — where the buyer starts
    "kitchen remodel cost", "kitchen cabinet cost", "replace kitchen cabinets",
    "new kitchen cabinets", "kitchen renovation",
    # the configurator framing: does anyone search for the product we are building?
    "online kitchen design", "kitchen design tool", "design your own kitchen",
    "kitchen cabinet configurator",
    # adjacent panel categories the same cell would serve
    "custom closet", "custom vanity", "custom wardrobe",
]
REQUIRED = ["GOOGLE_ADS_DEVELOPER_TOKEN", "GOOGLE_ADS_CLIENT_ID",
            "GOOGLE_ADS_CLIENT_SECRET", "GOOGLE_ADS_REFRESH_TOKEN",
            "GOOGLE_ADS_CUSTOMER_ID"]


def micros(v) -> float | None:
    return round(v / 1_000_000, 2) if v else None


def main() -> None:
    missing = [k for k in REQUIRED if not ENV.get(k)]
    if missing:
        log(f"→ {SOURCE}: SKIPPED — missing {', '.join(missing)}")
        record(SOURCE, "keyword-metrics", "googleads.googleapis.com", 0,
               status="blocked_no_credential", note=f"missing: {', '.join(missing)}")
        return

    with guard(SOURCE, "keyword-metrics", "googleads.googleapis.com"):
        from google.ads.googleads.client import GoogleAdsClient

        client = GoogleAdsClient.load_from_dict({
            "developer_token": ENV["GOOGLE_ADS_DEVELOPER_TOKEN"],
            "client_id": ENV["GOOGLE_ADS_CLIENT_ID"],
            "client_secret": ENV["GOOGLE_ADS_CLIENT_SECRET"],
            "refresh_token": ENV["GOOGLE_ADS_REFRESH_TOKEN"],
            "login_customer_id": ENV["GOOGLE_ADS_CUSTOMER_ID"].replace("-", ""),
            "use_proto_plus": True,
        })
        svc = client.get_service("KeywordPlanIdeaService")
        rows, raw = [], {}

        for geo_label, geo in (("California", CALIFORNIA), ("SF Bay Area DMA", SF_BAY_DMA)):
            req = client.get_type("GenerateKeywordIdeasRequest")
            req.customer_id = ENV["GOOGLE_ADS_CUSTOMER_ID"].replace("-", "")
            req.language = ENGLISH
            req.geo_target_constants.append(geo)
            req.include_adult_keywords = False
            req.keyword_plan_network = (
                client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH)
            req.keyword_seed.keywords.extend(SEEDS)

            response = svc.generate_keyword_ideas(request=req)
            raw[geo_label] = []
            for idea in response:
                m = idea.keyword_idea_metrics
                rec = {
                    "geo": geo_label,
                    "keyword": idea.text,
                    "avg_monthly_searches": m.avg_monthly_searches or 0,
                    "competition": m.competition.name if m.competition else "",
                    "competition_index": m.competition_index or 0,
                    "low_top_of_page_bid_usd": micros(m.low_top_of_page_bid_micros),
                    "high_top_of_page_bid_usd": micros(m.high_top_of_page_bid_micros),
                }
                rec["monthly_search_value_usd"] = round(
                    (rec["avg_monthly_searches"] or 0)
                    * (rec["high_top_of_page_bid_usd"] or 0), 2)
                rows.append(rec)
                raw[geo_label].append(rec)

        rows.sort(key=lambda r: -(r["avg_monthly_searches"] or 0))
        save_raw(SOURCE, "keyword-metrics", raw)
        save_csv("keyword_planner_metrics", rows)
        record(SOURCE, "keyword-metrics", "googleads.googleapis.com", len(rows),
               note=f"{len(SEEDS)} seeds, 2 geos")

        log(f"  {len(rows)} keyword ideas. Top by volume:")
        for r in rows[:12]:
            log(f"    {r['keyword'][:44]:<44} {r['avg_monthly_searches']:>7,}/mo  "
                f"CPC ${r['high_top_of_page_bid_usd'] or 0:.2f}  {r['geo']}")


if __name__ == "__main__":
    main()
