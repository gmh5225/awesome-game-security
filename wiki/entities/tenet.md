---
title: tenet
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__tenet.md
updated: 2026-08-07
confidence: medium
---

# tenet

IDA Pro plugin for exploring **program execution traces**. Provides a trace timeline visualization with forward and backward stepping through recorded execution, register and memory state inspection at any trace point, and visual navigation of complex control flow. Supports multiple trace formats and integrates with IDA's disassembly view. Aimed at reverse engineers using execution traces for malware analysis and vulnerability research. (source: wiki/sources/descriptions/gmh5225__tenet.md)

Complements WinDbg TTD replay in IDA via [[ttddbg]] (`.run` captures) and general trace viewers such as [[execution-trace-viewer]] and [[x64dbg-trace-reader]] when the workflow stays inside IDA's static-analysis UI.

## Links

- Repo: https://github.com/gmh5225/tenet

## Related

[[overviews/reverse-engineering]] · [[ttddbg]] · [[execution-trace-viewer]] · [[x64dbg-trace-reader]] · [[ida-pro-mcp]]
