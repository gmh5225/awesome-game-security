---
title: IvanMurzak Unreal MCP
kind: entity
topics: [game-engine, overview]
sources:
  - wiki/sources/descriptions/IvanMurzak__Unreal-MCP.md
  - wiki/sources/README-categories.md
updated: 2026-10-28
confidence: medium
---

# IvanMurzak Unreal MCP

Unreal Engine editor plugin stack that connects MCP clients to a live Unreal project: C++ editor plugin, .NET sidecar bridge over localhost IPC, npm CLI for install/agent setup, and embedded Python for scripted editor execution. Exposes dozens of built-in tools for spawning actors, editing levels and assets, Blueprint authoring/compile, C++ edit/build, viewport screenshots, and RQL (Reflection Query Language) queries/mutations against editor state. Agents may use the shared ai-game.dev cloud backend or a self-hosted [[gamedev-mcp-server]]; per-tool enablement and optional packaged-build runtime hooks when explicitly enabled. Targets Unreal developers and technical users pursuing AI-assisted authoring, deep editor automation, and programmatic project introspection. (source: wiki/sources/descriptions/IvanMurzak__Unreal-MCP.md) (source: wiki/sources/README-categories.md)

Distinct from kvick-games/chongdashu [[unreal-mcp]] MCP server samples listed under the same README label—this IvanMurzak tree is the official GameDev-MCP-Server companion Unreal plugin with RQL and cloud/self-hosted pairing. Complements [[ivanmurzak-godot-mcp]] on the same Game Develop MCP lane.

## Security research angles

- **Editor vs shipped player** — MCP tooling runs with Unreal Editor privileges during development; optional runtime hooks for packaged builds are gated and per-tool—map findings to [[engine-trust-boundaries]] before treating an agent-driven Blueprint or level edit as a live-player compromise.
- **Local bridge + remote control plane** — the .NET sidecar speaks MCP over localhost IPC while agents may attach via ai-game.dev or [[gamedev-mcp-server]]; pair origin allow-listing, OAuth/token handling, and session scope when threat-modeling remote agent sessions against high-impact tools (C++ compile, asset mutation, RQL writes).
- **RQL and reflection introspection** — programmatic editor queries complement but do not replace native layout evidence; correlate RQL/read tooling with [[unreal-object-model]] when reasoning about UObject/reflection limits on owned projects.

## Links

- Repo: https://github.com/IvanMurzak/Unreal-MCP

## Related

[[gamedev-mcp-server]] · [[engine-trust-boundaries]] · [[unreal-object-model]] · [[unreal-mcp]] · [[unreal-claude]] · [[unity-mcp]] · [[ivanmurzak-godot-mcp]] · [[overviews/game-engine]] · [[overviews/overview]]
