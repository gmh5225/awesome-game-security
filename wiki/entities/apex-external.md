---
title: apex-external
kind: entity
topics: [game-hacking, graphics-api, anti-cheat]
sources:
  - wiki/sources/descriptions/NekoRem__apex-external.md
updated: 2026-08-22
confidence: medium
---

# apex-external

**apex-external** (NekoRem/apex-external) is a C++ **external cheat framework** for **Apex Legends** that reads game memory from outside the target process and renders features through a separate overlay stack. It uses **OpenGL** with **GLFW** for the transparent overlay window, **Dear ImGui** for menus and configuration, and a custom **driver-style memory access layer** for cross-process reads and writes. Feature modules include player and loot **ESP**, **glow** highlighting, **aim assist** with smoothing and FOV controls, **recoil** compensation, **bunny hop**, and configurable visuals. Intended for game security researchers studying external overlay architecture and memory-driven cheating techniques under [[easy-anti-cheat]]. (source: wiki/sources/descriptions/NekoRem__apex-external.md)

Sits in the Apex Legends external lane beside kernel-assisted DX11 samples such as [[apex-external-cheat]] and [[apex-legends-driver-cheat]], and below-OS DMA stacks such as [[apex-dma-cheat-updated]].

## Links

- Repo: https://github.com/NekoRem/apex-external (External Apex Legends cheat framework with OpenGL/GLFW overlay and driver-style memory access)

## Related

[[easy-anti-cheat]] · [[world-to-screen]] · [[present-hook]] · [[apex-external-cheat]] · [[apex-legends-driver-cheat]] · [[apex-dma-cheat-updated]] · [[apexd3d-external]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]]
