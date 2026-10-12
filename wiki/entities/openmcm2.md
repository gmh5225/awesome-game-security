---
title: OpenMCM2
kind: entity
topics: [reverse-engineering, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/xshxdex98__OpenMCM2.md
  - wiki/sources/README-categories.md
updated: 2026-10-12
confidence: medium
---

# OpenMCM2

**OpenMCM2** (xshxdex98/OpenMCM2) is a **native rebuild** of *Motocross Madness 2*: disassemble the retail Windows PE, relink with a custom harness, and run new code beside the original image while **preserving retail sections byte-for-byte**. Listed under README **Cheat / RE Tools** as measured decompilation/preservation research—not a redistributable game build. (source: wiki/sources/descriptions/xshxdex98__OpenMCM2.md)

## Pipeline

Targets a fixed-base **MSVC 6.0 PE32** binary. **Ghidra Java exporters**, Python build scripts, and assembly/link steps recover functions, map **RTTI**, and verify relinked images against retail. Individual routines can be replaced with ported **C** that must match retail behavior except deliberate redirects. (source: wiki/sources/descriptions/xshxdex98__OpenMCM2.md)

## Renderer

Added runtime is mostly **C**, including an **OpenGL** implementation of **DirectDraw 7** and **Direct3D 7** without wrapper DLLs or injection. Optional DirectDraw tracing compares calls against the original renderer. Portable settings live in JSON beside the game directory. (source: wiki/sources/descriptions/xshxdex98__OpenMCM2.md)

## Audience

Reverse engineers and preservation researchers studying legacy protected PC titles—similar lanes to [[kabus22-linux]], [[motorstorm-mv-recomp]], and [[pipeline-disasm]] static rebuild workflows. (source: wiki/sources/descriptions/xshxdex98__OpenMCM2.md)

## Links

- Repo: https://github.com/xshxdex98/OpenMCM2

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[concepts/static-runtime-evidence]]
