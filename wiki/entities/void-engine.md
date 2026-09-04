---
title: Void Engine
kind: entity
topics: [game-engine, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/lannden1245__Void-Engine.md
  - wiki/sources/README-categories.md
updated: 2026-09-04
confidence: medium
---

# Void Engine

**Godot 4.x editor plugin** bundling custom nodes and utilities for multiplayer games with built-in protection and performance tooling. Written in **GDScript** and ships a **WhiteVoid AntiCheat** autoload that other components query to enforce game-mode integrity — debugger/process/window detection, honeypot integrity checks, and **HWID ban enforcement**. (source: wiki/sources/descriptions/lannden1245__Void-Engine.md)

Also includes **VoidNet** networking (ENet and Firebase-backed WebRTC with optional encryption, multi-region fallback, lobbies, and player sync), distance-based texture streaming, dynamic resolution and anti-aliasing management, procedural room generation, shader compilation, and editor-side **VoidForge** design tools. Listed under README **Anti Cheat > Open Source Anti Cheat System**.

## Anti-cheat surfaces

- **Debugger/process/window detection** — client integrity signals via WhiteVoid autoload
- **Honeypot integrity checks** — tamper and environment probes
- **HWID ban enforcement** — persistent identity blocking for repeat offenders

## Links

- Repo: https://github.com/lannden1245/Void-Engine

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[godot]] · [[better-godot-mcp]] · [[certael]] · [[bevy-personal-test]] · [[research-rigor]]
