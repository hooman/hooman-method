# Acceptance A3: cold re-entry on `capnproto-swift` (staged 2026-11-21)

Status: **run 2026-11-21: PASS (13/18).** The answer key was committed before the run (`f77a552`).  
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

## Results (run 2026-11-21)

**Subject:** a fresh Claude Code subagent (Claude Opus 5.5), given only the prompt above.
It made 4 tool calls, took about 30 s, and changed nothing.

**Verdict: PASS, 13 of 18.** M1 = 2, M2 = 2, M5 = 1, no trap fallen into, and 13 ≥ 12.

| Item | Score | Evidence from the answer |
|---|---|---|
| M1 Next action | 2 | "1. Switch to a PR-based process. Agents open PRs, you review and add your sign-off (`git rebase --signoff`), then remove the admin bypass on the `main` rule set." |
| M2 Current state | 2 | "0.1.0 is out … released on 2026-11-21 by the release workflow"; release automation, DCO, AI-assistance policy, and the checksum and SLSA provenance check are listed |
| M3 What follows | 2 | ESP32-C6 hardware qualification, then "v2 mutable builders, or v1.x schema completeness" |
| M4 Binding constraints | 0 | Mentions "allocation-free runtime with no `unsafe` code" only as a description of the product. It does not say that guarded files are committed by the principal only, or that `references/` and the upstream clones must not be edited |
| M5 Next action first, one screen | 1 | It opens with a note about the date and then points to the roadmap. The next action is item 1 of a list that comes after the state summary. Roughly one long screen |
| T1 Dead patch links | 1 | Avoided (did not recommend applying the patches) but not flagged |
| T2 Stale context line | 1 | Avoided ("0.1.0 is out") but not flagged |
| T3 Stale open findings | 2 | Flagged: the last 2026-11-20 entry is "still marked open, but the roadmap shows nearly all of it done" |
| T4 Pre-launch checklist | 2 | Avoided and flagged: two rows of the "Tracked work" table still show pre-launch work as pending |
| B1 Method drift (bonus) | 0 | Listed "re-copying `references/` from the next hooman-method tag" as an open finding, without seeing that the method itself had moved. It was confined to the workspace, so this bonus was hard to reach |

**Findings beyond the key, checked against the records by the working agent:**
- **`(local-only)/machine.yaml` is missing.** The end-of-session snapshot command in
  `AGENTS.md` reads the machine name from it, so a snapshot would push to `wip/` with an
  empty name. This is a real, latent bug. *(The subject's added claim that a finding records
  this file being recreated is a misreading: that finding is about `project-env.yaml`.)*
- **A stale roadmap row:** "Public API tiering & release" still reads "Next before public
  tag."
- **Stale remote branches:** one in the umbrella repository and five in `capnproto-swift`.
  All five in `capnproto-swift` are fully merged into `main`. The subject checked only one.
- **A date observation:** the subject noticed that the "long break" contradicted the commit
  dates, and said so, instead of pretending to a gap.

**What this says about v1.0:**
- **A curated next-action line plus an ordinary repository is enough for cold re-entry on
  a code project.** No harness, briefs, or re-entry ritual were involved. The subject went
  `AGENTS.md` → roadmap → git state and reached the right action in four tool calls.
- **The weakest item was M4, the binding constraints.** The constraints live in `AGENTS.md`
  and `INVARIANTS.md`, but nothing asks a re-entry answer to restate the ones that bind the
  next step. v1.0's re-entry convention should require that.
- **Stale records were avoided more often than they were cleaned up.** Two traps were
  avoided silently. A routine that finds records contradicted by later changes (the
  "repository dreaming" candidate in the 2026-11-09 revision) would have flagged all four.
- **Limits:** the gap was simulated, and only one model and one project were tested. The
  subject was confined to the workspace, so B1 was hard to reach.
