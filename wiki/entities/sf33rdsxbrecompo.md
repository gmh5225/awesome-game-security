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

## Audience

Developers and researchers studying reverse engineering, console binary preservation, and how **decompiled** retail game logic can be rehosted on modern desktops when users supply legally owned disc data—without shipping Xbox assets in the repository. (source: wiki/sources/descriptions/Manya3084__SF33RDSXBRecompo.md)

## Positioning

Listed under **Cheat → Source** beside other OG Xbox static-rehost ports such as [[ngbrecomp]] (xboxrecomp XBE lift) and [[jsrf-recomp]]. Unlike xboxrecomp forks, this project runs logic from the **3s-decomp-ogxb** decompilation pipeline rather than lifting the retail XBE directly. Shader and stub generation utilities help maintain parity with retail behavior; optional Android packaging extends the same stack. Preservation and console-binary RE research—not live multiplayer cheat delivery. Pair [[static-runtime-evidence]] when separating decompiled structure from runtime fidelity claims (graphics draw paths, audio cues, saves).

## Links

- Repo: https://github.com/Manya3084/SF33RDSXBRecompo

## Related

[[ngbrecomp]] · [[jsrf-recomp]] · [[xemu]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
