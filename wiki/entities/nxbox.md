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

Experimental UWP port of the Eden Nintendo Switch emulator stack for Xbox Series X|S (NspxMiguel/NXbox). C++/CMake tree with Dynarmic ARM64 JIT, Maxwell-oriented shader recompiler, video/audio subsystems, and Horizon OS documentation; ships Xbox packaging under `dist/nxbox` with AppxManifest. Port work covers UWP filesystem integration, OpenGL readback and GPU stall handling, Mesa on Direct3D 12, and title compatibility notes (e.g. Breath of the Wild). For cross-platform emulation, console sandbox limits, and low-level CPU/graphics RE—not production anti-cheat tooling. README category: Nintendo Switch. (source: wiki/sources/descriptions/NspxMiguel__NXbox.md)

Adjacent to [[opensw]] (Android Eden fork with live cheat import) and desktop [[nuzu]] mirrors on the same Eden lineage.

## Links

- Repo: https://github.com/NspxMiguel/NXbox

## Related

[[opensw]] · [[nuzu]] · [[yuzu-archive]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
