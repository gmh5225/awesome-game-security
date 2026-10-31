---
title: BottleShip
kind: entity
topics: [graphics-api, reverse-engineering]
sources:
  - wiki/sources/descriptions/jenissimo__bottleship.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: medium
---

# BottleShip

**Browser-based** engine that runs legacy **x86 Win32** games by pairing **v86** CPU emulation with high-level emulation of Win32, COM, and **DirectDraw/Direct3D 3–9** on modern web APIs. TypeScript host, Rust-to-WASM v86 core, **WebGPU** pipeline for fixed-function D3D states, **OPFS** virtual filesystem with WGB bundles and GOG import, WebAudio, and automation harnesses for load/input/debug snapshots. Targets compatibility research, game preservation, and study of how Windows titles call OS, graphics, audio, and threading layers without a native Windows host. (source: wiki/sources/descriptions/jenissimo__bottleship.md)

Listed under **DirectX → Emulation** beside software D3D9 stacks such as [[software-d3d9]].

## Links

- Repo: https://github.com/jenissimo/bottleship

## Related

[[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[software-d3d9]] · [[dxwrapper]] · [[winehooks]]
