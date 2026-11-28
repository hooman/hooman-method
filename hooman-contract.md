# Hooman — the contract with myself

v1.1.1 (2026-11-28) · canonical: <https://github.com/hooman/hooman-method>
Audience: me. The assistant reads only **Standing triggers**, only to apply contract.1 (`skills/hooman-assistant/SKILL.md`; this file is packed with that skill). Rationale: `hooman-notes.md`. Budget: 90 lines.

This document works at decision moments or not at all. It is organized by *when*, not by topic.

## Before invoking the method

Work informally below the threshold — chat, sketch, experiment, no apparatus. Escalate when **two or more** hold:

- [ ] I will return to this after a gap
- [ ] an agent will work across several steps without me
- [ ] there is more than one plausible path
- [ ] mistakes are expensive or hard to reverse
- [ ] I need an audit trail

This list is a mnemonic, not a gate. My judgment decides; the list keeps the judgment honest.

## At escalation — scope intake

Before clearing the first tranche (the draft PR's envelope), write three answers: the **smallest independently useful slice** · the **exclusion zone** · the **first decision** that needs making. If I cannot name the slice, the next task is scope decomposition — not setup, not implementation. Big is allowed; undefined is not.

## Before clearing the first tranche — direction check

- **Frame** — am I solving the right problem, or the first one that came to mind?
- **Adjacent domains** — what neighboring concern (personas, invariants) bears on this that I haven't pulled in?
- **Assumption** — what am I treating as settled that isn't?

## During review

Review outcomes, not steps: read the PR's summary and its checklist evidence. Merging is my commit, with my sign-off. Keep a few lines on where each agent or model has been reliable and where it has burned me; weight my attention accordingly — uniform review doesn't compound, calibrated review does.

Merge, close, or comment on every agent PR within a week. An unreviewed queue is the patch queue reborn; re-entry lists it by age (entry.3).

## At session close

First, check that the agent rewrote the track's next-action line and pushed. That single line is the re-entry surface; everything else in the close is optional. Findings go to the project's findings list (proj.8). Write a summary only if the session produced no durable artifact — and its first line is the next action.

## During audits — kill criteria

An artifact, rule, or binding is a deletion-or-merge candidate when any of these hold: not consulted in several cycles · I catch myself avoiding it · it duplicates what the context file already says · too few live entries to earn its own file. Adoption required observed friction; survival requires it too.

## Standing triggers

The agent may cite these by id (contract.1). My contract response is to act on the trigger or consciously override it out loud — not to argue with it.

- **T1 — tinkering spiral.** WHEN an interesting side problem appears mid-cycle → THEN one line to the findings list; return to the tranche. The idea is captured; it will keep.
- **T2 — process-as-avoidance.** WHEN I am editing the method or its docs in a second consecutive session with no roadmap movement → THEN close the method docs, read one next-action line, execute it. Method changes become findings lines, worked in a scheduled pass.
- **T3 — scope gravity.** WHEN a big new effort excites me and I reach for setup → THEN write the three scope-intake answers first. No workspace until the slice has a name.
- **T4 — anticipated friction.** WHEN I add a rule, template, or artifact "because it might help" → THEN name the friction event that already happened. If there is none, it goes to a findings line — not into the method.
- **T5 — premature binding.** WHEN I am tempted to build tooling for a rule → THEN the T4 test, applied to code. The manual discipline must hurt first.
- **T6 — abrupt ending.** WHEN a session is being cut off (interruption, fatigue) → THEN thirty seconds: update the next-action line. Everything else may die; that line may not.
- **T7 — budget breach.** WHEN a governed doc exceeds its stated budget → THEN prune before adding a word: rationale out to its own doc, duplicates merged, stale lines deleted.
- **T8 — ratio drift.** WHEN, over a month, method sessions rival project sessions → THEN T2 writ large: the method has become the avoidance. Park it; ship something.

## Enforcement

Triggers work at the decision moment or not at all. Noticing one after the fact is a findings line, not a failure review.
