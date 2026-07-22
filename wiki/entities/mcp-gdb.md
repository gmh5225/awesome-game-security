---
title: mcp-gdb
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/signal-slot__mcp-gdb.md
updated: 2026-07-22
confidence: medium
---

# mcp-gdb

MCP (Model Context Protocol) server that exposes GDB debugger functionality to AI coding assistants. LLMs can set breakpoints, inspect memory, read registers, step through code, and analyze program state through GDB's machine interface via MCP protocol calls—enabling AI-assisted debugging and binary-analysis workflows for developers and reverse engineers. (source: wiki/sources/descriptions/signal-slot__mcp-gdb.md)

Complements agent debugger bridges such as [[mcp-windbg]] (CDB/WinDbg) and MCP RE tooling such as [[ida-mcp-server-plugin]] / [[memmcp]] by targeting live GDB sessions rather than WinDbg dumps, IDA, or CE-style memory UIs.

## Links

- Repo: https://github.com/signal-slot/mcp-gdb (README tag: MCP for GDB)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[mcp-windbg]] · [[x64dbg]] · [[ida-mcp-server-plugin]] · [[memmcp]]
