---
title: apex-external-cheat
kind: entity
topics: [game-hacking, windows-kernel, graphics-api, anti-cheat]
sources:
  - wiki/sources/descriptions/bootmgfw__apex-external-cheat.md
updated: 2026-08-17
confidence: medium
---

# apex-external-cheat

**apex-external-cheat** (bootmgfw/apex-external-cheat; **Echo_Apex**) is a C++ **external** cheat for **Apex Legends** that reads game memory from outside the target process and renders features through an on-screen overlay. Built for 64-bit Windows with Visual Studio and C++17, it bundles **Dear ImGui** with **DirectX 11** and Win32 backends for menu and ESP drawing. The project is organized around **kernel driver communication**, game offset definitions, hitbox types, string encryption helpers, and a dedicated overlay module; the release build requires administrator privileges. Intended for game security researchers and reverse engineers studying external cheat design, kernel-assisted memory access, and anti-cheat evasion in Apex Legends under [[easy-anti-cheat]]. (source: wiki/sources/descriptions/bootmgfw__apex-external-cheat.md)

Sits in the kernel-assisted external lane beside other Apex Legends externals such as [[apexd3d-external]] and [[apex-legends-external-esp-aimbot-skinchanger]], below-OS DMA samples such as [[apex-dma-cheat-updated]], and bootmgfw driver primitives in [[lithium-kernel]].

## Links

- Repo: https://github.com/bootmgfw/apex-external-cheat (External Apex Legends cheat with driver-backed memory access and DX11 ImGui overlay)

## Related

[[easy-anti-cheat]] · [[world-to-screen]] · [[present-hook]] · [[lithium-kernel]] · [[apexd3d-external]] · [[apex-dma-cheat-updated]] · [[apex-full-cheat]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]]
