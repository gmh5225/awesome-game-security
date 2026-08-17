---
title: ida-bridge
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/cellebrite-labs__ida-bridge.md
updated: 2026-08-17
confidence: medium
---

# ida-bridge

**Agent bridge for IDA Pro 9+** (Cellebrite Labs): a Python framework with CLI, IDA UI plugin, and headless **idalib** runner that connects AI agents to live IDA databases over a WebSocket bridge server. Agents execute **IDAPython** and **SQL** without fragile API knowledge — the SQL layer exposes functions, disassembly, decompiler output, types, cross-references, and other IDB data. Supports stateful/stateless exec sessions, one-shot `exec-idb` headless runs, dyld shared-cache single-module extraction, and reusable analysis snippets; bundled `skills/ida-bridge/` agent skill. Targets reverse engineers and game security researchers for AI-assisted binary analysis, annotation, and exploration. (source: wiki/sources/descriptions/cellebrite-labs__ida-bridge.md)

UI IDA instances connect to a local bridge; agents use `ida-bridge list`, `exec`, and `supervisor` to discover targets, run sessions, and manage IDA lifecycle. When SQL is insufficient, the bundled skill directs agents to pair with **ida-docs** for verified IDAPython. Prerequisites: IDA Pro ≥ 9.0, macOS, optional `ida-setup` for unified `~/.idapro/venv`.

## Links

- Repo: https://github.com/cellebrite-labs/ida-bridge
- Companion skill/API docs: https://github.com/cellebrite-labs/ida-docs

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[idac]] · [[ida-cli]] · [[headless-ida-mcp-server]] · [[ida-pro-mcp]] · [[ida-mcp-server-plugin]] · [[iida-mcp]] · [[ida-assistant]]
