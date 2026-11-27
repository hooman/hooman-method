#!/usr/bin/env python3
"""Check the small invariants that keep the Hooman docs lean (v1.0)."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = "skills/hooman-assistant/SKILL.md"
CHECKPOINT = "skills/hooman-assistant/references/checkpoint.md"
PROJECT = "skills/hooman-assistant/references/project.md"
COMMENTS = "coding-conventions/swift/comment-standard.md"

LINE_BUDGETS = {
    "hooman-contract.md": 90,
    SKILL: 120,
    COMMENTS: 110,
}

# Rule ids must be unique within a file and across files.
RULE_FILES = {
    "hooman-contract.md": r"\*\*(T\d+)\s+—",
    SKILL: r"^-\s+([a-z]+\.\d+)\s+—",
    CHECKPOINT: r"^-\s+(cp\.\d+)\s+—",
    PROJECT: r"^-\s+(proj\.\d+)\s+—",
    COMMENTS: r"^-\s+((?:cm|ca|cr)\.\d+)\s+—",
}

# The checkpoint template is load-bearing: a resuming agent relies on these fields.
CHECKPOINT_MARKERS = [
    "## Envelope",
    "- **Outcome:**",
    "- **Why:**",
    "- **In scope:**",
    "- **Excluded:**",
    "- **Proof:**",
    "- **Stop conditions:**",
    "- **Authority:**",
    "## Checklist",
    "- [ ] 1. Design: approach written here, before any code",
]

# All skill files carry the same method revision.
VERSIONED = [SKILL, CHECKPOINT, PROJECT]
VERSION_RE = re.compile(r"^v(\d+\.\d+\.\d+) \(\d{4}-\d{2}-\d{2}\)", re.M)

LINK_RE = re.compile(r"\]\((?!https?://|mailto:|#)([^)#\s]+)")


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def check_line_budgets(errors: list[str]) -> None:
    for path, budget in LINE_BUDGETS.items():
        count = len(text(path).splitlines())
        if count > budget:
            errors.append(f"{path}: {count} lines exceeds budget {budget}")


def check_rule_ids(errors: list[str]) -> None:
    all_ids: list[tuple[str, str]] = []
    for path, pattern in RULE_FILES.items():
        found = re.findall(pattern, text(path), re.M)
        if not found:
            errors.append(f"{path}: no rule ids found")
        for rule_id, count in Counter(found).items():
            if count > 1:
                errors.append(f"{path}: duplicate rule id {rule_id}")
        all_ids.extend((rule_id, path) for rule_id in found)
    for rule_id, count in Counter(rule_id for rule_id, _ in all_ids).items():
        if count > 1:
            paths = sorted({p for found_id, p in all_ids if found_id == rule_id})
            errors.append(f"duplicate rule id {rule_id} across {', '.join(paths)}")


def check_checkpoint_template(errors: list[str]) -> None:
    body = text(CHECKPOINT)
    for marker in CHECKPOINT_MARKERS:
        if marker not in body:
            errors.append(f"{CHECKPOINT}: template missing {marker!r}")


def check_versions(errors: list[str]) -> None:
    versions = {}
    for path in VERSIONED:
        m = VERSION_RE.search(text(path))
        if not m:
            errors.append(f"{path}: no 'vX.Y.Z (YYYY-MM-DD)' revision line")
        else:
            versions[path] = m.group(1)
    if len(set(versions.values())) > 1:
        errors.append(f"skill files disagree on revision: {versions}")


def check_relative_links(errors: list[str]) -> None:
    for path in [SKILL, CHECKPOINT, PROJECT, "README.md", "hooman-method-context.md"]:
        base = (ROOT / path).parent
        for target in LINK_RE.findall(text(path)):
            if not (base / target).exists():
                errors.append(f"{path}: broken relative link {target}")


def main() -> int:
    errors: list[str] = []
    check_line_budgets(errors)
    check_rule_ids(errors)
    check_checkpoint_template(errors)
    check_versions(errors)
    check_relative_links(errors)

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print("docs ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
