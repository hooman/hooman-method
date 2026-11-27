# Swift comment standard

v0.1 (2026-11-27) · draft · cited by note C of [`swift-conventions.md`](swift-conventions.md).
Adapted from a private comment standard for shell and installer code, rewritten for Swift
libraries. Rules grow from friction, not anticipation: each assumption class cites the failure
it came from.

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
- cm.9 — **A prologue for every file:** what it is for, where it sits in the design (a link to
  the doc or decision), and the rules its callers rely on.
- cm.10 — **A doc comment carries what callers rely on:** preconditions, guarantees, error
  cases, limits, ownership and lifetime. It never restates the name. A self-evident
  declaration gets no doc comment, which is why a "document every public declaration" lint
  stays off.
- cm.11 — **Edge cases where they are handled:** empty, at the limit, one past it, `Int` on a
  32-bit target, hostile input. Say which are handled, and why the others cannot happen.
- cm.12 — **In a public repository, evidence stays generic:** the tool, version, platform and
  date. Never people, machines, private issues or internal incidents. Keep those pointers in
  a private record.

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

## The pass

- cr.1 — **"I cannot write a clean justification here" is a bug signal,** not a cue for a
  vaguer comment. Fix the code, or prove the bound, then write the comment.
- cr.2 — **The pass also removes comments:** ones that restate the code, ones that have
  drifted from it, and a `TODO` with no tracking pointer. A stale comment is worse than none.
- cr.3 — **When it runs:** after the code compiles and its tests and lint pass, and before
  the expensive step: review, a release, a hardware run. In a governed project that means
  every runtime PR before review, and the docs pass before each release.
- cr.4 — **The pass is tested.** Seed a known defect, such as one of the cited evidence
  cases, and confirm that a pass reading only this standard and the code flags it.
