# Chat-First Project Development with LLMs

*Working title — pick a real name when this gels.*

**Status:** Initial draft (May 21, 2026). Distilled from one project's experience. Will evolve as the methodology gets stress-tested across more projects and as session-mode practice matures.

---

## Why this exists

Working on a non-trivial project with an LLM hits a predictable ceiling. A single conversation can't hold the project's full context. Detail work pollutes the conversation's attention budget. Decisions made in one session get re-derived in the next. The LLM serializes all reasoning through one context window, and the output reflects the limits of one model's first-pass thinking.

The conventional response — "use a more capable model" or "use a coding agent" — is partial. What actually works is **role separation with mechanical artifacts**: a high-level conversational assistant (*Chat*) that holds strategy and direction, a coding agent (*Code*) that handles investigation and implementation, and a set of artifacts in the project tree that survive across sessions and across handoffs to entirely new agents.

This document describes that methodology. It is portable — no specific project, no specific LLM, no specific tooling. Examples below reference the Heddle project, where this approach was developed, but the structure transfers.

---

## The two-role split

### Chat — primary collaborator

A high-level conversational assistant. Default register: conceptual, strategic, architectural, decision-focused. Chat's job is to:

- Hold the project's vision and direction.
- Frame problems and surface decisions.
- Translate user intent into well-shaped work for Code.
- Review Code's output and weigh trade-offs.
- Keep the long arc visible across sessions.

What Chat **does not** do: read raw codebases page-by-page, generate file inventories, summarize CHANGELOGs in detail, or do any work whose output is *content* rather than *direction*. That work is offloaded.

### Code — research and design partner, then implementer

A coding agent (e.g. Claude Code) with full filesystem and execution access. Code's job is twofold:

1. **Research and design partner.** Given a high-level brief from Chat, investigate the relevant slice of the codebase, draft a plan, and surface trade-offs and decisions that need human input — *without implementing yet*.
2. **Implementer.** Once scope is locked through Chat iteration, execute the work.

The first role is the one most users underuse. Code is a remarkably effective design partner *when given an open-ended brief that asks it to think, not just to type*.

### The offload test

When Chat finds itself about to read a file, summarize a long doc, inventory a directory, or otherwise generate *details* rather than *direction*, that is the signal to write a Code brief instead. The test: is the content I'm about to produce **conceptual** (belongs in Chat) or **inventory / details** (belongs to Code)?

---

## The workspace shape

The artifacts that make the methodology work, in roughly the order you would create them in a new project.

### Project tree

A workspace is a parent directory holding one or more repos as flat siblings, plus a small set of process artifacts at the root.

```
<workspace>/
├── <repo-a>/
├── <repo-b>/
├── ...
├── AGENTS.md              # workspace conventions for AI agents
├── anchors/               # durable reference docs (philosophy, invariants, etc.)
├── roadmap/               # feature work, one file per track
├── session-starters/      # Chat→Code briefs, including audit-driven cycles
├── audits/                # audit reports, mechanically linked to cycles
└── <project>-context.md   # portable orientation for Chat sessions
```

### Anchors — durable reference

Short, stable documents that capture the project's invariants, philosophy, audience, and contract direction. Anchors evolve slowly. They are the docs an agent reads first to understand what the project values and what trade-offs are intentional. Common examples: `PHILOSOPHY.md` (what we are and are not for), `INVARIANTS.md` (what must hold across the codebase), `AUDIENCE_PERSONAS.md` (whom we are designing for).

### Roadmap — feature work

One file per **track**. Tracks have explicit lifecycle states: *idea → proposed → ready → in-flight → shipped*. Each track captures the problem, scope, non-scope, dependencies, and the current next concrete step. Roadmap docs persist across the whole life of the track — they are the durable record of intent.

### Session-starters — Chat→Code briefs

The folder where Chat-produced briefs land. Loose files at the root are one-off handoffs. Subfolders are **maintenance cycles** seeded from a review artifact (see *Audits* below). Code's response to any brief is written next to the input as `<brief-name>-feedback.md`.

### Audits — review artifacts

Periodic structured reviews that produce findings. Each audit is a file (or folder) in `audits/`, mechanically named so it links to a session-starter cycle:

```
audit:  audits/<repo>-audits/<topic>-audit-<YYYY-MM-DD>(.md|/)
cycle:  session-starters/<repo>-<topic>-<YYYY-MM-DD>/
```

The cycle is "the work the audit produced." Audits never get invented from imagination — they come from running an audit pass (manual, scripted, or LLM-driven). This is the protocol that keeps maintenance work disciplined and traceable.

### Project context — portable orientation

A single file (e.g. `<project>-context.md`) saved as a *project file* in the LLM platform (Anthropic project files, equivalent on other platforms). It is the document a fresh Chat session — including one started from mobile, with no filesystem access — reads to understand the project. It captures the platform shape, the audience, the work discipline, and the operating rules. It is **deliberately durable** — refresh on major shape changes, not per release.

Pair this with whatever **persistent user memory** your LLM platform offers. Memory captures temporal, evolving facts (in-flight tracks, recent state, working preferences); the project context file captures durable shape. The two complement each other — don't try to make one do the other's job.

---

## Session modes

*This section is the most tentative. It describes the categories of Chat session distinguishable so far. As the methodology matures, modes may get their own brief templates, starter prompts, or loaded-context recipes.*

| Mode | When | Output |
|---|---|---|
| **Vision / strategy** | Long-arc direction, new bets, positioning | Roadmap entries, anchor updates |
| **Track scoping** | Turning an intent into a defined feature track | `roadmap/<track>.md` |
| **Cycle opening** | Translating a need into a Code investigation brief | `session-starters/<brief>.md` |
| **Review** | Processing Code feedback, weighing trade-offs | Decisions committed to roadmap, anchors, or a next-round brief |
| **Architecture decision** | Committing to a design with documented rationale | An ADR or equivalent decision record |
| **Audit triage** | Reading audit findings, deciding what becomes a cycle | A maintenance-cycle scaffold |
| **Realignment** | Restructuring an existing project to fit this methodology | A migration plan, new anchors, retroactive roadmap |

Each mode shares the same Chat-Code split and the same offload discipline. What differs is what context the session needs loaded and what output shape it produces.

---

## The cycle-brief protocol

The most-used pattern in the methodology.

### Round 1 — Chat produces a brief

A brief is a markdown file written by Chat into `session-starters/`. It contains:

- **Type** — housekeeping / cycle-R1 / cycle-R2+ / implementation.
- **Related track** — pointer to a roadmap doc if any.
- **Goal** — what we want, conceptually, in a paragraph.
- **Read first / don't touch** — anchor docs and exclusions.
- **What to produce** — for R1 briefs, the shape of the response: plan, decision points, open questions, what would NOT be done without go-ahead.
- **Output location** — `<this-file>-feedback.md` adjacent.
- **Discipline guardrails** — for R1: *do not implement*. For implementation rounds: show diffs, run tests, etc.

Crucially, a cycle-opening brief asks Code to **think**, not to type. It explicitly forbids implementation.

### Round 2+ — review and refine

Code's feedback gets reviewed by Chat + human. The decisions surfaced by Code get answered. The plan gets refined. A round-2 brief may follow, narrower in scope. Iterate until scope is genuinely locked and implementable.

### Final round — implementation

A locked-scope brief that Code executes. Show-diff-before-write discipline applies to any file changes. The feedback file remains the audit trail.

---

## Operating rules

These apply in Chat sessions regardless of mode.

1. **Step by step.** Don't solve ahead of the conversation. Wait for direction.
2. **Direct register.** No hedging, no diplomatic softening. If reasoning has a gap, say so plainly.
3. **High-level and conceptual.** Default register for Chat. Push details to Code briefs.
4. **Sharpen, don't guess.** Vague description? Ask a pointed question rather than infer.
5. **Track the arc.** Notice when conversation drifts; ask if it's intentional.
6. **Don't assume cached internals.** Codebases change fast. Verify current state — or ask Code to investigate — before proposing changes.
7. **Bias toward concrete deliverables.** Working artifacts shape design more than planning documents do.
8. **Explicit exclusion zones.** If parts of the project are out of scope for Chat conversations (proprietary domain, third-party material, etc.), the project context file declares them. Filter ruthlessly when reading material adjacent to these zones.

---

## Bootstrapping a new project

Day one. Minimum viable setup:

1. **Create the workspace tree.** `anchors/`, `roadmap/`, `session-starters/`, `audits/`, `AGENTS.md`, project context file.
2. **Write two anchors.** A `PHILOSOPHY.md` (what this project is for and not for) and an `AUDIENCE_PERSONAS.md` (whom you're designing for, even if it's a list of one). Both can be stubs at first.
3. **Write the project context file.** A 1–2 page conceptual orientation. Load it as a project file in your LLM platform so it persists across sessions and devices.
4. **Define the first roadmap track.** Pick one substantive feature. Use it to exercise the cycle-brief pattern end-to-end.
5. **Start a Chat session** with the project context loaded. Frame the first cycle-opening brief together. Hand to Code. Review the feedback. Iterate.

That's the bootstrap. The rest accrues as the project grows.

---

## Realigning an existing project

For projects already in motion, retrofit incrementally:

1. **Inventory what exists.** Where does design intent currently live (issues, docs, README, scattered Slack)? Where does maintenance get planned? What's the current AI-agent collaboration pattern, if any?
2. **Write the project context file first.** It is the single highest-leverage artifact. It lets every Chat session start oriented.
3. **Add anchors as you reference them.** Don't write the full set up front. Write `PHILOSOPHY.md` when a decision needs the project's values stated. Write `INVARIANTS.md` when something gets broken that shouldn't have been.
4. **Adopt the cycle-brief pattern on the next piece of work.** Don't backfill old work into the structure. Use it forward.
5. **Move toward the roadmap / session-starter split** as you start a second track of work. With one track, you can keep everything in your head. With two, you need the artifacts.

Realignment is gradual. The methodology survives partial adoption better than most.

---

## What this document is not

- **Not a tooling spec.** It does not require any particular LLM, IDE, or platform. It works with whatever Chat-style assistant and whatever coding agent you have access to.
- **Not a coding methodology.** It governs *how you collaborate with LLMs*, not *how you write code*. Pair it with whatever engineering practices your project already uses.
- **Not a project-management methodology.** It is compatible with Agile, Shape Up, lazy-consensus, or whatever scheduling discipline your team prefers. It governs the *content* and *handoff* of work, not its *cadence*.
- **Not finished.** This is an initial draft, distilled from one project's experience. Expect it to evolve.

---

## Open questions for iteration

Areas where the methodology is least settled and most likely to refine with use:

- **Naming.** "Chat" and "Code" are role labels here, not product names. They work in conversation but may need disambiguation in a published version (e.g. "high-level assistant" vs "coding agent").
- **Session modes.** The mode list is descriptive of current practice, not prescriptive. Whether modes deserve their own brief templates, system-prompt variants, or context-loading recipes is open.
- **End-state for Chat→Code dispatch.** Today, briefs are produced as files, presented in chat, and saved to the workspace manually. An MCP-style "Chat dispatches Code briefs directly" capability would close the loop — worth a separate exploration once a reference implementation exists.
- **Multi-project user.** When one person runs several projects with this methodology, what convention reconciles user memory (which is account-scoped) with project context (which is project-scoped)? Probably project files do most of the work; worth confirming.
- **Team adoption.** Currently framed for a single principal working with LLMs. Adapting to multi-human teams — who writes the briefs, who reviews the feedback, how decisions get attributed — is unaddressed.

---

*Draft for iteration. Refine in place.*
Home location is this gist: 