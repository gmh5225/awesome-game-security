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

Rust Model Context Protocol server for Godot 4: stdio JSON-RPC plus a GDScript editor plugin over loopback WebSocket with shared-token auth. Live tools cover scene trees, undoable property edits, viewport screenshots, script create/validate, play/stop, and running-game debugger output, input, and captures; headless Godot CLI backs version checks and batch work when the GUI is closed. Targets Cursor/Claude-style agents automating Godot 4.x on Windows, Linux, and macOS. (source: wiki/sources/descriptions/zeegzoog__godot-mcp.md)

Complements text-first composite MCP [[better-godot-mcp]] and the shared engine-agnostic host [[gamedev-mcp-server]]; differs by driving the **live editor** undo stack rather than mostly offline `.tscn` parsing.

## Links

- Repo: https://github.com/zeegzoog/godot-mcp

## Related

[[better-godot-mcp]] · [[gamedev-mcp-server]] · [[gddumper]] · [[godot]] · [[overviews/game-engine]] · [[overviews/overview]]
