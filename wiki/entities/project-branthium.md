---
title: Project-Branthium
kind: entity
topics: [game-hacking, windows-kernel, graphics-api, anti-cheat]
sources:
  - wiki/sources/descriptions/KaylinOwO__Project-Branthium.md
updated: 2026-08-24
confidence: medium
---

# Project-Branthium

**Project-Branthium** (KaylinOwO/Project-Branthium) is a **Windows game cheating framework** that pairs a **user-mode client** with a **kernel driver** component. Written in **C++** with **Visual Studio** solution files, it includes low-level memory interaction code in both cheat and driver directories. Feature modules cover **aimbot** logic, **ESP** visuals, **entity caching**, and **weapon prediction**, with an **ImGui** and **DirectX 9** menu and overlay stack. Intended for game-hacking experimentation and reverse-engineering workflows, especially for **Apex Legends**-style targets under [[easy-anti-cheat]]. (source: wiki/sources/descriptions/KaylinOwO__Project-Branthium.md)

Sits in the Apex Legends hybrid UM+KM lane beside [[apex-legends-cheat]] and [[apex-mizu-base]]—combining kernel-assisted memory access with in-process DirectX overlay rendering rather than a pure external or internal-only scaffold.

## Architecture

| Component | Role |
|-----------|------|
| User-mode client | Feature modules, ImGui + DirectX 9 overlay/menu |
| Kernel driver | Low-level memory interaction for protected-process access |
| Entity cache | Cached game-state for ESP and aimbot |
| Weapon prediction | Ballistic/lead compensation for aim assistance |

See [[world-to-screen]] for ESP projection math and [[overviews/windows-kernel]] for the driver-side lane.

## Links

- Repo: https://github.com/KaylinOwO/Project-Branthium

## Related

[[apex-legends-cheat]] · [[apex-mizu-base]] · [[apex-legends-driver-cheat]] · [[easy-anti-cheat]] · [[world-to-screen]] · [[present-hook]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]]
