---
title: Apex-Legends-Esp
kind: entity
topics: [game-hacking, windows-kernel, graphics-api]
sources:
  - wiki/sources/descriptions/RavenOfTime__Apex-Legends-Esp.md
updated: 2026-08-21
confidence: medium
---

# Apex-Legends-Esp

**External ESP cheat source template** for shooter games, demonstrated on **Apex Legends** (RavenOfTime). C++ **Visual Studio** solution for Windows with three separable components: a **kernel driver** for cross-process memory access, a **user-mode overlay** for on-screen entity visualization, and a **[[kdmapper]]**-based loader for bringing the driver up without conventional signed-driver installation. Rendering uses **Windows GDI** rather than DirectX hooking. (source: wiki/sources/descriptions/RavenOfTime__Apex-Legends-Esp.md)

Positioned for **game-hacking learners** studying memory-read pipelines, kernel-assisted externals, and [[world-to-screen]] entity drawing. Sits beside educational GDI externals such as [[external-esp-hack-assaultcube]] and walkthrough labs such as [[lab-esp-and-aimbot]], and beside title-integrated Apex kernel externals such as [[apex-legends-driver-cheat]] and SDK samples such as [[apex-legends-sdk]] under [[easy-anti-cheat]].

## Architecture highlights

| Component | Role |
|-----------|------|
| Kernel driver | Cross-process memory read path for entity/state reconstruction |
| kdmapper loader | BYOVD-style manual map of the driver into kernel space |
| User-mode overlay | GDI window draws ESP boxes/names from RPM data |
| Visual Studio solution | End-to-end Windows C++ project layout for learners |

## Links

- Repo: https://github.com/RavenOfTime/Apex-Legends-Esp

## Related

[[kdmapper]] · [[world-to-screen]] · [[apex-legends-driver-cheat]] · [[apex-legends-sdk]] · [[apex-esp-old-project]] · [[external-esp-hack-assaultcube]] · [[lab-esp-and-aimbot]] · [[easy-anti-cheat]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]]
