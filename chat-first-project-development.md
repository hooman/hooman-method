# Chat-First Project Development with LLMs

*Working title — pick a real name when this gels.*

**Status:** Draft v0.2 (May 21, 2026). Updated from v0.1 with: anti-bureaucracy guardrail, doc-audience layering principle, handbook artifact, glossary discipline and naming rules, findings-from-chat pattern, and refined operating rules. Distilled from one project's experience; will evolve as the methodology gets stress-tested across more projects.

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

## Anti-bureaucracy guardrail

The methodology accretes artifacts, rules, conventions, and process. Without discipline, this becomes the kind of process manual nobody reads.

**The test for every new rule, template, convention, or artifact category: what specific friction did this solve?**

If the answer is hypothetical ("might be useful one day"), the rule isn't ready to codify. Write it only when real friction shows up. Maintain it only as long as the friction remains.

This applies equally to additions to this methodology doc, to the project handbook, to the glossary, and to operational templates. Conventions earn their place by paying their way.

---

## Doc-audience layering

Project documents serve different audiences. Mixing audiences in one document leads to bloat and to docs nobody fully reads. The methodology distinguishes three categories:

- **Agent-specific docs** — entry points for AI agents. Lean, pointer-heavy. Tell an agent how to operate in this workspace and where to find context. The canonical example is `AGENTS.md`.
- **Human-leaning docs** — entry points for humans (returning collaborators, new contributors). The canonical example is the project **handbook** (see below). Agents can read them, but they're optimized for humans.
- **Hybrid docs** — content that serves both. Anchors (philosophy, invariants, personas), roadmap tracks, the glossary. Both audiences read them; both audiences benefit from the same content.

**Companion principle: entry-point docs are thin and point outward; content lives in the docs that own the topic.** AGENTS.md doesn't restate the philosophy — it points to `PHILOSOPHY.md`. The handbook doesn't restate the rules — it points to the methodology doc. The glossary doesn't restate full architectural definitions — it points to anchors.

This keeps duplication low and definitions canonical.

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
├── AGENTS.md              # agent-specific entry point
├── HANDBOOK.md            # human-leaning navigation
├── GLOSSARY.md            # project vocabulary
├── anchors/               # durable reference docs (often inside a workspace-tooling repo)
├── roadmap/               # feature work, one file per track
├── session-starters/      # Chat→Code briefs, including audit-driven cycles
├── audits/                # audit reports, mechanically linked to cycles
├── overlays/              # workspace-tracked storage for files that don't belong in any single repo
└── <project>-context.md   # portable orientation; also loaded as a platform-level project file
```

### Anchors — durable reference

Short, stable documents that capture the project's invariants, philosophy, audience, and contract direction. Anchors evolve slowly. They are the docs an agent reads first to understand what the project values and what trade-offs are intentional. Common examples: `PHILOSOPHY.md` (what we are and are not for), `INVARIANTS.md` (what must hold across the codebase), `AUDIENCE_PERSONAS.md` (whom we are designing for).

### Handbook — Tier 1 navigation

A single file at the workspace root. Its job is purely locational: tell readers where artifacts live and which docs own which topics. It does **not** restate rules. Reads in two minutes. Updated lazily — when something moves or a new artifact category appears.

Two more tiers exist in principle but only earn their place on friction:

- **Tier 2** — per-folder READMEs where a folder has accumulated convention. Write when a new collaborator gets confused, not before.
- **Tier 3** — a "common tasks" cheat sheet indexed by goal. Write only if you find yourself repeatedly explaining the same workflow.

Don't bootstrap Tiers 2 and 3 preemptively. The Tier 1 handbook is enough for most projects.

### Roadmap — feature work

One file per **track**. Tracks have explicit lifecycle states: *idea → proposed → ready → in-flight → shipped → parked → retired*. Each track captures the problem, scope, non-scope, dependencies, and the current next concrete step. Roadmap docs persist across the whole life of the track — they are the durable record of intent.

### Session-starters — Chat→Code briefs

The folder where Chat-produced briefs land. Loose files at the root are one-off handoffs. Subfolders are **maintenance cycles** seeded from a review artifact (see *Audits* below). Code's response to any brief is written next to the input as `<brief-name>-feedback.md`.

A `findings-from-chat.md` lives at the root of this folder as a standing append-only log — see *The findings inbox* below.

### Audits — review artifacts

Periodic structured reviews that produce findings. Each audit is a file (or folder) in `audits/`, mechanically named so it links to a session-starter cycle:

```
audit:  audits/<repo>-audits/<topic>-audit-<YYYY-MM-DD>(.md|/)
cycle:  session-starters/<repo>-<topic>-<YYYY-MM-DD>/
```

The cycle is "the work the audit produced." Audits never get invented from imagination — they come from running an audit pass (manual, scripted, or LLM-driven).

### Overlays — workspace-tracked side storage

A directory at the workspace root whose contents are tracked as part of the workspace (synced across machines, version-controlled). Holds files that logically belong inside a project repo but shouldn't be tracked by that repo. The actual files live in `overlays/`; symlinks in the project repos point to them, preserving the logical location while keeping the physical storage workspace-scoped.

Use cases: migrating a legacy project into the workspace structure while preserving its untracked in-flight artifacts; development-transient files whose natural location is inside a repo but where repo-tracking is wrong.

### Glossary — project vocabulary

A single `GLOSSARY.md` at the workspace root. See the dedicated section below for what goes in it and the discipline around it.

### Project context — portable orientation

A single file (e.g. `<project>-context.md`) saved as a *project file* in the LLM platform (Anthropic project files, equivalent on other platforms). It is the document a fresh Chat session — including one started from mobile, with no filesystem access — reads to understand the project. It captures the platform shape, the audience, the work discipline, and the operating rules. It is **deliberately durable** — refresh on major shape changes, not per release.

Pair this with whatever **persistent user memory** your LLM platform offers. Memory captures temporal, evolving facts (in-flight tracks, recent state, working preferences); the project context file captures durable shape. The two complement each other — don't try to make one do the other's job.

---

## Glossary discipline

A project glossary is a real artifact, not a curiosity. The hardest moments in a project tend to be naming negotiations, renames, and resolving terms whose meanings have drifted. A disciplined glossary prevents most of them and shortens the rest.

### What goes in it

Three categories:

- **Coined project terms** — names this project invented or claimed.
- **Industry terms with project-specific meaning** — borrowed words where the project's meaning is narrower, wider, or different from the common ecosystem meaning.
- **Deprecated and superseded names** — every rename leaves an entry, marked with supersession date. Old docs and conversations need to keep resolving.

What stays out: any term used once and not recurring. The trigger for an entry is **recurrence in more than one place**, not first use.

### Structure

Categorized rather than flat. Personas, process terms, architecture terms, repos and artifacts, industry terms, deprecated. Alphabetical within each category.

### Ownership model — index with self-contained fallback

When a term has a natural home in an anchor doc or a roadmap track, the glossary entry is one or two sentences plus a pointer to the home doc. When a term doesn't fit a natural anchor (it's too small), the glossary entry is self-contained. Avoids duplication without forcing every term to grow a dedicated doc.

### Update discipline

- **Add when** the term appears in a second place. Single use stays informal.
- **Update when** scope shifts; date the edit in the git log.
- **Mark deprecated when** superseded. Format: `superseded by X (YYYY-MM-DD)`. Don't delete — old material needs the old name to resolve.
- **Same-commit rule**: a new term coined in a roadmap track gets its glossary entry in the same change. Catching it later means it drifts.

### Naming rules

Apply to all coined project naming — terms, files, directories, functions — not just glossary entries.

1. **Avoid overloaded terms.** If a word is heavily used in adjacent ecosystems (LLM tooling, your stack's stdlib, the user's likely vocabulary) with a specific meaning, don't reuse it for something else.
2. **Prefer single words.** Multi-word terms acquire shortenings whether you want them or not. Pre-shorten.
3. **Plain over poetic.** Reserve metaphor for things that genuinely are metaphors. Avoid *sentinel*, *scout*, *oracle*, *sage* unless the project is literally about that role.
4. **Reuse industry vocabulary deliberately.** When borrowing a common term, make sure the project meaning closely aligns with the established one. Loose alignment confuses more than it helps.
5. **Avoid acronyms unless they self-decode.** Common-phrase acronyms (e.g. OOBE for "out of the box experience") are borderline-acceptable. Project-internal acronyms earn their entries but shouldn't be coined casually.
6. **No version suffixes in primary names.** *v1 / v2 / v3* belong in artifacts (filenames, schemas), not in the term itself.
7. **Document rejected alternatives.** A glossary entry for a name should note what was considered and why this won. Prevents re-litigation later.
8. **Coined terms anchor somewhere.** A term floating as informal usage will drift. Anchor doc, roadmap track, or glossary entry — pick one. If none fits, the term probably isn't worth coining.

---

## The findings inbox

Chat sessions regularly notice issues in passing — undocumented features, dead links, drifted facts, naming inconsistencies. Without somewhere to drop them, these findings die when the session ends.

**`session-starters/findings-from-chat.md`** is the standing append-only log for these. One line per finding:

```
- **YYYY-MM-DD** — <description>. [<status>]
```

Status values: `open`, `dispatched` (Code brief written), `closed`.

Discipline: append when noticed, never debate in line. Code does periodic sweeps and either closes findings directly or escalates them into briefs. The file is lightweight by design — if a finding deserves more than one line, it deserves its own brief.

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

A brief is a markdown file written by Chat into `session-starters/`. The boilerplate:

- **Type** — housekeeping / cycle-R1 / cycle-R2+ / implementation.
- **Related track** — pointer to a roadmap doc if any.
- **Target repo(s)** — which siblings are in scope.
- **Goal** — what we want, conceptually, in a paragraph.
- **Read first** — anchor docs and adjacent material.
- **Don't touch** — exclusions, exclusion zones, out-of-scope adjacent surfaces.
- **What to produce** — for R1 briefs, the shape of the response: plan, decision points, open questions, what would NOT be done without go-ahead.
- **Output** — `<this-file>-feedback.md` adjacent.
- **Discipline guardrails** — for R1: *do not implement*. For implementation rounds: show diffs, run tests, etc.

A cycle-opening brief asks Code to **think**, not to type. It explicitly forbids implementation.

### Round 2+ — review and refine

Code's feedback gets reviewed by Chat + human. The decisions surfaced by Code get answered. The plan gets refined. A round-2 brief may follow, narrower in scope. Iterate until scope is genuinely locked and implementable.

### Final round — implementation

A locked-scope brief that Code executes. Show-diff-before-write discipline applies to any file changes. The feedback file remains the audit trail.

### Closure mechanics (future)

Today, briefs are produced as files in the cloud VM (or in Chat output), saved to the workspace manually, and Code is pointed at them. An end-state where Chat dispatches Code briefs directly via an MCP-style tool and reads the feedback inline is a natural evolution — closes the human-as-messenger loop. Worth a separate exploration once a reference implementation exists.

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
9. **Drop findings, don't carry them.** When Chat notices an issue that isn't the topic of the current session, append to `findings-from-chat.md` and move on. Don't expand the current conversation to absorb it.

---

## Bootstrapping a new project

Day one. Minimum viable setup:

1. **Create the workspace tree.** `anchors/`, `roadmap/`, `session-starters/`, `audits/`, `overlays/`, `AGENTS.md`, `HANDBOOK.md`, `GLOSSARY.md`, project context file.
2. **Write two anchors.** A `PHILOSOPHY.md` (what this project is for and not for) and an `AUDIENCE_PERSONAS.md` (whom you're designing for, even if it's a list of one). Both can be stubs at first.
3. **Write the project context file.** A 1–2 page conceptual orientation. Load it as a project file in your LLM platform so it persists across sessions and devices.
4. **Write the handbook.** A 1-page navigation index pointing at the artifacts above.
5. **Seed the glossary.** Even with just a handful of entries, it establishes the discipline.
6. **Define the first roadmap track.** Pick one substantive feature. Use it to exercise the cycle-brief pattern end-to-end.
7. **Start a Chat session** with the project context loaded. Frame the first cycle-opening brief together. Hand to Code. Review the feedback. Iterate.

That's the bootstrap. The rest accrues as the project grows.

---

## Realigning an existing project

For projects already in motion, retrofit incrementally:

1. **Inventory what exists.** Where does design intent currently live (issues, docs, README, scattered Slack)? Where does maintenance get planned? What's the current AI-agent collaboration pattern, if any?
2. **Write the project context file first.** It is the single highest-leverage artifact. It lets every Chat session start oriented.
3. **Write the handbook second.** Once you know what's where, capture it. The handbook is fast to write once the inventory is done.
4. **Add anchors as you reference them.** Don't write the full set up front. Write `PHILOSOPHY.md` when a decision needs the project's values stated. Write `INVARIANTS.md` when something gets broken that shouldn't have been.
5. **Adopt the cycle-brief pattern on the next piece of work.** Don't backfill old work into the structure. Use it forward.
6. **Move toward the roadmap / session-starter split** as you start a second track of work. With one track, you can keep everything in your head. With two, you need the artifacts.
7. **Seed the glossary on demand.** Add entries as terminology negotiations arise, not preemptively.

Realignment is gradual. The methodology survives partial adoption better than most.

---

## What this document is not

- **Not a tooling spec.** It does not require any particular LLM, IDE, or platform. It works with whatever Chat-style assistant and whatever coding agent you have access to.
- **Not a coding methodology.** It governs *how you collaborate with LLMs*, not *how you write code*. Pair it with whatever engineering practices your project already uses.
- **Not a project-management methodology.** It is compatible with Agile, Shape Up, lazy-consensus, or whatever scheduling discipline your team prefers. It governs the *content* and *handoff* of work, not its *cadence*.
- **Not finished.** This is an evolving draft, distilled from one project's experience. Expect it to evolve.

---

## Open questions for iteration

Areas where the methodology is least settled and most likely to refine with use:

- **Naming.** "Chat" and "Code" are role labels here, not product names. They work in conversation but may need disambiguation in a published version (e.g. "high-level assistant" vs "coding agent").
- **Session modes.** The mode list is descriptive of current practice, not prescriptive. Whether modes deserve their own brief templates, system-prompt variants, or context-loading recipes is open.
- **Closure of the Chat→Code loop.** Today the human is the messenger. An MCP-style direct dispatch is the obvious end-state but the design isn't settled.
- **Multi-project user.** When one person runs several projects with this methodology, what convention reconciles user memory (which is account-scoped) with project context (which is project-scoped)? Probably project files do most of the work; worth confirming as the case grows.
- **Team adoption.** Currently framed for a single principal working with LLMs. Adapting to multi-human teams — who writes the briefs, who reviews the feedback, how decisions get attributed — is unaddressed.
- **Anti-bureaucracy in practice.** The guardrail is stated, not tested. Some artifacts in this doc may already fail the "what specific friction did this solve?" check. Worth a periodic audit.

---

*Draft for iteration. Refine in place.*
The authoritative version of this document is here: https://gist.github.com/hooman/5811ee3bb7c235573299400167403985