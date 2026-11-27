# AGENTS.md — hooman-method

This repository follows the **Hooman Method** at the revision its own skill files carry
([`skills/hooman-assistant/SKILL.md`](skills/hooman-assistant/SKILL.md)). It is the method's
source: the agent rules, the principal's contract, the design stances and the coding conventions.
[`hooman-method-context.md`](hooman-method-context.md) holds the durable direction.

- **Next action:** the first line of [`roadmap/reboot.md`](roadmap/reboot.md).
- **Decisions:** the dated calls in `roadmap/reboot.md`.
- **Guarded paths:** [`.agents/guarded-paths`](.agents/guarded-paths). Agents draft them; they
  change through PRs the principal merges.
- **Gates:** `python3 tools/check-docs.py` (budgets, rule ids, the checkpoint template,
  revisions, links) and `python3 tools/package-skill.py --check` (each skill packs, and its
  revision agrees). The `check` workflow runs both on every PR and on `main`.
- **Releases:** the `release` workflow, which the principal dispatches. See the README.
