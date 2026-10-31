---
title: BottleShip
kind: entity
topics: [graphics-api, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/jenissimo__bottleship.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: high
---

# BottleShip

[jenissimo/bottleship](https://github.com/jenissimo/bottleship) — **browser-based** engine that boots legacy **x86 Win32 PE** executables by pairing **v86** CPU emulation with high-level emulation (HLE) of Win32, COM, and **DirectDraw/Direct3D 3–9** on modern web APIs. Targets compatibility work, game preservation, and deep study of how Windows games call OS, graphics, audio, and threading layers without a native Windows host. (source: wiki/sources/descriptions/jenissimo__bottleship.md)

## Stack

TypeScript host, **Rust-to-WASM v86** core, **WebGPU** graphics pipeline translating fixed-function Direct3D states, **WebAudio**, and an **OPFS**-backed virtual filesystem with **WGB** game bundles and **GOG** import support. (source: wiki/sources/descriptions/jenissimo__bottleship.md)

## Win32 and installer surface

Faithful **WinAPI module** implementations plus self-hosted parsers for common **installer and archive** formats ship in-tree—useful when tracing how retail titles depend on legacy setup and packaging paths. (source: wiki/sources/descriptions/jenissimo__bottleship.md)

## Automation

An **automation harness** loads titles, drives input, and captures **structured debug snapshots** for regression and API-coverage work. (source: wiki/sources/descriptions/jenissimo__bottleship.md)

## Research use

Apply [[static-runtime-evidence]] by separating **v86-emulated guest CPU** behavior from **reimplemented Win32/COM/D3D host paths** before treating WebGPU output or threading semantics as Windows-faithful references—parallel to lift-vs-HLE labeling on static recomp ports. (source: wiki/sources/descriptions/jenissimo__bottleship.md)

Listed under **DirectX → Emulation** beside software D3D9 stacks such as [[software-d3d9]].

## Links

- Repo: https://github.com/jenissimo/bottleship

## Related

[[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[software-d3d9]] · [[dxwrapper]] · [[winehooks]] · [[static-runtime-evidence]]
