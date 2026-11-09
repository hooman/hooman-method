# Hooman reboot

**Next action:** Fold the [2026-11-09 revision](#revision-2026-11-09-the-environment-moved) into the specification (four axes, design sessions, context boundaries); then run read-only entry assessments for Hooman, Heddle, and NAIMOR Knowledge Vaults; review the three mode decisions together; then clear one substantial T2 pilot tranche.

Lifecycle: **in-flight**  
Started: 2026-08-03  
Purpose: move Hooman from a manually maintained delegation method to a frontend-neutral, interruption-resilient operating system for substantial LLM-assisted work, without surrendering human direction or creating process for its own sake.

## Why this track exists

After a long disconnect, re-entry failed one level above the project: the principal's own contract, the available interaction model, and the answer to “where do I start?” all required reconstruction. The existing method handles project re-entry but assumes its operating contract still fits. The reboot adds contract fitness, dynamic tranche sizing, bounded autonomy, opportunistic recovery, and interchangeable human frontends.

Observed friction justifying this track:

- The principal could not cheaply recover the first action after the gap.
- Manual, artifact-by-artifact execution would create excessive attention and handoff cost.
- Long useful execution needs explicit guardrails and exception-based interruption.
- The system must eventually be operable through verbal conversation.
- The initial Codex project entry points at a path that no longer contains the checkout.
- The globally installed assistant skill and repository copy carry different version stamps.

## Linked working set

- [Reboot baseline audit](../audits/hooman-method-audits/reboot-baseline-audit-2026-08-03.md)
- [Specification](../session-starters/hooman-method-reboot-2026-08-03/spec.md)
- [Plan](../session-starters/hooman-method-reboot-2026-08-03/plan.md)
- [Tasks](../session-starters/hooman-method-reboot-2026-08-03/tasks.md)
- [HumanLayer candidate assessment](../../hooman-harness/aside/humanlayer-evaluation-2026-08-04.md)

## Milestones

- [x] Reconstruct the repository and ecosystem baseline.
- [x] Define reboot as distinct from ordinary cold re-entry.
- [x] Specify tranche sizing, autonomy, recovery, and frontend neutrality.
- [x] Decide the supporting harness's repository boundary.
- [x] Implement and prove the first end-to-end vertical slice.
- [ ] Pilot against a method project, a multi-repository software project, and a non-Git knowledge project.
- [ ] Add exception-driven recurring checks only after the manual flow is reliable.
- [ ] Add a voice frontend only after the neutral interaction contract survives the pilots.

## Success measures

- A warm project reaches useful work without a ceremonial catch-up.
- A stale project produces a one-screen, next-action-first re-entry result.
- A reboot detects that the operating contract itself needs revalidation.
- A cleared tranche completes a substantial outcome without routine human interruption.
- An interrupted tranche resumes from durable evidence and a safe next step.
- Canonical identity documents never change as a side effect of automation.
- The same core behavior can be driven from Codex, text chat, or voice through adapters.

## Exclusion zone

No custom dashboard, cross-project rollout, unattended external mutation, automatic canonical-document editing, A2A dependency, or wholesale artifact migration belongs in the first implementation slice.

## Revision 2026-11-09: the environment moved

Decided by the principal, 2026-11-08/09, from a review run in the Heddle workspace. **The reboot continues, and absorbs this revision.** When it ships, the method text is a reset: it is written fresh around the axes below, and carries no version or change history over from v0.8.x.

### What changed since 2026-08

- **Frontends merged.** Chat and Cowork are merging in Claude Desktop (from 2026-09-16), with Cowork running in the cloud by default (from 2026-10-06). Claude Code can be driven remotely from the apps and the web, and tasks can be dispatched from a phone. Every surface now has tools, so "a chat surface without tools" no longer exists.
- **Sessions talk to each other.** A session can list other sessions, including ones on other machines or on the web, and send them messages. Hand-offs no longer need a person to carry a brief between products.
- **Planning and recurring work are products.** Cloud planning runs parallel exploration with a critique pass; scheduled tasks run cloud sessions on a schedule or a repository event.
- **Agent memory curates itself.** "Dreaming" is an offline job that checks an agent's notes against its transcripts, corrects them, builds linked wikis and decides what is preloaded next time. It writes a new store and leaves the old one untouched, and has no human review step.
- **The human role is moving from approving actions to setting intent and reviewing outcomes.** People make most planning decisions and agents most execution decisions; supervision effort concentrates in planning; and the reasons behind a delegation must be stated up front.

This confirms the reboot's direction (frontend neutrality, bounded autonomy, artifacts over memory) and adds to it.

### The four axes (accepted)

The method is organised around four axes instead of a split by product surface:

| Axis | Meaning | Where the reboot already has it |
|---|---|---|
| **Stances:** explore, decide, build, review | A session or tranche declares its stance; any frontend can take any stance. Reconnaissance and mutation survive as the build stance's permission level | Entry modes and execution tranches cover *build*; *explore* and *decide* are new |
| **Context boundaries** | Each session states what it may and may not know. A clean room, where a session must not have read certain sources, is the general case, not a special one | Security's "access limited to sources the envelope requires" covers tools; this extends it to knowledge |
| **Decision rights** | One-way calls go to the principal, asked plainly: the question, one real example, what each option does, at most five at a time. Reversible work is done and then logged | The mandatory stops; "exceptions ask one decision-oriented question" |
| **Records** | The repository is truth. Agent memory, dreams and transcripts are caches, and change the repository only through reviewed changes | "Visible project artifacts override platform memory"; checkpoints |

### Exploration and design sessions

The reboot specifies execution tranches; design work needs its own shape:

1. **Frame.** The principal states the question and what a good answer would let them decide.
2. **Diverge.** Parallel explorers, each with a deliberately different brief or set of sources. Research is a delegated step with sources cited.
3. **Critique.** A separate agent whose only job is the opposing case.
4. **Converge.** One round of calls to the principal.
5. **Record.** A track entry or decision in the repository, in the principal's words where the call was theirs.

### Recurring checks: repository dreaming

The milestone "exception-driven recurring checks" gets its first candidate. A scheduled routine reads what merged across a project's repositories, finds written claims those changes made false, and proposes corrections as pull requests. It never rewrites directly, reads repository records only (never session transcripts), and an independent review agent checks each pull request before the principal merges. The Heddle workspace is designing it as its multi-repository pilot.

### Sources

- Anthropic, "The components of agent memory" (2026-11-06): <https://www.anthropic.com/research/components-of-agent-memory>
- Anthropic, "Measuring AI agent autonomy in practice": <https://www.anthropic.com/research/measuring-agent-autonomy>
- Anthropic, "How Claude Code is used in practice": <https://www.anthropic.com/research/claude-code-expertise>
- "The Work Behind Delegation: A Framework for Supervising AI Coding Agents", arXiv 2609.24234: <https://arxiv.org/abs/2609.24234>
- "Anticipatory Human Oversight of Agentic AI", arXiv 2609.24242: <https://arxiv.org/pdf/2609.24242>
- Claude Code scheduled tasks: <https://code.claude.com/docs/en/routines>
- Frontend changes (secondary): <https://www.clickforest.com/en/blog/claude-desktop-explained>; <https://simonwillison.net/2026/Feb/25/claude-code-remote-control/>; <https://claudefa.st/blog/guide/mechanics/cross-session-messaging>
