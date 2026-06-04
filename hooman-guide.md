# The Hooman Method — Operating Guide

*How to run the method. The reasoning, provenance, and references live in the companion: **`hooman-notes.md`** (same gist).*

**Status:** Draft v0.7.2 (2026-06-02). *v0.7.2 — adds the **Global references** section: some governing docs (the method itself, the design stances) are cross-project and live upstream, projected into each workspace via `references/` as a downstream copy that is never forked.* *v0.7.1 — consistency fix: Chat maintains a working representation of the project's direction but the human owns it; a proposed v0.8 package was considered and mostly declined (see changelog).* **v0.7** frames the method as an **escalation protocol** (explore informally below the threshold; add structure only once re-entry / delegation / review / mutation-safety begin to bite); moves *scale-to-stakes* to the front as the first decision; adds a **scope-intake gate** (name the smallest useful slice or decompose — *big is allowed, undefined is not*), **kill criteria** for the friction audit, a **process-as-avoidance** failure mode, and a **visible-artifacts-over-opaque-memory** rule. A compress-and-clarify pass, not new machinery. Full changelog in the companion.

**Canonical version:** <https://gist.github.com/hooman/5811ee3bb7c235573299400167403985>. Local copies may lag; treat the gist as authoritative.

---

## How to use these two documents

- **This guide** is operational: how to set up a workspace and run the method day to day. Read it to operate.
- **The companion** (`hooman-notes.md`) holds the *why*: motivation, what's distinctive, ecosystem positioning, verified references, the candidate-binding roadmap, and open questions. Consult it when you want the reasoning behind a prescription.

Each rule here keeps its short *why* inline; the extended rationale lives in the companion. (This is the method's own "table of contents, not textbook" rule applied to itself.)

---

## When to invoke — Hooman is an escalation protocol

Hooman does not govern all AI-assisted work, and is not meant to. Below the threshold, work the normal way: chat, sketch, experiment, run ad-hoc reconnaissance and code sessions. **Invoke the method only when informal exploration stops being enough** — when the work is large or durable enough that re-entry, delegation, review, or mutation-safety start to cost you. Concretely, escalate when **two or more** hold:

- you expect to return to this after a gap;
- an Executor will inspect or mutate nontrivial material;
- there is more than one plausible path;
- mistakes are expensive or hard to reverse;
- you need an audit trail.

Below that line the apparatus is overhead; above it, its absence is. (This is *scale-to-stakes* from *Bootstrapping*, stated up front because it is the first operational decision — not a classification to file every effort into from the start.)

**The scope-intake gate — big is allowed, undefined is not.** The failure this method most has to guard against is not premature invocation; it is **scope gravity** — a large, interesting effort entering the system as fog. So before the first real brief, name three things: the **smallest independently useful slice**, the **exclusion zone** (what is explicitly out), and the **first decision** that needs making. If you cannot name the slice, the next task is not setup or implementation — it is **scope decomposition**. (This is the *direction check* below, fired at the moment of escalation.)

---

## The two-role split

Working with an LLM on anything non-trivial hits a predictable ceiling: a single conversation can't hold the project's full context, detail work pollutes the attention budget, and decisions get re-derived each session.

But the ceiling that actually governs this method is sharper than that, and stating it explicitly explains most of what follows. **This method is built for a single principal doing intermittent, high-stakes work across many unrelated domains, whose main job is not this project and whose attention is the scarce resource.** The dominant cost in that situation is not bad output — it is *re-entry*: picking a project back up after a three-week gap and reconstructing what was decided, what was half-done, and what must not be touched. So the method optimizes for re-entry being cheap, delegation being the default, and the principal's scarce attention going to judgment rather than to rediscovering context or shuttling handoffs.

The response that works is **role separation with mechanical artifacts**: a conversational assistant (*Chat*) that holds strategy and direction, a tool-equipped agent (*the Executor*) that investigates and implements, and artifacts in the project tree that survive across sessions and across handoffs to entirely new agents. The human stays in the seat that can't be delegated — priorities, constraints, final decisions — and pushes reconnaissance, implementation, inventory, and cleanup outward.

### Chat — orchestration

A high-level conversational assistant. Default register: conceptual, strategic, architectural, decision-focused. **Chat maintains a working representation of the project's direction; it does not own that direction — the human owns priorities, constraints, and final decisions.** Chat's job:

- Maintain the visible working model of the project's direction.
- Frame problems and surface decisions.
- Translate intent into well-shaped briefs for the Executor.
- Review Executor output *with the human*, weighing trade-offs and alternatives.
- Keep the long arc visible across sessions.

What Chat **does not** do: bulk-process detail — read codebases page-by-page, generate file inventories, summarize long docs. That work is offloaded. Nor does Chat own priorities, silently expand scope, or replace the human's judgment — it may *challenge* the human's framing when evidence or logic warrants, but the authority to choose stays human. The exception that matters: Chat *may* inspect a targeted piece of evidence — a single pivotal file, one failing test, a narrow diff — when seeing it directly changes a decision. The rule is *don't bulk-process details*, not *never look*; an over-abstracted Chat that refuses to look at anything becomes hostage to the Executor's framing.

### Executor — investigate, then implement

A tool-equipped agent (e.g. Claude Code) with filesystem and execution access. The distinction from Chat is **embodiment, not subject matter**: the Executor has hands — it can read, run, and write — and it fills this role whether the work is code, a bill of materials, or a research brief.

The role runs in two modes with **different safety profiles**, and the method keeps them separate:

1. **Reconnaissance.** Given a brief, investigate the relevant slice, surface trade-offs and the decisions that need human input, and recommend a path — *without mutating anything*. Read-only. This is the mode most users underuse: the Executor is a remarkably effective design partner when the brief asks it to think, not to type.
2. **Mutation.** Once scope is locked through Chat iteration, execute. Writes are real; the discipline tightens accordingly (show-diff, tests, rollback).

The two modes carry different review requirements (see *Output contracts*) and, on a capable tool, different enforcement: reconnaissance maps to a read-only constraint like plan mode; mutation maps to show-diff-before-write. Treating them as one undifferentiated "do the work" role is the most common way unreviewed writes slip through.

### The offload test

When Chat finds itself about to read a file, summarize a long doc, inventory a directory, or otherwise generate *details* rather than *direction*, that is the signal to write an Executor brief instead. The test: is the content I'm about to produce **conceptual** (belongs in Chat) or **inventory / details** (belongs to the Executor)?

**A second axis — contextual weight — applies to persistence.** Before adding anything to a context file that loads automatically into future sessions — AGENTS.md, the project context file, SKILL.md frontmatter, anchor docs — ask whether the marginal signal justifies the marginal attention cost. Every line in a persistent context file claims a slice of every loader's attention budget, every session. Lines that aren't pulling their weight are net-negative. The directional axis asks where content goes *now*; the contextual-weight axis asks whether it earns persistence at all.

---

## Output contracts

Scarce attention makes **review cost the real bottleneck**, not execution. Vague delegated output forces you to reconstruct context just to judge it — the exact cost the method exists to avoid. So every delegated task carries a contract: *what "done enough to decide quickly" looks like for this kind of work.* The contract is stated in the brief and is what you check the response against.

Three contracts cover most work. Match the contract to the task, not to the role.

- **Reconnaissance (read-only investigation).** Returns: decision points surfaced; an **evidence map** tagging every material claim as *inspected* (read directly), *inferred* (reasoned from adjacent evidence), or *unverified* (assumed, not checked); assumptions marked; a recommended path; non-recommended paths briefly rejected; and an explicit statement that nothing was implemented. The evidence map is the load-bearing field — agents reliably produce plausible plans that under-report what they never actually looked at, and the tag forces that distinction into the open.
- **Mutation (implementation).** Returns: files changed; tests run and their result; risks remaining; manual checks still needed; rollback notes where relevant. Show-diff-before-write applies.
- **Analysis (research, drafting, non-code synthesis).** Returns: source quality separated from speculation; the strongest *opposing* evidence, not just the supporting case; practical decision implications; uncertainty labeled. This is the contract for work the Executor does outside software — a bill of materials, an analytical brief, a literature scan — where "good output" differs from a code plan.

A delegated task with no answer to "what does done-enough-to-decide look like?" isn't ready to dispatch. Of the three, the **evidence map is the one to keep if you keep only one** — it is what makes a plausible plan auditable instead of merely trusted.

---

## Anti-bureaucracy guardrail

The methodology accretes artifacts, rules, conventions, and process. Without discipline, this becomes the kind of process manual nobody reads.

**The test for every new rule, template, convention, or artifact category: what specific friction did this solve?**

If the answer is hypothetical ("might be useful one day"), the rule isn't ready to codify. Write it only when real friction shows up. Maintain it only as long as the friction remains.

This applies equally to additions to this methodology, to the project handbook, to the glossary, and to operational templates. Conventions earn their place by paying their way.

**The retrospective form: friction audit.** The same test applied backwards on a recurring pass. Walk the existing artifact set — anchors, roadmap tracks, glossary entries, operational templates, any bindings adopted — and ask of each: what friction does this still solve? Items that no longer pay their way get deprecated or removed; items where the friction has shifted get re-scoped; items still earning their place stay. Treat the friction audit as one audit type among the others (see *Audits — review artifacts*); its findings seed a maintenance cycle the same way any audit does. Run on a slow cadence, or whenever accretion outpaces use.

**Kill criteria — deletion triggers, not just adoption triggers.** "What friction does this still solve?" is necessary but not sufficient: without concrete signs to *delete*, the guardrail stays pure discipline, which is what the method otherwise tries to avoid. Treat these as heuristics that prompt a removal decision, not a tracking system — an artifact or mechanism is a candidate for deletion or merge when it has **not been consulted in several cycles**, when **you catch yourself avoiding it**, when it **duplicates what the project context file already says**, or when it has **too few live entries to earn its own file**. The friction audit is where they get applied.

---

## Doc-audience layering

**Underlying principle: every persistent context file is a table of contents, not a textbook.** Anything that loads into a reader's working context — agent or human, entry-point doc or SKILL frontmatter or cycle-brief boilerplate — should point at content, not contain it. Detail lives in the doc that owns the topic and is loaded just-in-time. This keeps every reader's attention budget available for the work, not the navigation.

Within this, project documents serve different audiences. Mixing audiences in one document leads to bloat and to docs nobody fully reads. The methodology distinguishes three categories:

- **Agent-specific docs** — entry points for AI agents. Lean, pointer-heavy. Tell an agent how to operate in this workspace and where to find context. The canonical example is `AGENTS.md`, increasingly a project-root convention across AI coding tools. Its effectiveness depends on being **operational** rather than narrative: command-first (the exact commands an agent should run), task-organized (sections by what an agent does, not by topic), closure-defined (every section says how an agent knows the task is done). Keep it under roughly 200 lines — past that, neither humans nor agents reliably read it.
- **Human-leaning docs** — entry points for humans (returning collaborators, new contributors). The canonical example is the project **handbook** (see below). Agents can read them, but they're optimized for humans.
- **Hybrid docs** — content that serves both. Anchors (philosophy, invariants, personas), roadmap tracks, the glossary. Both audiences read them; both benefit from the same content.

Specific cases of the underlying principle: AGENTS.md doesn't restate the philosophy — it points to `PHILOSOPHY.md`. The handbook doesn't restate the rules — it points to this guide. The glossary doesn't restate full architectural definitions — it points to anchors. Definitions stay canonical, duplication stays low.

### When AGENTS.md exceeds its budget — pruning order

A line limit without a pruning order invites arbitrary cuts. When AGENTS.md grows past its budget, remove in this order until it fits:

1. **Narrative rationale** — move to the handbook or an anchor.
2. **Duplicated rules** — keep one canonical statement, delete the rest.
3. **Stale setup notes** — anything describing a state the repo has left behind.
4. **Repo-specific content** — move down into that repo's nested AGENTS.md (see below).
5. **Commands that belong in repo docs** — point to them rather than inlining them.

### Anti-patterns to design against

- **Prose paragraphs in AGENTS.md.** Operational policy reads as imperative bullets, not narrative.
- **Ambiguous directives** ("be careful," "use good judgment"). Replace with concrete rules or remove.
- **Contradictory priorities** across sections. If two sections imply different orderings, pick one and reconcile.
- **"Docs AIs read but humans don't."** Files written entirely in agent-pleasing telegraphic style accrete around AI-heavy projects and quietly displace the human-readable doc surface. The handbook is the cure — keep it human-leaning and don't let it drift toward terse agent-style brevity.

### Context-file precedence

When multiple context files exist (AGENTS.md, CLAUDE.md, user-level memory, per-folder rules, overlays), they can contradict each other. Agents resolve such conflicts arbitrarily by default. Pick an explicit precedence rule for your workspace and document it in the handbook.

Typical default: **user-level < workspace-level < repo-level < per-folder; later overrides earlier**. Whatever you choose, write it down — a sleeping precedence ambiguity is a future hour of debugging.

**Nested AGENTS.md as the natural application.** In a multi-repo workspace, AGENTS.md doesn't live at a single level — it's a tree. A workspace-root AGENTS.md owns cross-cutting concerns (where artifacts live, conventions common to all repos). Each sibling repo's own AGENTS.md owns repo-specific content (stack, package manager, test commands, non-obvious patterns). Repo-level files *extend* the root — they don't restate it. The precedence rule above makes the layering unambiguous: closer files win for rules they state; rules they don't state inherit from the next level out.

---

## The workspace shape

The artifacts that make the methodology work, in roughly the order you would create them. They appear **on friction, not on day one** — see *Bootstrapping*.

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
├── references/            # projected global docs (method + design stances) — read-only, never forked
├── roadmap/               # feature work, one file per track
├── session-starters/      # Chat→Executor briefs, including audit-driven cycles
├── audits/                # audit reports, mechanically linked to cycles
├── overlays/              # workspace-tracked storage for files that don't belong in any single repo
└── <project>-context.md   # portable orientation; also loaded as a platform-level project file
```

### Anchors — durable reference

Short, stable documents that capture the project's invariants, philosophy, audience, and contract direction. Anchors evolve slowly. They are the docs an agent reads first to understand what the project values and what trade-offs are intentional. Common examples: `PHILOSOPHY.md` (what we are and are not for), `INVARIANTS.md` (what must hold across the codebase), `AUDIENCE_PERSONAS.md` (whom we are designing for).

Anchors function as the project's **constitution** — the same vocabulary used in spec-driven-development tooling. Cycle briefs cannot quietly override them: a plan that implies changing what an anchor states is a separate decision, a deliberate anchor revision, not a side effect of implementation.

**Propose-then-commit.** An agent may *draft* an anchor revision inside a cycle, but anchors change only by deliberate human commit — never auto-written by an end-of-session synthesis pass. The friction of committing them by hand is the feature: it is the gate that keeps them canonical. (The same rule governs the glossary.)

### Handbook — Tier 1 navigation

A single file at the workspace root. Its job is purely locational: tell readers where artifacts live and which docs own which topics. It does **not** restate rules. Reads in two minutes. Updated lazily — when something moves or a new artifact category appears.

Two more tiers exist in principle but only earn their place on friction:

- **Tier 2** — per-folder READMEs where a folder has accumulated convention. Write when a new collaborator gets confused, not before.
- **Tier 3** — a "common tasks" cheat sheet indexed by goal. Write only if you find yourself repeatedly explaining the same workflow.

Don't bootstrap Tiers 2 and 3 preemptively. The Tier 1 handbook is enough for most projects.

### Roadmap — feature work

One file per **track**. Tracks have explicit lifecycle states: *idea → proposed → ready → in-flight → shipped → parked → retired*. Each track captures the problem, scope, non-scope, dependencies, and — first, where re-entry will find it — the **current next concrete step**. Roadmap docs persist across the whole life of the track; they are the durable record of intent.

### Session-starters — Chat→Executor briefs

The folder where Chat-produced briefs land. Loose files at the root are one-off handoffs. Subfolders are **maintenance cycles** seeded from a review artifact (see *Audits* below). The Executor's response to any brief is written next to the input as `<brief-name>-feedback.md`.

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

**The six-month test.** If a fact will still be true six months from now, it belongs in the project context file. If it's the current state of a cycle, it belongs in memory. Borderline cases lean toward memory; promote to the context file only when stability is demonstrated. (The test is a heuristic, not a law — its job is to keep a stable, low-maintenance partition, not to second-guess the platform's own retrieval.)

**Visible artifacts beat opaque memory.** Platform memory is convenient but often opaque, non-auditable, and silently mutated by the platform — a mismatch with an otherwise inspectable, artifact-centric system. So treat memory as a *convenience cache, not a source of truth*: if a fact matters for re-entry and the platform's memory can't be reliably inspected, exported, or corrected, that fact belongs in a **visible artifact** — the roadmap's next-action line, a `STATUS` header, or a session-close summary — and the visible artifact wins on any conflict.

---

## Global references

The method has described the project workspace as self-contained. It is not quite: some governing documents are cross-project and live upstream of any single project.

**Two layers of governance:**

- **Project-local** — roadmap, decisions, parking lot, session-starters, anchors/invariants, the repo(s). These belong to one project and live in its workspace.
- **Global / upstream** — the method itself, and the design-stance docs (`design-stance-universal.md`; per-language stances such as `design-stance-swift.md`). Shared across all projects; a single upstream source of truth, version-controlled, outside any one project.

**Projection into a workspace.** Each workspace carries a `references/` folder that projects the relevant global docs in, so both Chat and the Executor can read them in-context. `references/` is a *downstream projection, not a source of truth* — the upstream copy is canonical; changes flow upstream→down; a project must never fork a global doc locally.

**Mechanism (being finalized — its own pass).** Candidates: symlinks from `references/` to the upstream location (Executor / filesystem side); pulling the upstream repo into project knowledge (Chat side — e.g. uploading the global docs as platform project files). The exact setup — a dotfiles-style installer, repo layout, sync cadence — is a deferred design task. What is settled now is the concept: a global layer, projected via `references/`, kept downstream of one upstream source.

---

## Glossary discipline

A project glossary is a real artifact, not a curiosity. The hardest moments in a project tend to be naming negotiations, renames, and resolving terms whose meanings have drifted. A disciplined glossary prevents most of them and shortens the rest.

### What goes in it

Three categories:

- **Coined project terms** — names this project invented or claimed.
- **Industry terms with project-specific meaning** — borrowed words where the project's meaning is narrower, wider, or different from the common ecosystem meaning.
- **Deprecated and superseded names** — every rename leaves an entry, marked with supersession date. Old docs and conversations need to keep resolving.

What stays out: any term used once and not recurring.

### Structure

Categorized rather than flat. Personas, process terms, architecture terms, repos and artifacts, industry terms, deprecated. Alphabetical within each category.

### Ownership model — index with self-contained fallback

When a term has a natural home in an anchor doc or a roadmap track, the glossary entry is one or two sentences plus a pointer to the home doc. When a term doesn't fit a natural anchor (it's too small), the glossary entry is self-contained. Avoids duplication without forcing every term to grow a dedicated doc.

### Update discipline

- **Add when** the term appears in a second place *and* ambiguity, reuse, or future lookup is likely. Recurrence alone isn't the trigger — many terms appear twice without earning an entry, and a glossary of low-value labels is its own cost.
- **Update when** scope shifts; date the edit in the git log.
- **Mark deprecated when** superseded. Format: `superseded by X (YYYY-MM-DD)`. Don't delete — old material needs the old name to resolve.
- **Same-commit rule**: a new term coined in a roadmap track gets its glossary entry in the same change. Catching it later means it drifts.
- **Propose-then-commit**: an agent may draft an entry, but the human commits it (the same-commit rule still applies). The glossary is canonical; it is not auto-written.

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

Status values: `open`, `dispatched` (Executor brief written), `closed`.

Discipline: append when noticed, never debate in line. The Executor does periodic sweeps and either closes findings directly or escalates them into briefs. The file is lightweight by design — if a finding deserves more than one line, it deserves its own brief.

---

## Session modes

The categories of Chat session distinguishable so far. The list is descriptive of current practice, not prescriptive; whether modes deserve their own brief templates or context-loading recipes is an open question (see the companion).

| Mode | When | Output |
|---|---|---|
| **Vision / strategy** | Long-arc direction, new bets, positioning | Roadmap entries, anchor updates |
| **Track scoping** | Turning an intent into a defined feature track | `roadmap/<track>.md` |
| **Cycle opening** | Translating a need into an Executor investigation brief | `session-starters/<brief>.md` |
| **Review** | Processing Executor feedback, weighing trade-offs | Decisions committed to roadmap, anchors, or a next-round brief |
| **Architecture decision** | Committing to a design with documented rationale | An ADR or equivalent decision record |
| **Audit triage** | Reading audit findings, deciding what becomes a cycle | A maintenance-cycle scaffold |
| **Realignment** | Restructuring an existing project to fit this methodology | A migration plan, new anchors, retroactive roadmap |

Each mode shares the same Chat–Executor split and the same offload discipline. What differs is what context the session needs loaded and what output shape it produces.

---

## Session close

Long Chat sessions accumulate context that's about to be discarded. Letting it die without a closing pass loses both the work and the loose threads. A short ritual makes the discard productive.

- **Session summary.** For sessions whose mode doesn't already produce a durable artifact (primarily vision/strategy, some review sessions), write a brief summary before closing. Its **first line is the single next concrete action** (this is what re-entry will read first); then what was decided and what was deferred. Destination depends on what was discussed — an anchor update, a roadmap-track update, or a new session-starter. Modes that already produce a durable artifact (track scoping, cycle opening) don't need a separate summary; the artifact *is* the summary.
- **Findings sweep.** Append any drive-by observations noticed during the session to `session-starters/findings-from-chat.md` (per *The findings inbox*). Doing this at session-close, not just inline, catches observations the inline discipline missed.

The ritual applies to long sessions, not every session. The signal: if you'd be sad to lose the context, write something before you lose it.

---

## Re-entry

Re-entry is the method's central use case (see *The two-role split*), and it is not only an information problem. After a long gap, the facts being *available* is necessary but not sufficient — a status dump still leaves you to *decide* what to do next, and for intermittent work the deciding is itself the cost. So the re-entry surface leads with the **single next concrete action**, not a state summary. The roadmap track's *current next concrete step* and the session-close summary's first line both exist for this. You re-enter by reading one line and moving, then pull more context only if the next step needs it. A re-entry surface that opens with a wall of state, forcing you to re-derive the next move, has lost the point of the method.

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
- **What to produce** — for R1 briefs, the reconnaissance contract (see *Output contracts*): plan, decision points, the evidence map, assumptions, what would NOT be done without go-ahead.
- **Output** — `<this-file>-feedback.md` adjacent.
- **Discipline guardrails** — for R1: *do not implement*. For implementation rounds: show diffs, run tests, etc.

A cycle-opening brief asks the Executor to **think**, not to type. It explicitly forbids implementation.

R1's *high-freedom* register — open-ended text, conceptual goals, exploration permitted — is the point: it lets the Executor surface trade-offs the brief didn't anticipate. Implementation briefs invert this: *low freedom*, exact diff discipline, named files, tests required. R2+ briefs sit between. **Brief specificity matches the round.**

When the executor tool is Claude Code, **plan mode** is the natural substrate for R1: its read-only-by-design constraint enforces the reconnaissance/mutation separation by tool rather than by honor system. The methodology stays portable across tools; the binding to a specific tool is platform-specific.

**The direction check.** The adversarial gate (below) scrutinizes the Executor's plan. Nothing otherwise scrutinizes *yours* — and for a single principal, your own framing is the unguarded single point of failure: the method routes all judgment to one person and then never checks it. Before a cycle-opening brief goes out, run a short check on the brief itself. It is far cheaper to catch a mis-framed brief here than after the Executor spends a cycle answering the wrong question:

- **Frame.** Am I solving the right problem, or the first one that came to mind?
- **Adjacent domains.** What neighboring domain — flagged by the project's personas or invariants — bears on this that I haven't pulled in?
- **Assumption.** What am I treating as settled that isn't?

This is the same instinct as a domain-scan pass turned on your own direction. Adopt it when a cycle has come back well-executed but aimed at the wrong target; until then, ordinary framing is enough.

### Round 2+ — review and refine

The Executor's feedback gets reviewed by Chat + human. The decisions surfaced get answered. The plan gets refined. A round-2 brief may follow, narrower in scope. Iterate until scope is genuinely locked and implementable.

**The adversarial gate.** Structured scrutiny at the R1→R2 transition, aimed at the Executor's plan. Ad-hoc review tends to drift toward agreement; the gate's job is to force four specific checks before the plan moves forward. Apply each lens explicitly to the R1 feedback before drafting the next brief:

- **Skeptic.** What does the plan assume that could be wrong? What did the Executor not question?
- **Invariant.** Does the plan touch anything in `INVARIANTS.md`? Does any proposed change create a new assumption that belongs there?
- **Scope.** Has the Executor proposed more than the brief asked? Is scope expanding beyond the roadmap track?
- **Omission.** What did the Executor *not* say? Are there adjacent areas the plan silently affects?

Note each lens's findings before drafting the next brief. Adopt when ad-hoc review starts letting issues through; ordinary review is enough until that pattern shows up.

**Trust calibration.** Uniform review every cycle doesn't compound; calibrated review does. As cycles accumulate, note where the Executor has been reliable and where it has burned you, and let that shift review weight — lighter scrutiny on proven-reliable zones, concentrated scrutiny on the rest. This is the attention-preservation goal applied to review itself. Keep the record informal (a few lines, not a system) until it earns more; a heavyweight reliability tracker is its own bureaucracy.

### Final round — implementation

A locked-scope brief the Executor runs in **mutation** mode, against the mutation contract (see *Output contracts*): files changed, tests run, risks, manual checks, rollback. Show-diff-before-write applies to any file changes. The feedback file remains the audit trail.

**A note on sub-agent dispatch.** When a brief is handed off to a sub-agent (rather than the primary executor session continuing the work), include all needed context explicitly in the brief — sub-agents start fresh with no inherited conversation history. Treat brief files as self-contained when sub-agents are in play. This is the single most common cause of sub-agent failures.

**The positive form: specify the interface.** A sub-agent brief should state explicitly what the sub-agent **receives** (the brief plus named files, nothing else), what it **returns** (a condensed result document — plan, decisions, summary — not raw intermediate reasoning), and what it **discards** (exploration dead-ends, redundant tool outputs, anything the parent doesn't need to read). Without the interface specified, sub-agents either over-share — drowning the parent in noise — or under-share — omitting what the parent needs to decide.

### Closure mechanics (future)

The end-state where Chat dispatches Executor briefs directly and reads the feedback inline — closing the human-as-messenger loop — is a design direction, not yet built. It is one of two deliberately deferred bindings; the trigger (re-expressed in cost terms) and the reasoning are in the companion's *Closure mechanics* and *Deferred bindings* notes.

### Escalation for large cycles

The default cycle-brief protocol is single-actor conversational — R1 brief → review → R2+ refinement → implementation. For cycles too large to span comfortably in one session, escalate to a persistent multi-document shape: a spec doc (what we're building and why), a plan doc (how it decomposes), and a tasks doc (discrete trackable steps).

This converges with what spec-driven tools produce by default (Spec-Kit, Kiro — see the companion for the mapping). Use the escalated form when the cycle clearly spans more than one working session; otherwise the conversational form is faster.

---

## Failure modes

The happy path — Chat briefs the Executor, reconnaissance surfaces decisions, Chat reviews, mutation proceeds — is the easy case to document. These are the failures that actually bite, each mapped to the mechanism that catches it. If a failure recurs and *no* mechanism catches it, that is the friction that justifies a new rule.

| Failure | Symptom | Caught by |
|---|---|---|
| Stale Executor context | Plan references code or conventions that have since changed | Reconnaissance + evidence map (*inspected* vs *unverified*) |
| Over-confident feedback | Plausible plan, unstated unknowns | Evidence map; Skeptic + Omission lenses |
| Over-scoped plan | Executor proposes more than the brief asked | Scope lens; locked-scope implementation brief |
| Hallucinated conventions | Executor invents repo patterns that don't exist | Evidence map; Invariant lens |
| Wrong target, well executed | Cycle comes back clean but answers the wrong question | The direction check (run *before* dispatch) |
| Duplicate artifacts | A second doc or term created for an existing concept | Glossary discipline; handbook as the locational index |
| Glossary overgrowth | Low-value terms accumulate; the glossary becomes a graveyard | Tightened add-trigger (recurrence *and* likely reuse) |
| Anchor conflict | A plan quietly implies changing an invariant | Anchors-as-constitution precedence; Invariant lens |
| Silent artifact drift | An agent edits a canonical doc without review | Propose-then-commit (anchors/glossary change only by human commit) |
| Premature binding | A tool encodes a rule before friction proved the need | Anti-bureaucracy guardrail; friction audit |
| Method leakage | Full apparatus applied to a small effort | Scale-to-stakes (see *Bootstrapping*) |
| Re-entry stall | Context is all present but the session won't start | Re-entry surface leads with the single next action |
| Process-as-avoidance | Building or refining the method substitutes for doing the work | Escalation threshold (don't invoke below it); scope-intake gate (name the slice); kill criteria |
| Stale next action | The re-entry line points at a step already done or overtaken | Session-close rewrites the next action first; the roadmap is the re-entry surface, kept current |
| Memory ⊥ artifacts | Platform memory contradicts the visible repo state | Visible artifacts win (see *Project context*); memory is a cache, not the source of truth |

---

## Operating rules

These apply in Chat sessions regardless of mode.

1. **Step by step.** Don't solve ahead of the conversation. Wait for direction. (This governs session behaviour, not project-structure design — the workspace shape is deliberate, not solved-ahead.)
2. **Direct register.** No hedging, no diplomatic softening. If reasoning has a gap, say so plainly.
3. **High-level and conceptual.** Default register for Chat. Push details to Executor briefs — but inspect a targeted piece of evidence directly when it changes a decision (see *Chat*).
4. **Sharpen, don't guess.** Vague description? Ask a pointed question rather than infer.
5. **Track the arc.** Notice when conversation drifts; ask if it's intentional.
6. **Don't assume cached internals.** Codebases change fast. Verify current state — or ask the Executor to investigate — before proposing changes.
7. **Bias toward concrete deliverables.** Working artifacts shape design more than planning documents do.
8. **Explicit exclusion zones.** If parts of the project are out of scope for Chat conversations (proprietary domain, third-party material, etc.), the project context file declares them. Filter ruthlessly when reading material adjacent to these zones.
9. **Drop findings, don't carry them.** When Chat notices an issue that isn't the topic of the current session, append to `findings-from-chat.md` and move on. Don't expand the current conversation to absorb it.

---

## Bootstrapping a new project

You are here because the work crossed the escalation threshold (see *When to invoke*); now **scale the apparatus to the stakes**. The full workspace shape is for a durable system whose confusion is expensive — work that affects others or that you'll carry for months. Most efforts need far less, and applying the full structure to a small one is the *method leakage* failure above. As a descriptive guide, not a taxonomy to file every effort into:

- A one-off chore lives in a single chat — no workspace.
- A recurring chore earns one checklist or note.
- A research or analysis thread earns a context note, a source log, and the findings inbox — but no implementation structure.
- A small software or process improvement earns a project context file, a brief, and a feedback file.
- A durable internal system earns the full shape below.

**For a durable system, bootstrap incrementally** — the same philosophy as realignment, not a day-one file-creation marathon. The single highest-leverage artifact is the project context file; write it and you can start working. The rest accrues on friction:

1. **Write the project context file.** A 1–2 page conceptual orientation. Load it as a platform project file so it persists across sessions and devices. This alone lets every Chat session start oriented.
2. **Write a one-page handbook** pointing at what exists so far. It grows as artifacts appear.
3. **Stub one anchor** — usually `PHILOSOPHY.md` (what this is and isn't for). Add `INVARIANTS.md` and `AUDIENCE_PERSONAS.md` when a decision or a breakage demands them, not before.
4. **Define one roadmap track** and use it to exercise the cycle-brief pattern end to end.
5. **Seed the glossary on demand** — entries as terminology negotiations arise.
6. **Start a Chat session** with the context loaded, frame the first cycle brief together, dispatch to the Executor, review the feedback, iterate.

The folders (`anchors/`, `roadmap/`, `session-starters/`, `audits/`, `overlays/`) and the remaining root files appear when the work calls for them. The structure that survives partial adoption is the structure that gets adopted.

---

## Realigning an existing project

For projects already in motion, retrofit incrementally — the same incremental philosophy that now governs bootstrap:

1. **Inventory what exists.** Where does design intent currently live (issues, docs, README, scattered chat)? Where does maintenance get planned? What's the current AI-agent collaboration pattern, if any?
2. **Write the project context file first.** It is the single highest-leverage artifact. It lets every Chat session start oriented.
3. **Write the handbook second.** Once you know what's where, capture it. The handbook is fast to write once the inventory is done.
4. **Add anchors as you reference them.** Don't write the full set up front. Write `PHILOSOPHY.md` when a decision needs the project's values stated. Write `INVARIANTS.md` when something gets broken that shouldn't have been.
5. **Adopt the cycle-brief pattern on the next piece of work.** Don't backfill old work into the structure. Use it forward.
6. **Move toward the roadmap / session-starter split** as you start a second track of work. With one track, you can keep everything in your head. With two, you need the artifacts.
7. **Seed the glossary on demand.** Add entries as terminology negotiations arise, not preemptively.

Realignment is gradual. The methodology survives partial adoption better than most.

---

## Tool bindings

Some rules may eventually earn a **tool binding** — the encoded form that runs a rule automatically rather than by discipline (a Skill, a plan-mode constraint, a scoped sub-agent, a scheduled audit run). Not every rule wants embodiment. **Adopt a binding only when the manual discipline shows real friction.** Premature binding produces bureaucracy that drifts from the rule it was meant to encode.

Two bindings are deliberately **deferred** in this version and should not be built yet: the **Chat→Executor MCP dispatch** loop (deferred on a cost-based friction trigger) and **auto-synthesis of canonical artifacts** (deferred on a stronger ground — auto-writing the constitution destroys the curation that makes it canonical; use propose-then-commit instead). The full concept → binding → trigger roadmap, and both deferral rationales, live in the companion.

---

## Scope — what this is and isn't

This is a methodology for *how you collaborate with LLMs on a project*, not how you write code and not how you schedule work. It requires no particular LLM, IDE, or platform; it's compatible with whatever engineering and project-management practices you already use. It is an evolving draft.

It is built for a **single principal**. Multi-human team adoption — who writes briefs, who accepts feedback, who arbitrates the glossary, who decides an artifact pays its way — is an explicit **non-goal** of this version, not an unsolved part of it. If the method ever generalizes to teams, that is later work.

The full version of these boundaries, what's distinctive about the method, and where it sits in the ecosystem are in the companion (`hooman-notes.md`).

---

*Operating guide. The why, provenance, and references: see **`hooman-notes.md`** (same gist).*

