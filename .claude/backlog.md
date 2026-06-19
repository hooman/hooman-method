# Deferred backlog — hooman-method

Small, non-urgent items to tackle when/if a bigger update happens. One entry per
item; mark `[done]` with a date when cleared. Not part of the method's canonical
doc set — Claude-maintained working notes, version-controlled so they survive
across sessions and gaps.

## Open

- **Stale version-stamp check for `tools/check-docs.py`.** Add a check that flags
  any governed doc whose `Draft vX.Y.Z (YYYY-MM-DD)` stamp date predates its last
  git-edit date — the class of miss behind the v0.8.1 reference sweep (2026-06-19).
  Reads git, so it's heavier than the current pure-text checks; scope with the
  principal before building. [open]

- **Manually reorder ws.9–11 in `skills/hooman-assistant/references/workspace.md`.**
  Cut/paste so the rule ids run in numeric order (currently ws.1–8, then ws.12–14,
  then ws.9–11 under the AGENTS.md-discipline heading). The principal does this by
  hand before the next content commit — deliberately not an automated renumber. [open]
