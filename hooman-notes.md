# Hooman — Companion: Rationale, Provenance & References

*The why behind the operating guide (**`hooman-guide.md`**, same gist): why the method exists, what's distinctive, where it sits in the ecosystem, verified references, the candidate-binding roadmap, and open questions. Read the guide to operate; read this when you want the reasoning.*

**Canonical version:** <https://gist.github.com/hooman/5811ee3bb7c235573299400167403985>.

---

## The name

**Hooman** is eponymous — named for its author (GitHub: `hooman`) — because it is, for now, a single-user method, not a universal standard. Naming it after the author is honest about that scope.

The name does double duty. It quietly encodes the method's premise — a *human* in the director's seat, directing AI executors ("Hooman" ≈ "human", and the human-in-the-loop is the whole point). And it sidesteps two collision problems at once: the crowded ecosystem vocabulary (*workflow, skill, agent, constitution* are all taken) and the method's own internal terms (*brief, cycle, offload*). It namespaces the entire toolkit: the `hooman` skill, the future `hooman-workspace` repo, this gist.

**Rejected alternatives** (per naming rule 7):

- **homer** — the author's old dial-up-BBS handle. Rejected as the primary name: dominated by Homer Simpson and the Greek poet, and already used by existing dev tools (a self-hosted dashboard; a SIP-capture tool). Kept only as a sentimental nod here.
- **"Chat-First Project Development with LLMs"** — the descriptive working title through v0.4. Retired as the primary name. It still describes the method accurately and could serve as a public descriptive subtitle if the method is ever published for others (e.g. *Hooman: Chat-First Project Development with LLMs*).

### Role labels: "Code" → "Executor" (v0.6)

The role labels are **Chat** (orchestration) and, as of v0.6, **Executor** (the tool-equipped agent). The executor role was renamed from "Code" because the distinction that actually matters between the two roles is **embodiment** — a tool-equipped agent with filesystem and execution access versus a conversational assistant — *not* subject matter. "Code" implied the work was always software; in practice the same role drafts bills of materials, structures analytical briefs, and runs research, not just source code. "Executor" names the function across domains. The tool that fills the role is still usually a coding agent (Claude Code); role and tool are distinct.

*Rejected alternatives:* **Synthesizer** (too drafting-specific — undersells implementation and execution); **Agent** (overloaded across the ecosystem, per naming rule 1); **Worker** (vague, says nothing about embodiment). **Chat** is retained — accurate for the orchestration role and not overloaded in this context.

The **reconnaissance / mutation** split *within* the Executor role is also new in v0.6. It reflects that the role bundles two functions with different safety profiles — read-only investigation versus real writes — which the cycle-brief protocol already separated as phases (plan-mode R1 vs show-diff implementation) but the old single "Code" label obscured.

---

## Why this exists

Working on a non-trivial project with an LLM hits a predictable ceiling. A single conversation can't hold the project's full context. Detail work pollutes the conversation's attention budget. Decisions made in one session get re-derived in the next. The LLM serializes all reasoning through one context window, and the output reflects the limits of one model's first-pass thinking.

The conventional response — "use a more capable model" or "use a coding agent" — is partial. But the deeper point, and the one that explains the method's shape, is *who it is for*:

> Hooman is a personal operating method for delegating complex, intermittent work to LLMs without losing the thread. It is built for a single principal whose main job is not this project and whose attention is split across operational, technical, family, civic, and personal domains. The dominant cost in that situation is not bad output — it is **re-entry**: picking a project back up after a long gap and reconstructing what was decided, what was half-done, and what must not be touched. The method separates judgment from execution — the human owns priorities, constraints, and final decisions; Chat holds direction and frames delegation; the Executor investigates, implements, audits, and summarizes; durable artifacts carry context across gaps — and it optimizes for re-entry being cheap, delegation being the default, and scarce attention going to judgment rather than to rediscovering context or shuttling handoffs.

That framing explains choices that otherwise read as overbuilt. The artifact system is not ceremony; it is **externalized working memory** for someone who may touch a project once a month between fabrication deadlines, family obligations, and IT emergencies. The roadmap, anchors, session summaries, glossary, and findings inbox are what make a three-week gap survivable.

Stated as design properties, the method optimizes for: fast re-entry after context gaps; clear delegation boundaries; persistent decision memory; low ceremony during active work; high recoverability when work stalls; protection from agent-generated sprawl; and separation between unrelated efforts (work systems, hobby projects, civic/parental research, personal curiosity). The *scale-to-stakes* rule in the guide's bootstrap section is the operational expression of that last property — not every effort earns the full apparatus.

---

## What's distinctive here

Most of this method is novel framing of patterns the LLM-tooling ecosystem has converged on independently: the orchestrator/executor split, plan-then-implement, project-root agent files, structured note-taking, sub-agent context isolation. What's genuinely distinctive — worth naming as contributions rather than reinventions:

- **The anti-bureaucracy guardrail.** Most methodologies accrete templates; very few have an explicit "must solve a real friction" rule as a precondition for adoption. Its operational complement, **scale-to-stakes** (choose the smallest shape that keeps re-entry cheap and delegation clean), is what stops the apparatus from colonizing every effort.
- **The offload test.** "Does this produce content / inventory / details? → Executor. Does it produce direction? → conversational role." Sharper than the implicit splits in most multi-agent frameworks.
- **Output contracts by task type**, including the **evidence map** (every R1 claim tagged *inspected / inferred / unverified*). A sharpening rather than a wholly novel idea, but rarely stated: it targets *review cost* directly, which is the real bottleneck for a time-scarce principal, and it forces the under-reported-unknowns failure of agent plans into the open.
- **The direction check** — an adversarial gate pointed at the *director's own framing*, not only the executor's plan. Novel as far as the survey found: most methods guard the agent's output and leave the single principal's judgment unchecked, which for a solo operator is the actual single point of failure.
- **The reconnaissance / mutation factoring** of the executor role — treating read-only investigation and real writes as two modes with distinct review profiles rather than two phases of one undifferentiated role.
- **Hooman as an escalation protocol**, with a **scope-intake gate** at the threshold. The method explicitly does not govern sub-threshold work, and its guard is aimed at *scope gravity* — large, interesting efforts entering as fog — rather than at premature use: *big is allowed, undefined is not*. Positioning the method as escalation-not-universal-workflow is what keeps its growing apparatus from reading as bloat.
- **Glossary discipline as a gated artifact**, with naming rules that apply before a term is added.
- **The findings inbox** as an explicit standing log for drive-by observations, swept on schedule.
- **Doc-audience layering**, particularly the agent / human-leaning / hybrid split and the *entry-point docs are thin* companion rule.

These are the parts most worth formalizing for reuse outside one project — and they are deliberately kept here, in the companion, so that personalizing the guide's framing (above) does not erode the generalizable spine.

---

## What this is not

- **Not a tooling spec.** It does not require any particular LLM, IDE, or platform. It works with whatever Chat-style assistant and whatever tool-equipped agent you have access to.
- **Not a coding methodology.** It governs *how you collaborate with LLMs*, not *how you write code*. Pair it with whatever engineering practices your project already uses.
- **Not a project-management methodology.** It is compatible with Agile, Shape Up, lazy-consensus, or whatever scheduling discipline you prefer. It governs the *content* and *handoff* of work, not its *cadence*.
- **Not a team methodology.** v0.6 is explicitly single-principal. Multi-human adoption — brief ownership, feedback acceptance, glossary arbitration, deciding what pays its way — is an explicit non-goal, not an open question (see the guide's *Scope* and *Open questions* below).
- **Not finished.** This is an evolving draft, distilled from one project's experience plus an ecosystem survey. Expect it to evolve.

---

## Ecosystem positioning & survey

The method was distilled from one project's practice (Heddle) plus a survey of the May 2026 AI-coding-agent ecosystem, triangulated across several independent LLM research tools to reduce single-source blind spots. Where it sits: it is a novel *framing* of patterns the ecosystem converged on independently — the orchestrator/executor split, plan-then-implement, project-root agent files (AGENTS.md), modular capability files (Skills / SKILL.md), the Model Context Protocol (MCP) for connecting agents to external systems, spec-driven tools (Spec-Kit, Kiro), and sub-agent context isolation. The distinctive contributions are listed under *What's distinctive*. The underlying research reports are kept in the author's archive, not published with the method.

*Source-integrity note:* the survey's distinct inputs were fewer than they appeared — verify source independence before treating any cross-tool "consensus" as strong. Lean on the *Verified references* below, which are checked against primary sources, rather than on the survey reports.

*On review independence (v0.6).* That caution generalizes beyond the survey. This revision was shaped partly by independent reviews from several frontier models, blind and context-aware; their recommendations converged strongly. Treat that convergence the same way. Frontier models share training data and house-style priors — they gravitate toward "personalize it, add a taxonomy, automate the loop" — so cross-model review consensus is lower-independence than it looks. The convergence flagged the changes worth *examining*; it did not by itself justify them. Each change in v0.6 was kept only where it survived the method's own tests (notably: did it solve real friction, and did it respect anti-premature-binding). Where the loudest recommendation failed those tests — e.g. "build the dispatch loop and auto-synthesis now" — it was declined; see *Deferred bindings*.

---

## Verified references

The ecosystem claims this method leans on were checked against primary sources (**verified as of May 2026**). These are current, public facts that will decay — re-check before relying on them — and they are **positioning, not load-bearing**: the method works whether or not they hold. This section resolves the former open question "Verification of ecosystem claims."

- **AGENTS.md is a Linux-Foundation-stewarded open standard.** *Verified.* The Linux Foundation formed the **Agentic AI Foundation (AAIF)** in December 2025, anchored by founding contributions: **MCP** (Anthropic), **goose** (Block), and **AGENTS.md** (OpenAI). Sources: [Linux Foundation press release](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation), [OpenAI](https://openai.com/index/agentic-ai-foundation/), [agents.md](https://agents.md/).
- **Adoption: 60,000+ open-source projects.** This is the figure stated by the AAIF / agents.md — consistent across sources, but **self-reported, not independently audited**. Cite it as such.
- **SKILL.md is cross-tool portable.** *Verified, with nuance.* The **Agent Skills** specification ([agentskills.io](https://agentskills.io/specification)) was released by Anthropic as an open standard (December 2025) and is compatible across Claude Code, OpenAI Codex CLI, Gemini CLI, OpenClaw, and OpenAI's Skills tool. Skills that adhere to the core SKILL.md format (YAML frontmatter `name` + `description`, plus a markdown body, with progressive disclosure of bundled files) are portable across tools without modification; tool-specific extensions are not guaranteed to carry over.

Also confirmed in passing: **MCP** was likewise contributed to the AAIF / Linux Foundation; the spec-driven tools **Spec-Kit** (GitHub: *constitution → specify → plan → tasks → implement*) and **Kiro** (AWS: `requirements.md` / `design.md` / `tasks.md`, with requirements in **EARS** notation — `WHEN <condition> THE SYSTEM SHALL <behavior>`) match the method's escalation shape and its use of anchors as a "constitution."

---

## From methodology to tooling — candidate bindings

Some concepts in the guide may eventually earn a **tool binding** — the encoded form that lets a rule run automatically rather than by discipline. Not every rule wants embodiment. These are **candidate** bindings: each is adopted only when its own trigger fires. The mapping fills in as the method matures.

| Concept | Candidate binding | Friction solved | Adoption trigger |
|---|---|---|---|
| Session modes | Auto-loadable instruction packs (Claude Skills, `agents.md`-compatible equivalents) | Mode context re-pasted by hand; mode discipline drifts | Mode context retyped across ≥3 sessions, or discipline visibly slipping |
| Cycle-brief R1 | Plan mode / read-only constraint | Executor starts implementing during R1 | First time R1 produces unrequested writes |
| Cycle-brief implement | Show-diff hooks, scoped tool allowlists | Unreviewed writes; scope creep via broad access | First unreviewed write that should have been caught |
| Sub-agent roles | Configured sub-agent definitions with tight tool scopes | Ad-hoc dispatch, inconsistent isolation | Sub-agent failure traced to missing/over-broad scope |
| Output contracts | Brief templates per task type with the evidence-map field built in | Review cost high; unknowns under-reported | Review repeatedly stalls reconstructing what the Executor checked |
| Direction check | A pre-dispatch checklist (skill or brief preamble) | A cycle answers the wrong question | A well-executed cycle comes back aimed at the wrong target |
| Findings inbox | A standing log today; eventually a structured-note tool | Drive-by findings lost; conversation drift | Findings lost despite the log, or the log outgrows one-liners |
| Glossary discipline | A gate that runs the naming rules before any term is added | Naming-rule checks applied inconsistently | Terms landing without rule checks; glossary drift |
| Audit cycles | Scheduled agent runs against narrow-slice auditors | Audits skipped indefinitely | Audits not happening without a schedule |
| Chat→Executor dispatch | An MCP server exposing the Executor as a callable tool | Human-as-messenger overhead | **Deferred** — cost-based (see *Closure mechanics* and *Deferred bindings*) |

The method defines the rules and shapes; the binding makes them executable. **Adopt bindings only when the manual discipline shows friction.** Premature binding produces bureaucracy that drifts from the rules it was meant to encode — the rules become aspirational while the encoded version runs out of alignment with them.

A cross-cutting binding *not* to build: **auto-writing canonical artifacts**. Where manual upkeep of the glossary or anchors slips under time pressure, the sanctioned mechanism is **propose-then-commit** — an agent drafts entries, the human commits them in-session — which cuts the compilation cost without surrendering the write path to the docs that are supposed to be canonical (see *Deferred bindings*).

---

## Closure mechanics (future)

Today, briefs are produced as files (in a cloud VM or in Chat output), saved to the workspace manually, and the Executor is pointed at them. An end-state where Chat dispatches Executor briefs directly via an MCP-style tool and reads the feedback inline is a natural evolution — it closes the human-as-messenger loop.

**When to build it.** The earlier statement of the trigger was by *count*: a single session that needs more than two rounds of human transcription. A vanilla R1 → R2 → implementation cycle already consumes two transcriptions; the count-trigger fires when a normal cycle no longer fits and the human keeps shuttling.

The real variable, though, is **cost per transcription, not count.** For an operator whose every context-switch carries a high cognitive tax, a single shuttle costs more than the count implies, and the threshold to build the dispatch tooling is correspondingly lower. Re-express the trigger as cost, and expect it to fire sooner for a high-cost operator than the generic count suggests — *without* discarding the trigger logic and building ahead of friction. Below the threshold the manual loop is fast enough; above it the dispatch tooling starts paying its cost. Build on observed friction, not anticipated friction.

---

## Deferred bindings (explicit)

Two bindings are deliberately *not* built in this version, logged here so the decision is explicit rather than quietly forgotten. Both were recommended by reviewers; both were declined on the method's own terms.

- **Chat→Executor MCP dispatch** — the zero-transcription loop. Deferred per the anti-premature-binding rule; the trigger is cost-based (see *Closure mechanics*). Attractive, but building it before the friction lands produces tooling that drifts from the rules it encodes.
- **Auto-synthesis of canonical artifacts** — having an agent extract decisions and definitions at session end and write them straight into anchors and the glossary. Deferred not merely on the friction rule but on a stronger ground: **auto-writing the project's constitution destroys the curation that makes it canonical.** The atrophy problem it would solve — manual upkeep slipping under time pressure — is real and worth taking seriously; the sanctioned answer is **propose-then-commit** (agent drafts, human commits in-session), which cuts the compilation cost without handing an agent the write path to the canonical docs.

The general principle: a binding that removes *friction* is a candidate; a binding that removes *curation* is a hazard.

---

## Open questions for iteration

Areas where the method is least settled and most likely to refine with use:

- **Session modes.** The mode list is descriptive of current practice, not prescriptive. Whether modes deserve their own brief templates, system-prompt variants, or context-loading recipes is open.
- **Trust calibration.** v0.6 says to track informally where the Executor is reliable and shift review weight accordingly, and to keep the record lightweight until it earns more. Whether a useful calibration can stay informal — or whether it inevitably wants a structured reliability record without becoming its own bureaucracy — is unproven.
- **Direction-check efficacy.** The director-side gate is new. Whether a pre-dispatch check on one's own framing reliably catches mis-framing, or mostly adds ceremony, is unproven; v0.6 gates its adoption on observed friction (a well-executed cycle aimed at the wrong target).
- **Closure of the Chat→Executor loop.** Today the human is the messenger. MCP-style direct dispatch is the obvious end-state but the design isn't settled, and it is deliberately deferred (see *Closure mechanics* and *Deferred bindings*).
- **Multi-project user.** The within-project memory/context split is operational via the six-month test. The remaining question for users running several projects: what content legitimately belongs in account-scoped user memory rather than per-project context? Likely candidates are durable cross-project preferences (working style, tool defaults), but those are also the easiest to over-claim into memory. Worth a separate audit as the multi-project case grows (Cap'n-Proto-for-Swift is the first second project). This is the *memory* axis; the parallel cross-project axis for *governing documents* — the method and the design stances — is now addressed by **Global references** (v0.7.2): they live upstream and project into each workspace via `references/`, with the projection mechanism still to be finalized.
- **Anti-bureaucracy in practice.** The friction audit (now with explicit **kill criteria**, v0.7) is described as a practice but hasn't been run against an actual artifact set. The remaining question is empirical: do the deletion triggers reliably distinguish pay-its-way artifacts from drift, and what cadence works? A useful first test would be this method's own doc set — now larger, which makes the test more pointed.
- **~~Team adoption.~~** *Out of scope (v0.6)* — see the guide's *Scope* and *What this is not*. Listed here only so the boundary is explicit rather than mistaken for an unsolved problem.
- **~~Role labels.~~** *Resolved (v0.6)* — "Code" → "Executor"; "Chat" retained. See *The name*.
- **~~Verification of ecosystem claims.~~** *Resolved* — see *Verified references*.

---

## Changelog

- **v0.7.2 (2026-06-02)** — Added a **Global references** section to the guide: some governing documents are cross-project and live upstream of any single workspace — the method itself and the design-stance docs — and project *into* each workspace via a `references/` folder as a downstream copy that is never forked. Prompted by observed friction, not anticipation: the first *second* project (Cap'n-Proto-for-Swift) needed the method and stance docs shared across workspaces, so the cross-project governance layer earned naming under the anti-bureaucracy rule. The projection *mechanism* — symlinks vs. pulling the upstream repo into project knowledge; installer, repo layout, sync cadence — is deferred to its own pass; only the concept is settled. Also added `references/` to the project-tree diagram, and noted the docs-vs-memory axis distinction under the *Multi-project user* open question.
- **v0.7.1 (2026-06-01)** — Consistency fix: in the Chat role, Chat *maintains a working representation of* the project's direction but the human *owns* it (the prior "hold the project's vision and direction" read as ownership). A proposed v0.8 package (artifact-lifecycle table, a "minimal first run" section, findings sweep-triggers, glossary-gate rewrite, ecosystem reinforcement) was **considered and mostly declined** — most of it either duplicated v0.7 or codified *anticipated* friction on a method with ~2 days of real use, against the anti-bureaucracy rule (build on observed friction). To be reconsidered per-item if the friction actually appears in use. Only the direction-ownership clarification was a present defect rather than anticipated friction, so only it was taken.
- **v0.7 (2026-05-29)** — Framed the method explicitly as an **escalation protocol**: a new *When to invoke* section up front states that Hooman does not govern sub-threshold work (explore informally first) and gives a two-of-five entry threshold; *scale-to-stakes* moved from the bootstrap tail to the front as the first operational decision. Added the **scope-intake gate** ("name the smallest independently useful slice, the exclusion zone, and the first decision, or decompose — *big is allowed, undefined is not*"), framed as the direction check fired at escalation and aimed at **scope gravity** as the dominant risk for this principal. Added **kill criteria** (deletion triggers) to the friction audit; a **visible-artifacts-over-opaque-memory** rule to *Project context*; and three failure-mode rows (**process-as-avoidance**, stale next-action, memory⊥artifacts). Centered the **evidence map** as the contract to keep if only one is kept. Softened "every rule has an eventual binding" → "some rules may earn one." Dated the ecosystem claims *verified as of* and marked them non-load-bearing. Prompted by a second external review, but per the *review-independence* note its **additions were mostly declined** (no third "minimum" doc, no Tier-0/1 machinery, no day-count inbox aging); only changes that survived the method's own tests were kept. A compress-and-clarify pass.
- **v0.6 (2026-05-29)** — Reframed the method's optimization target around a single principal doing intermittent, high-stakes, multi-domain work, with **re-entry** as the dominant cost (rewrote *Why this exists* and the guide's two-role-split opener). Renamed the executor role **Code → Executor** (embodiment, not subject matter) and split it into **reconnaissance / mutation** modes with distinct review profiles. Added **output contracts** by task type with the **evidence map** (*inspected / inferred / unverified*); a **direction check** (adversarial gate on the director's own framing); **trust calibration**; a **failure-modes** map; a **Re-entry** section (re-entry surface leads with the single next action); an AGENTS.md **pruning order**; and a tightened glossary add-trigger. Made **bootstrap incremental** under a **scale-to-stakes** rule (absorbing the effort-class idea as descriptive examples). Softened the Chat/Executor split (Chat may inspect targeted, decision-changing evidence). Introduced **propose-then-commit** for anchors and glossary. Demoted **team adoption** to an explicit non-goal. Converted the tooling table to **candidate bindings** with per-row triggers; added a **Deferred bindings** section (MCP dispatch; auto-synthesis) and re-expressed the dispatch trigger in **cost** terms. Added the **review-independence** note. Preserved the *What's distinctive* spine in the companion so the guide's personalization doesn't erode it.
- **v0.5 (2026-05-29)** — Named the method **Hooman** (retiring the "Chat-First Project Development" working title). Split the single document into this companion plus the operating guide (`hooman-guide.md`): motivation, what's distinctive, what-it-is-not, ecosystem positioning, the tool-binding roadmap, closure-mechanics, and open questions moved here; the guide keeps the operational content with its inline reasons. Added *The name*, *Ecosystem positioning & survey*, and *Verified references* (resolving the ecosystem-claims open question against primary sources).
- **v0.4 (2026-05-26)** — Updated from v0.3 with: "table of contents, not textbook" maxim for persistent context files; offload-test extended with a contextual-weight axis; six-month test for the memory-vs-project-context split; degrees-of-freedom calibrated across cycle rounds; operational trigger for the MCP-dispatch closure; adversarial review gate with four lenses (Skeptic/Invariant/Scope/Omission); positive sub-agent interface specification (receives/returns/discards); nested-AGENTS.md pattern formalized; *Session close* section; anchors named as the project's constitution with cycle-brief precedence; "Friction solved" column added to the methodology-to-tooling table; Spec-Kit and Kiro shapes mapped to the escalation pattern; friction audit added as the retrospective form of the anti-bureaucracy guardrail.
- **earlier** — see the gist's revision history.

---

*Companion to the operating guide (**`hooman-guide.md`**). Distilled from the Heddle project's practice plus a May 2026 ecosystem survey. An evolving draft — refine in place.*

