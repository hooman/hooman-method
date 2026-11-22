# Acceptance A3: cold re-entry on `capnproto-swift` (staged 2026-11-21)

Status: **staged. The answer key is committed before the run.**  
Track: [`roadmap/reboot.md`](../../roadmap/reboot.md) · Decided in the
[2026-11-21 design session](design-session-2026-11-21.md) (question 1: stage A3 and A8
before writing v1.0)

Scenario A3 (spec): *a long gap with a trusted contract yields a one-screen
next-action-first reconstruction.*

## Protocol

- **Subject:** a fresh agent with no conversation history. Platform memory for the
  workspace was checked first and is empty. The agent loads only what any new session
  in the workspace would: the global and workspace `AGENTS.md`/`CLAUDE.md`, plus whatever
  it chooses to read.
- **Gap:** simulated. The records are as they stood at the end of 2026-11-21. Nothing was
  tidied before the run; stale records are part of what is tested.
- **Prompt:** a returning principal's words, with no hints about where the state lives:

  > I'm coming back to capnproto-swift after a long break and don't remember where things
  > stand. Where do I start? Don't change anything; just tell me.

- **Constraint:** read-only. The agent may read anything in the workspace, but must not
  write or change anything, or send anything outside the workspace.
- **Grading:** the subject's answer is graded against the key below, which was committed
  before the run. Evidence for every score is quoted from the answer.

## Answer key (truth as of 2026-11-21, from the records)

### Must have (each 0, 1 or 2 points)

- **M1 Next action:** switch `capnproto-swift` to a PR-based process. Agents open PRs, the
  principal reviews and signs off, and the admin bypass on the `main` ruleset is removed.
  (Workspace `roadmap/README.md`, next-action line.)
- **M2 Current state:** `0.1.0` is released and public, with CI green. Release automation
  with provenance attestation, DCO, and the AI-assistance policy are in place.
- **M3 What follows:** 32-bit and real-hardware qualification (ESP32-C6), then a choice
  between v2 mutable builders and v1.x schema completeness.
- **M4 Constraints that bind the first step:**
  - the `-no-allocations` invariant, and zero `unsafe`
  - guarded files are committed by the principal only
  - `references/` and the upstream clones are never edited
- **M5 One screen, next action first:** the answer leads with the action and fits on one
  screen. Detail is optional and comes after.

### Traps (each 0 if fallen into, 1 if avoided, 2 if avoided and flagged as stale)

- **T1 Dead patch links:** `session-starters/README.md` links three `.patch` files,
  described as guarded and awaiting the owner. They were applied or superseded and moved
  to the Trash on 2026-11-21. Falling in means recommending that they be applied.
- **T2 Stale context line:** `capnproto-swift-context.md` says "a tagged release remains a
  separate decision". `0.1.0` has shipped. Falling in means saying no release exists, or
  recommending tagging.
- **T3 Stale open findings:** `findings-from-chat.md` has 13 `[open]` entries, some
  superseded (for example "no LICENSE yet", while MIT exists). Falling in means presenting
  a superseded finding as current work.
- **T4 Pre-launch checklist:** the roadmap's "Going public" checklist is complete.
  Falling in means presenting launch steps (push commits, go public, tag) as still to do.

### Bonus: operating-contract fitness (A4 signal, not required)

- **B1:** notices that the workspace's method text (`references/` at `v0.8.1`, and the
  Chat/Executor relay in `AGENTS.md`) may be out of date relative to upstream
  `hooman-method`. The 2026-11-21 calls changed distribution and the guard, but nothing
  was applied downstream. Seeing this requires looking outside the workspace, or reasoning
  from `references/UPSTREAM`.

### Pass criteria

- **Pass:** M1 = 2, M2 ≥ 1, M5 ≥ 1, no trap fallen into, and at least 12 of 18 points
  (M1–M5 and T1–T4).
- **Fail:** M1 < 2, or any trap fallen into. Every failure names the record that misled
  the subject, because that record is what needs fixing.

## Results

*(Recorded after the run.)*
