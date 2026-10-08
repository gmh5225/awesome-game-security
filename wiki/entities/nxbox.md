---
title: NXbox
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/NspxMiguel__NXbox.md
  - wiki/sources/README-categories.md
updated: 2026-10-08
confidence: medium
---

# NXbox

Experimental UWP port of the **Eden** Nintendo Switch emulator stack for **Xbox Series X|S** (NspxMiguel/NXbox). Targets developers and researchers studying cross-platform emulation, **AppContainer** sandbox limits, and low-level CPU/graphics behavior—not production anti-cheat tooling. README category: Nintendo Switch. (source: wiki/sources/descriptions/NspxMiguel__NXbox.md)

## Capabilities

Run Switch software on Series hardware via **Dynarmic** ARM64 JIT, a Maxwell-oriented shader recompiler, and Eden video/audio subsystems; includes Horizon OS documentation and Qt, Android, and dedicated **nxbox** launcher frontends. Title compatibility and memory work are documented for games such as *Breath of the Wild*. (source: wiki/sources/descriptions/NspxMiguel__NXbox.md)

## Architecture

C++/CMake tree with Xbox packaging under `dist/nxbox` and **AppxManifest**. Port-specific layers cover UWP filesystem integration, **OpenGL readback** and GPU stall handling, **Mesa on Direct3D 12** driver debugging, and device API research notes. (source: wiki/sources/descriptions/NspxMiguel__NXbox.md)

## Positioning

Cross-console counterpart to Android Eden fork [[opensw]] (live cheat import) and desktop [[nuzu]] mirrors on the same lineage; contrasts with archival [[yuzu-archive]] legal/ecosystem records. Useful when separating guest ARM64/Horizon behavior from host UWP graphics and sandbox constraints.

## Links

- Repo: https://github.com/NspxMiguel/NXbox

## Related

[[opensw]] · [[nuzu]] · [[yuzu-archive]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
