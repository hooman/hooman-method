# Hooman reboot baseline audit — 2026-08-03

contract: C-A

This audit links to [`session-starters/hooman-method-reboot-2026-08-03/`](../../session-starters/hooman-method-reboot-2026-08-03/) and records the evidence basis for the reboot. It changes no canonical method document.

## Baseline findings

1. **The central purpose remains valid.** `hooman-notes.md` already identifies re-entry, review cost, persistent decision memory, recoverability, and human judgment as the method's optimization targets. The reboot extends that premise rather than replacing it.
2. **The current method assumes the contract survives the gap.** Its re-entry mechanisms reconstruct project state, but there is no operational entry mode for revalidating the principal's contract, interaction assumptions, or current autonomy preference.
3. **The existing execution granularity taxes attention.** Every dispatched task becomes a brief, mutation requires every diff before writing, and session closure depends on a deliberate ritual. These are safe at low trust but do not yet describe how proven, reversible work earns a larger cleared tranche.
4. **Abrupt interruption is only partially handled.** T6 protects a next-action line when the human notices a session is ending. A supporting harness also needs opportunistic checkpoints that do not rely on the human or assistant anticipating the interruption.
5. **The role boundary is too attached to interaction form.** Chat and Executor remain useful logical responsibilities, but the runtime must express them as authority and capability boundaries so Codex, another agent runtime, or a voice frontend can implement them differently.
6. **The ecosystem now supplies much of the substrate.** Codex provides project-scoped threads, worktrees, goal-oriented execution, plugins, automations, mobile continuity, and broad knowledge-work tooling. Agent Skills provide portable instruction packages. MCP Apps can provide an inline UI later. OpenAI's Realtime and Agents SDKs support spoken sessions, tools, approvals, guardrails, and alternative transports.
7. **Long-horizon delegation requires stronger verification than fluent summaries.** Current research reports sparse but severe semantic degradation during repeated document editing. Agent eval guidance likewise emphasizes final environment state, traces, and maintained evaluation suites rather than trusting the agent's own completion statement.
8. **Security must be part of the execution envelope.** Retrieved pages, messages, documents, and tool output can contain hostile instructions. External content is data; authority comes only from the human, project policy, and the cleared envelope.
9. **The method repository lacks its own live re-entry surface.** Before this reboot package it had no explicit Hooman governance marker, roadmap, active cycle, or next-action artifact, despite teaching those mechanisms downstream.
10. **Concrete drift already exists.** The Codex project registry points at `/Volumes/Data/Developer/hooman-method`, while this checkout is `/Volumes/Data/Developer/(commons)/hooman-method`. The installed skill header says v0.8 while the repository skill says v0.8.1. A project doctor and projection check therefore solve observed—not anticipated—friction.

## Stable identity versus reboot candidates

### Preserve

- One principal owns priorities, constraints, and final decisions.
- Durable visible artifacts beat opaque memory.
- Re-entry leads with the next concrete action.
- Reconnaissance and mutation have different safety profiles.
- Canonical identity documents require deliberate human commitment.
- New rules and tools must name the friction they remove and continue earning their cost.

### Reconsider or extend

- Cold re-entry as the deepest normal entry mode.
- Human-visible artifact production as the unit of delegated work.
- Review every diff as the universal mutation rule.
- Session-close discipline as the only checkpoint mechanism.
- Chat and Executor as interface-specific roles rather than logical authority boundaries.
- The method repository's current docs-plus-skill boundary versus a separate supporting-harness implementation.

## Friction ledger for proposed bindings

| Proposed binding | Observed friction | Constraint |
|---|---|---|
| Entry-mode detector | The principal could not tell where to start after the gap | Time alone cannot select the mode |
| Project/path doctor | Saved project path no longer resolves to the checkout | Report before repairing; stable project identity cannot be only a path |
| Tranche envelope | Trivial execution steps multiply human handoffs | Stop only at declared exceptions |
| Autonomy governor | High-confidence work should run substantially farther | Authority never expands implicitly |
| Opportunistic checkpoint | Abrupt endings defeat deliberate close rituals | State must be rebuildable and resumable |
| Proof-of-done verifier | Long delegated edits can silently degrade content | Judge outcome and preserved invariants, not activity |
| Frontend adapter boundary | Codex is useful now; voice and other fronts are required later | No Codex identifier in core project state |
| Freshness engine | Internal and external facts decay at different rates | Refresh by class and invalidation trigger, not blanket rereading |

<sources>
- [primary] [`hooman-notes.md`](../../hooman-notes.md) — purpose, re-entry rationale, failure map, candidate bindings, and open questions.
- [primary] [`hooman-contract.md`](../../hooman-contract.md) — current escalation, scope intake, session close, and standing triggers.
- [primary] [`skills/hooman-assistant/`](../../skills/hooman-assistant/) — current roles, brief granularity, output contracts, artifact rules, and canonical protections.
- [primary] Git history through `5a9593d` — the concentrated May–June evolution, final June 19 maintenance commit, and absence of later project checkpoints.
- [primary] Codex project and task metadata inspected 2026-08-03 — saved-project path drift, project-scoped task timestamps, and available project/thread/automation capabilities.
- [primary] [OpenAI: Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/) — project threads, worktrees, skills, automations, and sandboxing.
- [primary] [OpenAI: Codex-maxxing for long-running work](https://openai.com/index/codex-maxxing-long-running-work/) — current long-running-work guidance.
- [primary] [OpenAI: Codex for knowledge work](https://openai.com/index/codex-for-knowledge-work/) — current use across research, data analysis, artifacts, and workflow automation.
- [primary] [OpenAI: Automations](https://openai.com/academy/codex-automations/) — scheduled and same-thread recurring work.
- [primary] [Agent Skills specification](https://agentskills.io/specification) — portable skill package shape.
- [primary] [MCP Apps](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/) — production inline interactive interfaces.
- [primary] [MCP Tasks](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks) — experimental durable task state; unsuitable as a first-slice dependency.
- [primary] [OpenAI Agents SDK: Voice Agents](https://openai.github.io/openai-agents-js/guides/voice-agents/) — spoken sessions, tools, approvals, guardrails, and transport abstraction.
- [primary] [OpenAI: Designing agents to resist prompt injection](https://openai.com/index/designing-agents-to-resist-prompt-injection/) — external-content threat model.
- [primary] [GitHub Spec Kit](https://github.github.com/spec-kit/) — current spec / plan / tasks workflows and cross-agent integrations.
- [primary] [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — selective context construction for long-running agents.
- [primary] [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — outcome, trace, grader, and maintained-suite evaluation model.
- [primary] [Microsoft Research: LLMs Corrupt Your Documents When You Delegate](https://www.microsoft.com/en-us/research/publication/llms-corrupt-your-documents-when-you-delegate/) — long-horizon semantic degradation risk.
- [secondary] [Designing meaningful human oversight in AI](https://link.springer.com/article/10.1007/s43681-026-01147-7) — distinction between machine operative agency and human evaluative agency.
</sources>

<opposing>
The strongest case against the proposed harness is that the Codex product is rapidly absorbing project continuity, goal execution, mobile control, automation, plugins, and knowledge-work features. A bespoke layer could duplicate features that soon become native, increase maintenance burden, and turn Hooman into the process-as-avoidance failure it warns about. A lighter alternative is to update the skill and rely entirely on Codex projects, task history, and automations. This case is strong enough that the first implementation must remain a thin policy and evidence layer, use adapters around native capabilities, and prove value on real projects before any dashboard, scheduler, or general agent platform is built.
</opposing>

<implications>
The reboot should preserve Hooman as the portable method and add the smallest supporting harness that enforces entry assessment, substantial cleared tranches, checkpoint recovery, evidence, and interface neutrality. Codex should be the first adapter and execution host. The first implementation should exercise a complete vertical path on real projects, while scheduled operation, a custom UI, voice transport, and interoperability protocols remain later adapters. The implementation-home decision is identity-bearing and therefore remains with the principal.
</implications>

<uncertainty>
- Codex exposes project and thread metadata to the current assistant, but the durability and public availability of those hooks for a distributable plugin are unverified — resolve with a local capability probe before implementation architecture is locked.
- The correct persistence location for cross-frontend checkpoints is unsettled — resolve by testing local private state plus project-visible next action across the three pilots.
- Voice SDKs support the required interaction mechanics, but a good spoken approval and review experience remains unproven — resolve only after the text interaction contract is stable.
- The correct repository boundary for the supporting harness is undecided — principal decision required before T1.
</uncertainty>
