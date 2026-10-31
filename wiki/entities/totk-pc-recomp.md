---
title: Tears of the Kingdom PC Recomp
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/valentderah__totk-pc-recomp.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: medium
---

# totk-pc-recomp

**TotK Recomp** ([valentderah/totk-pc-recomp](https://github.com/valentderah/totk-pc-recomp)) statically recompiles *The Legend of Zelda: Tears of the Kingdom* from Nintendo Switch **ARM64** retail binaries into a native **Windows x86-64** executable with a **Vulkan** graphics backend. Users supply their own game assets; the repository ships **no recompiled game binaries** or copyrighted content. (source: wiki/sources/descriptions/valentderah__totk-pc-recomp.md)

## Lift pipeline

A **Python-driven lifter and code generator** translates **NSO modules** into **C**. Output is validated with **differential tests** against the **Unicorn** CPU emulator. **Version-specific patch lists** adapt multiple retail game builds. A bundled **installer and build pipeline** compiles lifted code locally with **llvm-mingw**. (source: wiki/sources/descriptions/valentderah__totk-pc-recomp.md)

## Runtime host

The Windows runtime **emulates Switch kernel services**, **NVN** graphics, **audio**, **input**, and **filesystem** behavior. Optional enhancements include **resolution scaling**, **ultrawide layout**, and **frame-rate controls**. (source: wiki/sources/descriptions/valentderah__totk-pc-recomp.md)

## Research use

Targets researchers and developers studying **static recompilation**, **console binary lifting**, and **low-level game porting**. Apply the same [[static-runtime-evidence]] discipline as [[smo-recomp]] and [[letsgo-recomp]]: treat lifted guest code separately from reimplemented Horizon/NVN host services before citing renderer or gameplay fidelity. (source: wiki/sources/descriptions/valentderah__totk-pc-recomp.md)

## Links

- Repo: https://github.com/valentderah/totk-pc-recomp

## Related

[[smo-recomp]] · [[letsgo-recomp]] · [[nakagawa-recomp]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
