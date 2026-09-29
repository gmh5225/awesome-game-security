---
title: cheat-mcp
kind: entity
topics: [game-hacking, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/AnonymoDGH__cheat-mcp.md
updated: 2026-09-29
confidence: medium
---

# cheat-mcp

**cheat-mcp** (AnonymoDGH/cheat-mcp) is a **Windows-native Model Context Protocol server** that exposes live game-process memory tooling to AI assistants over **JSON-RPC on stdio**. Built in **C++17**, it targets game security researchers, reverse engineers, and anti-cheat analysts who need LLM-driven automation for Windows memory analysis and security assessment. (source: wiki/sources/descriptions/AnonymoDGH__cheat-mcp.md)

## Capabilities

- **Process and module inspection** — enumerate targets, modules, and memory regions for cross-process analysis.
- **Memory R/W and scanning** — Cheat Engine–style value and array-of-bytes scans, pointer resolution, byte patching, freeze and watch loops.
- **Injection** — DLL or shellcode injection via LoadLibrary, manual map, APC, and related methods.
- **Runtime hooks** — IAT hooking and time-scaling hooks for speed manipulation.
- **Anti-cheat reconnaissance** — detect user-mode modules and kernel drivers associated with [[easy-anti-cheat]], [[battleye]], and [[vanguard]]; debugger checks, foreign handle enumeration, network capture or injection.

Unlike [[cheatengine-mcp-bridge]] (named-pipe IPC driving a full Cheat Engine runtime) or [[ce-mcp-plugin]] (in-process CE plugin with async TCP), cheat-mcp is a **standalone native MCP server** that reimplements CE-like memory and injection primitives without requiring CE installed. Contrasts with Python [[memmcp]] (lighter CE-like MCP) and [[dsh-cheatengine]] (DeepSeek Harness TCP `ce_*` bridge).

## Links

- Repo: https://github.com/AnonymoDGH/cheat-mcp

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[cheatengine-mcp-bridge]] · [[ce-mcp-plugin]] · [[memmcp]] · [[dsh-cheatengine]] · [[cheat-engine]] · [[processhacker-mcp]]
