"""Shared plumbing for the furniture-demand collectors.

Every collector writes two things:
  data/raw/<source>/<YYYY-MM-DD>-<name>.json   verbatim API payload, never edited
  data/processed/<name>.csv                    tidy table the model and report read

and appends one line to data/MANIFEST.jsonl recording url, fetch time, row count and
status. Nothing downstream is allowed to quote a number that has no manifest line.
"""
from __future__ import annotations

import csv
import datetime as _dt
import json
import os
import pathlib
import sys
import time
import urllib.parse

import requests

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent

# This pipeline's outputs are per-idea state, so they live inside the idea folder with
# every other artifact about this idea — there is one `reports/` tree in the repo and one
# `data/` under it. The code stays at `scripts/research/` because the collectors outlive
# any single idea; only what they produce is idea-scoped.
RESEARCH = ROOT / "reports" / "custom-kitchen-cabinets" / "research"
RAW = RESEARCH / "data" / "raw"
PROC = RESEARCH / "data" / "processed"
MANIFEST = RESEARCH / "data" / "MANIFEST.jsonl"
TODAY = _dt.date.today().isoformat()

# The credential set lives at the repo root (the Assumption Lab half of this repo);
# this pipeline reads it rather than duplicating secrets.
ENV_CANDIDATES = [ROOT / ".env", ROOT.parent / ".env"]


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    for path in ENV_CANDIDATES:
        if not path.exists():
            continue
        for line in path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env.setdefault(k.strip(), v.strip().strip('"').strip("'"))
    env.update({k: v for k, v in os.environ.items() if k in env or k.endswith("_KEY")})
    return env


ENV = load_env()


def log(msg: str) -> None:
    print(f"[{_dt.datetime.now():%H:%M:%S}] {msg}", flush=True)


def get(url: str, params: dict | None = None, headers: dict | None = None,
        tries: int = 3, timeout: int = 60):
    """GET with linear backoff. Returns the response or raises the final error."""
    last = None
    for attempt in range(1, tries + 1):
        try:
            r = requests.get(url, params=params, headers=headers or {}, timeout=timeout)
            if r.status_code == 200:
                return r
            last = RuntimeError(f"HTTP {r.status_code}: {r.text[:300]}")
        except Exception as exc:  # noqa: BLE001 - collectors must degrade, not crash
            last = exc
        if attempt < tries:
            time.sleep(2 * attempt)
    raise last


def post(url: str, json_body: dict, headers: dict | None = None, tries: int = 3, timeout: int = 90):
    last = None
    for attempt in range(1, tries + 1):
        try:
            r = requests.post(url, json=json_body, headers=headers or {}, timeout=timeout)
            if r.status_code == 200:
                return r
            last = RuntimeError(f"HTTP {r.status_code}: {r.text[:300]}")
        except Exception as exc:  # noqa: BLE001
            last = exc
        if attempt < tries:
            time.sleep(2 * attempt)
    raise last


def save_raw(source: str, name: str, payload) -> pathlib.Path:
    d = RAW / source
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{TODAY}-{name}.json"
    p.write_text(json.dumps(payload, indent=2, default=str))
    return p


def save_csv(name: str, rows: list[dict], fieldnames: list[str] | None = None) -> pathlib.Path:
    PROC.mkdir(parents=True, exist_ok=True)
    p = PROC / f"{name}.csv"
    if not rows:
        p.write_text("")
        return p
    fieldnames = fieldnames or list(rows[0].keys())
    with p.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    return p


def record(source: str, dataset: str, url: str, rows: int, status: str = "ok",
           note: str = "") -> None:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with MANIFEST.open("a") as fh:
        fh.write(json.dumps({
            "fetched_at": _dt.datetime.now().isoformat(timespec="seconds"),
            "source": source,
            "dataset": dataset,
            "url": url,
            "rows": rows,
            "status": status,
            "note": note,
        }) + "\n")


def read_csv(name: str) -> list[dict]:
    p = PROC / f"{name}.csv"
    if not p.exists() or not p.read_text().strip():
        return []
    with p.open() as fh:
        return list(csv.DictReader(fh))


def census_rows(payload) -> list[dict]:
    """Census returns [header, *rows]; turn it into dicts."""
    if not payload or len(payload) < 2:
        return []
    header, *rows = payload
    return [dict(zip(header, r)) for r in rows]


def guard(source: str, dataset: str, url: str = ""):
    """Decorator-ish context: run a collector, log failure to the manifest, never crash the run."""
    class _G:
        def __enter__(self):
            log(f"→ {source}/{dataset}")
            return self

        def __exit__(self, exc_type, exc, tb):
            if exc is not None:
                log(f"  !! {source}/{dataset} failed: {exc}")
                record(source, dataset, url, 0, status="failed", note=str(exc)[:400])
                return True  # swallow
            return False
    return _G()
