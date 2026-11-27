# Project shape

v1.1.0 (2026-11-27) · part of the `hooman-assistant` skill · load when setting up a project
under the method, or realigning one.

A governed project needs very little: the repository's own records, gates that enforce what must
hold, and a short `AGENTS.md`. Add an artifact only when friction demands it. In one acceptance
run (A3, 2026-11-21: one model, a simulated gap, 13/18) a cold agent found the right next action
from the next-action line, the decisions, and git state. It missed the binding constraints;
entry.1 now asks for them.

## Required

- proj.1 — **`AGENTS.md`, a few lines, at the repository or workspace root:**
  - that the project follows the Hooman Method, the **revision it expects** (for example `v1.0.0`),
    and a link to that revision's text on GitHub, so cloud sessions and outside contributors can
    read it without a local install
  - what the project is, in one or two lines
  - the gate commands (build, test, the checks that enforce invariants)
  - where decisions, invariants, and the next action live

  Do not paste method rules into it; link to them.
- proj.2 — **Next-action line:** the first line of each roadmap track is the single next
  concrete action. It is the re-entry surface (records.2).
- proj.3 — **Decision log:** numbered decisions with the reasoning and the date, recorded in the
  principal's words where the call was theirs. A decision is changed by a later entry, never by
  silent edit.
- proj.4 — **Invariants with gates:** each invariant names the gate that enforces it, or is
  marked `unenforced`. An unenforced invariant is a candidate for a gate (verify.2).
- proj.5 — **`.agents/guarded-paths`:** one glob per line for the canonical files (`AGENTS.md`,
  anchors, the decision log, the context file, agent configuration). The user-level merge guard
  blocks an agent's push of these to the default branch; they change through a PR the principal
  merges. Keep any project commit guard that already blocks agent commits of them. The guard is
  removed only by the principal's call.

## When it earns it

- proj.6 — Anchors (what this is and is not for; whom it serves) once a decision needs them.
  A glossary once a term is ambiguous and recurs.
- proj.7 — Public repositories, when the principal takes one beyond a hobby: consider
  `CONTRIBUTING.md` with DCO sign-off and an AI-assistance policy, a required DCO check, branch and
  tag rulesets, and release automation with provenance. These are options, not requirements.
- proj.8 — Findings that are off the current task: one line in the project's findings list, or
  once the principal clears it, an issue in a public repository. Never a detour from the tranche.

## Not part of v1.0

- No `references/` projection of the method, and no tag pinning by copy. The method is installed
  once per machine, and projects name the revision (proj.1).
- No brief and feedback files, and no evidence-map contracts. The draft PR carries the envelope
  and the evidence ([`checkpoint.md`](checkpoint.md)).
- Existing v0.8 workspaces migrate when they are next worked on: replace the projection with
  proj.1, add proj.5, and keep their records. Never backfill old work into the new shape.
