---
title: Donkey Kong Bananza PC Recomp
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/Lucas-blip-png__dkb-pc-recomp.md
  - wiki/sources/README-categories.md
updated: 2026-11-03
confidence: medium
---

# dkb-pc-recomp

**DKB Recomp** ([Lucas-blip-png/dkb-pc-recomp](https://github.com/Lucas-blip-png/dkb-pc-recomp)) statically recompiles *Donkey Kong Bananza* from Nintendo **Switch 2** **ARM64** retail binaries into a native **Windows x86-64** executable with a **Vulkan** renderer. Users supply their own dumped main and SDK modules; the repository ships no game assets or recompiled binaries. Progress is early and tutorial-oriented, with a documented **NVN** / **SPIR-V** reverse-engineering pipeline. (source: wiki/sources/descriptions/Lucas-blip-png__dkb-pc-recomp.md)

## Lift pipeline

A **Python lifter** under `recomp/` translates dumped **main and SDK modules** into **generated C** compiled with **Clang**. The project extends **TotK Recomp** and **LAS Recomp** patterns with **version-specific binary patches**, **jumptable** handling, and **Unicorn-backed differential tests** that validate lifting against original ARM64 behavior. (source: wiki/sources/descriptions/Lucas-blip-png__dkb-pc-recomp.md)

## Runtime host

The **C/C++ runtime** emulates Switch services, implements an **NVN 2** graphics front end on **Vulkan**, and lowers **Ampere** guest shaders to **Maxwell** via **Eglantine**. (source: wiki/sources/descriptions/Lucas-blip-png__dkb-pc-recomp.md)

## Research use

Targets reverse engineers, preservation researchers, and developers studying **Switch 2** binaries, proprietary GPU APIs, and **static recompilation** pipelines—not anti-cheat or online security. Apply [[static-runtime-evidence]] the same way as [[totk-pc-recomp]], [[xcx-recomp]], [[smo-recomp]], and [[letsgo-recomp]]: separate lifted guest code from reimplemented NVN/host services before citing renderer or gameplay fidelity. (source: wiki/sources/descriptions/Lucas-blip-png__dkb-pc-recomp.md)

## Links

- Repo: https://github.com/Lucas-blip-png/dkb-pc-recomp

## Related

[[totk-pc-recomp]] · [[xcx-recomp]] · [[smo-recomp]] · [[letsgo-recomp]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
