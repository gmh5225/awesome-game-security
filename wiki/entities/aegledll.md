---
title: aegledll
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/AnarchDevelopment__aegledll.md
updated: 2026-09-02
confidence: medium
---

# aegledll

Windows injectable **internal DLL** client (**Aegleseeker**) that adds modular gameplay and HUD features to **Minecraft** through hooked rendering and game logic. Written primarily in **C++** with **HLSL** shaders, it uses **MinHook** for API hooking, **Dear ImGui** with a **DirectX 11** backend for the in-game menu and overlays, and **pattern scanning** to locate targets in memory. Module categories include combat helpers (reach, hitbox changes), movement utilities (auto-sprint, timer), visuals (ClickGUI, fullbright, motion blur, keystrokes, FPS/ping overlays), and misc options such as FPS unlock. Configuration management, an animated array-list HUD, blur menu shaders, and optional IRC-style networking round out the client. Useful for game-security research into DLL injection, DX11 overlay frameworks, and modular Minecraft cheat architecture. (source: wiki/sources/descriptions/AnarchDevelopment__aegledll.md)

## Architecture

- **Hooking** — MinHook on rendering and game-logic APIs; pattern scans for runtime targets.
- **Overlay** — ImGui + DirectX 11 menu; HLSL blur shaders for UI polish.
- **Modules** — pluggable combat, movement, visual, and misc feature set with config persistence.

Complements JVM-injection Minecraft clients such as [[phantom-client]], Java MCP clients such as [[yuri]], and Fabric mod-loader clients such as [[lenrete-mod]] in the Minecraft offensive client lane.

## Links

- Repo: https://github.com/AnarchDevelopment/aegledll

## Related

[[phantom-client]] · [[lenrete-mod]] · [[yuri]] · [[present-hook]] · [[ntminhook]] · [[imgui]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
