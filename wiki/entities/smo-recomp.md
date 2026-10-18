---
title: Super Mario Odyssey Recompiled
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/Coz-0__smo-recomp.md
  - wiki/sources/README-categories.md
updated: 2026-10-18
confidence: medium
---

# smo-recomp

Native Windows x64 port of *Super Mario Odyssey* (Switch firmware **1.4.1**, AArch64 guest) built by **static recompilation**—the retail executable is lifted to C and linked against a custom host runtime instead of emulating the Switch CPU with an interpreter or JIT. (source: wiki/sources/descriptions/Coz-0__smo-recomp.md)

## Stack

- **Lift:** Python-based ahead-of-time lifter (per-function translation); Clang compiles generated C.
- **Validation:** Unicorn differential tests per function for instruction fidelity.
- **Runtime:** reimplemented Switch system libraries, file I/O, audio, SDL3 input.
- **Graphics:** NVN-style API on Vulkan with Maxwell-to-SPIR-V shader translation.

## Audience

Researchers studying Switch binary structure, static recompilation pipelines, and how commercial titles can be ported to native hosts without a CPU emulator—beside other console static-recomp projects such as [[ngbrecomp]] and [[sc2-android-recomp]]. Users must supply their own **decrypted dump**; the repository ships no game assets.

## Links

- Repo: https://github.com/Coz-0/smo-recomp

## Related

[[ngbrecomp]] · [[sc2-android-recomp]] · [[static-runtime-evidence]] · [[opensw]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
