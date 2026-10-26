---
title: quen-mcp
kind: entity
topics: [game-engine, game-hacking]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/snackbar92hypernova__quen-mcp.md
updated: 2026-10-26
confidence: medium
---

# quen-mcp

**Quen** (snackbar92hypernova/quen-mcp) is a **Model Context Protocol** server and command-line tool that lets coding agents control a **single live Witcher 3** session for mod development, testing, and troubleshooting. The host stack is mainly **Rust**; a game-side package in **C++** and **WitcherScript** bridges the running title to the MCP host. Agents can launch the game with temporary settings and **mod parking**, load saves, capture screenshots, run **PresentMon** frame-time A/B performance measurements, and perform memory reads and patches while staging mods. Sessions, captures, and evidence persist in a local **SQLite** ledger; the tool restores the game folder on **every exit path**. Integrates with MCP clients such as Claude Code, VS Code, and Cursor, and can work alongside profiling and graphics tooling including Tracy, Nsight, RenderDoc, and ReShade. Primary audience: Witcher 3 mod authors and researchers who want repeatable, agent-driven in-game workflows instead of manual click-through testing. (source: wiki/sources/descriptions/snackbar92hypernova__quen-mcp.md)

Parallels [[dayz-mcp]] and [[godot-mcp]] on the Game Develop → MCP lane as **title-specific mod-dev automation** through in-game script/API bridges rather than generic editor-only MCP. Memory read/patch capabilities overlap the cheat-tooling surface but the README positions the project for owned-game mod QA and reproducible evidence collection.

## Links

- Repo: https://github.com/snackbar92hypernova/quen-mcp

## Related

[[dayz-mcp]] · [[godot-mcp]] · [[cheat-mcp]] · [[universal-modder]] · [[present-hook]] · [[overviews/game-engine]] · [[overviews/game-hacking]]
