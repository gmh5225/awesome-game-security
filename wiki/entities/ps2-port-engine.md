---
title: PS2 Port Engine
kind: entity
topics: [reverse-engineering, game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/danielgomesvieira2000__ps2-port-engine.md
  - wiki/sources/README-categories.md
updated: 2026-10-18
confidence: high
---

# PS2 Port Engine

**ps2-port-engine** ([danielgomesvieira2000/ps2-port-engine](https://github.com/danielgomesvieira2000/ps2-port-engine)) is a **verified PlayStation 2 decompilation toolchain** and **native PC port runtime** for turning retail PS2 executables into C++ ports whose behavior is checked against the original MIPS machine code. (source: wiki/sources/descriptions/danielgomesvieira2000__ps2-port-engine.md)

## Toolchain (`ps2decomp`)

Python **ps2decomp** and CLI tools handle **ELF and disc parsing**, **R5900 and VU disassembly**, automated analysis, symbolic derivation, instruction lifting, and **differential verification** against an R5900 interpreter before reconstructed game logic is emitted as C++17. (source: wiki/sources/descriptions/danielgomesvieira2000__ps2-port-engine.md)

## Runtime host

Rebuilt game code links to a host that replaces PS2 hardware: **EE kernel**, **IOP**, **DMA**, **SPU2**, **VIF**, **VUs**, pads, memory cards, and disc I/O. Display and input go through a **Vulkan-based Graphics Synthesizer** renderer and **SDL3**, with port features such as higher resolution and frame pacing. (source: wiki/sources/descriptions/danielgomesvieira2000__ps2-port-engine.md)

## Assets and research use

Ships **no game assets**; ports are built from **disc images the player owns**. The workflow targets reverse engineering for **interoperability**, **preservation**, and studying how commercial PS2 titles are structured and executed—not live online cheat development.

## Related

[[overviews/reverse-engineering]] · [[overviews/game-engine]] · [[overviews/graphics-api]] · [[static-runtime-evidence]] · [[ps2-ida-vu-micro]] · [[vifterpreter]]

## Links

- Repo: https://github.com/danielgomesvieira2000/ps2-port-engine
