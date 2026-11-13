---
title: MKSM
kind: entity
topics: [reverse-engineering, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/lagando__MKSM.md
updated: 2026-11-13
confidence: medium
---

# MKSM

**MKSM** ([lagando/MKSM](https://github.com/lagando/MKSM)) **statically recompiles** retail *Mortal Kombat: Shaolin Monks* (PlayStation 2, NTSC-U **SLUS-210.87**) into **native host code** via a **PS2Recomp** toolchain clone and patch layer, running on modern PCs **without a conventional emulator dispatch loop**. Users supply a **legally obtained ISO**; the repository ships **no game assets**. (source: wiki/sources/descriptions/lagando__MKSM.md)

## Toolchain and runtime

Primary implementation is **C++** with shell build scripts, optional GPU compute and vertex shaders for the **Graphics Synthesizer**, and automation to extract files from the user-owned disc image. The runtime models or accelerates PS2 subsystems including **EE**, **IOP**, **DMA**, **VIF**, **VU0/VU1** microcode (with **x86-64 JIT**), **GIF/GS** rendering (including a **Vulkan** GS path), audio through real IOP modules, and game-specific high-level hooks for **CDVD**, libc math, and boot flow. Architecture notes, regression tests, and performance tuning support preservation and subsystem-boundary RE. (source: wiki/sources/descriptions/lagando__MKSM.md)

## Research use

Useful for reverse engineers and preservationists studying how a complex PS2 action title maps onto a **determinism-oriented recompiled runtime**, and for comparing **lifted guest logic** vs **host-reimplemented** graphics and I/O paths. Apply [[static-runtime-evidence]] labeling beside [[vp2s-recomp]] and [[gow-pc-port]] in the PS2 static-recomp cluster. (source: wiki/sources/descriptions/lagando__MKSM.md)

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[static-runtime-evidence]] · [[vp2s-recomp]] · [[gow-pc-port]] · [[ps2-port-engine]]

## Links

- Repo: https://github.com/lagando/MKSM
