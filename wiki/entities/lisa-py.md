---
title: lisa.py
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ant4g0nist__lisa.py.md
updated: 2026-08-18
confidence: medium
---

# lisa.py

**LLDB integration** that exposes debugger capabilities through a **Model Context Protocol (MCP) server**. Combines Python components for an LLDB plugin and an MCP bridge so AI assistants can drive debugging through structured tool calls — target creation, process control, breakpoints, backtraces, disassembly, memory reads, and expression evaluation. Intended for reverse-engineering and vulnerability research workflows where interactive debugging needs to be automated or assistant-assisted. (source: wiki/sources/descriptions/ant4g0nist__lisa.py.md)

Sits in the same agent-driven debugger lane as [[gdb-mcp]] / [[mcp-gdb]] (GDB) and [[mcp-windbg]] (CDB/WinDbg), but targets LLDB sessions — including macOS/iOS/Android attach workflows where LLDB is the native debugger. Complements LLDB-centric tooling such as [[klldb]] (Linux kernel debugging) and [[lldbext-dump]] (Android live capture → minidump).

## Links

- Repo: https://github.com/ant4g0nist/lisa.py (README tag: MCP for LLDB)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[gdb-mcp]] · [[mcp-gdb]] · [[mcp-windbg]] · [[klldb]] · [[lldbext-dump]] · [[pyre]]
