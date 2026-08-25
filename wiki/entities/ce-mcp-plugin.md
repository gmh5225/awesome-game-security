---
title: CE MCP Plugin
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Eruditi__CE-MCP-Plugin.md
updated: 2026-08-25
confidence: medium
---

# CE MCP Plugin

**CE MCP Plugin** (Eruditi/CE-MCP-Plugin) is a **Cheat Engine plugin** that exposes memory editing and process-control features through an **AI-oriented command channel**. Implemented in **C with Lua integration**, it uses **asynchronous TCP** communication to receive and execute remote instructions without blocking the CE host interface. (source: wiki/sources/descriptions/Eruditi__CE-MCP-Plugin.md)

The command set covers memory read/write, value freezing, disassembly and assembly, process management, and DLL injection. Primary use case: automating game memory research workflows from external tooling and experimenting with **AI-assisted Cheat Engine control** — Game Develop / MCP for Cheat Engine lane.

Unlike [[cheatengine-mcp-bridge]] (named-pipe IPC + Python FastMCP + CE Lua worker), this path is an **in-process CE plugin** with a **TCP remote-command channel**. Contrasts with [[memmcp]] (standalone Python CE-like MCP without full CE runtime) and [[dsh-cheatengine]] (DeepSeek Harness TCP `ce_*` tools rather than native CE plugin semantics).

## Links

- Repo: https://github.com/Eruditi/CE-MCP-Plugin

## Related

[[cheat-engine]] · [[cheatengine-mcp-bridge]] · [[dsh-cheatengine]] · [[memmcp]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
