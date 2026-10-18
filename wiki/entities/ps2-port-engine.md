---
title: PS2 Port Engine
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/danielgomesvieira2000__ps2-port-engine.md
  - wiki/sources/README-categories.md
updated: 2026-10-18
confidence: high
---

# PS2 Port Engine

**ps2-port-engine** (danielgomesvieira2000/ps2-port-engine) is a **verified PlayStation 2 decompilation toolchain** and **native PC port runtime**: Python **ps2decomp** lifts retail MIPS (R5900/VU) into C++ with differential checks against an interpreter, then links to a host that emulates EE kernel, IOP, DMA, SPU2, VIF, pads, memory cards, and disc I/O behind a **Vulkan Graphics Synthesizer** renderer and SDL3 input. (source: wiki/sources/descriptions/danielgomesvieira2000__ps2-port-engine.md)

Ships **no game assets**; ports are built from disc images the researcher owns. Useful for preservation, interoperability study, and console binary structure—not live online cheat development.

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[static-runtime-evidence]] · [[vifterpreter]]

## Links

- Repo: https://github.com/danielgomesvieira2000/ps2-port-engine
