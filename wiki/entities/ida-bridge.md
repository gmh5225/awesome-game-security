---
title: ida-bridge
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - https://github.com/cellebrite-labs/ida-bridge
updated: 2026-08-04
confidence: medium
---

# ida-bridge

**Agent bridge for IDA Pro 9+** (Cellebrite Labs): a CLI + plugin + headless `idalib` runner that lets AI agents execute **IDAPython** and **SQL** queries against live IDA databases. UI IDA instances connect to a local bridge server over WebSocket; agents use `ida-bridge list`, `exec`, and `supervisor` to discover targets, run stateless or stateful sessions, launch/stop/save instances, and fire one-shot `exec-idb` probes.

The SQL layer sidesteps stale IDAPython knowledge by translating standard queries (e.g. `SELECT name, start_ea FROM funcs WHERE name LIKE '%auth%'`) into correct IDA 9.x API calls internally (IDA-over-SQL lineage from idasql/libxsql). When SQL is insufficient, the bundled `skills/ida-bridge/` skill directs agents to pair with **ida-docs** for verified IDAPython. Supports dyld shared-cache single-module IDB creation on macOS. Prerequisites: IDA Pro ≥ 9.0, macOS, optional `ida-setup` for unified `~/.idapro/venv`.

## Links

- Repo: https://github.com/cellebrite-labs/ida-bridge
- Companion skill/API docs: https://github.com/cellebrite-labs/ida-docs

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[idac]] · [[ida-pro-mcp]] · [[ida-mcp-server-plugin]] · [[iida-mcp]] · [[ida-assistant]]
