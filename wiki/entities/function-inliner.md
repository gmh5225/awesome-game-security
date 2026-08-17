---
title: FunctionInliner
kind: entity
topics: [reverse-engineering, game-hacking, mobile-security]
sources:
  - wiki/sources/descriptions/cellebrite-labs__FunctionInliner.md
updated: 2026-08-17
confidence: medium
---

# FunctionInliner

IDA Pro plugin that reverses compiler **function outlining** optimization (e.g. `clang --moutline`) by inlining outlined helpers back into their callers. For each caller it clones the outlined function, replaces `BL` calls with direct branches to the clone, converts clone `RET` instructions to branches back to the caller, and registers each clone as a function chunk. Supports manual context-menu inlining and heuristic batch identification of all outlined functions. Mainly useful when space-optimized ARM binaries break Hex-Rays decompilation and static analysis workflows. (source: wiki/sources/descriptions/cellebrite-labs__FunctionInliner.md)

Not a call-hierarchy UI tool—that lane is [[ida-func-outline]]. Complements Hex-Rays-facing plugins such as [[genmc]] and [[happyida]], and other Cellebrite Labs IDA tooling such as [[ida-kcpp]], [[labsync]], and [[ida-bridge]].

## Links

- Repo: https://github.com/cellebrite-labs/FunctionInliner

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-func-outline]] · [[genmc]] · [[happyida]] · [[ida-kcpp]] · [[labsync]] · [[ida-bridge]]
