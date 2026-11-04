---
title: COD6-NX
kind: entity
topics: [reverse-engineering, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/GreenieSparkles__COD6-NX.md
  - wiki/sources/README-categories.md
updated: 2026-11-04
confidence: medium
---

# COD6-NX

**COD6-NX** ([GreenieSparkles/COD6-NX](https://github.com/GreenieSparkles/COD6-NX)) is a **work-in-progress Nintendo Switch homebrew port** of *Call of Duty: Modern Warfare 2* that runs **Xbox 360 game logic through static recompilation** rather than wrapping a full X360 emulator. The retail **`default.xex`** is translated to **ARM64 C++** with **ReXGlue** (Xenia-derived), built via **CMake**, **devkitA64**, and **libnx**. (source: wiki/sources/descriptions/GreenieSparkles__COD6-NX.md)

## Graphics bring-up

Graphics use a **custom native Vulkan renderer** on **NVK/Mesa** instead of the slow generic Switch SDK path. Implementation work centers on **PM4 command streams**, render/skinning hooks, texture and render-target management, **GLSL compute shaders**, and runtime diagnostics for reverse-engineering the legacy **Xenos** GPU pipeline. (source: wiki/sources/descriptions/GreenieSparkles__COD6-NX.md)

## Scope limits

Research-oriented **homebrew porter** tooling only: **no copyrighted game data** in-repo; users must supply assets from a **legally owned copy**. Not an online anti-cheat or live-service bypass surface. (source: wiki/sources/descriptions/GreenieSparkles__COD6-NX.md)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[nhl-legacy-remaster]] · [[mcla-pc]] · [[static-runtime-evidence]]

## Links

- Repo: https://github.com/GreenieSparkles/COD6-NX
