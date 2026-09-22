---
title: Conglomerate CS2
kind: entity
topics: [game-hacking, graphics-api, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/Kryx7z__Conglomerate-Cs2.md
updated: 2026-09-22
confidence: medium
---

# Conglomerate CS2

**Conglomerate-CS2** (Kryx7z/Conglomerate-Cs2) is an open-source **internal Counter-Strike 2 cheat framework** built as a Windows injectable DLL. Written in C++ with Visual Studio, it hooks into the CS2 process and renders an in-game configuration menu. The stack uses **[[kiero]]** and **MinHook** to intercept **DirectX 11** rendering, **Dear ImGui** for the overlay UI, and pattern scanning, vfunc calls, and **Source 2 schema parsing** to locate game interfaces and entity data. Feature modules include aim assistance, chams, movement tweaks, spectator lists, visual overlays (anti-flash, FOV changes), and world modifications, backed by JSON configuration and keybind support. The codebase reverse engineers CS2 structures such as `CGameEntitySystem`, player pawns, weapons, and engine client interfaces. README tags it TempleWare-based with a Visual Studio build and DLL injection workflow. Intended for game security researchers and reverse engineers studying internal cheat architecture, memory hooking techniques, and behaviors anti-cheat systems must detect in CS2. (source: wiki/sources/descriptions/Kryx7z__Conglomerate-Cs2.md)

Sits in the in-process Source 2 internal lane beside framework samples such as [[kisssart-cs2-cheat-base]], [[cs2-cheat-base]], and [[asphyxia-cs2]], and feature-rich internals such as [[rabsztyncc-cs2-internal]] and [[cs2-cheat-source]].

## Links

- Repo: https://github.com/Kryx7z/Conglomerate-Cs2 (Open-source internal Counter-Strike 2 cheat in C++ (TempleWare-based) with Visual Studio build and DLL injection workflow)

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[kiero]] · [[present-hook]] · [[draw-call-hook]] · [[cs2-cheat-base]] · [[kisssart-cs2-cheat-base]] · [[asphyxia-cs2]] · [[cs2-cheat-source]] · [[rabsztyncc-cs2-internal]] · [[cs2-internal-sdk]] · [[source-netvars]] · [[counterstrike2]]
