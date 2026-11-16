---
title: timeLink
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/HanYolo1__timeLink.md
  - wiki/sources/README-categories.md
updated: 2026-11-16
confidence: medium
---

# timelink

**timeLink** ([HanYolo1/timeLink](https://github.com/HanYolo1/timeLink)) is an active **Longshot**-lineage fork that **statically recompiles** AArch64 code from a supported Nintendo Switch title into **C**, then builds a native **Windows or Linux** program. The host reimplements **Horizon OS** and **NVN 2** while replaying GPU work on **Vulkan**—not by emulating the Switch CPU. (source: wiki/sources/descriptions/HanYolo1__timeLink.md)

## Pipeline

- **nx2 tooling:** Python pipeline for dump, lift, and compile.
- **Host layers:** C/C++ runtime plus Vulkan renderer; optional upscaling and frame-generation paths.
- **Distribution model:** Launcher/builder produces binaries from the user’s **local game files** only—no shipped copyrighted assets. (source: wiki/sources/descriptions/HanYolo1__timeLink.md)

## Validation

Contributors use automated tests, **Unicorn**-backed instruction checks, shader lowering and **SPIR-V** tooling, pipeline caching, and GPU compatibility work including **mesh-shader fallbacks**. Documented status tables track bring-up progress. (source: wiki/sources/descriptions/HanYolo1__timeLink.md)

## Research use

Targets reverse engineers, graphics/platform researchers, and preservation-minded developers studying how large commercial Switch software becomes auditable native code. Apply [[static-runtime-evidence]] labeling—lifted guest logic vs reimplemented Horizon/NVN 2/Vulkan services—alongside [[smo-recomp]], [[totk-pc-recomp]], and [[dkb-pc-recomp]]. (source: wiki/sources/descriptions/HanYolo1__timeLink.md)

Listed under **Cheat / Source** (README Switch static recompilation lane).

## Links

- Repo: https://github.com/HanYolo1/timeLink (Longshot fork; Switch static recomp to Windows/Linux Vulkan; BYO-assets build flow)

## Related

[[smo-recomp]] · [[totk-pc-recomp]] · [[letsgo-recomp]] · [[dkb-pc-recomp]] · [[xcx-recomp]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]