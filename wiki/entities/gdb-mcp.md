---
title: gdb-mcp
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/jtang613__gdb-mcp.md
updated: 2026-08-02
confidence: medium
---

# gdb-mcp

Lightweight MCP (Model Context Protocol) server that bridges GDB to AI assistants via FastMCP and SSE transport. LLMs control live GDB debugging sessions through a gdb-command proxy—breakpoints, memory inspection, register reads, and stepping—enabling AI-assisted dynamic analysis for reverse engineers and game-security researchers. (source: wiki/sources/descriptions/jtang613__gdb-mcp.md)

Peer to [[mcp-gdb]] (signal-slot) with a FastMCP + SSE stack rather than GDB MI-only wiring; complements [[mcp-windbg]] for Windows kernel dumps and MCP RE tooling such as [[ida-pro-mcp]] / [[ghidra-headless-mcp]].

## Links

- Repo: https://github.com/jtang613/gdb-mcp (README tag: Lightweight MCP server for GDB automation — FastMCP, SSE, gdb-command proxy)

## Related

[[overviews/reverse-engineering]] · [[mcp-gdb]] · [[mcp-windbg]] · [[pince]] · [[gdb-windows-binaries]] · [[ida-pro-mcp]]
