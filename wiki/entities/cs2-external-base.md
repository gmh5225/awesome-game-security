---
title: CS2-external-base
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/UnnamedZ03__CS2-external-base.md
updated: 2026-08-20
confidence: medium
---

# CS2-external-base

Basic **external Counter-Strike 2 overlay visualization framework** from UnnamedZ03. Written in C++, it demonstrates overlay-side structure for external tooling: team checks and multiple ESP outputs including box, health, distance, skeleton, and text displays. The project intentionally omits memory read/write driver components, positioning itself as an educational starter base for studying external cheat architecture without bundled kernel access layers. README **External** tag. (source: wiki/sources/descriptions/UnnamedZ03__CS2-external-base.md)

## Architecture highlights

| Component | Role |
|-----------|------|
| Overlay renderer | ESP box, health, distance, skeleton, and text draw paths |
| Team checks | Friendly/enemy filtering for visualization |
| (omitted) | No bundled memory R/W or kernel driver interface |

Contrast with full-stack externals such as [[cs2-ext]] (kernel driver + D3D11 overlay) or [[valthrun]] (Rust kernel read-only framework). Pair with [[world-to-screen]] for projection math and [[pythoncs2]] for another educational external workflow sample.

## Links

- Repo: https://github.com/UnnamedZ03/CS2-external-base

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[cs2-ext]] · [[cs2-external-cheat]] · [[cs2-external]] · [[cs2-external-1]] · [[pythoncs2]] · [[titled-gui-cs2]] · [[world-to-screen]] · [[valthrun]]
