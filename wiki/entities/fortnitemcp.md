---
title: FortniteMCP
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/SternI__FortniteMCP.md
updated: 2026-11-12
confidence: medium
---

# FortniteMCP

**FortniteMCP** (SternI/fortnitemcp) is an injectable Windows DLL that hosts an in-process **Model Context Protocol** server inside **offline or private Unreal Engine** game builds so MCP clients and coding agents can automate research and testing in controlled local environments. It is built primarily in **C++20** with MSVC, uses **MinHook** for game-thread dispatch, and exposes tools for memory read/write (with pattern scanning), UE reflection and **ProcessEvent** calls, simulated keyboard and mouse input, and optional helper DLL loading over authenticated loopback HTTP or a stdio bridge. Build-specific configuration and Fortnite or UE6-oriented property decoders support walking obfuscated layouts, resolving globals, and tuning layouts at runtime. A companion Python **mitmproxy**-based HTTP MCP server captures and replays HTTPS traffic for API research alongside the in-game tooling. (source: wiki/sources/descriptions/SternI__FortniteMCP.md)

Contrasts with **editor-side** Unreal MCP integrations such as [[unreal-mcp]], [[ivanmurzak-unreal-mcp]], and [[unreal-claude]] by targeting **live shipped-game process** inspection rather than Unreal Editor automation. Adjacent agent memory/RE MCP bridges include [[memmcp]], [[cheatengine-mcp-bridge]], [[cheat-mcp]], and [[llm-game-automation-mcp]].

## Links

- Repo: https://github.com/sterni/fortnitemcp (Game Develop / MCP server)

## Related

[[unreal-mcp]] · [[unreal-object-model]] · [[re-ue4ss]] · [[memmcp]] · [[cheatengine-mcp-bridge]] · [[llm-game-automation-mcp]] · [[present-hook]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
