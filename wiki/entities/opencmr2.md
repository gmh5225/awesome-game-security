---
title: OpenCMR2
kind: entity
topics: [reverse-engineering, game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/pablocpas__OpenCMR2.md
updated: 2026-10-15
confidence: medium
---

# OpenCMR2

Native cross-platform port of **Colin McRae Rally 2.0** (Linux, Windows, macOS, Android) built on the **CMR2Decomp** decompiled recreation of the original PC executable—not emulation or a compatibility layer. Game logic remains C++ from the decompilation; a separate platform layer replaces legacy **DirectDraw**, **Direct3D 7**, **DirectSound**, **DirectInput**, **DirectPlay**, and **Bink** with **SDL3**, GPU shaders via the SDL GPU API on **Vulkan** and **Metal**, an integrated Bink decoder, and **UDP** networking. **Clang** + **CMake** builds; Android shell in **Kotlin**. The team validates fixed-point math, startup tables, and long vehicle simulation runs against the retail binary for **bit-exact physics parity** across frame rates—useful for studying deterministic simulation and faithful multiplayer protocol behavior on a documented late-1990s commercial title. **No game assets** ship in the repo; users supply licensed retail data. (source: wiki/sources/descriptions/pablocpas__OpenCMR2.md)

## Links

- Repo: https://github.com/pablocpas/OpenCMR2 (README: native SDL3/Vulkan/Metal port from CMR2Decomp; cross-platform replacement of legacy DirectX APIs)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-engine]] · [[overviews/graphics-api]] · [[axis-web]] · [[devilution]]
