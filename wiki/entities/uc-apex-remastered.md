---
title: UC-Apex-Remastered
kind: entity
topics: [game-hacking, windows-kernel, graphics-api, anti-cheat]
sources:
  - wiki/sources/descriptions/BaconToaster__UC-Apex-Remastered.md
updated: 2026-09-01
confidence: medium
---

# UC-Apex-Remastered

**UC-Apex-Remastered** (BaconToaster/UC-Apex-Remastered) is a **Windows C++ game-hacking framework** for **Apex Legends** that pairs a **kernel driver** with a **user-mode client**. The driver provides **privileged memory operations** and **communication routines**; the user-mode side implements **gameplay modules** and **process interaction**. Rendering uses **DirectX 9** and **ImGui** for overlay output and in-tool controls, with **Visual Studio** and **WDK** build targets. Intended for game security research into **driver-assisted memory access** and **real-time overlay** techniques under [[easy-anti-cheat]]. (source: wiki/sources/descriptions/BaconToaster__UC-Apex-Remastered.md)

Sits in the Apex Legends hybrid UM+KM lane beside [[project-branthium]] and [[apex-legends-cheat]]—combining kernel-side cross-process access with DirectX 9 overlay rendering rather than a pure external-only or internal-only scaffold.

## Architecture

| Component | Role |
|-----------|------|
| Kernel driver | Privileged memory operations and UM↔KM communication |
| User-mode client | Gameplay modules and target-process interaction |
| DirectX 9 + ImGui | Overlay rendering and in-tool controls |
| VS / WDK build | Separate driver and client compilation targets |

See [[world-to-screen]] for ESP projection and [[overviews/windows-kernel]] for the driver-side lane.

## Links

- Repo: https://github.com/BaconToaster/UC-Apex-Remastered

## Related

[[project-branthium]] · [[apex-legends-cheat]] · [[apex-legends-driver-cheat]] · [[apex-mizu-base]] · [[easy-anti-cheat]] · [[world-to-screen]] · [[present-hook]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]]
