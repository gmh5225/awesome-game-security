---
title: csgo-cheat
kind: entity
topics: [game-hacking, graphics-api, reverse-engineering]
sources:
  - wiki/sources/descriptions/manka81__csgo_cheat.md
updated: 2026-08-31
confidence: medium
---

# csgo-cheat

Modular **C++17** framework for building an **external** Counter-Strike: Global Offensive overlay on Windows. Combines a **MemoryReader** module with **pattern scanning** and **offset auto-detection** (including **hazedumper** presets), **3D world-to-screen** math, and a transparent **DirectX 11 Dear ImGui** overlay for ESP boxes, skeletons, snaplines, and HUD elements. Implements **aim assist**, **triggerbot**, **no-recoil compensation**, **bunny hop**, and **camera rotation** via **WriteProcessMemory** and **SendInput**, with configuration persisted in **INI** files. Written primarily in C++ with a small Python helper for memory operations; targets game security researchers, reverse engineers, and anti-cheat analysts studying external cheat techniques and client-side memory manipulation. (source: wiki/sources/descriptions/manka81__csgo_cheat.md)

Treat as a full-stack external CS:GO framework for studying modular memory-read/write workflows, offset bootstrap, and DX11 overlay rendering—not a maintained cheat product.

## Architecture

| Module | Role |
|--------|------|
| MemoryReader | Out-of-process reads/writes; pattern scan + offset auto-detection |
| Offset bootstrap | hazedumper preset integration for post-patch layouts |
| World-to-screen | 3D view projection for ESP and aim FOV math |
| DX11 ImGui overlay | Transparent layered window; boxes, skeletons, snaplines, HUD |
| Input / write path | WriteProcessMemory + SendInput for aim, recoil, movement |
| Config | INI persistence for feature toggles and tuning |

See [[hazedumper]] for offset feeds, [[world-to-screen]] for projection math, and [[external-cheat-v3]] for a DX9 ImGui external counterpart in the same lane.

## Links

- Repo: https://github.com/manka81/csgo_cheat

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[hazedumper]] · [[csgo-external-cheat]] · [[external-cheat-v3]] · [[le-chiffre]] · [[csgo-cheats]] · [[csgo-external-esp]] · [[world-to-screen]]
