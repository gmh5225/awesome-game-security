---
title: pubg-mobile-memory-hacking
kind: entity
topics: [mobile-security, game-hacking, windows-kernel, graphics-api]
sources:
  - wiki/sources/descriptions/atulkunal999__pubg_mobile_memory_hacking.md
updated: 2026-08-18
confidence: medium
---

# pubg-mobile-memory-hacking

**PUBG Mobile** cheat for the **Gameloop** (Tencent GameLoop) Android emulator on Windows (atulkunal999). C++ implementation with **ESP** and **aimbot**, using a **kernel driver** for cross-process memory access, a **DirectX-based overlay** for ESP rendering, and bundled **Unreal Engine SDK headers** for game-structure reads. Driver load uses **DSEFix**; the project targets **x64** builds and attaches via **window detection through process enumeration**. (source: wiki/sources/descriptions/atulkunal999__pubg_mobile_memory_hacking.md)

Useful for game security researchers studying how mobile battle-royale titles are cheated when run on PC emulators with kernel-level RPM and external graphics overlays — a different host surface than on-device Android memory editors.

## Links

- Repo: https://github.com/atulkunal999/pubg_mobile_memory_hacking

## Related

[[pubg-mobile-memory-hacking-examples]] · [[pubg-dx]] · [[bypass-pubg-mobile-imgui]] · [[pubgm-sdk-and-offsets]] · [[present-hook]] · [[world-to-screen]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
