---
title: ttd-capa-cpp
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/HullaBrian__ttd-capa-cpp.md
  - wiki/sources/README-categories.md
updated: 2026-09-22
confidence: medium
---

# ttd-capa-cpp

**ttd-capa** (HullaBrian/ttd-capa-cpp) is a **capa-compatible capability extractor** that analyzes Microsoft **Time Travel Debugging (TTD)** traces to surface malware and program behavior that static file scans cannot see. Written primarily in C++ with Python wrapper scripts, it replays recorded execution traces through a native extractor built on the TTD SDK, decodes API call arguments using Win32 and native API metadata indexes, and matches results against capa rules via a high-performance C++ capa reimplementation. Features include dynamic API-call extraction, optional code-region scanning to recover capabilities from unpacked or runtime-generated code, timeline reporting of when capabilities executed, and an embeddable DLL for integration into custom analysis tools. README category: Cheat / RE Tools. (source: wiki/sources/descriptions/HullaBrian__ttd-capa-cpp.md)

Complements TTD replay tooling such as [[ttddbg]] (IDA `.run` trace replay), WinDbg-centric stacks such as [[mcp-windbg]] and [[windbg-decompile-ext]], and TTD anti-debug stress samples such as [[ttd-anti-debugging]].

## Links

- Repo: https://github.com/HullaBrian/ttd-capa-cpp

## Related

[[overviews/reverse-engineering]] · [[ttddbg]] · [[mcp-windbg]] · [[windbg-decompile-ext]] · [[ttd-anti-debugging]] · [[tenet]] · [[execution-trace-viewer]] · [[dynamic-binary-instrumentation]]
