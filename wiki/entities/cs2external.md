---
title: cs2External
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/Tokyodidit__cs2External.md
updated: 2026-08-20
confidence: medium
---

# cs2External

**External Counter-Strike 2 ESP** from Tokyodidit. Written in C++, it reads game process memory with configurable JSON offsets and applies world-to-screen math to track in-game entities. Rendering uses a transparent **Win32/GDI overlay** that draws boxes, health bars, and player names. Positioned for cheat prototyping and practical game memory analysis. README **External** tag. (source: wiki/sources/descriptions/Tokyodidit__cs2External.md)

## Architecture highlights

| Component | Role |
|-----------|------|
| Process memory reads | Out-of-process entity/state access |
| JSON offsets | Configurable layout without hard-coded rebuilds |
| World-to-screen | 3D entity positions → 2D overlay coordinates |
| Win32/GDI overlay | Transparent layered window; box / health / name ESP |

Contrasts with D3D11/ImGui externals such as [[cs2-external-1]] and [[titled-gui-cs2]], and overlay-only scaffolds such as [[cs2-external-base]] that omit bundled memory access. Pair with [[world-to-screen]] for projection math and [[cs2-offsets]] for offset feeds.

## Links

- Repo: https://github.com/Tokyodidit/cs2External

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[cs2-external-base]] · [[cs2-external-cheat]] · [[cs2-external]] · [[cs2-external-1]] · [[pythoncs2]] · [[titled-gui-cs2]] · [[cs2-offsets]] · [[world-to-screen]]
