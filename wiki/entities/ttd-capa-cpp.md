---
title: ttd-capa-cpp
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/HullaBrian__ttd-capa-cpp.md
  - wiki/sources/README-categories.md
updated: 2026-09-22
confidence: medium
---

# ttd-capa-cpp

**ttd-capa** (HullaBrian/ttd-capa-cpp) is a **capa-compatible capability extractor** that analyzes Microsoft **Time Travel Debugging (TTD)** traces to surface malware and program behavior that static file scans cannot see. (source: wiki/sources/descriptions/HullaBrian__ttd-capa-cpp.md)

Written primarily in C++ with Python wrapper scripts, it replays recorded execution traces through a native extractor built on the TTD SDK, decodes API call arguments using Win32 and native API metadata indexes, and matches results against capa rules via a high-performance C++ capa reimplementation. README category: Cheat / RE Tools.

## Key features

- Dynamic API-call extraction from full-process TTD recordings
- Optional code-region scanning to recover capabilities from unpacked or runtime-generated code
- Timeline reporting of when matched capabilities executed
- Embeddable DLL for integration into custom analysis pipelines

## Audience

Reverse engineers, malware analysts, and game security researchers who need **behavioral capability detection** from TTD traces rather than static binaries alone. Pair with [[static-runtime-evidence]] when separating static inference from trace-backed findings.

Complements TTD replay tooling such as [[ttddbg]] (IDA `.run` trace replay), programmatic WinDbg/TTD stacks such as [[windbg-tool]] and [[mcp-windbg]], and TTD anti-debug stress samples such as [[ttd-anti-debugging]].

## Links

- Repo: https://github.com/HullaBrian/ttd-capa-cpp

## Related

[[overviews/reverse-engineering]] · [[static-runtime-evidence]] · [[ttddbg]] · [[windbg-tool]] · [[mcp-windbg]] · [[windbg-decompile-ext]] · [[ttd-anti-debugging]] · [[tenet]] · [[execution-trace-viewer]] · [[dynamic-binary-instrumentation]]
