---
title: Savage Wind Recomp
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/Revivedx__SavageWindRecomp.md
  - wiki/sources/README-categories.md
updated: 2026-11-19
confidence: medium
---

# savage-wind-recomp

**Savage Wind Recomp** ([Revivedx/SavageWindRecomp](https://github.com/Revivedx/SavageWindRecomp)) is a work-in-progress **static recompilation** port of *The Legend of Zelda: Breath of the Wild* (Nintendo Switch **1.9.0**) to a native PC game library on **Windows** and **Linux**, built on **LAS Recomp** patterns. Users supply their own extracted game files; the repository ships runtime, toolchain, and docs—**no game assets**. (source: wiki/sources/descriptions/Revivedx__SavageWindRecomp.md)

## Lift pipeline

The toolchain loads Switch **NSO** modules, lifts **AArch64** instructions, applies **version-aware patches**, and emits **C** that players compile locally from BYO dumps. Python utilities integrate **Capstone**, **Unicorn**, and **Ghidra** helpers for analysis and codegen. (source: wiki/sources/descriptions/Revivedx__SavageWindRecomp.md)

## Runtime host

The host runtime high-level-emulates Switch **OS services**, translates **Maxwell** shaders, and renders via **Vulkan** (optional **Metal**). The project bundles profiling, memory scanning, and extensive gameplay and graphics customization for research and modding. (source: wiki/sources/descriptions/Revivedx__SavageWindRecomp.md)

## Research use

Targets reverse engineers, porting researchers, and advanced players studying **console binary translation**, guest-to-host **ABI** mapping, and large-scale static recompilation—not anti-cheat or online security. Apply [[static-runtime-evidence]] the same way as [[totk-pc-recomp]], [[letsgo-recomp]], and [[timelink]]: separate lifted guest code from reimplemented Horizon/GPU host services before citing fidelity. (source: wiki/sources/descriptions/Revivedx__SavageWindRecomp.md)

## Links

- Repo: https://github.com/Revivedx/SavageWindRecomp

## Related

[[totk-pc-recomp]] · [[letsgo-recomp]] · [[timelink]] · [[smo-recomp]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]