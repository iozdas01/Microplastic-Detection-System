"""arXiv paper scan for the research map — no key required.

Reproduces the batch-1 source selection recorded in
`reports/outreach/research-map.md`: arXiv cs.RO, published on or after a
cutoff date, ranked on a brownfield-axis keyword score.

Batch 1 persisted only its counts, so batch 2 could not resume from it. This module
writes the full ranked shortlist to disk so every later batch can.

CLI:
    python -m scripts.data.arxiv --since 2026-01-01 [--max 400] \
        [--shortlist reports/outreach/research-map-shortlist.csv] \
        [--exclude-map reports/outreach/research-map.md]

Emits JSON `{scanned, on_axis, papers: [...], errors: [...]}` on stdout and, when
--shortlist is given, writes the ranked on-axis rows as CSV.

Python API:
    from scripts.data.arxiv import scan
    result = scan(since="2026-01-01", max_results=400)
"""

from __future__ import annotations

import argparse
import csv
import gzip
import io
import re
import sys
import tarfile
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

from scripts.data._common import emit_json, http_get

ARXIV_ENDPOINT = "https://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"
PAGE_SIZE = 100

# Brownfield-axis keyword score. Weights encode what the map actually reads for:
# where the work runs, where its training data comes from, and whether either
# transfers to a site the team does not control. A paper scoring 0 is off-axis.
AXIS_KEYWORDS: dict[str, int] = {
    # environment / site control — the strongest signal
    "brownfield": 5, "factory": 4, "manufacturing": 4, "industrial": 3,
    "production line": 5, "shop floor": 5, "warehouse": 3, "plant": 2,
    "workcell": 5, "work cell": 5, "assembly line": 4, "in the wild": 3,
    "real-world deployment": 4, "real world deployment": 4, "deployment": 2,
    # data origin / volume — what the map's data axes need
    "real robot data": 5, "real-world data": 4, "teleoperation": 3,
    "demonstration": 2, "dataset": 2, "data collection": 4, "egocentric": 3,
    "human video": 4, "sim-to-real": 4, "sim2real": 4, "synthetic data": 3,
    "domain randomization": 3, "domain randomisation": 3, "digital twin": 4,
    # integration labour / transferability
    "cross-embodiment": 4, "cross embodiment": 4, "generalization": 2,
    "generalisation": 2, "transfer": 2, "calibration": 3, "commissioning": 5,
    "system identification": 4, "retrofit": 5, "legacy": 3,
    # contact / dynamics — the H2A4 seam
    "contact-rich": 4, "contact rich": 4, "force control": 4, "insertion": 3,
    "proprioception": 4, "tactile": 3, "joint dynamics": 5, "actuator": 3,
}

MIN_SCORE = 4
DEFAULT_QUERY = "cat:cs.RO"


def _score(text: str) -> tuple[int, list[str]]:
    """Brownfield-axis keyword score plus the terms that fired."""
    lower = text.lower()
    total = 0
    hits: list[str] = []
    for term, weight in AXIS_KEYWORDS.items():
        if term in lower:
            total += weight
            hits.append(term)
    return total, hits


def _parse_feed(xml_text: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    papers = []
    for entry in root.findall(f"{ATOM}entry"):
        raw_id = (entry.findtext(f"{ATOM}id") or "").strip()
        arxiv_id = raw_id.rsplit("/", 1)[-1]
        title = " ".join((entry.findtext(f"{ATOM}title") or "").split())
        summary = " ".join((entry.findtext(f"{ATOM}summary") or "").split())
        published = (entry.findtext(f"{ATOM}published") or "").strip()
        authors = [
            (a.findtext(f"{ATOM}name") or "").strip()
            for a in entry.findall(f"{ATOM}author")
        ]
        papers.append({
            "arxiv_id": arxiv_id,
            "title": title,
            "abstract": summary,
            "published": published,
            "authors": authors,
            "url": f"https://arxiv.org/abs/{arxiv_id.split('v')[0]}",
        })
    return papers


def _already_classified(map_path: Path) -> set[str]:
    """arXiv ids already carrying a row in the research map, so batches don't repeat."""
    if not map_path or not map_path.exists():
        return set()
    text = map_path.read_text(encoding="utf-8")
    return set(re.findall(r"arxiv\.org/abs/([0-9]{4}\.[0-9]{4,5})", text))


def scan(
    since: str,
    max_results: int = 400,
    exclude_map: Path | None = None,
    query: str = DEFAULT_QUERY,
    min_score: int = MIN_SCORE,
) -> dict:
    """Scan an arXiv query since `since`, rank on the brownfield axis, drop classified ids.

    `query` is an arXiv search_query string and defaults to `cat:cs.RO`, the batch-1
    selection. Themes that do not live in the robotics category — agent/tool-use work in
    cs.AI, MES and interoperability work in eess.SY — need their own query, which is why
    this is a parameter rather than a constant.
    """
    errors: list[str] = []
    collected: list[dict] = []

    for start in range(0, max_results, PAGE_SIZE):
        query = urllib.parse.urlencode({
            "search_query": query,
            "start": start,
            "max_results": min(PAGE_SIZE, max_results - start),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        })
        try:
            resp = http_get(f"{ARXIV_ENDPOINT}?{query}", headers={"Accept": "application/atom+xml"})
            page = _parse_feed(resp.text)
        except Exception as exc:  # noqa: BLE001 — surfaced in the payload, not raised
            errors.append(f"page start={start}: {exc}")
            break
        if not page:
            break
        collected.extend(page)
        # arXiv asks for 3s between calls; honour it rather than getting throttled.
        time.sleep(3)

    # Date filter is applied here rather than in the query: arXiv's date syntax is
    # unreliable across mirrors, and descending submittedDate makes this exact.
    in_window = [p for p in collected if p["published"][:10] >= since]

    classified = _already_classified(exclude_map) if exclude_map else set()

    on_axis = []
    for paper in in_window:
        score, hits = _score(f"{paper['title']} {paper['abstract']}")
        if score < min_score:
            continue
        base_id = paper["arxiv_id"].split("v")[0]
        paper = {
            **paper,
            "axis_score": score,
            "axis_terms": sorted(hits),
            "already_classified": base_id in classified,
        }
        on_axis.append(paper)

    on_axis.sort(key=lambda p: (-p["axis_score"], p["published"]), reverse=False)

    return {
        "query": query,
        "scanned": len(collected),
        "in_window": len(in_window),
        "on_axis": len(on_axis),
        "papers": on_axis,
        "errors": errors,
    }


def write_shortlist(result: dict, path: Path) -> None:
    """Persist the ranked shortlist so a later batch can resume without rescanning."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow([
            "arxiv_id", "published", "axis_score", "already_classified",
            "title", "url", "axis_terms",
        ])
        for paper in result["papers"]:
            writer.writerow([
                paper["arxiv_id"],
                paper["published"][:10],
                paper["axis_score"],
                "yes" if paper["already_classified"] else "no",
                paper["title"],
                paper["url"],
                "|".join(paper["axis_terms"]),
            ])


EMAIL_RE = re.compile(r"[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}", re.I)

# Addresses that are never a contactable author. Two kinds ship inside the same
# .tex the authors wrote, and BOTH have already been mined into a real batch:
#   boilerplate  conference/publisher contact lines (proceedings-questions@aaai.org)
#   placeholders the template's example author, left in (janedoe@berkeley.edu)
# A placeholder is the dangerous one — it is a real, deliverable domain, so it
# looks like a find and reaches a stranger. Filter both rather than trusting the
# reader to notice.
EMAIL_NOISE = re.compile(
    r"(latex|ctan|texlive|overleaf|ieee|acm\.org|aaai|elsevier|springer|usenix|"
    r"proceedings|noreply|no-reply|example\.(com|org)|your|email@|author@|xxx|"
    r"j(ane|ohn)\.?doe|firstname|lastname|yourname|anonymous|submission)", re.I)

PERSONAL_DOMAINS = {
    "gmail.com", "googlemail.com", "hotmail.com", "outlook.com", "yahoo.com",
    "icloud.com", "proton.me", "protonmail.com", "aol.com", "qq.com", "163.com",
}


def _source_texts(payload: bytes) -> list[str]:
    """Every .tex/.txt stream inside an arXiv e-print package."""
    streams: list[bytes] = []
    try:
        with tarfile.open(fileobj=io.BytesIO(payload), mode="r:*") as archive:
            for member in archive.getmembers():
                if not member.isfile() or member.size > 5_000_000:
                    continue
                if not member.name.lower().endswith((".tex", ".txt")):
                    continue
                extracted = archive.extractfile(member)
                if extracted:
                    streams.append(extracted.read())
    except tarfile.TarError:
        try:
            streams.append(gzip.decompress(payload))
        except OSError:
            streams.append(payload)
    return [blob.decode("utf-8", errors="ignore") for blob in streams]


def paper_emails(identifier: str, keep_personal: bool = False) -> list[str]:
    """Author-PUBLISHED emails from a paper's own arXiv source package.

    Only addresses the authors themselves put in the paper. Nothing is guessed
    from a name and a domain, and no enrichment provider is called — a mined
    address is one the author chose to publish, which is what makes cold contact
    on it defensible.
    """
    identifier = identifier.strip().removeprefix("arXiv:").removeprefix("arxiv:")
    url = f"https://export.arxiv.org/e-print/{urllib.parse.quote(identifier)}"
    request = urllib.request.Request(url, headers={"User-Agent": "startup-research-outreach/1.0"})

    # e-print packages run to several MB and the connection truncates often enough
    # that a single attempt loses roughly one paper in five. A truncated read is a
    # transport failure, not "this paper publishes no address" — retry rather than
    # silently record an empty result, which is how batch 2 got its empty rows.
    # e-print packages run to tens of MB and the connection truncates at buffer
    # boundaries often enough that a single read() loses roughly one paper in four.
    # Read in chunks so a short read is visible, and retry — a truncated download is
    # a transport failure, NOT "this paper publishes no address". Recording those as
    # empty is exactly how a batch ends up with unreachable rows.
    payload = b""
    for attempt in range(3):
        try:
            chunks, size = [], 0
            with urllib.request.urlopen(request, timeout=180) as response:
                expected = response.headers.get("Content-Length")
                while True:
                    chunk = response.read(65536)
                    if not chunk:
                        break
                    chunks.append(chunk)
                    size += len(chunk)
            if expected and size < int(expected):
                raise OSError(f"short read: {size} of {expected} bytes")
            payload = b"".join(chunks)
            break
        except Exception:
            if attempt == 2:
                raise
            time.sleep(5 * (attempt + 1))

    emails: set[str] = set()
    for text in _source_texts(payload):
        # Authors routinely escape or obfuscate the address in LaTeX.
        cleaned = (text.replace("\\_", "_").replace("\\-", "-")
                       .replace("{at}", "@").replace("[at]", "@")
                       .replace("\\{at\\}", "@").replace("(at)", "@")
                       .replace("{dot}", ".").replace("[dot]", "."))
        # \email{a@b.com, c@d.com} and mailto: links carry the rest.
        for m in re.finditer(r"\\(?:email|correspondingauthor)\{([^}]*)\}", cleaned):
            emails.update(EMAIL_RE.findall(m.group(1)))
        emails.update(EMAIL_RE.findall(cleaned))

    out = set()
    for e in emails:
        e = e.rstrip(".,;:").lower()
        if EMAIL_NOISE.search(e):
            continue
        if not keep_personal and e.rsplit("@", 1)[-1] in PERSONAL_DOMAINS:
            continue
        out.add(e)
    return sorted(out)


def mine(identifiers: list[str], keep_personal: bool = False,
         pause: float = 3.0) -> dict:
    """paper_emails over many ids, with the failures kept rather than dropped."""
    found, errors = {}, []
    for i, ident in enumerate(identifiers):
        if i:
            time.sleep(pause)  # arXiv asks for ~1 request / 3s on e-print
        try:
            found[ident] = paper_emails(ident, keep_personal=keep_personal)
        except Exception as exc:  # noqa: BLE001 — one bad id must not kill the batch
            found[ident] = []
            errors.append({"id": ident, "error": f"{type(exc).__name__}: {exc}"})
    return {
        "mined": len(identifiers),
        "with_email": sum(1 for v in found.values() if v),
        "emails": found,
        "errors": errors,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--since", default="2026-01-01")
    parser.add_argument("--max", type=int, default=400, dest="max_results")
    parser.add_argument("--shortlist", type=Path, default=None)
    parser.add_argument("--exclude-map", type=Path, default=None)
    parser.add_argument("--emails", default=None, metavar="IDS",
                        help="comma-separated arXiv ids: mine author-published "
                             "emails from their source packages and exit")
    parser.add_argument("--query", default=DEFAULT_QUERY,
                        help="arXiv search_query (default: cat:cs.RO)")
    parser.add_argument("--min-score", type=int, default=MIN_SCORE,
                        help=f"axis-score floor (default: {MIN_SCORE})")
    parser.add_argument("--keep-personal", action="store_true",
                        help="keep gmail/qq-style addresses (dropped by default)")
    args = parser.parse_args(argv)

    if args.emails:
        ids = [x.strip() for x in args.emails.split(",") if x.strip()]
        emit_json(mine(ids, keep_personal=args.keep_personal))
        return 0

    result = scan(
        since=args.since,
        max_results=args.max_results,
        exclude_map=args.exclude_map,
        query=args.query,
        min_score=args.min_score,
    )
    if args.shortlist:
        write_shortlist(result, args.shortlist)
        result["shortlist_written"] = str(args.shortlist)

    # Abstracts are long; the CSV carries them out of band.
    emit_json({**result, "papers": [
        {k: v for k, v in p.items() if k != "abstract"} for p in result["papers"][:40]
    ]})
    return 0


if __name__ == "__main__":
    sys.exit(main())
