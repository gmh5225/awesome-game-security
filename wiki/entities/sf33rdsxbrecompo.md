---
title: SF33RDSXBRecompo
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/Manya3084__SF33RDSXBRecompo.md
  - wiki/sources/README-categories.md
updated: 2026-10-22
confidence: high
---

# SF33RDSXBRecompo

**SF33RDSXBRecompo** ([Manya3084/SF33RDSXBRecompo](https://github.com/Manya3084/SF33RDSXBRecompo)) is a native **x86-64** port of *Street Fighter III: 3rd Strike* that runs decompiled original Xbox game logic on **Linux and Windows** without building retail Xbox runtime binaries. (source: wiki/sources/descriptions/Manya3084__SF33RDSXBRecompo.md)

## Stack

| Layer | Role |
|-------|------|
| **Game logic** | Lifted from the **3s-decomp-ogxb** OG Xbox decompilation pipeline |
| **Platform services** | C reimplementation (not full-system Xbox emulation) |
| **Windowing / input** | SDL3 |
| **Graphics** | Vulkan or OpenGL, including NV2A-style draw paths |
| **Audio** | OpenAL (ADX, AIX, XACT cues) |
| **Saves** | SQLite |
| **Assets** | User-supplied Xbox disc image or extracted XBE + AFS tree |
| **Tooling** | XBE header, XDVDFS, and disc-archive readers; Python helpers tied to ogxb; CMake build with optional Android packaging and shader/stub generators |

## Positioning

Listed under **Cheat → Source** beside other OG Xbox static-rehost ports such as [[ngbrecomp]] and [[jsrf-recomp]]. Preservation and console-binary RE research—not live multiplayer cheat delivery. Pair [[static-runtime-evidence]] when comparing lifted logic against retail traces.

## Related

[[ngbrecomp]] · [[jsrf-recomp]] · [[xemu]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
