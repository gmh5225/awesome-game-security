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

**fs15-reconstruction** ([nat649/fs15-reconstruction](https://github.com/nat649/fs15-reconstruction)) is an early-stage **Farming Simulator 15 / GIANTS Engine 6** decompilation and native reconstruction project driven by fixture-based differential validation against retail binaries. (source: wiki/sources/descriptions/nat649__fs15-reconstruction.md)

## Toolchain

C++17/CMake core with Python validation scripts, PowerShell build helpers, and a **LuaJIT** host that re-hosts recovered Lua modules. Work targets scene graphs, file streams, animation, OpenGL draw paths, and **Bullet** vehicle physics, comparing reconstructed behavior to original code through large test fixtures. (source: wiki/sources/descriptions/nat649__fs15-reconstruction.md)

## Research track

A parallel lane runs original GE6 x64 instructions on Linux under controlled VMs and platform adapters to study startup, rendering, and scripting without replacing the commercial executable wholesale. **Local game files are required**; the repo ships no commercial assets.

## Related

[[overviews/reverse-engineering]] · [[overviews/game-engine]] · [[static-runtime-evidence]] · [[ps2-port-engine]]

## Links

- Repo: https://github.com/nat649/fs15-reconstruction
