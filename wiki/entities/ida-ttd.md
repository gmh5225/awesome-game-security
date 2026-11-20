---
title: ida-ttd
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/HullaBrian__ida-ttd.md
  - wiki/sources/README-categories.md
updated: 2026-11-20
confidence: medium
---

# ida-ttd

**ida-ttd** (HullaBrian/ida-ttd) is an **IDA Pro 9.5 plugin** that loads **time-travel debugging (TTD)** recordings as a full debugger session inside IDA, so analysts can step forward and backward through execution and query the entire trace while staying in IDA’s disassembly and decompiler context. (source: wiki/sources/descriptions/HullaBrian__ida-ttd.md)

It supports Microsoft TTD `.run` files via the TTD Replay SDK and **Sogen** `.sogttd` traces through a modular C++ backend, with companion Python scripting for automation. README category: Cheat / RE Tools.

## Key features

- Bookmarks, timelines, and recording-wide queries
- API and pattern call logging with decoded Win32 arguments
- Memory read/write/execute searches, value origin tracing, syscall and handle inspection
- Coverage and heatmap views; recovered strings and buffers
- Fork-and-compare replay on Sogen recordings

## Audience

Windows x64 reverse engineers and malware or anti-cheat researchers who want recorded execution tied to IDA analysis rather than live-only debugging. Pair with [[static-runtime-evidence]] when separating static inference from trace-backed findings.

Complements lighter IDA `.run` replay via [[ttddbg]], capa extraction from traces via [[ttd-capa-cpp]], and WinDbg-centric TTD stacks such as [[windbg-tool]] and [[mcp-windbg]].

## Links

- Repo: https://github.com/HullaBrian/ida-ttd

## Related

[[overviews/reverse-engineering]] · [[static-runtime-evidence]] · [[ttddbg]] · [[ttd-capa-cpp]] · [[windbg-tool]] · [[mcp-windbg]] · [[tenet]] · [[execution-trace-viewer]] · [[windbg-decompile-ext]] · [[sogen]]