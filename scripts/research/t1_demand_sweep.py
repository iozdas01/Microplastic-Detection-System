"""Tier 1 — where does "make me this" demand actually concentrate, across every material.

`t1_custom_categories.py` sweeps the categories *underneath* furniture. This one sweeps
sideways instead: given that someone wants something manufactured to order, which family
do they want it in, and do they arrive using consumer words ("custom fire pit") or trade
words ("cnc machining service")?

That distinction is the whole point. A category can be large in aggregate spend and still
have nobody arriving at a website to ask for it — which is the failure mode the previous
furniture-only pass found and the reason it is worth measuring the trade vocabulary
alongside the consumer vocabulary rather than assuming they behave alike.

Anchored on "custom furniture" in every batch, which measured at 14.6 mean index against
both "custom signs" (25.2) and "custom t shirts" (16.9) — mid-scale enough to keep
resolution on small terms without being crushed by large ones. It is also the anchor that
makes this sweep directly comparable to the furniture-only ranking already on file.

WHAT THIS INSTRUMENT CANNOT SEE: search volume measures people who *search*. A maintenance
engineer with a blocked production part phones a shop they already know, or emails the OEM.
Absence here is evidence about arrival-by-search only, never about absence of the pain.
Read the `buyer` column before drawing any conclusion from a low score.
"""
from __future__ import annotations

import sys
import time

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import guard, log, record, save_csv, save_raw  # noqa: E402
from t1_google_trends import GEO, TIMEFRAME, Trends  # noqa: E402

SOURCE = "google-trends"
ANCHOR = "custom furniture"

# (term, family, buyer, vocabulary)
#   buyer      — who types this: consumer | business | mixed
#   vocabulary — consumer names the OBJECT, trade names the PROCESS or the SHOP.
#                Keeping them apart is what lets the sweep tell "no demand" from
#                "demand that does not arrive through a search box".
TERMS: list[tuple[str, str, str, str]] = [
    # ── sign & display ────────────────────────────────────────────────────
    ("custom signs",              "sign_display",    "mixed",    "object"),
    ("custom neon sign",          "sign_display",    "consumer", "object"),
    ("custom metal signs",        "sign_display",    "mixed",    "object"),
    ("custom engraving",          "sign_display",    "mixed",    "process"),
    # ── metal fabrication ─────────────────────────────────────────────────
    ("custom metal fabrication",  "metal_fab",       "mixed",    "process"),
    ("metal fabrication near me", "metal_fab",       "mixed",    "shop"),
    ("custom fire pit",           "metal_fab",       "consumer", "object"),
    ("custom gates",              "metal_fab",       "consumer", "object"),
    ("custom railings",           "metal_fab",       "mixed",    "object"),
    ("custom steel table",        "metal_fab",       "consumer", "object"),
    # ── machining ─────────────────────────────────────────────────────────
    ("cnc machining service",     "machining",       "business", "shop"),
    ("custom machined parts",     "machining",       "business", "object"),
    ("machine shop near me",      "machining",       "mixed",    "shop"),
    ("precision machining",       "machining",       "business", "process"),
    # ── blocked / obsolete parts — the H2 lane ────────────────────────────
    ("custom replacement part",   "parts_repair",    "mixed",    "object"),
    ("obsolete parts",            "parts_repair",    "business", "object"),
    ("reverse engineering parts", "parts_repair",    "business", "process"),
    ("part no longer available",  "parts_repair",    "mixed",    "object"),
    # ── additive ──────────────────────────────────────────────────────────
    ("3d printing service",       "additive",        "mixed",    "shop"),
    ("custom 3d printed parts",   "additive",        "mixed",    "object"),
    ("rapid prototyping service", "additive",        "business", "shop"),
    # ── laser / waterjet cutting ──────────────────────────────────────────
    ("custom laser cutting",      "cutting",         "mixed",    "process"),
    ("laser cutting service",     "cutting",         "mixed",    "shop"),
    ("waterjet cutting service",  "cutting",         "business", "shop"),
    # ── wood & panel (linkage to the furniture-only ranking) ──────────────
    ("custom cabinets",           "wood_panel",      "consumer", "object"),
    ("custom closet",             "wood_panel",      "consumer", "object"),
    ("custom built ins",          "wood_panel",      "consumer", "object"),
    ("custom wood furniture",     "wood_panel",      "consumer", "object"),
    # ── automotive & powersports ──────────────────────────────────────────
    ("custom car parts",          "auto_moto",       "consumer", "object"),
    ("custom motorcycle parts",   "auto_moto",       "consumer", "object"),
    ("custom exhaust",            "auto_moto",       "consumer", "object"),
    ("custom wheels",             "auto_moto",       "consumer", "object"),
    # ── plastics & moulding ───────────────────────────────────────────────
    ("custom injection molding",  "plastics",        "business", "process"),
    ("custom acrylic",            "plastics",        "mixed",    "object"),
    ("custom silicone mold",      "plastics",        "mixed",    "object"),
    # ── industrial hardware ───────────────────────────────────────────────
    ("custom enclosure",          "industrial",      "business", "object"),
    ("custom brackets",           "industrial",      "mixed",    "object"),
    ("custom tooling",            "industrial",      "business", "object"),
    # ── stone & surfaces ──────────────────────────────────────────────────
    ("custom countertops",        "stone_surface",   "consumer", "object"),
    # ── trailers & equipment ──────────────────────────────────────────────
    ("custom trailer",            "trailer_equip",   "mixed",    "object"),
    ("custom truck bed",          "trailer_equip",   "consumer", "object"),
    # ── soft goods — CALIBRATION ONLY, not machinable. Included so the
    #    machinable families can be read against a category that is known to
    #    sustain a real made-to-order web business. ─────────────────────────
    ("custom t shirts",           "soft_goods_cal",  "mixed",    "object"),
    ("custom embroidery",         "soft_goods_cal",  "mixed",    "process"),
]

META = {t: (fam, buyer, vocab) for t, fam, buyer, vocab in TERMS}


def run_sweep(tr, anchor: str, terms_meta: dict[str, tuple[str, str, str]],
              dataset: str, csv_prefix: str, batch_sleep: float = 3.0):
    """Anchored batch sweep. Shared so a narrower sweep reuses the anchoring, the
    resolution guard and the momentum window rather than reimplementing them.

    `terms_meta` maps term -> (family, buyer, vocabulary). Returns (rows, related).
    """
    keywords = list(terms_meta)
    batches = [keywords[i:i + 4] for i in range(0, len(keywords), 4)]
    rows, related, raw = [], [], {}
    anchor_done = False

    for bi, batch in enumerate(batches):
        terms = [anchor] + batch
        log(f"  batch {bi + 1}/{len(batches)}: {', '.join(batch)}")
        try:
            widgets = tr.widgets(terms)
        except Exception as exc:  # noqa: BLE001
            log(f"    !! explore failed: {str(exc)[:90]}")
            time.sleep(batch_sleep * 3)  # 429 is the usual cause; back off harder
            continue

        try:
            ts = tr.widget_data(widgets["TIMESERIES"], "multiline")
            raw[f"batch{bi}-ts"] = ts
            points = ts["default"]["timelineData"]
            n = max(len(points), 1)
            anchor_mean = sum(p["value"][0] for p in points) / n or 1

            for ti, term in enumerate(terms):
                if ti == 0 and anchor_done:
                    continue
                series = [p["value"][ti] for p in points]
                mean = sum(series) / n
                # Resolution guard: a term that sits at or below 1 for most of the window
                # is not measured, it is rounded.
                at_or_below_1 = sum(1 for v in series if v <= 1) / n
                recent = series[-52:] if len(series) >= 104 else []
                prior = series[-104:-52] if len(series) >= 104 else []
                yoy = None
                if recent and prior and sum(prior) > 0:
                    yoy = round((sum(recent) / 52) / (sum(prior) / 52) - 1, 4)
                fam, buyer, vocab = terms_meta.get(term, ("anchor", "mixed", "object"))
                rows.append({
                    "keyword": term,
                    "family": fam,
                    "buyer": buyer,
                    "vocabulary": vocab,
                    "is_anchor": ti == 0,
                    "mean_index": round(mean, 3),
                    "vs_anchor": round(mean / anchor_mean, 4),
                    "weeks_at_or_below_1": round(at_or_below_1, 3),
                    "resolved": at_or_below_1 < 0.5,
                    "momentum_yoy": yoy,
                    "batch": bi,
                })
                if ti == 0:
                    anchor_done = True
        except Exception as exc:  # noqa: BLE001
            log(f"    timeseries unavailable: {str(exc)[:80]}")

        for ti, term in enumerate(terms):
            if ti == 0:
                continue
            wid = f"RELATED_QUERIES_{ti}"
            if wid not in widgets:
                continue
            try:
                rq = tr.widget_data(widgets[wid], "relatedsearches")
            except Exception as exc:  # noqa: BLE001
                log(f"    related for '{term}': {str(exc)[:60]}")
                continue
            raw[f"batch{bi}-related-{ti}"] = rq
            for li, block in enumerate(rq.get("default", {}).get("rankedList", [])):
                kind = "top" if li == 0 else "rising"
                for item in block.get("rankedKeyword", []):
                    related.append({
                        "seed_term": term,
                        "family": terms_meta.get(term, ("", "", ""))[0],
                        "kind": kind,
                        "query": item.get("query", ""),
                        "value": item.get("value"),
                        "formatted_value": item.get("formattedValue", ""),
                    })
            time.sleep(1.5)
        time.sleep(batch_sleep)

    rows.sort(key=lambda r: -r["vs_anchor"])
    save_raw(SOURCE, dataset, raw)
    save_csv(csv_prefix, rows)
    save_csv(f"{csv_prefix}_related", related)
    return rows, related


def main() -> None:
    with guard(SOURCE, "custom-demand-sweep", "trends.google.com"):
        tr = Trends()
        rows, related = run_sweep(tr, ANCHOR, META, "custom-demand-sweep", "demand_sweep")
        record(SOURCE, "custom-demand-sweep", "trends.google.com",
               len(rows) + len(related),
               note=f"anchor='{ANCHOR}' geo={GEO} timeframe={TIMEFRAME} "
                    f"terms={len(META)} resolved={sum(1 for r in rows if r['resolved'])}")

        log("")
        log(f"  Interest relative to '{ANCHOR}' = 1.000 ({GEO}, {TIMEFRAME}):")
        log(f"    {'keyword':<28}{'family':<16}{'buyer':<10}{'vs':>8}  {'res':<5}{'yoy':>8}")
        for r in rows:
            yoy = f"{r['momentum_yoy']:+.0%}" if r["momentum_yoy"] is not None else "    \u2014"
            flag = "ok" if r["resolved"] else "THIN"
            log(f"    {r['keyword']:<28}{r['family']:<16}{r['buyer']:<10}"
                f"{r['vs_anchor']:>8.3f}  {flag:<5}{yoy:>8}")


if __name__ == "__main__":
    main()
