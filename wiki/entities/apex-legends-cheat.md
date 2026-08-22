---
title: apex-legends-cheat
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat, graphics-api]
sources:
  - wiki/sources/descriptions/NMan1__apex-legends-cheat.md
updated: 2026-08-22
confidence: medium
---

# apex-legends-cheat

**apex-legends-cheat** (NMan1/apex-legends-cheat) is an **external Windows cheat architecture** for **Apex Legends** built around a **kernel driver**, **loader**, and **client DLL** components. The C++ codebase splits into separate Visual Studio projects for driver-side logic, user-mode loading, and feature modules. Feature modules include **ESP** and **chams-style** visuals plus input-assisted aiming utilities. Its bypass approach centers on **syscall hooking** and **kernel-thread execution** rather than conventional in-process rendering hooks. Intended for reverse engineering and anti-cheat research into kernel-mediated cheat pipelines under [[easy-anti-cheat]]. (source: wiki/sources/descriptions/NMan1__apex-legends-cheat.md)

Sits in the Apex Legends kernel-assisted external lane beside [[apex-legends-driver-cheat]] and [[apex-external]], and complements NMan1's COD samples [[external-warzone-cheat]] and [[warzone-internal]] with a battle-royale kernel-driver + client-DLL path.

## Architecture

| Component | Role |
|-----------|------|
| Kernel driver | Driver-side logic for cross-process memory and kernel-thread execution |
| Loader | User-mode loading and driver bring-up |
| Client DLL | Feature modules: ESP, chams, input-assisted aim |
| Syscall hooking | Bypass lane centered on syscall interception |

See [[world-to-screen]] for ESP projection and [[easy-anti-cheat]] for the protected-title context.

## Links

- Repo: https://github.com/NMan1/apex-legends-cheat

## Related

[[apex-legends-driver-cheat]] · [[apex-external]] · [[apex-external-cheat]] · [[external-warzone-cheat]] · [[warzone-internal]] · [[easy-anti-cheat]] · [[world-to-screen]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
