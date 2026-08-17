---
title: ToCode
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/buzzer-re__ToCode.md
updated: 2026-08-17
confidence: medium
---

# ToCode

Binary-to-source analysis tool that transforms executables into source-code-like project trees coding agents can traverse, analyze, and use as an oracle for large binaries. Uses **IDA Pro** or **radare2** backends to decompile functions, cluster them by similarity, generate meaningful names, and export structured analysis results with **Semgrep** rule integration. (source: wiki/sources/descriptions/buzzer-re__ToCode.md)

Complements live MCP disassembler bridges ([[ida-pro-mcp]], [[radare2-mcp]]) by materializing an offline, agent-readable corpus instead of requiring a connected RE session. Pairs with whole-program summarization pipelines such as [[gpt-wpre]] and function-similarity tooling such as [[binlex]] / [[mcrit-plugin]] for large-scale binary triage.

## Links

- Repo: https://github.com/buzzer-re/ToCode

## Related

[[overviews/reverse-engineering]] · [[ida-pro-mcp]] · [[radare2-mcp]] · [[gpt-wpre]] · [[binlex]] · [[idaclu]]
