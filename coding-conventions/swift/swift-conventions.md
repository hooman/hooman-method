# Swift Conventions — Coding Guidelines Index

> Global doc in hooman-method; projects name the revision they follow (`project.md`, proj.1). Sibling to `design-stance-swift.md`, which it cites for the *why* (forward-feature orientation). A lean index: it points at rules, it does not restate them. A project keeps its own specifics: floors, toolchain pins, and which optional lints are on.
>
> **v0.2 · 2026-11-27 · draft.** Seeded from friction in two Swift projects, capnproto-swift and a private one. Categories grow as friction appears, not by anticipation.

Evidence labels: **[V]** verified, with the tool, version, OS and date; **[S]** primary source; **[?]** unverified.

## How to use

Before writing code, find the **task-type** below and read the linked rules. The draft PR's design step names the rows it relies on. Each row carries a **when-enforced** tag that says which pass owns it:

- **coding-time** — shapes the code, and can't be retrofitted.
- **review** — enforced in review or in the comment-review pass, as judgement rather than counts.
- **tool** — a mechanical pass: the compiler, the formatter or a linter.

*Forward-path discipline (all rows): when a current-idiom tool or API snags, surface it as a decision point — don't silently fall back to its legacy equivalent. This is the universal stance's "never silently default," applied to tooling.*

## Taxonomy

| Task-type | Enforced | Rules live in |
|---|---|---|
| Compiler settings | tool | Swift 6 mode, the upcoming Swift 7 features, strict memory safety, warnings as errors → **note D**. |
| Tests | coding-time | Swift Testing only, never XCTest. Availability, noncopyable values, naming options → **note A**. |
| Types & buffers ("currency types") | coding-time | `[UInt8]` / `Span` over `Data`; Foundation only where it has no alternative → **note B**. Project carrier and alignment: the project's `DECISIONS.md`. |
| Imports | coding-time | → **note B**. A Foundation-free core where Embedded-clean is required: the project's `INVARIANTS.md`. |
| Generics | coding-time | Prefer constraints over existentials; reach for `any P` only deliberately. A hard "never `any P`" is a project invariant where it applies. |
| Naming & API design | coding-time + review | Swift API Design Guidelines — <https://www.swift.org/documentation/api-design-guidelines/>. |
| Fluency | review | Code that reads as Swift, not C → **note E**. |
| Comments & doc comments | coding-time + review | DocC markup → **note C**; what a comment must carry, and the comment-review pass → [`comment-standard.md`](comment-standard.md). |
| Formatting | tool | `swift format` against a committed `.swift-format` (Apple's formatter, bundled in the Swift 6 toolchain). Which documentation rules are on is a project choice (comment standard, cm.10). |
| Lint | tool | SwiftLint — *deliberately* (third-party; its rules don't port off-platform). Not a default. |
| Section markers | coding-time | `// MARK:` when a file has more than one concern, so the outline reads as a table of contents. `// TODO:` and `// FIXME:` name their tracking issue (cr.2). |

*Not yet populated (accrete on friction): concurrency, error handling, logging, …*

## Notes

**A — Swift Testing.**
- **Availability:** `@available` on a `@Test` works. An unavailable test is reported as skipped, with its reason ("Requires macOS 99") [V: Swift 6.4.2, macOS 27.3, 2026-11-27]. Prefer it to a runtime `guard #available`, which passes silently. This corrects v0.1, which said `@Test` can't carry `@available`.
- **Noncopyable values:** hoist them into a local before `#expect` or `#require` [V: a private project, Swift 6.4, 2026-10].
- **Project options:**
  - test names as raw identifiers (SE-0451), which `swift test --filter` matches
  - `package` access in place of `@testable import` [?: that this lets tests run against optimized builds]
- **Setup, not a convention:** `swift test` needs a Swift.org toolchain, not the Command Line Tools. Keep that in the project's `AGENTS.md` or README, since it depends on the environment and goes stale.

**B — Currency types & imports.**
- In portable code, prefer `[UInt8]` and `Span` over `Data`, and choose the integer width and signedness the data actually needs.
- `FoundationEssentials` is **not importable on macOS** [V: Swift 6.4.2, macOS 27.3, 2026-11-27, "unable to resolve module dependency"]. It is expected on Linux through swift-corelibs-foundation [?]. On Apple platforms the choice is Foundation or nothing, so keep Foundation at the edges, where it has no alternative: JSON coding, for example.
- Where Embedded-clean is required, the core imports no Foundation at all. That hard line is the project's `INVARIANTS.md`, not this doc.

**C — Doc-comment markup** (enforced in review).
- Follow DocC markup: `///`, then `- Parameters:`, `- Returns:` and `- Throws:`, and the contract callouts (`- Precondition:`, `- Complexity:`, …).
- Whether those sections are required on every public declaration, or only where they carry something beyond the summary, is a project choice, pending question Q3 of the 2026-11-27 audit.
- What a comment must say, and the pass that checks it, are in [`comment-standard.md`](comment-standard.md). Findings cite its rule ids (`cm.4`).
- Uninferable rationale lives in the project's `DECISIONS.md`, never invented.

**D — Compiler settings,** the default for a new package. Both projects arrived at this set on their own [V: capnproto-swift `Package.swift`, 2026-11-27].
- Swift 6 language mode.
- The six upcoming features that become defaults in Swift 7, listed one by one rather than through a bundle whose contents vary by toolchain:
  - `ExistentialAny` (SE-0335)
  - `InternalImportsByDefault` (SE-0409)
  - `MemberImportVisibility` (SE-0444)
  - `InferIsolatedConformances` (SE-0470)
  - `NonisolatedNonsendingByDefault` (SE-0461)
  - `ImmutableWeakCaptures` (SE-0481)
- `.defaultIsolation(nil)` for libraries and command-line tools; main-actor isolation by default is meant for app targets [?].
- `.strictMemorySafety()` (SE-0458) on production targets, with every `unsafe` construct marked and kept in one layer.
- `.treatAllWarnings(as: .error)`, with CI's toolchain pinned so that an update is deliberate.
- **Caveat:** diagnostics differ between toolchains. For example, 6.3 requires `unsafe` on `withUnsafeBytes` and 6.4 rejects it as redundant [V: a private project, 2026-10]. Gate on the CI toolchain, not only the local one.

**E — Fluency** (review judgement; flag and explain, never count).
- **Say a convention once:** a repeated foreign idiom, such as `-1` plus `errno`, goes in one well-named helper at the narrowest scope.
- **Tables over branches:** a mapping between domains is data.
- **Minimum scope:** local, then `fileprivate`, then the type, then the module.
- **Expressions over statements:** `if` and `switch` expressions; `guard` for preconditions.
- **The loop says what progresses:** `stride`, `zip` and `sequence`, rather than counters and flags.
- **Reuse the model you have.**
- **An abstraction earns its place** only if it makes the call site shorter *and* clearer; clever is not the goal.
- **Names and literals carry meaning.**
- **Short enough to see whole.**

The aim is fewer lines of *code* and more words of *reason*. A fluency pass and a literate pass together can make a file longer, and that is fine. *Evidence:* in a private project's file-system layer, a fluency pass cut a 31-line `open` to 13 lines, and every system call became one readable line. The literate pass then made the files longer again, almost all of it comments carrying intent and evidence [V: 2026-10].

---
*When this outgrows an inline index, it becomes a Skill: this file as the `SKILL.md` router, each note a small bundled detail doc loaded on demand. Accrete, don't proliferate.*
