---
title: DayZ ESP
kind: entity
topics: [game-hacking, windows-kernel, graphics-api]
sources:
  - wiki/sources/descriptions/cmachale14-eng__DayZESP.md
  - wiki/sources/README-categories.md
updated: 2026-10-24
confidence: medium
---

# DayZ ESP

**DayZ ESP** (cmachale14-eng/DayZESP) is a Windows **external** cheat for the Enfusion-based **DayZ** client: a standalone C++20 (MinGW) executable draws a **DirectX 11** Dear ImGui overlay while reading live game state through **kernel-mode** cross-process memory access backed by the Intel **`iqvw64e.sys`** vulnerable driver ([[byovd]] / kdmapper-family lane). Supporting modules cover process memory I/O, offset tables, entity and item discovery, name resolution, and optional dumping. (source: wiki/sources/descriptions/cmachale14-eng__DayZESP.md) (source: wiki/sources/README-categories.md)

## Research framing

Targets analysts studying how kernel-assisted external ESP stacks interact with **BattlEye**-protected clients and platform mitigations such as Memory Integrity and Secure Boot—not production deployment guidance. (source: wiki/sources/descriptions/cmachale14-eng__DayZESP.md)

## Positioning

Listed under README **Cheat** beside [[external-dayz-cheat]] (D3D9 overlay + custom kernel driver) and [[dayz-cheat]] (usermode RPM external); contrasts with [[dayz-mcp]] (server-authoritative Enforce Script automation) and [[dayz-server-battleye-remover]] (server BE patch research).

## Links

- Repo: https://github.com/cmachale14-eng/DayZESP [External DayZ ESP with DX11 ImGui overlay and iqvw64e.sys BYOVD kernel memory reads for BattlEye-protected process access]

## Related

[[battleye]] · [[world-to-screen]] · [[present-hook]] · [[byovd]] · [[kdmapper]] · [[external-dayz-cheat]] · [[dayz-cheat]] · [[dayzzz]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]]
