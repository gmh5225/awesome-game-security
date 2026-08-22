---
title: flirtnite
kind: entity
topics: [game-hacking, graphics-api, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/NurdAlert__flirtnite.md
updated: 2026-08-22
confidence: medium
---

# flirtnite

**flirtnite** (NurdAlert) is a C++ **external Fortnite cheat framework** that pairs low-level out-of-process memory access with real-time overlay rendering. It exposes a **Hyper-V–based interface layer** for cross-process reads/writes, ships **Unreal structure handling** code, and includes gameplay modules for **entity processing** and **aiming logic**. The rendering stack uses **ImGui with DirectX 9–style integration** for an in-game menu and ESP-style visuals. Primary use case is advanced game-security research into offensive tooling and anti-cheat evasion on EAC-protected UE clients. (source: wiki/sources/descriptions/NurdAlert__flirtnite.md)

From the same author as [[modded-voyager]], but oriented toward **Fortnite external cheat architecture** rather than pre-OS UEFI hypervisor loading. Sits beside driver-backed and leaked Fortnite externals such as [[fortnite-external-cheat-leak]], [[interic-fortnite-external-cheat]], and [[fortnite-external-cheat-base]].

## Links

- Repo: https://github.com/NurdAlert/flirtnite

## Related

[[modded-voyager]] · [[easy-anti-cheat]] · [[unreal-object-model]] · [[world-to-screen]] · [[fortnite-external-cheat-leak]] · [[interic-fortnite-external-cheat]] · [[fortnite-external-cheat-base]] · [[hyper-rev]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
