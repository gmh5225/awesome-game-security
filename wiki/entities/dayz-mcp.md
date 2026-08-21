---
title: dayz-mcp
kind: entity
topics: [game-engine, game-hacking]
sources:
  - wiki/sources/descriptions/willy92wins__dayz-mcp.md
updated: 2026-08-21
confidence: medium
---

# dayz-mcp

Model Context Protocol (MCP) server that lets AI agents programmatically control a running DayZ client or dedicated server through dozens of typed tools (53 in the README). A Windows Python daemon and MCP server talk to an in-game Enforce Script bridge mod that dispatches **server-authoritative** commands for world setup, player and vehicle manipulation, telemetry, logging, and scene observation—without keyboard input or OCR. Supports an autonomous mod-development loop: pack addons, launch test instances, place entities, drive vehicles, capture screenshots, and assert on structured engine state. Session leases, localhost-only binding, credential management, and audit trails provide a controlled automation surface for local testing and server administration. Targets DayZ mod developers, server operators, and researchers who need repeatable, scriptable Enfusion interaction for development, QA, and operational workflows. (source: wiki/sources/descriptions/willy92wins__dayz-mcp.md)

Contrasts with offensive DayZ samples such as [[dayz-cheat]], [[external-dayz-cheat]], and [[dayzzz]] (external memory reads, overlays, SDK generation) by driving the game through sanctioned in-process script APIs rather than out-of-process RPM or render hooks. Complements editor/runtime MCP bridges such as [[unity-mcp]] and [[better-godot-mcp]] on the Game Develop → MCP lane for title-specific Enfusion modding automation.

## Links

- Repo: https://github.com/willy92wins/dayz-mcp

## Related

[[dayzzz]] · [[dayz-cheat]] · [[external-dayz-cheat]] · [[unity-mcp]] · [[better-godot-mcp]] · [[battleye]] · [[overviews/game-engine]] · [[overviews/game-hacking]]
