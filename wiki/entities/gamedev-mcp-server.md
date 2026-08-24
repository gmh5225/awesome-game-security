---
title: GameDev MCP Server
kind: entity
topics: [game-engine, overview]
sources:
  - wiki/sources/descriptions/IvanMurzak__GameDev-MCP-Server.md
updated: 2026-08-24
confidence: medium
---

# GameDev MCP Server

Engine-agnostic C# ASP.NET Core Model Context Protocol (MCP) server that acts as a local proxy host shared by Unity-MCP, Godot-MCP, and Unreal-MCP engine plugins. It is a thin host over NuGet packages that bridge MCP clients such as Claude, Cursor, and Copilot to an in-editor or in-game plugin over SignalR, with no engine-specific code in this project. Supports stdio and streamableHttp client transports, configurable authentication (including OAuth), origin allow-listing, and session handling; ships as standalone executables, a Docker image, and a global .NET tool. Primary use case: letting AI coding agents control and inspect game engines during development through a common local MCP endpoint. (source: wiki/sources/descriptions/IvanMurzak__GameDev-MCP-Server.md)

Sits above per-engine MCP plugins on the Game Develop → MCP server lane—[[unity-mcp]], [[unreal-mcp]], and [[better-godot-mcp]] can share this host instead of each embedding its own transport stack. Complements multi-engine agent scaffolds such as [[everything-game-dev-code]] and MCP infrastructure helpers like [[mcpup]] when the goal is one local endpoint for several engine integrations.

## Links

- Repo: https://github.com/IvanMurzak/GameDev-MCP-Server

## Related

[[unity-mcp]] · [[unreal-mcp]] · [[better-godot-mcp]] · [[everything-game-dev-code]] · [[mcpup]] · [[overviews/game-engine]] · [[overviews/overview]]
