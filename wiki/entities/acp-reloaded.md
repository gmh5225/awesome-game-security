---
title: ACP-Reloaded
kind: entity
topics: [game-hacking, graphics-api, reverse-engineering]
sources:
  - wiki/sources/descriptions/justsomesnake__ACP-Reloaded.md
updated: 2026-11-21
confidence: medium
---

# ACP-Reloaded

**ACP-Reloaded** (justsomesnake) is a Windows PC mod that rebuilds Ubisoft's Animus Control Panel for *Assassin's Creed Origins* as a standalone in-game overlay, restoring live access to the game's developer tuning parameters in Hacked Animus saves without the deprecated Uplay overlay. It is implemented in C++ with CMake and MSVC, loading via a `dinput8.dll` proxy or ASI plugin and hooking DirectX 11, intercepting window messages and XInput, bridging Uplay events, and drawing an ImGui-based panel with optional Origins-themed UI. The mod exposes all 109 ACP parameters with presets, search, undo, character portraits, and controller navigation, plus quality-of-life features (frame limiting, sharpening, save backups) and opt-in experimental helpers for time, weather, teleportation, and progression on a verified game build. Supporting Python tools generate parameter tables; the tree includes tests for pacing, input filtering, sync, and the proxy loader. Audience: modders, reverse engineers, and game-security researchers studying how triple-A clients expose simulation state and how third-party code hooks graphics, input, and platform services to manipulate that state at runtime. (source: wiki/sources/descriptions/justsomesnake__ACP-Reloaded.md)

## Links

- Repo: https://github.com/justsomesnake/ACP-Reloaded

## Related

[[present-hook]] · [[directxhook]] · [[ingame-overlay]] · [[imgui]] · [[sr5-tweak-menu]] · [[h7-mod-engine]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]]