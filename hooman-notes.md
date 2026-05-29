# Hooman — Companion: Rationale, Provenance & References

*The why behind the operating guide (**`hooman-guide.md`**, same gist): why the method exists, what's distinctive, where it sits in the ecosystem, verified references, the tool-binding roadmap, and open questions. Read the guide to operate; read this when you want the reasoning.*

**Canonical version:** <https://gist.github.com/hooman/5811ee3bb7c235573299400167403985>.

---

## The name

**Hooman** is eponymous — named for its author (GitHub: `hooman`) — because it is, for now, a single-user method, not a universal standard. Naming it after the author is honest about that scope.

The name does double duty. It quietly encodes the method's premise — a *human* in the director's seat, directing AI executors ("Hooman" ≈ "human", and the human-in-the-loop is the whole point). And it sidesteps two collision problems at once: the crowded ecosystem vocabulary (*workflow, skill, agent, constitution* are all taken) and the method's own internal terms (*brief, cycle, offload*). It namespaces the entire toolkit: the `hooman` skill, the future `hooman-workspace` repo, this gist.

**Rejected alternatives** (per naming rule 7):

- **homer** — the author's old dial-up-BBS handle. Rejected as the primary name: dominated by Homer Simpson and the Greek poet, and already used by existing dev tools (a self-hosted dashboard; a SIP-capture tool). Kept only as a sentimental nod here.
- **"Chat-First Project Development with LLMs"** — the descriptive working title through v0.4. Retired as the primary name. It still describes the method accurately and could serve as a public descriptive subtitle if the method is ever published for others.

The role labels **Chat** and **Code** are unaffected by this naming and remain an open question (see *Open questions*).

---

## Why this exists

Working on a non-trivial project with an LLM hits a predictable ceiling. A single conversation can't hold the project's full context. Detail work pollutes the conversation's attention budget. Decisions made in one session get re-derived in the next. The LLM serializes all reasoning through one context window, and the output reflects the limits of one model's first-pass thinking.

The conventional response — "use a more capable model" or "use a coding agent" — is partial. What actually works is **role separation with mechanical artifacts**: a high-level conversational assistant (*Chat*) that holds strategy and direction, a coding agent (*Code*) that handles investigation and implementation, and a set of artifacts in the project tree that survive across sessions and across handoffs to entirely new agents.

The method is portable — no specific project, no specific LLM, no specific tooling. Examples reference the Heddle project, where the approach was developed, but the structure transfers; Cap'n-Proto-for-Swift is the first non-Heddle project to exercise it.

---

## What's distinctive here

Most of this method is novel framing of patterns the LLM-tooling ecosystem has converged on independently: the orchestrator/executor split, plan-then-implement, project-root agent files, structured note-taking, sub-agent context isolation. What's genuinely distinctive — worth naming as contributions rather than reinventions:

- **The anti-bureaucracy guardrail.** Most methodologies accrete templates; very few have an explicit "must solve a real friction" rule as a precondition for adoption.
- **The offload test.** "Does this produce content / inventory / details? → executor. Does it produce direction? → conversational role." Sharper than the implicit splits in most multi-agent frameworks.
- **Glossary discipline as a gated artifact**, with naming rules that apply before a term is added.
- **The findings inbox** as an explicit standing log for drive-by observations, swept on schedule.
- **Doc-audience layering**, particularly the agent / human-leaning / hybrid split and the *entry-point docs are thin* companion rule.

These are the parts most worth formalizing for reuse outside one project.

---

## What this is not

- **Not a tooling spec.** It does not require any particular LLM, IDE, or platform. It works with whatever Chat-style assistant and whatever coding agent you have access to.
- **Not a coding methodology.** It governs *how you collaborate with LLMs*, not *how you write code*. Pair it with whatever engineering practices your project already uses.
- **Not a project-management methodology.** It is compatible with Agile, Shape Up, lazy-consensus, or whatever scheduling discipline your team prefers. It governs the *content* and *handoff* of work, not its *cadence*.
- **Not finished.** This is an evolving draft, distilled from one project's experience plus an ecosystem survey. Expect it to evolve.

---

## Ecosystem positioning & survey

The method was distilled from one project's practice (Heddle) plus a survey of the May 2026 AI-coding-agent ecosystem, triangulated across several independent LLM research tools to reduce single-source blind spots. Where it sits: it is a novel *framing* of patterns the ecosystem converged on independently — the orchestrator/executor split, plan-then-implement, project-root agent files (AGENTS.md), modular capability files (Skills / SKILL.md), the Model Context Protocol (MCP) for connecting agents to external systems, spec-driven tools (Spec-Kit, Kiro), and sub-agent context isolation. The distinctive contributions are listed under *What's distinctive*. The underlying research reports are kept in the author's archive, not published with the method.

*Source-integrity note:* the survey's distinct inputs were fewer than they appeared — verify source independence before treating any cross-tool "consensus" as strong. Lean on the *Verified references* below, which are checked against primary sources, rather than on the survey reports.

---

## Verified references

The ecosystem claims this method leans on were checked against primary sources (May 2026). This section resolves the former open question "Verification of ecosystem claims."

- **AGENTS.md is a Linux-Foundation-stewarded open standard.** *Verified.* The Linux Foundation formed the **Agentic AI Foundation (AAIF)** in December 2025, anchored by founding contributions: **MCP** (Anthropic), **goose** (Block), and **AGENTS.md** (OpenAI). Sources: [Linux Foundation press release](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation), [OpenAI](https://openai.com/index/agentic-ai-foundation/), [agents.md](https://agents.md/).
- **Adoption: 60,000+ open-source projects.** This is the figure stated by the AAIF / agents.md — consistent across sources, but **self-reported, not independently audited**. Cite it as such.
- **SKILL.md is cross-tool portable.** *Verified, with nuance.* The **Agent Skills** specification ([agentskills.io](https://agentskills.io/specification)) was released by Anthropic as an open standard (December 2025) and is compatible across Claude Code, OpenAI Codex CLI, Gemini CLI, OpenClaw, and OpenAI's Skills tool. Skills that adhere to the core SKILL.md format (YAML frontmatter `name` + `description`, plus a markdown body, with progressive disclosure of bundled files) are portable across tools without modification; tool-specific extensions are not guaranteed to carry over.

Also confirmed in passing: **MCP** was likewise contributed to the AAIF / Linux Foundation; the spec-driven tools **Spec-Kit** (GitHub: *constitution → specify → plan → tasks → implement*) and **Kiro** (AWS: `requirements.md` / `design.md` / `tasks.md`, with requirements in **EARS** notation — `WHEN <condition> THE SYSTEM SHALL <behavior>`) match the method's escalation shape and its use of anchors as a "constitution."

---

## From methodology to tooling

Each concept in the guide has an eventual **tool binding** — the encoded form that lets the rule run automatically rather than by discipline. As the method matures, the mapping fills in:

| Concept | Tool binding | Friction solved |
|---|---|---|
| Session modes | Auto-loadable instruction packs (e.g. Claude Skills, `agents.md`-compatible equivalents) | Mode context re-pasted by hand each session; mode discipline drifts when not in muscle memory |
| Cycle-brief R1 | Plan mode or equivalent read-only constraint | Code starts implementing during R1 despite the brief saying not to |
| Cycle-brief implement | Show-diff hooks, scoped tool allowlists | Unreviewed file writes; scope creep through broad tool access |
| Sub-agent roles (reviewer, auditor, implementer) | Configured sub-agent definitions with tight tool scopes | Ad-hoc dispatch with inconsistent isolation; sub-agents over- or under-scoped per session |
| Findings inbox | A standing log file today; eventually a structured-note tool | Drive-by findings lost when not captured; conversation drift when absorbed inline |
| Glossary discipline | A skill or gate that runs the naming rules as a checklist before any term is added | Naming-rule checks applied inconsistently; new terms drift before glossary entries land |
| Audit cycles | Scheduled agent runs against narrow-slice auditors | Audits skipped indefinitely without explicit scheduling |
| Chat→Code dispatch | An MCP server exposing the executor as a callable tool | Human-as-messenger overhead exceeds two transcriptions per session (see *Closure mechanics*) |

The method defines the rules and shapes; the tool binding makes them executable. **Adopt bindings only when the manual discipline shows friction.** Premature binding produces bureaucracy that drifts from the rules it was meant to encode — the rules become aspirational while the encoded version runs out of alignment with them.

---

## Closure mechanics (future)

Today, briefs are produced as files (in a cloud VM or in Chat output), saved to the workspace manually, and Code is pointed at them. An end-state where Chat dispatches Code briefs directly via an MCP-style tool and reads the feedback inline is a natural evolution — it closes the human-as-messenger loop.

**When to build it.** The signal is a single session that needs more than two rounds of human transcription — copying Code's feedback into a new brief, dispatching, transcribing the next feedback back. A vanilla R1 → R2 → implementation cycle already consumes two transcriptions; the trigger is when a normal cycle no longer fits and the human keeps shuttling. Below that threshold, the manual loop is fast enough; above it, the dispatch tooling starts paying its cost. Build on observed friction, not anticipated friction.

---

## Open questions for iteration

Areas where the method is least settled and most likely to refine with use:

- **Role labels.** "Chat" and "Code" are role labels, not product names. They work in conversation but may need disambiguation in any published version (e.g. "high-level assistant" vs "coding agent"). *(The method's own name is now settled — see* The name*.)*
- **Session modes.** The mode list is descriptive of current practice, not prescriptive. Whether modes deserve their own brief templates, system-prompt variants, or context-loading recipes is open.
- **Closure of the Chat→Code loop.** Today the human is the messenger. An MCP-style direct dispatch is the obvious end-state but the design isn't settled (see *Closure mechanics*).
- **Multi-project user.** The within-project memory/context split is operational via the six-month test. The remaining question for users running several projects: what content legitimately belongs in account-scoped user memory rather than per-project context? Likely candidates are durable cross-project preferences (working style, tool defaults), but those are also the easiest to over-claim into memory. Worth a separate audit as the multi-project case grows (Cap'n-Proto-for-Swift is the first second project).
- **Team adoption.** Currently framed for a single principal working with LLMs. Adapting to multi-human teams — who writes the briefs, who reviews the feedback, how decisions get attributed — is unaddressed.
- **Anti-bureaucracy in practice.** The friction audit is described as a practice but hasn't been run against an actual artifact set. The remaining question is empirical: does the audit reliably distinguish pay-its-way artifacts from drift, and what cadence works? A useful first test would be this method's own doc set.
- **~~Verification of ecosystem claims.~~** *Resolved — see* Verified references.

---

## Changelog

- **v0.5 (2026-05-29)** — Named the method **Hooman** (retiring the "Chat-First Project Development" working title). Split the single document into this companion plus the operating guide (`hooman-guide.md`): motivation, what's distinctive, what-it-is-not, ecosystem positioning, the tool-binding roadmap, closure-mechanics, and open questions moved here; the guide keeps the operational content with its inline reasons. Added *The name*, *Ecosystem positioning & survey*, and *Verified references* (resolving the ecosystem-claims open question against primary sources).
- **v0.4 (2026-05-26)** — Updated from v0.3 with: "table of contents, not textbook" maxim for persistent context files; offload-test extended with a contextual-weight axis; six-month test for the memory-vs-project-context split; degrees-of-freedom calibrated across cycle rounds; operational trigger for the MCP-dispatch closure; adversarial review gate with four lenses (Skeptic/Invariant/Scope/Omission); positive sub-agent interface specification (receives/returns/discards); nested-AGENTS.md pattern formalized; *Session close* section; anchors named as the project's constitution with cycle-brief precedence; "Friction solved" column added to the methodology-to-tooling table; Spec-Kit and Kiro shapes mapped to the escalation pattern; friction audit added as the retrospective form of the anti-bureaucracy guardrail.
- **earlier** — see the gist's revision history.

---

*Companion to the operating guide (**`hooman-guide.md`**). Distilled from the Heddle project's practice plus a May 2026 ecosystem survey. An evolving draft — refine in place.*
