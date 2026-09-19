---
title: jsrf-recomp
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/andeecollard__jsrf-recomp.md
  - wiki/sources/README-categories.md
updated: 2026-09-19
confidence: medium
---

# jsrf-recomp

Specialized fork of sp00nznet/xboxrecomp that statically recompiles *Jet Set Radio Future* (original Xbox XBE) to native macOS ARM64 by translating the executable into C instead of emulating it. (source: wiki/sources/descriptions/andeecollard__jsrf-recomp.md)

## Stack

- **Runtime:** replacement Xbox kernel plus NV2A GPU and MCPX APU hardware models extracted from [[xemu]].
- **Translation layers:** D3D8 graphics, DirectSound audio, and Xbox controller input.
- **Build:** C and Python with CMake.
- **Validation:** extensive diagnostics harness that compares recompiled behavior against reference emulator traces. (source: wiki/sources/descriptions/andeecollard__jsrf-recomp.md)

Sits in the README `Xbox` lane beside HLE playback via [[xenia]] / [[xemu]], Xbox 360→Windows porting via [[recompiler]], and original-Xbox LLE via [[xemu]] — but targets **static binary recompilation** of a specific OG Xbox title to native macOS rather than runtime emulation or 360 executable porting.

## Audience

Researchers and developers working on Xbox game preservation, static binary recompilation, and low-level reverse engineering of original Xbox titles. (source: wiki/sources/descriptions/andeecollard__jsrf-recomp.md)

## Links

- Repo: https://github.com/andeecollard/jsrf-recomp (README tag: WIP static recompilation of Jet Set Radio Future (Xbox XBE) to native macOS, built on sp00nznet/xboxrecomp)

## Related

[[recompiler]] · [[xemu]] · [[xenia]] · [[xenia-mac]] · [[xbox360-emu]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
