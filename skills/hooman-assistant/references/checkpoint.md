# The draft PR as checkpoint

v1.1.1 (2026-11-28) · part of the `hooman-assistant` skill · load when starting, resuming, or
reviewing a tranche of delegated work (tranche.1–5).

A tranche is one outcome. Its checkpoint is a **draft pull request**, opened before any code is
written. Its description holds the envelope and a checklist. The PR is what survives when a
session ends without warning. A cold agent must be able to find it, judge how far it got, and
finish it on the same branch. In one acceptance run (A8, 2026-11-21: one model, the cut right
after a checkpoint push) a cold agent did exactly that on stock GitHub. A cut in the middle of a
push is untested.

## Description template

Copy it verbatim. Leave no section empty: write `none`.

```markdown
## Envelope

- **Outcome:** <the environment state that will be true when this is done>
- **Why:** <the reason, in one line, so a resuming agent can judge trade-offs>
- **In scope:** <files, systems, sources>
- **Excluded:** <what must not change>
- **Proof:** <the gates or evidence that show the outcome, and where they run>
- **Stop conditions:** <what ends the tranche with a question instead of a workaround>
- **Authority:** <side effects cleared: pushes, external services, installs; "none beyond this branch">

## Checklist

- [ ] 1. Design: approach written here, before any code
- [ ] 2. <step>
- [ ] N. Summary with evidence; side effects undone or listed
```

## Rules

- cp.1 — Open the draft PR first, from an isolated branch and checkout. Push the design (step 1)
  before writing code. The design is the expensive thinking; it must survive.
- cp.2 — After each step: commit, push, then tick the box, with a one-line evidence note under it
  (commit, command, or log line). Never tick a box ahead of its push.
- cp.3 — Only pushed state counts. Push often enough that a lost local checkout costs at most the
  step in progress.
- cp.4 — **Resuming:**
  - find the PR from durable state: open draft PRs, branches, the next-action line
  - re-verify what the ticked boxes claim before building on them
  - correct the record where it is wrong
  - continue the same branch
  - open a second PR only with a stated reason
- cp.5 — At a stop condition: checkpoint, then ask one question in the PR and in the session.
- cp.6 — The PR stays a draft and unmerged. The principal marks it ready and merges, and the
  merge is the commit (decisions.4).
- cp.7 — Projects that require DCO: the agent's commits are not signed off. The principal adds
  the sign-off after review (`git rebase --signoff`). The failing DCO check is expected until
  then.
