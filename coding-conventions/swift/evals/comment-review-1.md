# Comment-review eval 1: capnproto-swift builders before #22

Answer key, committed before the run (subst.1, cr.4).

**The fixture:** two files of [capnproto-swift](https://github.com/hooman/capnproto-swift) at
`3255db7`, before PR #22:
- `Sources/CapnpRuntime/MessageBuilder.swift`
- `Sources/CapnpRuntime/ListBuilder.swift`

**The reader:** a fresh agent that did not write the standard. It reads only those two files
and the standard at hooman-method `5b51294`, then runs the pass. It never sees git history,
#22 or this key.

**The redaction:** in the copy it reads, the evidence lines of ca.1, ca.2 and ca.5 say
"[redacted for this eval]", because they describe the defects below.

## Key: the two defects a pass must find

- **K1 (cm.4, ca.1, cr.1): pointer offsets can be truncated.**
  - `linkStruct` in `MessageBuilder.swift` and `linkList` in `ListBuilder.swift` store
    `UInt32(truncatingIfNeeded: offsetWords &<< 2)`, with no stated bound.
  - A near pointer's offset is a signed 30-bit word count, but `init(storage:)` accepts
    up to 2^32 − 1 words.
  - With more than 4 GiB of storage, an object can land beyond 2^29 − 1 words, and its
    pointer is silently wrong.
- **K2 (cm.4, ca.1, ca.5): struct-list element sizes are not checked.**
  - `linkList` writes the inline-composite tag word from `shape.dataWords` and
    `shape.pointerCount` through `truncatingIfNeeded`.
  - It never checks them against 0...0xFFFF, as `linkStruct` does.
  - The sizes come from a public protocol's `_capnpDataWords` and `_capnpPointerCount`.
  - An out-of-range size is truncated. A negative one shrinks the allocation, and the
    build still reports success.

## Scoring

- **Recall:** a key item counts as found only when the finding names its location and its
  consequence. A rule id alone does not count.
- **Extras:** a person judges each extra finding as valid, a matter of taste, or a false
  positive.
- **Grading:** the session that wrote the standard prepared this run and does not grade it
  alone. The principal confirms the verdict.
