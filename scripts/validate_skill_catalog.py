#!/usr/bin/env python3
"""Validate active startup skills, their bridges, and the skill contract.

Frontmatter shape is delegated to skill-creator's quick_validate. Everything
else here enforces the contract in CLAUDE.md, which was previously prose only:
a 200-line cap, no founder names, no per-idea state (dates, contact IDs,
slugs), and no absolute paths outside the repo. Ten of eleven skills violated
the line cap on the day these checks were written, and four named a founder.
"""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLAUDE_SKILLS = ROOT / ".claude" / "skills"
AGENT_SKILLS = ROOT / ".agents" / "skills"
QUICK_VALIDATOR = (
    AGENT_SKILLS / "skill-creator" / "scripts" / "quick_validate.py"
)


def load_quick_validator():
    if not QUICK_VALIDATOR.is_file():
        raise RuntimeError(f"Bundled validator not found: {QUICK_VALIDATOR}")

    spec = importlib.util.spec_from_file_location(
        "repo_skill_quick_validate", QUICK_VALIDATOR
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load validator: {QUICK_VALIDATOR}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_frontmatter_name(skill_md: Path, yaml_module) -> str:
    content = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return ""
    parsed = yaml_module.safe_load(match.group(1))
    if not isinstance(parsed, dict):
        return ""
    name = parsed.get("name", "")
    return name.strip() if isinstance(name, str) else ""


MAX_SKILL_LINES = 200

# Contract checks over SKILL.md bodies. Founder names are read from founder.md
# so this file does not become a second author for who the founders are.
CONTRACT_PATTERNS = [
    ("per-idea date",
     re.compile(r"\b20\d{2}-[01]\d-[0-3]\d\b"),
     "dated state belongs in reports/{slug}/, not in a shared definition"),
    ("contact id",
     re.compile(r"(?<![A-Za-z0-9])C\d{1,3}\s+[A-Z][a-z]+"),
     "use {contact_id} {Name} placeholders"),
    ("idea slug",
     re.compile(r"reports/(?!\{slug\})[a-z][a-z0-9-]{4,}/"),
     "use reports/{slug}/"),
    ("external absolute path",
     re.compile(r"[`\s]~/(?!\.claude)[A-Za-z]"),
     "paths outside the repo belong in machine-local memory"),
]


def founder_names() -> list[str]:
    """First names of the founders, read from founder.md — the one author."""
    fm = ROOT / "founder.md"
    if not fm.is_file():
        return []
    return [m.split()[0] for m in re.findall(r"^\s*- name: (.+)$",
                                             fm.read_text(encoding="utf-8"), re.M)]


def contract_errors(skill: Path, names: list[str]) -> list[str]:
    """Enforce the CLAUDE.md skill contract over SKILL.md (not references/)."""
    out = []
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    body = text.split("---", 2)[-1] if text.startswith("---") else text

    count = len(text.splitlines())
    if count > MAX_SKILL_LINES:
        out.append(
            f"{skill.name}: SKILL.md is {count} lines (cap {MAX_SKILL_LINES}) "
            "— move mechanics to references/"
        )

    for name in names:
        if re.search(r"\b%s\b" % re.escape(name), body):
            out.append(
                f"{skill.name}: names founder {name!r} — write 'the founder'; "
                "per-founder facts live in founders/*.md"
            )

    for label, pattern, hint in CONTRACT_PATTERNS:
        m = pattern.search(body)
        if m:
            out.append(f"{skill.name}: {label} {m.group(0)!r} — {hint}")
    return out


def active_skills() -> list[Path]:
    return sorted(
        path
        for path in CLAUDE_SKILLS.glob("startup-*")
        if path.is_dir() and (path / "SKILL.md").is_file()
    )


def main() -> int:
    try:
        validator = load_quick_validator()
    except Exception as exc:  # dependency/loading errors should remain concise
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    skills = active_skills()
    if not skills:
        print("ERROR: no active startup skills found", file=sys.stderr)
        return 1

    errors: list[str] = []
    expected_names = {skill.name for skill in skills}
    names = founder_names()

    for skill in skills:
        valid, message = validator.validate_skill(skill)
        if not valid:
            errors.append(f"{skill.name}: {message}")
            continue

        frontmatter_name = read_frontmatter_name(skill / "SKILL.md", validator.yaml)
        if frontmatter_name != skill.name:
            errors.append(
                f"{skill.name}: frontmatter name is {frontmatter_name!r}; "
                f"expected {skill.name!r}"
            )

        errors.extend(contract_errors(skill, names))

        bridge = AGENT_SKILLS / skill.name
        if not bridge.is_symlink():
            errors.append(f"{skill.name}: missing Codex bridge {bridge.relative_to(ROOT)}")
        elif bridge.resolve() != skill.resolve():
            errors.append(
                f"{skill.name}: bridge resolves to {bridge.resolve()}, "
                f"expected {skill.resolve()}"
            )

    for bridge in sorted(AGENT_SKILLS.glob("startup-*")):
        if bridge.name not in expected_names:
            errors.append(f"{bridge.name}: stale Codex bridge without an active skill")

    if errors:
        print(f"Skill catalog validation failed ({len(errors)} issue(s)):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Skill catalog valid: {len(skills)} active startup skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
