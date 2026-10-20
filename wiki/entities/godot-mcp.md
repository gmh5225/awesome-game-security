---
title: godot-mcp
kind: entity
topics: [game-engine, overview]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/zeegzoog__godot-mcp.md
updated: 2026-10-20
confidence: medium
---

# godot-mcp

Cross-platform Rust MCP server for Godot 4: stdio JSON-RPC (Tokio) plus a GDScript editor plugin bridged over loopback WebSocket with shared-token auth, project-path checks, and identifier validation to limit drive-by or cross-process abuse. Live tools cover scene trees, undoable property edits (editor undo stack), viewport screenshots, script create/syntax-check, play/stop, and running-game remote-debugger output, tree inspection, input, and screenshots; headless Godot CLI backs version checks, script validation, and batch work when the GUI is closed. Targets Cursor/Claude-style agents automating Godot 4.x development, testing, and live debugging on Windows, Linux, and macOS. (source: wiki/sources/descriptions/zeegzoog__godot-mcp.md)

Complements text-first composite MCP [[better-godot-mcp]] and the shared engine-agnostic host [[gamedev-mcp-server]]; differs by driving the **live editor** undo stack rather than mostly offline `.tscn` parsing.

## Links

- Repo: https://github.com/zeegzoog/godot-mcp

## Related

[[better-godot-mcp]] · [[gamedev-mcp-server]] · [[gddumper]] · [[godot]] · [[overviews/game-engine]] · [[overviews/overview]]
