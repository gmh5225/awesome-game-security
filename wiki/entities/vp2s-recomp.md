---
title: VP2S Recomp
kind: entity
topics: [reverse-engineering, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/TheBozos__VP2S_Recomp.md
  - wiki/sources/README-categories.md
updated: 2026-11-04
confidence: medium
---

# VP2S Recomp

**VP2S_Recomp** ([TheBozos/VP2S_Recomp](https://github.com/TheBozos/VP2S_Recomp)) is a **native Windows port** of *Valkyrie Profile 2: Silmeria* (NTSC-U **SLUS-21452**) that **statically recompiles** retail PlayStation 2 **MIPS R5900** executables, overlay modules, and **IOP** modules into C++ instead of running a full PS2 emulator stack. Users supply **legally obtained disc data**; the repository ships **no game assets**. (source: wiki/sources/descriptions/TheBozos__VP2S_Recomp.md)

## Toolchain

The project builds on **PS2Recomp** with **Ghidra** (Emotion Engine extension), Python/shell automation, and a custom runtime linker. Function mapping, encrypted-module handling, and disc asset extraction feed a playable PC binary. (source: wiki/sources/descriptions/TheBozos__VP2S_Recomp.md)

## Native host paths

Rendering, audio, UI, models, textures, and cutscenes use **native OpenGL** and **FFmpeg**, deliberately **avoiding default GS, VU1, and SPU2 emulation** while preserving the game’s own logic—useful for studying how much of a commercial PS2 title can run without classic emulator subsystems. (source: wiki/sources/descriptions/TheBozos__VP2S_Recomp.md)

## Research use

Targets reverse engineers and preservationists studying **PS2 binary analysis**, **static recompilation**, and **lift-vs-runtime** boundaries. Fits the README **Cheat → Source** lane beside [[gow-pc-port]] and [[ps2-port-engine]] with [[static-runtime-evidence]] labeling. (source: wiki/sources/README-categories.md)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[gow-pc-port]] · [[ps2-port-engine]] · [[static-runtime-evidence]]

## Links

- Repo: https://github.com/TheBozos/VP2S_Recomp
