---
title: Samidare
kind: entity
topics: [game-hacking, windows-kernel, graphics-api]
sources:
  - wiki/sources/descriptions/M3351AN__Samidare.md
updated: 2026-08-23
confidence: medium
---

# Samidare

**External Counter-Strike 2 cheat** from **M3351AN** that reads game state through a **kernel driver communication interface** from a separate usermode process. Implemented in **C++**, it combines **FIFO-based driver communication**, **offset management**, **DirectX overlay rendering**, and **math utilities** for world-to-screen coordinate calculations. Primary research value: studying **driver-assisted external cheat implementations** and **overlay rendering techniques** for protected-process game memory access. README **External Ring3/Ring0** tag. (source: wiki/sources/descriptions/M3351AN__Samidare.md)

Sits in the kernel-assisted CS2 external lane beside [[ukia-rpm]], [[cs2-ext]], and [[valthrun]], and beside same-author kernel PoCs such as [[usugumo]], [[shirakumo]], and [[zhangbing-injector]].

## Architecture highlights

| Component | Role |
|-----------|------|
| Kernel driver (FIFO comm) | Cross-process game memory reads via FIFO-based KM↔UM interface |
| Offset management | Game structure / field offset bootstrap and maintenance |
| DirectX overlay | External on-screen rendering for ESP and UI feedback |
| Math utilities | Coordinate transforms for entity/world-to-screen calculations |

## Links

- Repo: https://github.com/M3351AN/Samidare (README: External Ring3/Ring0)

## Related

[[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]] · [[ukia-rpm]] · [[usugumo]] · [[shirakumo]] · [[cs2-ext]] · [[cs2-external-cheat]] · [[driver-physical-rw]] · [[km-um-communication]] · [[world-to-screen]] · [[present-hook]]
