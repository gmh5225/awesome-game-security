---
title: cheatengine-mcp-bridge
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/miscusi-peek__cheatengine-mcp-bridge.md
updated: 2026-07-29
confidence: medium
---

# cheatengine-mcp-bridge

MCP bridge that connects AI agents to a live Cheat Engine instance over a named-pipe IPC path. A Lua worker thread inside CE stays synchronized with a Python FastMCP server, targeting sub-2ms command latency. Exposes 40+ tools for memory reads, AOB scanning, pointer-chain traversal, structure dissection, RTTI class identification, hardware breakpoints (DR0–DR3), and DBVM hypervisor-level tracing. (source: wiki/sources/descriptions/miscusi-peek__cheatengine-mcp-bridge.md)

Unlike standalone Python memory MCP servers such as [[memmcp]], this path drives the full CE runtime (Lua engine, scanner, debugger, DBVM) rather than reimplementing CE-like primitives. Pairs with CE Lua plugins such as [[gddumper]] and AC-facing CE detection research such as [[cedetector]].

## Links

- Repo: https://github.com/miscusi-peek/cheatengine-mcp-bridge

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[memmcp]] · [[gddumper]] · [[cedetector]] · [[dma-cheat-engine-loader]] · [[ghidra-headless-mcp]] · [[ida-pro-mcp]] · [[mcp-windbg]]
