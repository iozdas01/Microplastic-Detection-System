"""Tier 1 — Etsy: the only place unit-level demand for custom tables is public.

The brief is right that this is the best unit data available: Etsy shops publish lifetime
sales counts and review counts, so you can count how many custom tables a maker has
actually sold, and at what price. eRank and Alura resell a view of this; the Etsy Open
API v3 gives it directly and is free for a personal app.

    ETSY_API_KEY  — "keystring" from https://www.etsy.com/developers/register

Etsy's public HTML is behind a bot wall (a plain fetch returns 403), so the API is the
route that works; scripts/README notes the browser fallback if an API key is refused.
"""
from __future__ import annotations

import sys
import time

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import ENV, get, guard, log, record, save_csv, save_raw  # noqa: E402

SOURCE = "etsy"
BASE = "https://openapi.etsy.com/v3/application"
QUERIES = ["custom dining table", "solid wood dining table", "walnut dining table",
           "live edge dining table", "custom wood desk", "handmade dining table"]
PER_QUERY = 100


def main() -> None:
    key = ENV.get("ETSY_API_KEY")
    if not key:
        log(f"→ {SOURCE}: SKIPPED — no ETSY_API_KEY "
            "(free: https://www.etsy.com/developers/register)")
        record(SOURCE, "listings-and-shop-sales", BASE, 0,
               status="blocked_no_credential", note="ETSY_API_KEY not set")
        return

    with guard(SOURCE, "listings-and-shop-sales", BASE):
        headers = {"x-api-key": key}
        listings, raw = [], {}
        shop_ids: set[int] = set()

        for q in QUERIES:
            payload = get(f"{BASE}/listings/active", headers=headers, timeout=60,
                          params={"keywords": q, "limit": PER_QUERY,
                                  "sort_on": "score"}).json()
            raw[q] = payload
            for it in payload.get("results", []):
                price = it.get("price") or {}
                amount = price.get("amount")
                divisor = price.get("divisor") or 100
                listings.append({
                    "query": q,
                    "listing_id": it.get("listing_id"),
                    "shop_id": it.get("shop_id"),
                    "title": (it.get("title") or "")[:160],
                    "price_usd": round(amount / divisor, 2) if amount else None,
                    "currency": price.get("currency_code", ""),
                    "quantity": it.get("quantity"),
                    "num_favorers": it.get("num_favorers"),
                    "made_to_order": it.get("when_made", ""),
                    "views": it.get("views"),
                    "url": it.get("url", ""),
                })
                if it.get("shop_id"):
                    shop_ids.add(it["shop_id"])
            time.sleep(0.4)

        # Lifetime sales per shop — the number that makes this source worth using.
        shops = []
        for sid in sorted(shop_ids):
            try:
                s = get(f"{BASE}/shops/{sid}", headers=headers, timeout=45).json()
            except Exception:  # noqa: BLE001
                continue
            shops.append({
                "shop_id": sid, "shop_name": s.get("shop_name", ""),
                "lifetime_sales": s.get("transaction_sold_count"),
                "review_count": s.get("review_count"),
                "review_average": s.get("review_average"),
                "listing_active_count": s.get("listing_active_count"),
                "created_timestamp": s.get("create_date") or s.get("created_timestamp"),
                "url": s.get("url", ""),
            })
            time.sleep(0.3)

        save_raw(SOURCE, "listings-and-shop-sales", raw)
        save_csv("etsy_listings", listings)
        save_csv("etsy_shops", shops)
        record(SOURCE, "listings-and-shop-sales", BASE, len(listings) + len(shops),
               note=f"{len(QUERIES)} queries, {len(shops)} shops resolved")

        prices = sorted(x["price_usd"] for x in listings if x["price_usd"])
        if prices:
            med = prices[len(prices) // 2]
            log(f"  {len(listings)} listings, median price ${med:,.0f}, "
                f"range ${prices[0]:,.0f}–${prices[-1]:,.0f}")
        top = sorted([s for s in shops if s["lifetime_sales"]],
                     key=lambda s: -s["lifetime_sales"])[:10]
        for s in top:
            log(f"    {s['shop_name'][:34]:<34} {s['lifetime_sales']:>8,} lifetime sales")


if __name__ == "__main__":
    main()
