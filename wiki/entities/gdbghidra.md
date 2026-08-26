---
title: gdbghidra
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Comsecuris__gdbghidra.md
updated: 2026-08-26
confidence: medium
---

# gdbghidra

**gdbghidra** — bridge that synchronizes live GDB debugging context with the Ghidra UI. Combines a GDB-side Python client with a Java Ghidra extension to exchange execution state in real time: cursor and stack synchronization, register propagation into decompilation context, breakpoint control, and relocation handling. Built for reverse engineers who want interactive debugging and static analysis to stay aligned in one workflow. (source: wiki/sources/descriptions/Comsecuris__gdbghidra.md)

Complements Ghidra automation bridges such as [[ghidra-bridge]] (CPython scripting) and agent-facing MCP paths like [[ghidramcp]] / [[ghidra-headless-mcp]]; pairs live GDB sessions with [[gdb-mcp]] / [[mcp-gdb]] when mixing manual debugger control and LLM-assisted analysis.

## Links

- Repo: https://github.com/Comsecuris/gdbghidra (README: GDB session)

## Related

[[ghidra]] · [[ghidra-bridge]] · [[gdb-mcp]] · [[mcp-gdb]] · [[gdb-windows-binaries]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
