---
title: x64dbg Trace Reader
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mibho__x64dbgTraceReader.md
updated: 2026-07-30
confidence: medium
---

# x64dbg Trace Reader

Standalone parser for [[x64dbg]]'s `.trace64` binary trace format. Deserializes instruction records, disassembles them via Capstone, and supports regex-based filtering over execution traces. Reconstructs per-instruction register and memory state from the compact trace buffer for **offline** analysis after a debug session. (source: wiki/sources/descriptions/mibho__x64dbgTraceReader.md)

Complements live tracing inside x64dbg and general trace viewers such as [[execution-trace-viewer]] when working specifically with x64dbg's native trace export format.

## Links

- Repo: https://github.com/mibho/x64dbgTraceReader

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[execution-trace-viewer]] · [[xfindout]]
