"""GDELT queries — two surfaces:

  * ``news``     (REST, keyless)  — per-company article lookup for personalisation
  * ``timeline`` (BigQuery, GCP)  — category aggregates: monthly mentions, tone,
                                    entity timelines, geographic distribution

CLI:
    # Per-company news (REST, allowlist-filtered):
    python -m scripts.data.gdelt news \
        --company "Mærsk A/S" --keywords "delays,downtime" [--months 6]

    # Category aggregates (BigQuery — needs GCP_PROJECT_ID + GOOGLE_APPLICATION_CREDENTIALS):
    python -m scripts.data.gdelt timeline \
        --themes "WIND_ENERGY,WORKPLACE_SAFETY" \
        --start-date 2022-01-01 --end-date 2026-07-05 \
        [--entities "Voliro,Aerones,Skygauge"]

Emits JSON on stdout. Rate-limit + cost-cap logic preserved from the original
mining/intel implementations.

Python API:
    from scripts.data.gdelt import query_news, query_timeline
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import sys
import time
import unicodedata
import urllib.parse
from pathlib import Path
from typing import Any

from scripts.data._common import (
    LATIN_FOLD,
    LEGAL_SUFFIXES,
    NEWS_DOMAIN_ALLOWLIST,
    emit_json,
    http_get,
    is_enabled,
    log_manifest,
)


# ---------------------------------------------------------------------------
# REST (per-company news) — throttled, allowlist-filtered
# ---------------------------------------------------------------------------

# GDELT's REST endpoint (api.gdeltproject.org/api/v2/doc/doc) enforces roughly
# one request per 5 seconds. Exceeding it returns HTTP 429 after ~9 seconds, so
# timeouts under 10s never see the throttle message and make the API look dead.
_GDELT_STATUS = {"last_call_ts": 0.0, "consecutive_failures": 0, "dead": False}
_GDELT_MIN_INTERVAL_SEC = 5.5


def _throttle_wait() -> None:
    elapsed = time.time() - _GDELT_STATUS["last_call_ts"]
    if elapsed < _GDELT_MIN_INTERVAL_SEC:
        time.sleep(_GDELT_MIN_INTERVAL_SEC - elapsed)
    _GDELT_STATUS["last_call_ts"] = time.time()


def _name_variants(company: str, parent_entity: str | None = None) -> list[str]:
    """GDELT search is literal — try the raw name and a legal-suffix-stripped one."""
    import html as _html
    variants: list[str] = []
    if company:
        variants.append(_html.unescape(company))
        stripped = _html.unescape(company).translate(LATIN_FOLD)
        stripped = unicodedata.normalize("NFKD", stripped)
        stripped = "".join(c for c in stripped if not unicodedata.combining(c))
        tokens = stripped.split()
        while tokens and tokens[-1].rstrip(".,").lower() in LEGAL_SUFFIXES:
            tokens.pop()
        stripped = " ".join(tokens).strip()
        if stripped and stripped != variants[0]:
            variants.append(stripped)
    if parent_entity and parent_entity not in variants:
        variants.append(parent_entity)
    return variants


def query_news(company: str, keywords: list[str], months_back: int = 6,
               slug: str | None = None,
               parent_entity: str | None = None) -> list[dict]:
    """Company-scoped GDELT REST news search. Throttled, allowlist-filtered.

    Registry gate: ``gdelt_rest`` must be enabled. Returns up to 5 articles from
    the trusted-domain allowlist.
    """
    if not is_enabled("gdelt_rest"):
        return []
    if _GDELT_STATUS["dead"]:
        log_manifest(slug, {"phase": "api_call", "api": "gdelt_rest",
                            "company": company, "decision": "skip",
                            "reason": "circuit_breaker_open"})
        return []

    endpoint = "https://api.gdeltproject.org/api/v2/doc/doc"
    articles: list[dict] = []
    tried: list[str] = []
    variants = _name_variants(company, parent_entity)

    for name_variant in variants[:2]:
        _throttle_wait()
        tried.append(name_variant)
        query = f'"{name_variant}" ({" OR ".join(keywords)})'
        params = {
            "query": query,
            "mode": "ArtList",
            "maxrecords": 10,
            "format": "json",
            "timespan": f"{months_back}M",
            "sort": "DateDesc",
        }
        r = http_get(endpoint, params=params, timeout=20, retries=1)
        if r is None:
            _GDELT_STATUS["consecutive_failures"] += 1
            if _GDELT_STATUS["consecutive_failures"] >= 5:
                _GDELT_STATUS["dead"] = True
                log_manifest(slug, {"phase": "circuit_breaker",
                                    "api": "gdelt_rest", "state": "OPEN",
                                    "reason": "5_consecutive_network_failures"})
                return []
            continue
        if r.status_code == 429:
            time.sleep(10)
            _GDELT_STATUS["consecutive_failures"] += 1
            continue
        if r.status_code != 200:
            _GDELT_STATUS["consecutive_failures"] += 1
            continue
        _GDELT_STATUS["consecutive_failures"] = 0
        try:
            articles = r.json().get("articles", []) or []
        except ValueError:
            articles = []
        if articles:
            break

    filtered: list[dict] = []
    for a in articles:
        url = a.get("url", "")
        domain = urllib.parse.urlparse(url).netloc.lower().lstrip("www.")
        if not any(domain.endswith(d) for d in NEWS_DOMAIN_ALLOWLIST):
            continue
        seendate = a.get("seendate", "")
        try:
            date_iso = datetime.datetime.strptime(seendate[:8], "%Y%m%d").strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            date_iso = ""
        filtered.append({
            "title": a.get("title", ""),
            "date": date_iso,
            "url": url,
            "domain": domain,
            "source": "GDELT",
        })
        if len(filtered) >= 5:
            break

    log_manifest(slug, {"phase": "api_call", "api": "gdelt_rest",
                        "company": company, "tried_variants": tried,
                        "result_count": len(filtered)})
    return filtered


# ---------------------------------------------------------------------------
# BigQuery (category aggregates) — dry-run guarded, usage-logged
# ---------------------------------------------------------------------------

BQ_MAX_MB_PER_QUERY = 2000
BQ_USAGE_LOG = ".gdelt-usage.log"


def _bq_dry_run_and_execute(client: Any, sql: str, query_name: str,
                            max_mb: int = BQ_MAX_MB_PER_QUERY):
    """Dry-run first, refuse if projected scan > max_mb, log actual bytes on success."""
    from google.cloud import bigquery  # local import — only needed for BigQuery path

    dry_config = bigquery.QueryJobConfig(dry_run=True, use_query_cache=False)
    dry = client.query(sql, job_config=dry_config)
    mb = dry.total_bytes_processed / 1024 / 1024
    if mb > max_mb:
        return {
            "error": f"Query '{query_name}' would scan {mb:.0f} MB — over the {max_mb} MB cap",
            "would_scan_mb": mb,
            "query_name": query_name,
        }, mb

    job = client.query(sql)
    rows = [dict(r) for r in job.result()]
    actual_mb = job.total_bytes_processed / 1024 / 1024
    try:
        with open(BQ_USAGE_LOG, "a") as f:
            f.write(f"{datetime.datetime.utcnow().isoformat()}\t{query_name}\t{actual_mb:.1f}\n")
    except Exception:
        pass
    return {"rows": rows, "mb_scanned": actual_mb, "row_count": len(rows)}, actual_mb


def _theme_or_clause(themes: list[str]) -> str:
    conditions = " OR ".join(f"V2Themes LIKE '%{t.strip()}%'" for t in themes if t.strip())
    return f"({conditions})" if conditions else "TRUE"


def _bq_timeline_sql(themes: list[str], start_date: str, end_date: str) -> str:
    return f"""
    SELECT
      DATE_TRUNC(DATE(_PARTITIONTIME), MONTH) AS month,
      COUNT(*) AS mentions
    FROM `gdelt-bq.gdeltv2.gkg_partitioned`
    WHERE _PARTITIONTIME >= "{start_date}"
      AND _PARTITIONTIME < "{end_date}"
      AND {_theme_or_clause(themes)}
    GROUP BY month
    ORDER BY month
    """


def _bq_negative_articles_sql(themes: list[str], start_date: str, end_date: str,
                              limit: int = 25) -> str:
    return f"""
    SELECT
      DATE(_PARTITIONTIME) AS date,
      DocumentIdentifier AS url,
      SourceCommonName AS source,
      SAFE_CAST(REGEXP_EXTRACT(V2Tone, r'^([-\\d.]+)') AS FLOAT64) AS avg_tone,
      SUBSTR(V2Themes, 0, 400) AS themes_snippet
    FROM `gdelt-bq.gdeltv2.gkg_partitioned`
    WHERE _PARTITIONTIME >= "{start_date}"
      AND _PARTITIONTIME < "{end_date}"
      AND {_theme_or_clause(themes)}
      AND V2Tone IS NOT NULL
    ORDER BY avg_tone ASC
    LIMIT {limit}
    """


def _bq_entity_timelines_sql(entities: list[str], start_date: str, end_date: str) -> str:
    any_entity = " OR ".join(f"UPPER(V2Organizations) LIKE '%{e.strip().upper()}%'"
                             for e in entities)
    per_entity_selects = ", ".join(
        f"SUM(CASE WHEN UPPER(V2Organizations) LIKE '%{e.strip().upper()}%' THEN 1 ELSE 0 END) "
        f"AS `{e.strip().lower().replace(' ', '_')}_mentions`" for e in entities
    )
    return f"""
    SELECT
      DATE_TRUNC(DATE(_PARTITIONTIME), MONTH) AS month,
      SUM(CASE WHEN {any_entity} THEN 1 ELSE 0 END) AS mentions,
      {per_entity_selects}
    FROM `gdelt-bq.gdeltv2.gkg_partitioned`
    WHERE _PARTITIONTIME >= "{start_date}"
      AND _PARTITIONTIME < "{end_date}"
      AND ({any_entity})
    GROUP BY month
    ORDER BY month
    """


def _bq_geographic_spread_sql(themes: list[str], start_date: str, end_date: str,
                              limit: int = 20) -> str:
    return f"""
    WITH filtered AS (
      SELECT V2Locations
      FROM `gdelt-bq.gdeltv2.gkg_partitioned`
      WHERE _PARTITIONTIME >= "{start_date}"
        AND _PARTITIONTIME < "{end_date}"
        AND {_theme_or_clause(themes)}
        AND V2Locations IS NOT NULL
    )
    SELECT
      country_code,
      COUNT(*) AS mentions
    FROM filtered,
    UNNEST(SPLIT(V2Locations, ';')) AS loc
    CROSS JOIN UNNEST([SPLIT(loc, '#')[SAFE_OFFSET(3)]]) AS country_code
    WHERE country_code IS NOT NULL AND LENGTH(country_code) = 2
    GROUP BY country_code
    ORDER BY mentions DESC
    LIMIT {limit}
    """


def query_timeline(themes: list[str], start_date: str, end_date: str,
                   entities: list[str] | None = None,
                   max_mb: int = BQ_MAX_MB_PER_QUERY) -> dict:
    """Run the 4-query BigQuery aggregate suite. Requires GCP creds."""
    try:
        from google.cloud import bigquery
    except ImportError:
        return {"error": "google-cloud-bigquery not installed. "
                          "Run: pip3 install --user google-cloud-bigquery"}

    project = os.environ.get("GCP_PROJECT_ID", "").strip()
    if not project:
        return {"error": "GCP_PROJECT_ID not set"}
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        return {"error": "GOOGLE_APPLICATION_CREDENTIALS not set"}

    client = bigquery.Client(project=project)
    entities = entities or []
    output: dict[str, Any] = {
        "project": project,
        "themes": themes,
        "entities": entities,
        "start_date": start_date,
        "end_date": end_date,
        "generated_at": datetime.datetime.utcnow().isoformat(),
        "total_mb_scanned": 0.0,
        "queries": {},
    }

    for name, sql in [
        ("timeline", _bq_timeline_sql(themes, start_date, end_date)),
        ("negative_articles", _bq_negative_articles_sql(themes, start_date, end_date)),
    ]:
        result, mb = _bq_dry_run_and_execute(client, sql, name, max_mb=max_mb)
        output["queries"][name] = result
        output["total_mb_scanned"] += mb

    if entities:
        sql = _bq_entity_timelines_sql(entities, start_date, end_date)
        result, mb = _bq_dry_run_and_execute(client, sql, "entity_timelines",
                                             max_mb=max_mb)
        output["queries"]["entity_timelines"] = result
        output["total_mb_scanned"] += mb

    sql = _bq_geographic_spread_sql(themes, start_date, end_date)
    result, mb = _bq_dry_run_and_execute(client, sql, "geographic_spread",
                                         max_mb=max_mb)
    output["queries"]["geographic_spread"] = result
    output["total_mb_scanned"] += mb

    output["total_mb_scanned"] = round(output["total_mb_scanned"], 1)
    return output


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    ap = argparse.ArgumentParser(description="GDELT queries — REST news + BigQuery aggregates")
    sub = ap.add_subparsers(dest="mode", required=True)

    p_news = sub.add_parser("news", help="Per-company REST news search")
    p_news.add_argument("--company", required=True)
    p_news.add_argument("--keywords", required=True,
                        help="Comma-separated keywords ANDed with company")
    p_news.add_argument("--months", type=int, default=6)
    p_news.add_argument("--parent-entity", default="")
    p_news.add_argument("--slug", default="")

    p_tl = sub.add_parser("timeline", help="BigQuery category aggregates")
    p_tl.add_argument("--themes", required=True,
                      help="Comma-separated GDELT theme substrings")
    p_tl.add_argument("--entities", default="",
                      help="Optional comma-separated org names to track over time")
    p_tl.add_argument("--start-date", required=True)
    p_tl.add_argument("--end-date", required=True)
    p_tl.add_argument("--max-mb", type=int, default=BQ_MAX_MB_PER_QUERY)

    args = ap.parse_args()

    if args.mode == "news":
        keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
        emit_json(query_news(
            company=args.company,
            keywords=keywords,
            months_back=args.months,
            slug=args.slug or None,
            parent_entity=args.parent_entity or None,
        ))
    elif args.mode == "timeline":
        themes = [t.strip() for t in args.themes.split(",") if t.strip()]
        entities = [e.strip() for e in args.entities.split(",") if e.strip()]
        emit_json(query_timeline(
            themes=themes,
            start_date=args.start_date,
            end_date=args.end_date,
            entities=entities,
            max_mb=args.max_mb,
        ))


if __name__ == "__main__":
    main()
