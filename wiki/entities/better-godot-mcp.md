---
title: better-godot-mcp
kind: entity
topics: [game-engine, overview]
sources:
  - wiki/sources/descriptions/n24q02m__better-godot-mcp.md
updated: 2026-08-24
confidence: medium
---

# better-godot-mcp

TypeScript Model Context Protocol (MCP) server that lets AI coding agents create and modify Godot Engine 4.x projects via seventeen composite mega-tools (scenes, nodes, GDScript, shaders, animation, tilemaps, physics, audio, navigation, UI, input maps, signals, resources, run/export). Scene and script edits can run without the Godot editor by parsing `.tscn` and related files as text; optional headless/editor launches use an auto-detected Godot binary over stdio or Streamable HTTP. Targets Node.js with bun, includes Docker packaging, and hardens local file/process ops against path traversal and command injection. Fits Game Develop → MCP server for Godot AI-assisted gamedev (Claude Code, Cursor, etc.). (source: wiki/sources/descriptions/n24q02m__better-godot-mcp.md)

Complements Unity editor MCP [[unity-mcp]] and the shared engine-agnostic host [[gamedev-mcp-server]] (Godot-MCP plugin lane); also HITL/docs MCP such as [[interactive-feedback-mcp]] / [[deepwiki-mcp]] on the agent-tooling side; sits beside Godot runtime RE dumpers such as [[gddumper]] (Cheat Engine Lua SceneTree/GDScript) when the goal is project authoring rather than live-process inspection.

## Links

- Repo: https://github.com/n24q02m/better-godot-mcp

## Related

[[gamedev-mcp-server]] · [[unity-mcp]] · [[gddumper]] · [[interactive-feedback-mcp]] · [[deepwiki-mcp]] · [[overviews/game-engine]] · [[overviews/overview]]
