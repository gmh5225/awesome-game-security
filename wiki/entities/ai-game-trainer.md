---
title: AI Game Trainer
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Hello-DaTang__AI-Game-Trainer.md
updated: 2026-11-14
confidence: medium
---

# AI Game Trainer

**AI Game Trainer** (Hello-DaTang/AI-Game-Trainer) is a Windows **local-first** application that turns Cheat Engine discoveries into reusable, **per-game trainer presets** controlled from a **browser-based console**. It targets offline single-player modding and memory-editing workflows, explicitly avoiding kernel tooling, anti-cheat evasion, and online multiplayer tampering. (source: wiki/sources/descriptions/Hello-DaTang__AI-Game-Trainer.md)

## Architecture

- **CE bridge:** talks to Cheat Engine through the upstream **MCP Lua bridge** (named pipe, or optional loopback TCP relay)—the same agent↔CE IPC family as [[cheatengine-mcp-bridge]]
- **Service layer:** Python **HTTP** API with **SQLite** persistence; imports and exports full cheat tables as **`.CT`** files
- **Workflow:** capture validated address-list or Auto Assembler script records from CE, persist tables, later reload and enable or disable specific memory records against a single matching game executable
- **Agent pairing:** designed to work with external Codex plus CE MCP for exploration
- **Distribution:** PyInstaller portable build and bundled smoke-test demo to verify the CE read-write path without a full Python toolchain on the host

Sits beside [[apprentice]] and [[freeplay]] as an offline CE-table-oriented trainer console, but keeps CE running as the memory engine while the Python service owns library metadata and toggle UX rather than reimplementing scan/debug primitives.

## Links

- Repo: https://github.com/Hello-DaTang/AI-Game-Trainer

## Related

[[cheat-engine]] · [[cheatengine-mcp-bridge]] · [[cheat-engine-tables]] · [[cttrainer]] · [[apprentice]] · [[freeplay]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]