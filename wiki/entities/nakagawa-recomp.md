---
title: Nakagawa Recomp
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/README-categories.md
updated: 2026-10-27
confidence: low
---

# nakagawa-recomp

**nakagawa-recomp** (Jstar269/nakagawa-recomp) is a static recompiler and runtime that lifts **PlayStation Portable (MIPS)** game binaries to native **Windows** with **Vulkan** and **SDL3**, requiring user-supplied disc assets. The README positions it alongside an **hst-decomp** reverse-engineering workflow for PSP titles. (source: wiki/sources/README-categories.md)

## Stack

- **Lift:** MIPS PSP executables to native Windows via static recompilation (not full CPU emulation of the handheld).
- **Graphics:** Vulkan rendering path with SDL3 windowing/input.
- **Assets:** BYO disc content; no copyrighted game files in the repository.

## Research hooks

Useful for studying MIPS→x64 static lift boundaries, PSP format RE, and runtime replacement patterns beside other console static-recomp lanes such as [[letsgo-recomp]] and [[smo-recomp]].

## Links

- Repo: https://github.com/Jstar269/nakagawa-recomp

## Related

[[letsgo-recomp]] · [[smo-recomp]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
