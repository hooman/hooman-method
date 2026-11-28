#!/usr/bin/env python3
"""Pack each skill under skills/ into a deterministic `<name>.skill` file.

A `.skill` file is a zip archive whose root holds the skill's folder (`<name>/SKILL.md`, ...),
the layout the skill-creator's `package_skill.py` builds and the Skills upload accepts. This
script applies the same validation as that tool's `quick_validate.py`, with no third-party
packages: the frontmatter parser accepts only single-line `key: value` pairs and rejects
anything else rather than guess at YAML. It adds the method's own checks:

- the frontmatter name equals the folder name
- every revision stamp (`vX.Y.Z (YYYY-MM-DD)`) in the skill's Markdown agrees, and equals
  `--version` when one is given (the release tag)
- a `(vX.Y` in the description agrees with the stamp's major.minor

Archives are reproducible: entries in sorted order, fixed timestamps and permissions, so the
attested release asset can be rebuilt from its tag and compared byte for byte.

Usage:
    tools/package-skill.py [--version X.Y.Z] [--out DIR] [--check] [SKILL_DIR ...]

With no SKILL_DIR, every folder under skills/ that holds a SKILL.md. --check validates and
builds in memory, writing nothing. Exit status 1 on any failure.
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import io
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Mirrors skill-creator's package_skill.py: excluded at any depth, or only at the skill root.
EXCLUDE_DIRS = {"__pycache__", "node_modules"}
ROOT_EXCLUDE_DIRS = {"evals"}
EXCLUDE_FILES = {".DS_Store"}
EXCLUDE_GLOBS = {"*.pyc"}

ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
STAMP_RE = re.compile(r"^v(\d+)\.(\d+)\.(\d+) \(\d{4}-\d{2}-\d{2}\)", re.M)
DESCRIPTION_VERSION_RE = re.compile(r"\(v(\d+)\.(\d+)\b")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")

# 1980-01-01 is the earliest time a zip entry can hold.
FIXED_TIME = (1980, 1, 1, 0, 0, 0)


def packaged_files(skill: Path) -> list[Path]:
    """Files that go into the archive, relative to the skill folder, sorted."""
    files = []
    for path in skill.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(skill)
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        if len(rel.parts) > 1 and rel.parts[0] in ROOT_EXCLUDE_DIRS:
            continue
        if rel.name in EXCLUDE_FILES or any(fnmatch.fnmatch(rel.name, g) for g in EXCLUDE_GLOBS):
            continue
        files.append(rel)
    return sorted(files, key=lambda p: p.as_posix())


def frontmatter(text: str) -> dict[str, str]:
    """Single-line `key: value` frontmatter. Raises ValueError for anything else."""
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise ValueError("no frontmatter: SKILL.md must start with '---' and close it")
    fields: dict[str, str] = {}
    for number, line in enumerate(match.group(1).splitlines(), start=2):
        key, sep, value = line.partition(":")
        if not sep or not key or key != key.strip() or not value.startswith(" "):
            raise ValueError(f"frontmatter line {number} is not a single-line 'key: value'")
        value = value.strip()
        if not value or value[0] in "|>[{'\"&*!%@`" or ": " in value or " #" in value:
            # YAML would read these as another type, or cut the value short.
            raise ValueError(f"frontmatter line {number}: only plain scalar values are supported")
        if key in fields:
            raise ValueError(f"frontmatter key {key!r} appears twice")
        fields[key] = value
    return fields


def validate(skill: Path, version: str | None) -> list[str]:
    errors: list[str] = []
    skill_md = skill / "SKILL.md"
    if not skill_md.is_file():
        return [f"{skill}: no SKILL.md"]
    files = packaged_files(skill)
    nested = [f.as_posix() for f in files if f.name == "SKILL.md" and f != Path("SKILL.md")]
    if nested:
        errors.append(f"{skill}: more than one SKILL.md would be packaged: {', '.join(nested)}")

    try:
        fields = frontmatter(skill_md.read_text(encoding="utf-8"))
    except ValueError as error:
        return errors + [f"{skill_md}: {error}"]
    unexpected = sorted(set(fields) - ALLOWED_KEYS)
    if unexpected:
        errors.append(f"{skill_md}: unexpected frontmatter keys: {', '.join(unexpected)}")
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not name:
        errors.append(f"{skill_md}: missing name")
    elif not NAME_RE.match(name) or len(name) > 64:
        errors.append(f"{skill_md}: name {name!r} must be kebab-case, at most 64 characters")
    elif name != skill.name:
        errors.append(f"{skill_md}: name {name!r} differs from its folder {skill.name!r}")
    if not description:
        errors.append(f"{skill_md}: missing description")
    elif len(description) > 1024:
        errors.append(f"{skill_md}: description is {len(description)} characters (max 1024)")
    elif "<" in description or ">" in description:
        errors.append(f"{skill_md}: description cannot contain angle brackets")

    stamps = {}
    for rel in files:
        if rel.suffix == ".md":
            match = STAMP_RE.search((skill / rel).read_text(encoding="utf-8"))
            if match:
                stamps[rel.as_posix()] = ".".join(match.groups())
    if "SKILL.md" not in stamps:
        errors.append(f"{skill_md}: no 'vX.Y.Z (YYYY-MM-DD)' revision stamp")
    elif len(set(stamps.values())) > 1:
        errors.append(f"{skill}: revision stamps disagree: {stamps}")
    else:
        revision = stamps["SKILL.md"]
        if version is not None and revision != version:
            errors.append(f"{skill}: revision {revision} is not the release version {version}")
        quoted = DESCRIPTION_VERSION_RE.search(description)
        if quoted and ".".join(quoted.groups()) != ".".join(revision.split(".")[:2]):
            errors.append(
                f"{skill_md}: description says v{'.'.join(quoted.groups())}, "
                f"the stamp says {revision}"
            )
    return errors


def build(skill: Path) -> bytes:
    """The archive's bytes: `<name>/<file>` entries, sorted, with fixed metadata."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        for rel in packaged_files(skill):
            info = zipfile.ZipInfo(f"{skill.name}/{rel.as_posix()}", date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16  # a regular file, rw-r--r--
            info.create_system = 3  # Unix, so the mode bits above are honoured
            archive.writestr(info, (skill / rel).read_bytes())
    return buffer.getvalue()


def round_trip(skill: Path, data: bytes) -> list[str]:
    """Unzip what was built and compare every entry with its source file."""
    expected = {f"{skill.name}/{rel.as_posix()}": rel for rel in packaged_files(skill)}
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        names = archive.namelist()
        if sorted(names) != sorted(expected):
            return [f"{skill}: archive entries differ from the source files"]
        for name, rel in expected.items():
            if archive.read(name) != (skill / rel).read_bytes():
                return [f"{skill}: archive entry {name} differs from its source"]
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("skills", nargs="*", type=Path, help="skill folders (default: all)")
    parser.add_argument("--version", help="release version X.Y.Z every stamp must equal")
    parser.add_argument("--out", type=Path, default=ROOT / "dist", help="output folder")
    parser.add_argument("--check", action="store_true", help="validate and build; write nothing")
    args = parser.parse_args()

    if args.version is not None and not SEMVER_RE.match(args.version):
        print(f"FAIL: version {args.version!r} is not X.Y.Z (no leading v)", file=sys.stderr)
        return 1
    skills = [p.resolve() for p in args.skills] or sorted(
        p.parent for p in (ROOT / "skills").glob("*/SKILL.md")
    )
    if not skills:
        print("FAIL: no skills found", file=sys.stderr)
        return 1

    errors: list[str] = []
    built: dict[Path, bytes] = {}
    for skill in skills:
        problems = validate(skill, args.version)
        if not problems:
            data = build(skill)
            problems = round_trip(skill, data)
            if build(skill) != data:
                problems.append(f"{skill}: two builds differ; the archive is not reproducible")
            built[skill] = data
        errors.extend(problems)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    for skill, data in built.items():
        digest = hashlib.sha256(data).hexdigest()
        if args.check:
            print(f"ok {skill.name}.skill ({len(data)} bytes, sha256 {digest})")
            continue
        args.out.mkdir(parents=True, exist_ok=True)
        target = args.out / f"{skill.name}.skill"
        target.write_bytes(data)
        (args.out / f"{skill.name}.skill.sha256").write_text(f"{digest}  {target.name}\n")
        print(f"wrote {target} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
