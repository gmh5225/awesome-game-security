---
title: victory-fork
kind: entity
topics: [graphics-api, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/fxceless__victory-fork.md
updated: 2026-11-25
confidence: medium
---

# victory-fork

**victory-fork** is a work-in-progress GPL fork of Marvisak **VIctory**, a Rust compatibility layer that runs Xbox Series X|S game executables natively on Windows when the user supplies their own game files. The workspace bundles a PE loader, high-level emulation of Xbox runtime services, decoders for console asset formats, and a Direct3D 12 graphics stack that recompiles console shaders to DXIL on demand. (source: wiki/sources/descriptions/fxceless__victory-fork.md)

This fork tracks upstream VIctory while targeting GPU, memory, and rendering fixes that improve in-world playback, frame times, and stability on real PC hardware. It is aimed at developers and researchers studying Xbox Series platform behavior, native PC porting of console titles, graphics-pipeline translation, and how retail console games bind to Windows and D3D12.

## Links

- Repo: https://github.com/fxceless/victory-fork (README: GPL fork of Marvisak VIctory for Xbox Series titles on Windows—D3D12 backend, shader recompiler fixes, performance tuning; BYO game files)

## Related

[[velox]] · [[mesia-unified]] · [[xenia]] · [[nxbox]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]