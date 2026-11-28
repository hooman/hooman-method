# Changelog

Releases of the Hooman Method. Versions follow [Semantic Versioning](https://semver.org/) as it
applies to rules: a patch fixes wording or records, a minor adds documents or rules without
breaking a governed project, and a major resets the rules. Each release is tagged `vX.Y.Z` and
carries one `.skill` file per skill, built by `tools/package-skill.py` and attested. The release
workflow requires an entry headed `## [X.Y.Z] - YYYY-MM-DD`.

## [Unreleased]

## [1.1.0] - 2026-11-27

### Added
- **`coding-conventions/swift/comment-standard.md`:** what a comment must carry (`cm.*`), the
  Swift assumption classes with the failure each came from (`ca.*`), and the comment-review pass
  (`cr.*`). Its ids and a 110-line budget are checked.
- **Swift conventions v0.2:** compiler settings (note D) and fluency (note E), evidence labels.
- **Releases with `.skill` files:** `tools/package-skill.py` packs each skill reproducibly and
  validates it. The `release` workflow attests the files and attaches them, and the `check`
  workflow runs the gates on every PR.
- **`AGENTS.md`** for this repository (proj.1), and this changelog.
- **The 2026-11-27 full audit** (`audits/hooman-method-audits/full-audit-2026-11-27.md`).

### Changed
- **Design stances:** written in v1.0 terms. Stances replace the Chat/Executor roles, and the
  documents live here, not in `references/`.
- **`check-docs.py`** checks links in every Markdown file.

### Fixed
- **Swift conventions:** note A, since `@Test` does carry `@available`; note B, since
  `FoundationEssentials` isn't importable on macOS.
- **Records:** the stale README and roadmap lines; a broken link; historical banners.

## [1.0.0] - 2026-11-21

**Hooman Method v1.0.0: a fresh start for Git and code projects.** It carries no rules over from v0.8.x. The v0.8.x history remains in git.

Agents now work autonomously across many steps, on tooled surfaces, with pull requests, CI, and hooks available. v1.0 leans on those instead of a hand-carried relay of briefs. The principal sets intent, makes one-way calls, and merges; agents do the work in between and prove it.

### What's in it
- **[Agent rules](https://github.com/hooman/hooman-method/blob/v1.0.0/skills/hooman-assistant/SKILL.md),** organized around four axes: stances, context boundaries, decision rights, and records. They also cover:
  - re-entry: next action first, then the constraints that bind it and what waits on the principal
  - the draft PR as checkpoint
  - executable gates, and named substitutes where no gate is possible
- **[`checkpoint.md`](https://github.com/hooman/hooman-method/blob/v1.0.0/skills/hooman-assistant/references/checkpoint.md):** the draft-PR envelope and checklist template.
- **[`project.md`](https://github.com/hooman/hooman-method/blob/v1.0.0/skills/hooman-assistant/references/project.md):** the minimal project shape. Each project's `AGENTS.md` names the method revision it expects; there are no `references/` copies.
- **[The principal's contract](https://github.com/hooman/hooman-method/blob/v1.0.0/hooman-contract.md),** revised for v1.0.

### Evidence it rests on
- [Design session](https://github.com/hooman/hooman-method/blob/v1.0.0/session-starters/hooman-method-reboot-2026-08-03/design-session-2026-11-21.md), with an independent critique.
- Acceptance runs: [A3, cold re-entry](https://github.com/hooman/hooman-method/blob/v1.0.0/session-starters/hooman-method-reboot-2026-08-03/acceptance-a3-cold-reentry-2026-11-21.md), passed 13/18, and [A8, interruption and resumption](https://github.com/hooman/hooman-method/blob/v1.0.0/session-starters/hooman-method-reboot-2026-08-03/acceptance-a8-interruption-2026-11-21.md), passed.
- [Traceability table](https://github.com/hooman/hooman-method/blob/v1.0.0/session-starters/hooman-method-reboot-2026-08-03/v1.0-traceability-2026-11-21.md), with what is deferred and what is open.

### Retired
- The Chat/Executor relay, briefs and feedback files, and the C-R/C-M/C-A contracts and evidence maps.
- The workspace tree and `references/` projections.
- `hooman-harness` is frozen, with a decision due by 2027-02-21.

### Not yet covered
- knowledge vaults
- voice frontends and replacing the host
- a separate agent identity without merge rights
- another vendor's models (every acceptance run used the same model)
