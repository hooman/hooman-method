# Hooman reboot — implementation plan

Status: **T1 complete; T2 ready**  
Specification: [`spec.md`](spec.md)

## Architecture direction

Keep the portable method independent from runtime mechanics. The supporting harness should have:

1. **Neutral core:** entry assessment, freshness policy, tranche envelope, authority policy, state transitions, checkpoints, and result schema.
2. **Frontend adapters:** Codex first; spoken, mobile, and other chat surfaces later.
3. **Source adapters:** filesystem and Git first; then project systems only when they are authoritative for a pilot.
4. **Execution adapters:** current Codex agent and isolated local work first; other runtimes only after a demonstrated need.
5. **Evidence and checkpoint store:** inspectable local state with project-visible next actions; no opaque memory as sole truth.
6. **Evaluation harness:** deterministic fixtures plus transcript and outcome review for the entry, autonomy, interruption, and security scenarios.

Do not introduce a standalone scheduler, dashboard, agent-to-agent protocol, vector database, or general workflow engine. Use host capabilities behind adapters until a missing capability is proven.

## Tranche P1 — End-to-end local pilot

### Outcome

A selected project travels through assessment, envelope clearance, meaningful isolated execution, verification, checkpointing, and interruption recovery using Codex as the first host.

### Included

- Resolve project identity and detect missing or moved roots.
- Read project activity, repository state, and declared re-entry artifacts.
- Implement evidence-based entry-mode selection.
- Generate concise orientation and a structured execution envelope.
- Execute one reversible local task against a fixture or approved pilot worktree.
- Verify the resulting environment state.
- Persist and reload a checkpoint.
- Exercise A1, A4, A5, A6, A7, A8, and A10 from the specification.

### Excluded

External writes, recurring automation, custom UI, voice transport, broad connector installation, canonical Hooman edits, and production portfolio rollout.

### Proof

- Automated scenario results for deterministic routing and state transitions.
- A recorded Hooman reboot assessment that detects the current path mismatch.
- A completed local execution with validation and no routine approval requests.
- A forced-interruption demonstration that resumes from the stored checkpoint.
- A fake non-Codex frontend adapter proving the core has no Codex dependency.

## Tranche P2 — Three-project calibration

### Outcome

The harness selects useful modes and tranche sizes across three distinct project shapes without producing redundant project truth.

Pilot set:

- `hooman-method` — method and durable-document work.
- Heddle workspace — multi-repository software work.
- NAIMOR Knowledge Vaults — non-Git knowledge work.

Add only the source adapters and freshness policies each pilot actually requires. Record false catch-ups, missed stale evidence, human corrections, interruptions, validation failures, and review time. Revise routing and envelope policy from observed errors.

### Proof

- At least two warm/direct and two re-entry/reboot trials.
- One substantial execution per project type.
- No automatic canonical-document changes.
- Review of every failed or disputed trajectory, not scores alone.
- A deletion list for rules, fields, or artifacts that failed to earn their cost.

## Tranche P3 — Exception-driven operation

### Outcome

Reliable repeated checks reduce chores without creating a status-report treadmill.

Add session-close proposals, opportunistic checkpoints, and one portfolio exception scan using native host automation. Add project-specific recurring checks only where volatility or operational responsibility justifies them. Run unattended work read-only until its evidence and false-positive record justify a wider envelope.

### Proof

- Automation reports only changes, stale sources, blocked work, or required decisions.
- Every recurring run names its authority ceiling and next review date.
- Unchanged projects produce no human-attention demand.
- First unattended results are manually reviewed before recurrence is trusted.

## Tranche P4 — Spoken frontend

### Outcome

The stable interaction contract works through natural spoken conversation without weakening approval, evidence, or recovery semantics.

Implement voice as a frontend adapter using a supported realtime transport. Delegate long reasoning and execution to the same backend harness rather than embedding project logic in the realtime session. Preserve concise spoken summaries alongside durable structured records.

### Proof

- Acceptance scenario A9 passes with interruption, correction, approval, exception, and completion turns.
- A spoken session can resume a tranche started in Codex and vice versa.
- The human can request evidence drill-down without hearing a full diff or report.
- Transcription errors cannot silently authorize consequential actions.

## Tranche P5 — Optional portfolio surface

Build an inline or standalone portfolio view only if the native project picker and exception automation still impose observed navigation cost. The surface is a projection of core state, never a second project database.

## Evaluation and trust calibration

For each tranche, preserve the input state, selected envelope, action trace, final environment state, validation evidence, human correction, and resumption result. Use deterministic graders for paths, state transitions, permissions, files, and tests; use human review for whether orientation and tranche sizing were actually useful.

Autonomy widens by demonstrated zone:

- New or disputed zone: reconnaissance and proposal.
- Proven local reversible zone: substantial isolated execution plus validation.
- Proven recurring zone: unattended read-only operation.
- External or irreversible zone: explicit transaction-specific authority regardless of general reliability.

## Rollback posture

- Method documents remain unchanged until separately approved.
- Runtime work occurs in an isolated repository/worktree.
- Checkpoint schema changes are versioned and migratable.
- Host adapters can be removed without altering neutral project records.
- Any automation can be disabled without losing project-visible next actions.
