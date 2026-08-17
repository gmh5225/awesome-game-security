---
title: x64dbg-mcp
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/bromoket__x64dbg_mcp.md
updated: 2026-08-17
confidence: medium
---

# x64dbg-mcp

Model Context Protocol (MCP) server that exposes full [[x64dbg]] control to AI assistants through 23 mega-tools mapping 151 REST endpoints. A TypeScript MCP server uses Zod discriminated unions for type-safe endpoint routing; a native x64dbg plugin (`.dp64` / `.dp32`) bridges the debugger to the REST API. Coverage includes stepping, breakpoints, memory operations, disassembly, tracing, anti-debug bypasses, control-flow analysis, and PE dumping. Compatible with Claude, Cursor, Windsurf, and other MCP clients — aimed at reverse engineers seeking AI-augmented debugging workflows and automated binary analysis through x64dbg. (source: wiki/sources/descriptions/bromoket__x64dbg_mcp.md)

Dedicated MCP + native REST plugin rather than Automate RPC or an in-debugger chat panel: complements [[x64dbg-automate-pyclient]] (Python Automate ZeroMQ/msgpack + optional MCP) and [[x64dbg-rippy]] (WebView2 LLM panel inside x64dbg), and sits beside MCP bridges such as [[ida-pro-mcp]], [[binary-ninja-mcp]], and [[radare2-mcp]] for agent-driven Windows user-mode attach workflows.

## Links

- Repo: https://github.com/bromoket/x64dbg_mcp

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[x64dbg-automate-pyclient]] · [[x64dbg-rippy]] · [[ida-pro-mcp]] · [[binary-ninja-mcp]] · [[radare2-mcp]] · [[rev-tools-setup]]
