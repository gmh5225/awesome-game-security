---
title: VoltClient
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/TheHeadphonesAreNeeded__VoltClient.md
updated: 2026-08-20
confidence: medium
---

# VoltClient

Educational **external C++ cheat client** for AssaultCube (TheHeadphonesAreNeeded/VoltClient). Attaches to `ac_client.exe` and reads/writes process memory via Windows `ReadProcessMemory` / `WriteProcessMemory` against documented offsets for version 1.3.0.2, with world-to-screen math for overlay rendering. The UI is a **DirectX 11 transparent overlay** with Dear ImGui: ESP boxes, health bars, tracers, FOV circle, and a smoothed FOV-based aimbot toggled from an in-game menu. Aimed at game security researchers, reverse engineers, and learners studying external overlays, memory reading, and anti-cheat-relevant techniques on a simple FPS title. (source: wiki/sources/descriptions/TheHeadphonesAreNeeded__VoltClient.md)

## Links

- Repo: https://github.com/TheHeadphonesAreNeeded/VoltClient

## Related

[[assaultcube]] · [[external-esp-hack-assaultcube]] · [[simple-ac-internal-cheat]] · [[assault-cube-cheat]] · [[world-to-screen]] · [[imoverlay-dx11]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
