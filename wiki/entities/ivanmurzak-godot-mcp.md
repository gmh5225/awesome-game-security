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

C# Godot 4 editor addon that connects LLM coding agents to the live Godot editor through the Model Context Protocol, pairing with [[gamedev-mcp-server]] (self-hosted or ai-game.dev cloud) over SignalR. MCP tools expose editor and runtime capabilities: RQL for querying and mutating scenes and resources, script execution and diagnostics, viewport screenshots, reflection-based method calls, console logs, and optional extension modules for popular Godot ecosystems. Editor UI covers cloud/local server selection, OAuth or token authentication, one-click agent configurators for common AI clients, and the `godot-cli` npm package for installation and headless workflows. Targets game developers automating Godot authoring and technical readers studying how remote agents drive live editors and in-game script execution. (source: wiki/sources/descriptions/IvanMurzak__Godot-MCP.md) (source: wiki/sources/README-categories.md)

Complements zeegzoog [[godot-mcp]] (Rust stdio MCP + GDScript WebSocket bridge) and [[better-godot-mcp]] composite tooling on the same README lane—IvanMurzak's addon is the SignalR client intended for the shared GameDev MCP proxy host alongside [[ivanmurzak-unreal-mcp]].

## Security research angles

- **Editor vs shipped export** — MCP tooling runs with editor privileges during dev; the project documents which capabilities remain available in exported player builds versus editor-only paths—map findings to [[engine-trust-boundaries]] before treating an agent-driven edit as a player-runtime compromise.
- **Remote agent control plane** — SignalR sessions to a local or cloud MCP host combine OAuth/token auth on the server with high-impact tools (scene mutation, script run, reflection calls); pair with [[gamedev-mcp-server]] origin allow-listing and session handling when threat-modeling agent workflows.
- **Automation evidence** — RQL mutations, diagnostics, and console logs can support reproducible authoring traces or abuse-case demos on owned projects without implying anti-cheat bypass.

## Links

- Repo: https://github.com/IvanMurzak/Godot-MCP

## Related

[[gamedev-mcp-server]] · [[engine-trust-boundaries]] · [[godot-mcp]] · [[better-godot-mcp]] · [[ivanmurzak-unreal-mcp]] · [[godot]] · [[overviews/game-engine]] · [[overviews/overview]]
