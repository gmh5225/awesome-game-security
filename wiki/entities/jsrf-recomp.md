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

WIP static recompilation of *Jet Set Radio Future* (original Xbox XBE) to native macOS ARM64, built on sp00nznet/xboxrecomp. Translates the XBE into C rather than emulating it: replacement Xbox kernel, NV2A GPU and MCPX APU hardware models (from xemu), plus D3D8 graphics, DirectSound audio, and Xbox controller input translation layers. C and Python with CMake; includes a diagnostics harness for validating recompiled behavior against reference emulator traces. (source: wiki/sources/descriptions/andeecollard__jsrf-recomp.md)

Sits in the README `Xbox` lane beside HLE playback via [[xenia]] / [[xemu]], Xbox360→Windows porting via [[recompiler]], and original-Xbox LLE via [[xemu]] — but targets **static binary recompilation** of a specific OG Xbox title to native macOS rather than runtime emulation or 360 executable porting.

## Links

- Repo: https://github.com/andeecollard/jsrf-recomp (README tag: WIP static recompilation of Jet Set Radio Future (Xbox XBE) to native macOS, built on sp00nznet/xboxrecomp)

## Related

[[recompiler]] · [[xemu]] · [[xenia]] · [[xenia-mac]] · [[xbox360-emu]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
