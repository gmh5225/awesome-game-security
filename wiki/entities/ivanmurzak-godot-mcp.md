---
title: IvanMurzak Godot MCP
kind: entity
topics: [game-engine, overview]
sources:
  - wiki/sources/descriptions/IvanMurzak__Godot-MCP.md
  - wiki/sources/README-categories.md
updated: 2026-10-28
confidence: medium
---

# IvanMurzak Godot MCP

C# Godot 4 editor addon that pairs with an external [[gamedev-mcp-server]] over SignalR so LLM agents drive the editor through MCP. Tools cover RQL scene/resource query and mutation, script execution/diagnostics, screenshots, reflection-based method calls, console logs, and optional ecosystem extension modules. Editor UI supports cloud or local server connection, OAuth/token auth, one-click agent configurators for common AI clients, and a `godot-cli` npm package for install/headless workflows; documents runtime security boundaries for exported builds. (source: wiki/sources/descriptions/IvanMurzak__Godot-MCP.md) (source: wiki/sources/README-categories.md)

Complements zeegzoog [[godot-mcp]] (Rust stdio MCP + GDScript WebSocket bridge) and [[better-godot-mcp]] composite tooling on the same README lane—IvanMurzak's addon is the SignalR client intended for the shared GameDev MCP proxy host.

## Links

- Repo: https://github.com/IvanMurzak/Godot-MCP

## Related

[[gamedev-mcp-server]] · [[godot-mcp]] · [[better-godot-mcp]] · [[ivanmurzak-unreal-mcp]] · [[godot]] · [[overviews/game-engine]] · [[overviews/overview]]
