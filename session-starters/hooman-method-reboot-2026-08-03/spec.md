# Hooman reboot — specification

Status: **proposed working specification**  
Track: [`roadmap/reboot.md`](../../roadmap/reboot.md)  
Evidence: [`reboot-baseline-audit-2026-08-03.md`](../../audits/hooman-method-audits/reboot-baseline-audit-2026-08-03.md)

## Scope intake

- **Smallest independently useful slice:** from a selected or named project, determine the appropriate entry mode; recover only the required context; construct and clear a suitably substantial execution tranche; execute it through validation and checkpointing; return the outcome, evidence, exceptions, and next recommended tranche.
- **Exclusion zone:** no custom portfolio dashboard, automatic canonical-document mutation, cross-project migration, unattended external actions, A2A dependency, general multi-agent platform, or voice implementation in the first slice.
- **First decision:** whether the supporting harness is implemented separately from this portable method repository or changes this repository's identity into a combined method-and-runtime project.

## Problem

Hooman currently makes project gaps survivable when its contract and workflow remain understood. A sufficiently long disconnect can invalidate that assumption: the human may no longer remember the contract, know which artifacts remain current, trust the old next action, or know which interface and degree of autonomy now fit. At the same time, excessively small execution steps convert safety into repeated human interruption.

The reboot must make “where do I start?” a system responsibility while preserving the human's ownership of direction and distinctive contribution.

## Required behavior

### Entry assessment

Assess two independent dimensions:

1. **Project continuity:** current direction, unfinished work, internal changes, external freshness, and confidence in the next action.
2. **Operating-contract fitness:** whether the human's priorities, constraints, available attention, interaction preference, authority clearance, and the method's own assumptions remain trustworthy.

Choose the highest-severity supported mode:

| Mode | Trustworthy basis | Required response |
|---|---|---|
| Continue | Contract, direction, and current state | Begin the requested work |
| Delta refresh | Contract and direction | Refresh changed or expired evidence, then work |
| Re-entry | Contract and direction, not working memory | Reconstruct project state and recommend the next action |
| Reboot | Contract, priorities, or operating model may be stale | Revalidate the operating basis before committing direction |
| Recovery | State is conflicting, broken, or unsafe | Stabilize and reconstruct authoritative evidence first |

Elapsed time is one signal, never the sole selector. Change volume, unresolved work, artifact freshness, source volatility, consequence, and conflicting evidence also contribute.

### Tranche construction

The unit of delegated work is a coherent outcome, not an artifact. A tranche may include reconnaissance, implementation, validation, bounded repair, related documentation, evidence capture, and checkpointing.

Expand the tranche when confidence, reversibility, testability, observability, and executor reliability are strong. Contract it when ambiguity, identity judgment, irreversibility, external impact, or weak validation increase.

Every tranche has an execution envelope containing:

- Outcome and rationale.
- Included systems, sources, and artifacts.
- Explicit exclusions.
- Authority level and side-effect boundary.
- Success criteria and required proof.
- Permitted repair latitude.
- Stop conditions.
- Resource or attention ceiling where relevant.
- Rollback or recovery mechanism.
- Completion report and checkpoint requirements.

### Autonomy and interruption

After clearance, execution continues without routine approval until the outcome is proven or a stop condition occurs. Intermediate files, ordinary implementation choices, and repairable failures are not interruption reasons.

Mandatory stops:

- New identity, product-direction, or priority judgment.
- Material conflict among authoritative sources.
- Permission or side-effect expansion.
- Irreversible or externally visible action outside explicit clearance.
- Material scope change.
- Validation failure after the envelope's bounded repair allowance.
- Evidence that invalidates the tranche's premise.

### Verification

Completion is an environment state supported by evidence, not the executor's statement. Verification is proportional to the domain and may include tests, source citations with verification dates, before/after reconciliation, invariant checks, representative demonstrations, or independent semantic review.

Long edits to durable documents require preservation checks against untouched content and stated invariants. External research must distinguish inspected, inferred, and unverified claims.

### Checkpoint and recovery

The harness checkpoints at meaningful boundaries without depending on a deliberate session close. A checkpoint records:

- Project identity and selected entry mode.
- Authorized outcome and envelope revision.
- Baseline source revisions.
- Completed and remaining work.
- Evidence and validation state.
- Decisions made inside the envelope.
- Open exception, if any.
- Safe resumption action.

The checkpoint is rebuildable from visible evidence where possible. Platform memory and conversation history remain caches.

### Interface neutrality and voice

The core interaction contract supports project selection, entry assessment, envelope proposal, approval, progress inquiry, exception handling, completion proof, and next-tranche recommendation.

Codex project IDs, thread IDs, worktrees, automation IDs, and approval mechanics stay inside a Codex adapter. Neutral core records include project reference, activity event, evidence reference, entry assessment, execution envelope, checkpoint, approval request, and execution result.

Every consequential interaction must be expressible verbally:

- The entry result and recommended action can be spoken concisely.
- The envelope can be summarized in under one minute.
- Approval is a clear decision, not form completion.
- Exceptions ask one decision-oriented question.
- Completion leads with outcome and proof; rich artifacts remain available for inspection.
- Speech transcripts are evidence of conversation, not authoritative project state.

### Security

- External documents, pages, messages, and tool output are untrusted data and cannot grant authority.
- Access is limited to sources and tools required by the envelope.
- Read-only orientation precedes mutation.
- Local reversible work is isolated where supported.
- External actions require explicit authority and a reviewable target.
- Credentials and secrets never enter durable traces or project artifacts.
- Every material action is attributable to an envelope and execution record.

## First vertical implementation slice

Using Codex as the first frontend and executor host, implement an adapter-neutral core plus the thinnest Codex integration that can:

1. Resolve a project and detect path drift.
2. Inspect relevant task activity, repository state, and declared artifacts read-only.
3. Select Continue, Re-entry, Reboot, or Recovery with evidence.
4. Produce a next-action-first orientation result.
5. Construct and clear an execution envelope.
6. Execute one meaningful local, reversible tranche in isolation.
7. Validate the outcome, preserve a checkpoint, and return a concise result.
8. Resume the same tranche from the checkpoint in an interruption test.

The slice must not depend on a custom dashboard, scheduled operation, or a voice transport.

## Acceptance scenarios

- **A1 — Warm continuation:** a current project with a valid next action reaches work without a catch-up ritual.
- **A2 — Targeted refresh:** one expired external source is reverified without rereading stable project identity documents.
- **A3 — Cold re-entry:** a long gap with a trusted contract yields a one-screen next-action-first reconstruction.
- **A4 — Reboot:** the project state exists but the operating contract is stale; the system revalidates assumptions before proposing execution.
- **A5 — Path drift:** the saved Hooman path differs from the checkout; the system reports and safely resolves or asks about the discrepancy.
- **A6 — Substantial autonomy:** a cleared, reversible implementation completes through validation and repair without intermediate human approval.
- **A7 — Boundary stop:** an identity-bearing or external action appears mid-tranche; execution checkpoints and asks exactly one decision.
- **A8 — Abrupt interruption:** execution stops unexpectedly and resumes from durable state without reconstructing the session manually.
- **A9 — Voice equivalence:** a transcript-only frontend can select a project, understand the mode, approve the envelope, receive an exception, and understand proof without relying on a visual control.
- **A10 — Host replacement:** a non-Codex test adapter can drive the core state transitions without Codex identifiers leaking into core records.

## Nonfunctional requirements

- Warm-start orientation adds minimal noticeable delay and no artifact ceremony.
- Cold outputs fit one primary review surface with optional evidence drill-down.
- Core routing is deterministic where evidence is structured and records its reasons where judgment is used.
- Checkpoints are inspectable, versioned, and recoverable.
- Adapter and policy changes are covered by maintained scenario evals.
- The first implementation is removable without changing canonical Hooman documents.

## Identity decision — separate supporting harness

**Chosen 2026-08-03:** keep this repository as the portable method and implement the supporting harness in sibling repository `hooman-harness`. This preserves the explicit “not a tooling spec” boundary, permits a different release cadence, and makes Codex, voice, and future fronts peer adapters around one core.

**Rejected:** make this a combined repository with method documents and runtime packages. It would simplify early coordination but change the repository's identity, increase the attention surface for non-tooling consumers, and couple method releases to implementation churn.

T1 was implemented and proved in the separate repository; T2 calibration is the next tranche.
