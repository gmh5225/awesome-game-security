---
title: unreal-mcp
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/descriptions/kvick-games__UnrealMCP.md
  - wiki/sources/descriptions/chongdashu__unreal-mcp.md
updated: 2026-08-17
confidence: medium
---

# unreal-mcp

Model Context Protocol (MCP) server integration for Unreal Engine that exposes Unreal Editor functionality to AI assistants and automation tools. Fits the Game Develop → MCP server lane; useful for game developers, reverse engineers, and tooling builders wiring agents into Unreal projects rather than reversing shipped game binaries. (source: wiki/sources/descriptions/kvick-games__UnrealMCP.md) (source: wiki/sources/descriptions/chongdashu__unreal-mcp.md)

The README lists two independent implementations under the same label:

- **kvick-games/UnrealMCP** — editor integration for asset management, level editing, blueprint manipulation, and project configuration (source: wiki/sources/descriptions/kvick-games__UnrealMCP.md)
- **chongdashu/unreal-mcp** — experimental MCP for Unreal Engine; currently in an experimental state (source: wiki/sources/descriptions/chongdashu__unreal-mcp.md)

Complements editor-side Unity MCP [[unity-mcp]] and Godot MCP [[better-godot-mcp]] on the Game Develop → MCP server lane; sits opposite Unreal SDK/explorer tooling such as [[unrealengine4-swissknife]] and [[ts-ue4dumper]] when the goal is authoring automation rather than live-process RE.

## Links

- Repo (kvick-games): https://github.com/kvick-games/UnrealMCP
- Repo (chongdashu): https://github.com/chongdashu/unreal-mcp

## Related

[[unity-mcp]] · [[better-godot-mcp]] · [[unicli]] · [[unreal-object-model]] · [[overviews/game-engine]] · [[overviews/overview]]
