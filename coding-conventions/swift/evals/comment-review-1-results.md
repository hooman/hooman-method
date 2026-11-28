# Comment-review eval 1: results, run 1 (2026-11-27)

**The run:**
- **Who:** a fresh subagent. It did not write the standard, the fixture or the key.
- **Inputs:** only the three fixture files: the standard at `5b51294`, with the redactions the key describes, and the two builder files at capnproto-swift `3255db7`. It had no git, repository or web access.
- **When:** the key was committed first, at `d1cbf77`.
- **Grading:** preliminary, by the session that prepared the run (the key forbids that session grading alone); **the principal confirms it.**

## Recall: 2 of 2

| Key | Found as | Location and consequence | Verdict |
|---|---|---|---|
| K1 | F1, must fix (ca.1, ca.5, cm.4, cr.1) | `linkStruct` and `linkList`, at the `offsetWords &<< 2` stores. Above 2^29 words a pointer is written truncated and the build reports success. It gave a concrete 5 GiB case, and proposed the same 2^29-word cap #22 adopted | found |
| K2 | F2, should fix (ca.4, ca.5, cm.5) | `linkList`'s composite branch. An oversized size is truncated in the tag; a negative one shrinks `used`, so later allocations overwrite live objects | found; the key would rate it must fix |

F1 says it found K1 by cr.1: it tried to write the cm.4 justification for the truncation and could not.

## Extras

| # | Finding | Preliminary verdict |
|---|---|---|
| F3 | After a failure, a list view reports `count == 0`, so a caller that loops over `list.count` adds nothing to `requiredByteCount`, and the retry still fails | **valid and new.** Confirmed in the code: `ListLayout.phantom` sets `count: 0`. It was not in the key and was unknown before the run |
| F4 | The `listTooLong` doc comment says lists "arrive in a later release" | valid; #22 had already fixed it |
| F5 | Generic integer conversions have no ca.3 comment | taste. The Embedded gate passes, so they don't allocate, but saying why is in the spirit of ca.3 |
| F6 | The header's "every pointer points forward" omits the zero-sized struct's offset −1 | valid, minor |
| F7 | Text and data cost a nesting level here, which may be stricter than readers | to check against capnproto-swift's reader. A false refusal at worst, never false success |
| F8 | No doc comments on the `CapnpListBuilder` requirements and the `element(at:)` getters; an out-of-range read returns zero silently | valid (cm.10) |

No false positives.

## Process note

The subagent could not write its report file ("Subagents should return findings as text"), so it returned the report as its final message, and this file records it.
