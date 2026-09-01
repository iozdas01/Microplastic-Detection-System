"""Shared helpers for scripts/data/* modules.

Contains: HTTP with retry, name normalization, registry gate, manifest logging,
allowlists, currency conversion, EDGAR-style name cleanup, non-operator filters.
Every source module imports from here — nothing else should be duplicated.
"""

from __future__ import annotations

import html as _html
import json
import os
import re
import sys
import time
import unicodedata
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import requests
import yaml


# ---------------------------------------------------------------------------
# Repo paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]
API_REGISTRY_PATH = REPO_ROOT / "api-registry.yaml"


# ---------------------------------------------------------------------------
# HTTP defaults
# ---------------------------------------------------------------------------

# EDGAR requires a contact address in the User-Agent; set EDGAR_USER_AGENT_EMAIL in .env.
# No personal default here — a committed address is one founder's identity in shared code.
USER_AGENT_EMAIL = os.environ.get("EDGAR_USER_AGENT_EMAIL", "")
USER_AGENT = f"startup-lab/1.0 ({USER_AGENT_EMAIL})" if USER_AGENT_EMAIL else "startup-lab/1.0"
DEFAULT_HEADERS = {"User-Agent": USER_AGENT, "Accept": "application/json"}


# ---------------------------------------------------------------------------
# Name-normalization constants
# ---------------------------------------------------------------------------

LEGAL_SUFFIXES = {
    "ltd", "limited", "plc", "llp", "llc", "inc", "corp", "corporation",
    "gmbh", "ag", "sa", "srl", "bv", "nv", "as", "a/s", "aps", "oy", "ab",
    "spa", "s.a.", "s.p.a.", "s.r.l.", "co", "company", "group", "holdings",
    "holding", "services", "service",
}

# Fold latin extended-A/B letters that NFKD leaves intact.
LATIN_FOLD = str.maketrans({
    "Ø": "O", "ø": "o", "Æ": "AE", "æ": "ae", "Œ": "OE", "œ": "oe",
    "Þ": "Th", "þ": "th", "Ð": "D", "ð": "d", "Ł": "L", "ł": "l",
    "ß": "ss",
})


# ---------------------------------------------------------------------------
# Non-operator / defunct filters (used by intel + any discovery source)
# ---------------------------------------------------------------------------

NON_OPERATOR_PATTERNS = [
    # Funds / investment vehicles / pensions
    "INVESTORS", "FUND", "HOLDINGS TRUST", "CAPITAL PARTNERS",
    "MULTI-ASSET", "PENSION", "SICAV", "SIF ",
    "MASTER TRUST", "DEFINED BENEFIT", "DEFINED CONTRIBUTION",
    "RETIREMENT TRUST", "RETIREMENT PLAN", "SAVINGS PLAN",
    "ENDOWMENT",
    # Government agencies / ministries
    "MINISTRY OF", "MINISTERIE", "DEPARTMENT OF", " AGENCY",
    "RIJKSDIENST", "AUTHORITY OF", "COMMISSION OF",
    "LANDSKAPSREGERING", "VASSDRAG",
    "AĢENTŪRA", "AGENTŪRA", "AGENCIJA",
    "АГЕНТСТВО",
    "ADMINISTRACIJA", "SEKRETARIATAS",
    "HAFENBEHÖRDE",
    "SECRETARIAT",
    # Recruitment / staffing
    "RECRUIT", "STAFFING", "TALENT", "RESOURCING", "MANPOWER",
    "MATCHTECH", "GATTACA", "JONATHAN LEE", "ASTUTE", "MORSON",
    "RULLION", "TAYLOR HOPKINSON", "NES GROUP", "STOWEN",
    "COBURG BANKS", "HAYS ", "ADECCO", "RANDSTAD",
    "AD WARRIOR", "WARRIOR LTD",
    "HSB TECHNICAL",
    "GLOBAL HIGHLAND", "ERSG",
    # Academic / research
    "UNIVERSITY", "UNIVERSITET", "UNIVERSITAT", "COLLEGE",
    "POLYTECHNIC", "HOCHSCHULE", "INSTITUTT",
    "STIFTELSEN", "TECHNICAL INSTITUTE",
    "NORDIC ENERGY RESEARCH",
    # Legal / consultancy
    "QED LEGAL", "LEGAL LTD", "LAW LLP", "SOLICITORS", "BARRISTERS",
    "CONSULTANCY LTD", "CONSULTING LTD", "CONSULTANTS LTD",
    "ADVISORY LTD", "ADVISORS LTD",
    # Ports
    "PORT OF ", "PORT AUTHORITY", "HARBOUR AUTHORITY",
    # Trade associations
    " ASSOCIATION", "TRADE BODY", "LOBBY",
    "FEDERATION OF", "CONFEDERATION",
    " COUNCIL",
    # Transmission grid operators
    "RÉSEAU DE TRANSPORT", "TRANSMISSION SYSTEM OPERATOR",
    "NATIONAL GRID", " TSO", "TERNA",
    # Investment banks / defunct-adjacent
    "INVESTMENT BANK", "AKTIENGESELLSCHAFT IN ABWICKLUNG",
    # NOTE: every pattern here must be STRUCTURAL — a company form that is not an
    # operator in any market (fund, university, law firm, port, trade body, TSO).
    # Named companies that are off-scope for one idea belong in that assumption's
    # `icp_out_of_scope`, never here: this list is read by every idea.
]

IN_LIQUIDATION_PATTERNS = [
    "in abwicklung", "in liquidation", "en liquidation", "in liquidatie",
    "en liquidación", "in liquidazione", "(dissolved)", "(defunct)",
    "(in insolvency)", "(struck off)", "в ликвидации",
]

# News domains we trust for company_news hooks.
NEWS_DOMAIN_ALLOWLIST = {
    "reuters.com", "bloomberg.com", "ft.com", "wsj.com", "nytimes.com",
    "cnbc.com", "businesswire.com", "prnewswire.com", "reneweconomy.com.au",
    "windpowermonthly.com", "windpower-monthly.com", "rechargenews.com",
    "offshorewind.biz", "windeurope.org", "greentechmedia.com",
    "utilitydive.com", "energy-storage.news", "power-technology.com",
    "renews.biz", "renewablesnow.com", "spglobal.com", "iea.org",
    "ftadviser.com", "theguardian.com", "bbc.co.uk", "bbc.com",
    "electrek.co", "cleantechnica.com", "pv-magazine.com",
}

CURRENCY_TO_GBP = {"GBP": 1.0, "EUR": 0.85, "USD": 0.79, "DKK": 0.114}


# ---------------------------------------------------------------------------
# EDGAR name cleanup
# ---------------------------------------------------------------------------

EDGAR_METADATA_RE = re.compile(r"\s*\([^)]*\)\s*\(CIK\s+\d+\)\s*$")


def clean_edgar_name(name: str) -> tuple[str, str]:
    """Strip 'ALLIANT ENERGY CORP  (LNT)  (CIK 0000352541)' → ('ALLIANT ENERGY CORP', '0000352541').

    Also HTML-unescapes so `&amp;` becomes `&` before downstream dedup.
    """
    if not name:
        return name, ""
    name = _html.unescape(name)
    m = re.search(r"\(CIK\s+(\d+)\)\s*$", name)
    cik = m.group(1) if m else ""
    cleaned = EDGAR_METADATA_RE.sub("", name).strip()
    return cleaned, cik


def is_name_out_of_scope(name: str) -> bool:
    """True if the name matches a known non-operator / defunct pattern."""
    if not name:
        return False
    name = _html.unescape(name)
    upper = name.upper()
    if any(p in upper for p in NON_OPERATOR_PATTERNS):
        return True
    lower = name.lower()
    if any(p in lower for p in IN_LIQUIDATION_PATTERNS):
        return True
    return False


def normalize_name(name: str) -> str:
    """Fold diacritics + drop legal suffixes so name-variants collapse for dedup."""
    if not name:
        return ""
    s = name.translate(LATIN_FOLD)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s/]", " ", s)
    tokens = [t for t in s.split() if t and t not in LEGAL_SUFFIXES]
    return " ".join(tokens).strip()


def to_gbp(value: float | int | None, currency: str) -> float:
    if value is None:
        return 0.0
    try:
        v = float(value)
    except (ValueError, TypeError):
        return 0.0
    rate = CURRENCY_TO_GBP.get((currency or "GBP").upper(), 0.85)
    return v * rate


# ---------------------------------------------------------------------------
# HTTP with retry
# ---------------------------------------------------------------------------


def http_get(
    url: str,
    params: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
    timeout: int = 30,
    retries: int = 3,
    backoff: float = 2.0,
) -> requests.Response | None:
    """GET with exponential-backoff retry. Returns None after `retries` failures."""
    hdrs = {**DEFAULT_HEADERS, **(headers or {})}
    for attempt in range(retries):
        try:
            r = requests.get(url, params=params, headers=hdrs, timeout=timeout)
            if r.status_code == 429:
                time.sleep(backoff ** (attempt + 2))
                continue
            return r
        except requests.RequestException as e:
            if attempt == retries - 1:
                print(f"[warn] http_get failed after {retries}: {url} — {e}",
                      file=sys.stderr)
                return None
            time.sleep(backoff ** (attempt + 1))
    return None


def cutoff_date(months_back: int) -> str:
    return (datetime.now(timezone.utc) - timedelta(days=months_back * 30)).strftime("%Y-%m-%d")


# ---------------------------------------------------------------------------
# Registry gate + manifest log
# ---------------------------------------------------------------------------

_REGISTRY_CACHE: dict[str, Any] | None = None


def load_registry() -> dict[str, Any]:
    """Load api-registry.yaml from repo root, cached."""
    global _REGISTRY_CACHE
    if _REGISTRY_CACHE is None:
        with open(API_REGISTRY_PATH, "r", encoding="utf-8") as f:
            _REGISTRY_CACHE = yaml.safe_load(f)
    return _REGISTRY_CACHE


def is_enabled(api_key: str) -> bool:
    """True if the API is `enabled: true` AND all `env_keys` are present."""
    reg = load_registry().get("apis", {})
    if api_key not in reg:
        return False
    entry = reg[api_key]
    if not entry.get("enabled", False):
        return False
    for env_key in entry.get("env_keys", []) or []:
        if not os.environ.get(env_key):
            return False
    return True


def manifest_path(slug: str) -> Path:
    return REPO_ROOT / "reports" / slug / "outreach" / ".intel-manifest.jsonl"


def log_manifest(slug: str | None, entry: dict[str, Any]) -> None:
    """Append a JSONL entry to the intel manifest. Never raises."""
    if not slug:
        return
    try:
        path = manifest_path(slug)
        path.parent.mkdir(parents=True, exist_ok=True)
        entry = {"ts": datetime.now(timezone.utc).isoformat(), **entry}
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception as e:
        print(f"[warn] manifest log failed: {e}", file=sys.stderr)


# ---------------------------------------------------------------------------
# CLI utility — emit JSON to stdout
# ---------------------------------------------------------------------------


def emit_json(payload: Any) -> None:
    """Print JSON to stdout with sensible defaults for CLI outputs."""
    print(json.dumps(payload, ensure_ascii=False, default=str))
