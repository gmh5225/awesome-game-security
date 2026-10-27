---
title: Nakagawa Recomp
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/Jstar269__nakagawa-recomp.md
  - wiki/sources/README-categories.md
updated: 2026-10-27
confidence: medium
---

# nakagawa-recomp

**Nakagawa Recomp** (Jstar269/nakagawa-recomp) statically recompiles **PlayStation Portable (MIPS)** game binaries into native **C** you build and run on **Windows** through an integrated launcher and player—aimed at developers, preservationists, and reverse engineers who want analyzable PSP executables and playable native ports rather than conventional emulation alone. The project forks the **sal063** PSP recompilation lineage and pairs with an **hst-decomp** reverse-engineering workflow for PSP titles. (source: wiki/sources/descriptions/Jstar269__nakagawa-recomp.md)

## Stack

- **Lift:** PSP EBOOT/executable modules → generated C; **MIPS guest runtime** with **VFPU** support data rather than a full handheld CPU interpreter.
- **Build:** Engine core primarily **C**; **Python** tools for codegen, pipeline tests, cosimulation against a reference interpreter, **decomp.me** export, and optional verification against real PSP hardware.
- **Runtime / UI:** **Vulkan** rendering; **SDL3** launcher and player for setup, controller mapping, and running recompiled titles.
- **Assets:** BYO disc content; no copyrighted game files in the repository.

## Research hooks

Cosimulation and optional hardware checks support labeling which lifted paths match reference behavior before treating the Windows build as a fidelity reference—useful beside other static-recomp lanes such as [[letsgo-recomp]], [[smo-recomp]], and [[ps2-port-engine]]. (source: wiki/sources/descriptions/Jstar269__nakagawa-recomp.md)

## Links

- Repo: https://github.com/Jstar269/nakagawa-recomp

## Related

[[letsgo-recomp]] · [[smo-recomp]] · [[ps2-port-engine]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
