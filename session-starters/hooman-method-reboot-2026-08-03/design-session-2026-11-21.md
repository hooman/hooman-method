# Design session 2026-11-21: what v1.0 should be, given a working day without the harness

Status: **closed 2026-11-21: calls converged and revised after the independent critique**  
Track: [`roadmap/reboot.md`](../../roadmap/reboot.md) · Spec: [`spec.md`](spec.md) · Shape: the
design-session sequence from the [2026-11-09 revision](../../roadmap/reboot.md#exploration-and-design-sessions)
(frame, diverge, critique, converge, record).

This is the **frame and critique** for the v1.0 reset. It proposes no method text. It
gathers one day's evidence, sets it against the spec, argues the opposing case, and puts at
most five one-way calls to the principal. The v1.0 text is written after those calls.

## 1. Frame

The principal's question, in their own words (2026-11-21):

> "My circumstances have changed and technology have moved beyond chat interfaces. Models
> have improved and can successfully do more complex tasks autonomously. … I think I should
> be able to achieve more with the limited time and attention that I have. I want to
> completely rethink Hooman-Method to today's horizon. looking forward and what is
> emerging, not what has already established. I am also thining of moving beyond just
> hobby stage and get a bit serious about some of the work."

They then clarified "serious": **public open source first, maybe commercial later.**

A good answer lets the principal decide **what v1.0 is made of**: which parts of the reboot
spec become method text, which become platform conventions, and whether `hooman-harness`
is still the vehicle.

## 2. What is already decided (not reopened here)

- The reboot continues. v1.0 is written fresh and carries no history over from v0.8.x
  (2026-11-09).
- The four axes are stances, context boundaries, decision rights, and records (2026-11-09).
- Entry assessment covers both project continuity and whether the operating contract
  still fits. Execution is in outcome-sized tranches, with mandatory stops and
  checkpoints (spec, 2026-08-03).
- The method stays portable, and the harness, if any, lives in a separate repository
  (D1, 2026-08-03).

## 3. Evidence: one working day, 2026-11-21

**Scope of the evidence.** This is one session with one strong model (Claude Opus 5.5 in
Claude Code). The project was the `capnproto-swift` workspace, a Git and code project with
strong executable gates. It ran warm: the previous day was a working session.

**Outcome.** The project went from "local commits, private repo" to a public, verified
`0.1.0` release in one sitting:
- fresh-clone smoke test, and the CI toolchain question settled in a matching container
- a CI defect found and fixed: a test that only fails when run as root
- public API tiering, with compile-fail fixtures that enforce it
- the repo made public, with branch and tag rulesets
- release automation with build-provenance attestation
- DCO sign-off and an AI-assistance policy

No `hooman-harness` code ran. No brief or feedback files were written. The previous day's
session, with a different vendor's model, did write four brief and feedback pairs (`C-M`),
and its outcomes were also sound.

**Spec acceptance scenarios vs what the day exercised:**

| Scenario | Exercised? | How, or why not |
|---|---|---|
| A1 Warm continuation | Partly | The agent oriented from the roadmap's next-action line and the repo. No catch-up ritual was needed |
| A2 Targeted refresh | No | — |
| A3 Cold re-entry | No | The project was warm |
| A4 Reboot | Partly | The principal asked to "completely rethink" the method without recalling that a reboot had been in flight since August. The agent found that out only by reading this repo (see §4) |
| A5 Path drift | No | Two apparent clones turned out to be one directory reached by two paths (same inode). There was no drift to detect |
| A6 Substantial autonomy | **Yes** | Several cleared tranches ran through validation and bounded repair: the root-only test fix, and the `package` → `internal` reversal after an empirical compile failure |
| A7 Boundary stop | **Yes** | One-way calls went to the principal as at most three plain questions (API tiering, release signing, access level). The commit guard stopped three agent commits of guarded docs |
| A8 Abrupt interruption | No | — |
| A9 Voice | No | — |
| A10 Host replacement | No | — |

**Isolation was mostly not tested.** By the principal's instruction, most changes went
straight to `main` under an admin bypass. A PR-based flow is the next step on that project.

## 4. Observed friction (each item names an event that happened)

1. **Stale human-commit queue.** Seven guarded-document patches were waiting for a human
   `git apply` and commit, the oldest since 2026-09-08. Two of them blocked launch. Once
   routed as a single pasted command, all were cleared in minutes.
2. **The commit guard cost three round-trips in one day:** decisions, invariants, and
   `.claude/settings.json`. It was right each time; the cost is that each needed the
   principal to paste a command.
3. **The projection hid the reboot.** The workspace's `references/` is pinned at `v0.8.1`
   (refreshed 2026-10-12). Downstream, the method still describes a Chat → human →
   Executor relay. Neither the August reboot nor the November revision reached the project
   that actually ran.
4. **The harness is dormant.** `hooman-harness` has one commit (2026-08-15), no local
   checkout, and T2 has not started in three months. Meanwhile the platform shipped
   most of what T1 built: worktrees, cloud and background sessions, scheduled routines,
   cross-session messages, monitors, structured questions, and hooks.
5. **Claims about history were wrong twice in one day, and verification caught both.**
   - The agent said the previous day "wrote no briefs". It had written four pairs.
   - A reviewer suggested the clones showed path drift. They were the same directory.

   Both were caught by checking records, not by recalling them.
6. **Gates, not prose, caught every defect.** A container run of CI caught the root-only
   test. The compiler caught `package` needing `-package-name`. Then lint, then the
   compile-fail suite's directory allowlist. None was caught by a brief or a review rule.

## 5. Reading the evidence

What the day supports:

- **Records over memory** (axis 4) held, and it matters most for the agent's *own*
  narrative. Both factual errors were stale-recall claims, and checking the repository
  fixed them.
- **Decision rights** (axis 3) worked as written: a few plain questions, options with
  consequences, reversible work done and logged. One call was reopened, correctly, when
  new evidence (the `-package-name` requirement) changed the trade-off.
- **Most enforcement belongs in executable gates** (CI, compile-fail contracts, rulesets,
  hooks). Prose rules mattered where they *produced* gates: `INVARIANTS.md` is why the
  `-no-allocations` and symbol-audit gates exist.
- **Most of the harness's job is now done by the platform.** Entry assessment, tranche
  sizing, and stops ran as agent behavior plus a few repo artifacts: the next-action line,
  the decision log, and the roadmap checklist.

## 6. Critique: the strongest opposing case

- **One warm day proves little about the hard cases.** Cold re-entry, reboot, interruption,
  and non-code projects (the knowledge-vault pilot) are exactly the cases the harness was
  designed for, and none occurred. "The gates do the work" has no analogue in a knowledge
  vault, which has no compiler, CI, or test suite.
- **Model dependence is untested.** The day used a frontier model. The previous day's
  other-vendor model mostly ignored `CLAUDE.md` and still did well, but it was operating
  inside a workspace the apparatus had built: invariants, gates, a curated roadmap.
  Removing the apparatus is not the same experiment as ignoring it.
- **The platform is a moving, single-vendor target.** Conventions that rely on one
  vendor's features give up the spec's frontend neutrality (A10) and the voice goal (A9).
  A thin neutral core is what survives a change of vendor.
- **The friction items are cheap to fix without a reset.** A stale queue, a pinned
  projection, and guard round-trips each have small, local fixes. None demands rewriting
  the method.

Response, to be tested rather than assumed: the critique argues for **conventions plus
verification wherever a gate is impossible**, and for running the pilots before building
anything. It does not show that the harness specifically is needed. Its strongest point is
the knowledge vault: v1.0 must say what plays the role of a gate where there is no
compiler.

## 7. Calls for the principal (one-way; at most five)

**C1 — `hooman-harness`.**
- (a) Continue: run T2 on the harness as planned.
- (b) Retire: archive it, and carry its concepts (entry modes, envelope, checkpoint) as
  conventions that agents follow on stock platforms.
- (c) **Freeze** *(proposed)*: run the T2 pilots without the harness, and revive it only
  for friction a pilot actually hits. A10 and A9 stay open questions, not commitments.

**C2 — v1.0 scope.**
- (a) **Git and code projects first** *(proposed)*, with the knowledge vault as the next
  slice, and an explicit "what replaces a gate" section.
- (b) All three project shapes in v1.0.

**C3 — Distribution.**
- (a) Keep the `references/` copy pinned to a tag.
- (b) **Install once per machine** *(proposed)*, through the dotfiles that already manage
  `~/.config/agents/AGENTS.md`. Each project's `AGENTS.md` then shrinks to a few lines:
  what the project is, its gate commands, and where its decisions live. Projections and
  tag pinning are dropped.

**C4 — Guarded canonical documents.**
- (a) Keep the local hook that blocks agent commits.
- (b) **Use pull requests instead** *(proposed)*: agents open PRs for anchors, decisions,
  and context files, and the principal's merge is the act of committing. The hook stays
  only for repositories with no remote review.

**C5 — How this design session finishes.**
- (a) **Separate critique agent** *(proposed)*: one independent agent, with only this
  document and the spec (a clean room), argues against the converged answer before v1.0
  text is written. The agent-teams flag is now enabled in the workspace.
- (b) No separate agent; the critique in §6 stands.

Plus one go-ahead, not a design call: **may the agent commit this document on its branch
and open a PR in `hooman-method`?** The repo is public.

## 8. Converge: the principal's calls (2026-11-21)

In the principal's words: **"proposed on all."**

| Call | Decision |
|---|---|
| C1 | **Freeze `hooman-harness`.** Run the T2 pilots on stock platforms without it; revive it only for friction a pilot actually hits. A9 (voice) and A10 (host replacement) become open questions, not commitments. |
| C2 | **v1.0 covers Git and code projects first.** The knowledge vault is the next slice and needs an explicit section on what replaces a gate. |
| C3 | **Install once per machine** through the dotfiles that manage `~/.config/agents/AGENTS.md`. Each project's `AGENTS.md` keeps a few lines: what the project is, its gate commands, and where its decisions live. `references/` projections and tag pinning are dropped. |
| C4 | **Pull requests replace the commit guard** for anchors, decisions, and context files. Agents open the PR, and the principal's merge is the act of committing. The hook stays only where there is no remote review. |
| C5 | **One independent critique agent.** It works in a clean room, reading only this document and `spec.md`, and argues against this converged answer before any v1.0 text is written. |

## 9. Independent critique (C5)

A separate agent ran in a clean room: it read only this document (through §8) and
`spec.md`, and could not write. Its findings, condensed:

- **C1 (freeze the harness):**
  - "Revive on friction" may never fire, because warm code pilots do not produce the
    friction the harness exists for.
  - spec.md still assigns checkpointing and T2 to the harness.
  - *Safeguard:* stage A3 and A8 deliberately, and set a date by which "freeze" becomes
    "retire" or "revive".
- **C2 (code projects first):**
  - §8 quietly moved the "what replaces a gate" section from v1.0 into the vault slice.
  - Code projects have prose with no compiler too: anchors, decisions, and the method
    itself.
  - *Safeguard:* write the gate-substitute section in v1.0, and apply it to v1.0's own
    text.
- **C3 (install once per machine):**
  - It fixes staleness by giving up reproducibility. Nothing records which method revision
    a session ran under.
  - It leaves gaps for cloud sessions without `~/.config/agents`, for machines that drift
    apart, and for outside contributors' agents.
  - *Safeguard:* each project's `AGENTS.md` names the method revision it expects, the
    entry check reports a mismatch, and one cloud-session test runs before v1.0.
- **C4 (PRs instead of the commit guard):**
  - If the agent can merge its own PR or bypass the ruleset, C4 removes the one control
    that worked (§4.2).
  - A PR queue can go stale exactly like the patch queue did (§4.1).
  - *Safeguard:* CODEOWNERS on guarded paths, no bypass on them, and a recorded failed
    self-merge attempt. Keep the hook until then.
- **What §6 softened:**
  - It never argued against C3 or C4.
  - It scored A4 "partly" when it was a miss: the system did not surface the in-flight
    reboot.
  - It under-used the other-vendor model ignoring `CLAUDE.md`, which threatens the premise
    that installed method text governs behavior.
- **Evidence stretched:**
  - Decision rights worked under the v0.8.1 text, which says nothing about v1.0.
  - A6 counted the public release, which is not reversible, while isolation went
    untested.
  - A7 lacked a mid-tranche checkpoint and the "exactly one decision" the spec requires.
  - "Gates caught every defect" counts only the defects gates caught.
- **Dropped from the spec without amending it:**
  - A2 (freshness of external sources), A5 (path drift), A8 (interruption), and Recovery
    mode
  - the execution envelope, and "every material action attributable to an envelope"
  - scenario evals and recorded routing reasons
  - A9 and A10, which C1 demoted while the spec still requires them

**Fact check by the working agent (2026-11-21).** The C4 risk is real, not hypothetical.
The agent runs under the principal's `gh` identity, which has admin rights, and pushed to
`main` all day through the admin bypass. Nothing today stops it from merging its own PR.
On §4.5, the working agent caught both false claims itself, by checking records: the
"no briefs" claim by reading the 2026-11-20 commits, and the path-drift claim by
comparing inodes. The principal did not catch either.

**Open questions put to the principal:**
1. When to stage A3 (cold start) and A8 (interruption) relative to writing v1.0.
2. How a project records which method revision it expects (C3).
3. What actually stops an agent from merging a guarded-doc PR (C4).

**Principal's answers (2026-11-21), each the proposed option:**

1. **Stage the hard scenarios first.** Before any v1.0 text is written, two tests run on
   `capnproto-swift`:
   - A3: a fresh agent with no memory re-enters the project cold.
   - A8: a session is killed mid-tranche and then resumed.

   v1.0 is written from what they show.
2. **C3, revised: `AGENTS.md` names the method revision.** Each project's short `AGENTS.md`
   states the method revision it expects and links the canonical text on GitHub, so cloud
   sessions and outside contributors can read it. The entry check reports a mismatch with
   what is installed.
3. **C4, revised: keep the hook until a stop is proven.** The local commit guard stays
   alongside PRs. A merge guard is added for agents that blocks `gh pr merge` and pushes
   to `main` on guarded paths. The hook is retired only after a recorded, failed
   self-merge attempt.

## 10. Record

Next:
- stage A3 and A8 on `capnproto-swift`
- add the agent merge guard, and record a failed self-merge attempt
- write the v1.0 text for Git and code projects, including a "what replaces a gate"
  section applied to v1.0's own text
- amend `spec.md` where the calls changed it (A9 and A10 become open questions, and the
  harness no longer owns checkpointing)

Until then, nothing in `hooman-contract.md`, `skills/hooman-assistant/`, or the design
stances changes.
