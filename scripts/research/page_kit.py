"""Small HTML helpers so the page builder reads as content, not as string plumbing.

Everything escapes by default. Where a builder needs inline markup — a <span class="note">
inside a sentence — it passes an `html=True` fragment explicitly, which keeps the escaping
decision visible at the call site rather than buried in a helper.
"""
from __future__ import annotations

import html as _html
from typing import Iterable


def esc(v) -> str:
    return _html.escape(str(v), quote=True)


class Raw(str):
    """Marks a string as already-safe HTML."""


def _cell(v) -> str:
    return v if isinstance(v, Raw) else esc(v)


def tag(name: str, content: str = "", **attrs) -> Raw:
    a = "".join(f' {k.rstrip("_").replace("_", "-")}="{esc(v)}"'
                for k, v in attrs.items() if v not in (None, "", False))
    return Raw(f"<{name}{a}>{content}</{name}>")


def note(text) -> Raw:
    return tag("span", esc(text), class_="note")


def table(caption: str, headers: Iterable, rows: Iterable[Iterable],
          aligns: Iterable[str] | None = None,
          row_classes: Iterable[str | None] | None = None) -> Raw:
    """A scrollable table. `aligns` is one of '', 'num', 'wrap', 'dim' per column."""
    headers = list(headers)
    aligns = list(aligns) if aligns else [""] * len(headers)
    row_classes = list(row_classes) if row_classes else []

    head = "".join(
        f'<th{f" class=\"{a}\"" if a in ("num", "wrap") else ""}>{_cell(h)}</th>'
        for h, a in zip(headers, aligns))

    body = []
    for i, r in enumerate(rows):
        cls = row_classes[i] if i < len(row_classes) else None
        tds = "".join(
            f'<td{f" class=\"{a}\"" if a else ""}>{_cell(c)}</td>'
            for c, a in zip(r, aligns))
        body.append(f'<tr{f" class=\"{cls}\"" if cls else ""}>{tds}</tr>')

    return Raw(
        '<div class="bleed scroll"><table>'
        f'<caption>{_cell(caption)}</caption>'
        f'<thead><tr>{head}</tr></thead>'
        f'<tbody>{"".join(body)}</tbody>'
        '</table></div>')


def bar_cell(fraction: float) -> Raw:
    """A proportional bar for a table cell; fraction is 0..1 of the row maximum."""
    pct = max(min(fraction, 1.0), 0.0) * 100
    return Raw(f'<span class="track"><i style="width:{pct:.2f}%"></i></span>')


def stat(value: str, key: str, sub: str, negative: bool = False) -> Raw:
    return Raw(
        f'<div class="stat{" neg" if negative else ""}">'
        f'<span class="n">{esc(value)}</span>'
        f'<span class="k">{esc(key)}</span>'
        f'<span class="s">{esc(sub)}</span></div>')


def usd(v: float, unit: str | None = None, dp: int | None = None) -> str:
    """Money at a sensible magnitude. unit=None picks bn/m/k automatically."""
    if unit is None:
        unit = "bn" if abs(v) >= 1e9 else "m" if abs(v) >= 1e6 else "k"
    div = {"bn": 1e9, "m": 1e6, "k": 1e3, "": 1}[unit]
    dp = dp if dp is not None else (2 if unit == "bn" else 1)
    return f"${v/div:,.{dp}f}{unit}"


def pct(v: float, dp: int = 1, sign: bool = False) -> str:
    return f"{v*100:+.{dp}f}%" if sign else f"{v*100:.{dp}f}%"
