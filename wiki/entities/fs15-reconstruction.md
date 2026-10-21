---
title: FS15 Reconstruction
kind: entity
topics: [reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/nat649__fs15-reconstruction.md
  - wiki/sources/README-categories.md
updated: 2026-10-21
confidence: high
---

# FS15 Reconstruction

**fs15-reconstruction** ([nat649/fs15-reconstruction](https://github.com/nat649/fs15-reconstruction)) is an independent, early-stage research effort to decompile and reconstruct **Farming Simulator 15** and its **GIANTS Engine 6 (GE6)** runtime from native binaries and user-supplied game assets—not a drop-in commercial replacement. (source: wiki/sources/descriptions/nat649__fs15-reconstruction.md)

## Toolchain

C++17/CMake core with Python validation scripts, PowerShell build helpers, and a **LuaJIT** script host that re-hosts hundreds of recovered Lua modules. Recovered subsystems include scene graphs, file streams, animation, OpenGL draw paths, and **Bullet**-backed vehicle physics; large fixture-based differential tests compare reconstructed behavior against original code paths. (source: wiki/sources/descriptions/nat649__fs15-reconstruction.md)

## Research track

A parallel lane executes original GE6 x64 instructions on Linux under controlled VMs and platform adapters to study boot, rendering, and scripting without wholesale replacement of the retail executable—useful for mapping **script–native boundaries** and engine startup. **Local game files are required**; the repo ships no commercial assets.

## Audience

Reverse engineers, proprietary engine researchers, and analysts who need reproducible evidence and tooling for GE6 internals, boot paths, and Lua/native interop—not live multiplayer cheat delivery.

## Related

[[overviews/reverse-engineering]] · [[overviews/game-engine]] · [[static-runtime-evidence]] · [[ps2-port-engine]]

## Links

- Repo: https://github.com/nat649/fs15-reconstruction
