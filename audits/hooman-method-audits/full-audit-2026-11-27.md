# hooman-method full audit — 2026-11-27

Scope: every tracked file at `main` `ed6a9b4`, six days after `v1.0.0`. Requested by the principal
together with a `.skill` release mechanism and an update of the Swift conventions from a second,
private Swift project. Done in hooman-method PR #8.

**Method.** I read every live document in full and the historical ones (`session-starters/`,
`audits/`, `hooman-notes.md`) for their headers and links. A script checked every relative link in
every tracked Markdown file. Two Swift claims were compiled on a probe package. The installed skill
was compared byte for byte with the repository. **Inspected** marks what I checked directly;
**inferred** marks a judgement.

**Dispositions:**
- **fixed:** done in this PR
- **question:** a call for the principal, listed at the end
- **kept:** looked at, and no change is needed
- **deferred:** waits, with the reason given

## Findings

### Records

- **A-1 — The roadmap's next action is done.** fixed.
  - **Inspected:** `roadmap/reboot.md` says "Install v1.0. The synced claude.ai `hooman-assistant` skill still serves v0.8". On 2026-11-27 the synced copy under `~/.claude/skills/synced/…/hooman-assistant/` was byte-identical (`cmp`) to `skills/hooman-assistant/` at `v1.0.0`, all three files.
  - **Inspected:** the capnproto-swift workspace's `AGENTS.md` names `v1.0.0` and has no `references/` directory, so the second half, the migration, is done too.
- **A-2 — Broken link.** fixed.
  - **Inspected:** `roadmap/reboot.md` links `../../hooman-harness/aside/…`. That path is outside this repository, and `hooman/hooman-harness` is private, so the link resolves for nobody on GitHub.
- **A-3 — The link check missed A-2.** fixed.
  - **Inspected:** `tools/check-docs.py` checked links in only five files.
  - **Fix:** it now checks every tracked Markdown file.
- **A-4 — README is stale about the contract.** fixed.
  - **Inspected:** `README.md` says the contract "is still the v0.8.1 text, and will be revised separately". It was revised for v1.0 in `40c697f` (2026-11-21), and its header reads `v1.0.0`.
- **A-5 — The decision log lives in the roadmap.** kept.
  - **Inspected:** the calls C1 to C5 are under "Calls 2026-11-21" in `roadmap/reboot.md`; proj.3 asks for a decision log.
  - **Inferred:** five calls in one track don't yet earn a separate file (the contract's kill criteria).

### Live reference documents still in v0.x vocabulary

- **A-6 — The design stances use retired roles.** fixed for the header; **question Q2** for the role mapping.
  - **Inspected:** both stances date from 2026-06 (v0.8). Their headers say "Binds: Chat and the Executor" and "Home: `references/`". The universal stance gives scouting duties to "Chat" and to "the Executor … in every reconnaissance (R1) output".
  - **Inspected:** the `v1.0.0` release notes list "the Chat/Executor relay, briefs and feedback files" and "`references/` projections" as retired.
  - **Inferred:** replacing the roles with v1.0 stances changes who must scout and when, so the mapping is proposed for the principal to confirm. The certainty process itself is unchanged; a preservation diff is in the PR.
- **A-7 — The Swift stance's version list is stale.** fixed.
  - **Inspected:** it says "5.10 / 6.0 / 6.1 / 6.2 / trunk differ meaningfully". The current release is 6.4.2, and projects under the method use 6.4.
- **A-8 — `swift-conventions.md` describes retired machinery.** fixed.
  - **Inspected:** its header says it is "projected into each workspace via `references/`". Its "coding-time" tag says to "carry these in the implementation brief's *Read first*". `project.md` retires both.
  - This stale header is what misled a capnproto-swift session on 2026-11-27 into reporting a missing `references/` copy as a gap.
- **A-9 — Note A is wrong.** fixed.
  - Note A says "`@Test` can't carry `@available`".
  - **Inspected:** on Swift 6.4.2 and macOS 27.3 (2026-11-27), a test marked `@available(macOS 99, *)` compiles, and is reported as `Test future() skipped: "Requires macOS 99"`. One marked `@available(macOS 1, *)` runs.
- **A-10 — Note B gives advice that doesn't compile on macOS.** fixed.
  - Note B says to prefer `FoundationEssentials` over `Foundation`.
  - **Inspected:** on Swift 6.4.2 and macOS 27.3 (2026-11-27), `import FoundationEssentials` fails with "unable to resolve module dependency". The private project recorded the same.
  - **Not checked:** Linux, where swift-corelibs-foundation is expected to provide it (inferred, unverified). The note now says it is platform-dependent.

### Historical documents

- **A-11 — `hooman-notes.md` doesn't say it's historical.** fixed with a banner only.
  - **Inspected:** its opening describes "the operating set" as `SKILL.md` + `contracts.md` + `workspace.md`, and its status is "Draft v0.8.1". The README calls it historical, but the file itself doesn't say so.
  - Its content stays as written, because `project.md` forbids backfilling.
- **A-12 — `.claude/backlog.md` is stale.** fixed.
  - **Inspected:** item 2 asks to reorder `ws.9–11` in `references/workspace.md`, a file that no longer exists. Item 1 refers to the v0.8 stamp format `Draft vX.Y.Z (YYYY-MM-DD)`.
  - **Fix:** item 2 is closed as obsolete. Item 1 is restated against the v1.0 stamp, and is still open.
- **A-13 — `session-starters/` and `audits/`.** kept.
  - **Inspected:** they are dated records of the reboot. Their v0.x vocabulary is correct for their time.

### The repository against its own method

- **A-14 — No `AGENTS.md`.** fixed.
  - **Inspected:** proj.1 requires `AGENTS.md` at the root, naming the revision and the gate commands. This repository has `hooman-method-context.md` (the v0.8 "context file"), which names no gates.
  - **Fix:** a short `AGENTS.md` is added. Adding it to `.agents/guarded-paths` is a principal commit: an edit to the oversight list itself, delivered as a patch with a one-command apply script.
- **A-15 — No gate runs in CI.** fixed.
  - **Inspected:** there is no `.github/` directory. `check-docs.py` runs only by hand, "before tagging a release" (README). verify.1 and verify.2 prefer executable gates.
  - **Fix:** a `check` workflow on every PR and push.
- **A-16 — No release mechanism.** fixed; the `v1.0.0` backfill is **question Q5**.
  - **Inspected:** the `v1.0.0` release has no assets, and installing means copying the folder by hand.
  - **Fix:** `tools/package-skill.py` builds a deterministic `.skill` per skill. The `release` workflow validates the version against the stamps and `CHANGELOG.md`, runs the checks, packs, attests and releases.
- **A-17 — No changelog in the repository.** fixed.
  - **Inspected:** the `v1.0.0` notes exist only on GitHub.
  - **Fix:** `CHANGELOG.md` starts at 1.0.0, copied from those notes.
- **A-18 — Tags are not protected.** **question Q6** (settings belong to the principal, decisions.1).
  - **Inspected:** `gh api repos/hooman/hooman-method/rulesets` returns `[]`, and immutable releases are off. A tag can be moved or deleted.
- **A-19 — The license doesn't suit code.** **question Q7**.
  - **Inspected:** `LICENSE` is CC BY 4.0, and now covers `tools/*.py` and the workflows too. Creative Commons advises against its licenses for software.
- **A-20 — `SKILL.md` has no room left.** **question Q4** for the candidate rules.
  - **Inspected:** it is 118 of its 120 lines, so no rule can be added without pruning.
  - **Inferred:** practice since `v1.0.0` produced four candidates, each with its friction event, so they pass T4. They are listed under Q4. The fourth was added after the audit, when issue #1 was closed.
- **A-21 — A second version string in the skill.** fixed.
  - **Inspected:** the skill's description says "(v1.0, Git and code projects)", which no check compared with the revision stamp.
  - **Fix:** the packer checks that it agrees with the stamp's major.minor.

- **A-23 — The roadmap's milestones and success measures, scored.** kept.
  - **Inspected:** of the open milestones, "pilot against a method project, a multi-repository software project, and a non-Git knowledge project" is two-thirds under way. This repository is the method pilot, and the capnproto-swift workspace (three repositories of its own) is the software pilot, at `0.3.0` released. The knowledge vault has not started; C2 puts it next.
  - **Inspected:** "canonical identity documents never change as a side effect of automation" held in this audit. Auto mode refused the agent's commit of `.agents/guarded-paths`, so that commit is the principal's.
  - **Inferred:** the measures need no rewording yet.
- **A-24 — A version string nothing checks.** fixed.
  - **Inspected:** `hooman-method-context.md` named the revision in prose, outside both checks.
  - **Fix:** it now points to the stamp in `SKILL.md`, as `AGENTS.md` does.

### The comment standard drafted in this PR

- **A-22 — The comment standard has not been tested yet.** **question Q3**.
  - cr.4 needs a clean-room run: a separate agent that reads only the standard and capnproto-swift at `3255db7` must find both #22 defects.
  - The private project's design is the concrete form: a planted fixture, a scorer, and a fresh agent that never grades its own run.

## Insights from a private Swift project

That project is private and unpublished. Only general patterns are taken, with no names, paths or ids.

| # | Pattern | Verdict | Where |
|---|---|---|---|
| P-1 | Every rule carries its reason, its evidence and how it is enforced | **adopt** | comment standard, Swift conventions |
| P-2 | Evidence labels: verified here, primary source, unverified | **adopt** in the conventions; for the agent rules (subst.5), **question Q4** | conventions |
| P-3 | Compiler settings: Swift 6 mode, the six upcoming Swift 7 features, strict memory safety, warnings as errors, `defaultIsolation(nil)` for libraries | **adopt** as the default. capnproto-swift reached the same set on its own, which makes two projects | Swift conventions, note D |
| P-4 | Rules only a review can check, and fluency rules (say a convention once, tables over branches, minimum scope, expressions over statements, abstractions earn their place, fits on one screen) | **adopt** as review judgement, not as counts | Swift conventions, note E |
| P-5 | Literate clarity: comments are code (a wrong comment is a bug; a `TODO` names its issue; no commented-out code, no history in comments), contract callouts (`- Precondition:`, `- Complexity:` …), every public declaration documented with a summary that carries the contract | **adopt** the first two. Documenting every public declaration conflicts with capnproto-swift, which leaves that lint off: **question Q3** | comment standard |
| P-6 | A review skill with evals: a planted-defect fixture, a recall scorer, run by a fresh agent that never grades its own run | **adapt** as cr.4. The skill itself is **deferred** under T5: the manual pass has run once, so it hasn't hurt yet | comment standard |
| P-7 | Gate markers that tie a review verdict to the commit it read, checked by a script | **deferred**. Project-level, for capnproto-swift item 4. For checkpoints (cp.2), part of Q4 | workspace proposals |
| P-8 | A session-close ritual: capture only what already cost something, phrased trigger-first, and send it to the document that holds that kind of knowledge | **adapt**. It matches the contract's session close and T4; the trigger-first phrasing is part of Q4 | Q4 |
| P-9 | Carry-over in layers: the general method in one source, each project keeping its specifics; extract on the second user; "enforce, don't remind" | **kept**. It is how this repository already relates to projects, and verify.2 | none |
| P-10 | A coverage floor that only rises; a release guide an agent can follow; docs checked before a release | **deferred**. Project-level | capnproto-swift proposals |
| P-11 | Test names as raw identifiers (SE-0451); `package` access in place of `@testable` | **adopt as an option**. capnproto-swift uses `@testable` and plain names | Swift conventions, note A |

## Questions for the principal

1. **Q1 — Version.** This PR adds files and changes reference documents, but no agent rule. My recommendation is `v1.1.0`, proposed in the stamps commit.
   - **What depends on the number,** so a different answer is one commit: the stamp lines in the three skill files, the description's `(v1.1, …)`, the `CHANGELOG.md` heading, and README's "each release from `v1.1.0`".
   - **The contract stays at `v1.0.0` on purpose:** it is revised separately, and its text did not change.
2. **Q2 — Design-stance roles.** The proposed mapping:
   - "Chat surfaces candidates as a design forms" becomes "in the explore and decide stances, the session surfaces candidates".
   - "The Executor's R1 output names candidates" becomes "in the build stance, the draft PR's design step (checklist step 1) names the candidates noticed and whether each meets the threshold".
   - Confirm it or reword it.
3. **Q3 — Comment standard.**
   - Where it lives: here (recommended), or in capnproto-swift.
   - DocC sections and documenting every public declaration, project by project. My recommendation: the shared rule is that a required summary carries the contract, and each project decides whether a lint requires one.
   - The go to spawn the clean-room test agent (A-22).
4. **Q4 — Candidate agent rules from practice.** None are added, since `SKILL.md` is full (A-20):
   - a guarded change ships with a one-command apply script. The friction: on 2026-11-26 the principal kept switching to the agent's worktree to apply patches.
   - verify.3 also requires checking that the control actually applied. The friction: on 2026-11-27 a formatter reflow made a text-match control silently not apply.
   - evidence labels in subst.5.
   - checkpoint evidence that names the commit it read.
   - a change to an existing test, or a deleted or weakened assertion, is its own commit with its reason, kept apart from the fix. A mechanical check could enforce it. The friction: on 2026-11-27, capnproto-swift #22 had to change an earlier answer key whose expected value was the bug itself (`09d1340`). Kept separate, the change could be reviewed; inside the fix, it would have hidden a weakened test. Issue #1 proposed the same check.
5. **Q5 — Backfill.** Attach a `.skill` to the published `v1.0.0` release? It changes a published release; my recommendation is no, and let `v1.1.0` be the first release with one.
**Later, a second batch** (decisions.1 asks at most five at a time):

6. **Q6 — Tag protection.** A ruleset that makes `v*` tags immutable, as capnproto-swift has.
7. **Q7 — License for code.** For example, MIT for `tools/` and `.github/`, with CC BY 4.0 kept for the docs.
