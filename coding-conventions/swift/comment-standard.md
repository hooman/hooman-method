# Swift comment standard

v0.2 (2026-11-27) · draft · cited by note C of [`swift-conventions.md`](swift-conventions.md).
Adapted from two private sources, rewritten for Swift: a comment standard for shell and installer
code, and the literate-clarity rules of a Swift project. Rules grow from friction, not
anticipation: each assumption class cites the failure it came from. Evidence labels are those of
`swift-conventions.md`: [V] verified, [S] primary source, [?] unverified.

A comment says **why**; the code already says what. The standard has two uses: a guide while
writing, and the checklist of a **comment-review pass**. That pass is a bug hunt, not a
writing task. Trying to justify a line in prose is a second read of the logic with a different
goal, and the lines that resist justification are where the defects are (cr.1).

Findings cite rule ids. An id is never renumbered or reused; a retired rule keeps its id,
marked retired.

## What a comment carries

- cm.1 — **Why, not what.** No comment restates the line below it.
- cm.2 — **The technique or invariant, named, with its source:** a spec section, an SE
  proposal, a paper. "Bump allocation; every pointer points forward" can be checked against
  its definition. A narrated sequence of steps cannot.
- cm.3 — **Every deviation** from the idiomatic or obvious form, and why it is needed. If the
  code looks wrong at a glance and is not, that is a comment.
- cm.4 — **Every operation that can lose information silently:** `truncatingIfNeeded`,
  wrapping operators (`&+`, `&<<`), `bitPattern` conversions, `unsafe`, `!` and `try!`. The
  comment names the bound that makes it safe and where that bound is enforced.
- cm.5 — **Every skipped or narrowed check:** the error that is not handled, and why it cannot
  arise here, or why it is acceptable if it does.
- cm.6 — **Every non-obvious ordering dependency:** why B must follow A, especially when they
  are far apart.
- cm.7 — **The observed failure behind defensive code,** so a later reader does not simplify
  it back out.
- cm.8 — **Dated evidence on a toolchain or platform fact:** the tool, the version and the
  date, with the condition for removing a workaround ("Swift 6.2 and 6.3 only").
- cm.9 — **A prologue for every file, and for every type with rules of its own:** what it is
  for, where it sits in the design (a link to the doc or decision), and the rules its callers
  rely on.
- cm.10 — **A doc comment carries what callers rely on:** preconditions, guarantees, error
  cases, limits, units, ownership and lifetime, and what `nil` means. Use DocC callouts where a
  contract exists (`- Precondition:`, `- Postcondition:`, `- Invariant:`, `- Complexity:`,
  `- Important:`, `- Warning:`; the full list is swift-markdown's `Aside.Kind` [S]). A summary
  never only restates the name. Whether a lint requires a doc comment on every public
  declaration is the project's choice. Where one does, a required summary on a declaration
  with a hidden contract (a persisted value, a wire field) must state it.
- cm.11 — **Edge cases where they are handled:** empty, at the limit, one past it, `Int` on a
  32-bit target, hostile input. Say which are handled, and why the others cannot happen.
- cm.12 — **In a public repository, evidence stays generic:** the tool, version, platform and
  date. Never people, machines, private issues or internal incidents. Keep those pointers in
  a private record.
- cm.13 — **Comments are code.** A comment that contradicts the code is a bug, and is reviewed
  as one, and it is the finding reviews most often miss. No commented-out code, and no
  history in comments; git holds it.

## Assumption classes to walk

For code that is Embedded-clean, decodes untrusted bytes, or targets 32-bit platforms, check
each class and confirm it is handled and commented, or not applicable.

- ca.1 — **Field widths.** Every store into a narrower field names the bound that keeps it in
  range. *Evidence:* capnproto-swift #22. A 30-bit pointer offset was truncated once storage
  passed 4 GiB, and struct-list sizes were truncated into 16-bit fields.
- ca.2 — **`Int` is 32 bits on Wasm and microcontrollers.** Every product, shift and
  conversion holds at both widths. *Evidence:* `1 << 32` is 0 on a 32-bit target, caught while writing
  #22. capnproto-swift has dedicated 32-bit suites under WasmKit and QEMU.
- ca.3 — **Hidden allocation.** Variadic calls, generic integer conversions, existentials,
  escaping closures and `modify` coroutines can allocate. On an allocation-free path, say why
  this form is the allocation-free one. *Evidence:* the three-argument `min` allocated an
  array (capnproto-swift `a06efae`); generic widening allocates on 32-bit Embedded
  (`Widen.swift`); public get/set properties emit an allocating `modify` coroutine (D-18).
- ca.4 — **Untrusted input.** Every length, offset and count from outside is bounded before
  use, and arithmetic on it cannot overflow or trap. *Evidence:* the hostile-input reader
  tests of capnproto-swift.
- ca.5 — **Fail loud, never false success.** A path that writes something wrong must report
  an error. *Evidence:* before #22, a struct list with a negative element size built
  "successfully" with a corrupt tag word.
- ca.6 — **API flags that silently do nothing.** Some flag combinations are ignored rather
  than refused. Document what each flag does alone, and refuse a combination the platform would
  ignore. *Evidence:* in a private project, writing the doc comment for an "exclusive" open flag
  found that `O_EXCL` without `O_CREAT` is ignored on macOS (`man 2 open`) [V], so "only if new"
  silently opened an existing file.

## The pass

- cr.1 — **"I cannot write a clean justification here" is a bug signal,** not a cue for a
  vaguer comment. Fix the code, or prove the bound, then write the comment.
- cr.2 — **The pass also removes comments:** ones that restate the code, ones that have
  drifted from it, and a `TODO` with no tracking pointer. A stale comment is worse than none.
- cr.3 — **When it runs:** after the code compiles and its tests and lint pass, and before
  the expensive step: review, a release, a hardware run. In a governed project that means
  every runtime PR before review, and the docs pass before each release.
- cr.4 — **The pass is tested:**
  - a fixture with planted defects and an answer key of rule ids, such as the cited evidence
    cases
  - a scorer that reports recall against the key
  - a run by an agent that didn't write the standard or the fixture
  A person still judges each finding and each extra. The author may prepare a run, but never
  grades it.
- cr.5 — **The report:**
  - each finding cites its rule id, `file:line`, a severity (must fix, should fix, consider)
    and a concrete fix
  - a "Verified" section names what was checked and found sound
  - few, certain findings are better than many speculative ones; a doubtful one goes under
    "consider", with the reasoning
