# hooman-method

A personal operating method for LLM-assisted work that matters, pauses for weeks, and cannot
safely live only in chat history.

The **Hooman Method** is built for one principal whose attention is split across many projects,
responsibilities, and long gaps between sessions. Attention is the scarce resource. The method's
job is to spend it only on judgement: setting intent, making one-way calls, and reviewing and
merging outcomes. Agents do the work in between and prove it.

**v1.0** (2026-11-21) is a fresh start for Git and code projects. Agents now work autonomously
across many steps, on tooled surfaces, with pull requests, CI, and hooks available. The method
leans on those instead of a hand-carried relay of briefs. v1.0 rests on two acceptance runs
(cold re-entry, and interruption with resumption) and a recorded design session. Their records
are under [`session-starters/hooman-method-reboot-2026-08-03/`](session-starters/hooman-method-reboot-2026-08-03/).

It stays an escalation protocol. Below the threshold, work informally. Above it, keep just
enough durable structure for the work to survive interruption, delegation, and review.

## Contents

- [`skills/hooman-assistant/SKILL.md`](skills/hooman-assistant/SKILL.md): the agent rules,
  organised around four axes: stances, context boundaries, decision rights, and records.
  - [`references/checkpoint.md`](skills/hooman-assistant/references/checkpoint.md): the draft
    PR as checkpoint.
  - [`references/project.md`](skills/hooman-assistant/references/project.md): the minimal
    shape of a governed project.
- [`hooman-contract.md`](hooman-contract.md): the principal's contract with themselves. Agents
  read only its standing triggers. The `.skill` file carries it as `references/hooman-contract.md`.
- [`design-stance/`](design-stance/) and [`coding-conventions/`](coding-conventions/): design
  stances and coding-guideline indexes.
- [`hooman-notes.md`](hooman-notes.md): rationale and provenance from v0.x. Historical; never
  needed to operate.
- [`tools/check-docs.py`](tools/check-docs.py): document checks (budgets, unique rule ids, the
  checkpoint template, consistent revisions, and links in every Markdown file).
- [`tools/package-skill.py`](tools/package-skill.py): packs each skill into a reproducible
  `.skill` file, after validating it.
- [`CHANGELOG.md`](CHANGELOG.md), [`AGENTS.md`](AGENTS.md), and the dated
  [`audits/`](audits/hooman-method-audits/).
- [`roadmap/reboot.md`](roadmap/reboot.md): the current track and its next action.

## Using it

- **Install once per machine,** not per project. The skill goes where the agent discovers
  skills, and the principal's dotfiles manage that. Each release from `v1.1.0` attaches
  `hooman-assistant.skill`: upload it as a skill in Claude, or unzip it into a skills folder.
  Check it first with
  `gh attestation verify hooman-assistant.skill -R hooman/hooman-method`.
- **Each project's `AGENTS.md` names the revision it expects** and links to that revision's
  text here, so cloud sessions and outside contributors can read it
  ([`project.md`](skills/hooman-assistant/references/project.md), proj.1). There is no
  `references/` copy and no tag pinning by copy.
- **Canonical documents,** here and in governed projects, change only through pull requests the
  principal merges. A user-level merge guard stops agents from merging, or from pushing guarded
  paths to the default branch.

## Checks

`python3 tools/check-docs.py` and `python3 tools/package-skill.py --check`. The `check` workflow
runs both on every PR and on `main`, and uploads the packed `.skill` files as an artifact.

## Releasing

The principal releases; agents prepare the release PR.

1. In a PR, turn `## [Unreleased]` in `CHANGELOG.md` into `## [X.Y.Z] - YYYY-MM-DD`. Set the
   revision stamp `vX.Y.Z (YYYY-MM-DD)` in every skill file, and the `(vX.Y, …)` in the
   skill's description, to match. `package-skill.py --check --version X.Y.Z` must pass.
2. Merge it, then run `gh workflow run release.yml -R hooman/hooman-method -f version=X.Y.Z`.
   From `main`, the workflow:
   - checks the version, the changelog entry and the stamps
   - runs the checks on that commit
   - packs each skill and attests the `.skill` files
   - creates the tag `vX.Y.Z` and the release, with the files attached, in one step
3. Install from the release asset, and update any project `AGENTS.md` that should move to the
   new revision.

## Versioning & license

Releases are tagged. In v1.0.0 the agent rules and references are a reset, carrying no rules
over from v0.8.x, whose history remains in git. The principal's contract (`hooman-contract.md`)
was revised for v1.0 at the same time. Docs are licensed **CC BY 4.0** (see `LICENSE`). Code, meaning
`tools/` and `.github/`, is licensed **MIT** (see `LICENSE-CODE`).
