---
title: Ninja Gaiden II Recompiled
kind: entity
topics: [reverse-engineering, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/gamboozino__ng2recomp.md
  - wiki/sources/README-categories.md
updated: 2026-11-08
confidence: medium
---

# ng2recomp

**Ninja Gaiden II Recompiled** (gamboozino/ng2recomp) statically recompiles the Xbox 360 retail build of *Ninja Gaiden II* into native Linux and Windows binaries instead of running the title inside a full-system emulator. Listed under README **Cheat** (static recompilation via ReXGlue with a custom Vulkan renderer; BYO game assets). (source: wiki/sources/descriptions/gamboozino__ng2recomp.md) (source: wiki/sources/README-categories.md)

## Static recompilation

Built on the **ReXGlue** SDK with C++23 and CMake, the project lifts the guest PowerPC machine code to host binaries and hooks Direct3D usage into a **custom Vulkan renderer**. **Xenos** GPU shaders are pre-translated to SPIR-V at build time using a patched **XenosRecomp** pipeline. (source: wiki/sources/descriptions/gamboozino__ng2recomp.md)

## RE workflow

The codebase documents reverse-engineering workflows such as loading the retail **XEX** in Ghidra and mapping D3D call sites, plus tooling to extract shaders from user-supplied game assets. (source: wiki/sources/descriptions/gamboozino__ng2recomp.md)

## Audience

Targets researchers and developers studying console binary translation, graphics pipeline reuse, and practical static recompilation of retail game executables—not live anti-cheat or online-service analysis. (source: wiki/sources/descriptions/gamboozino__ng2recomp.md)

## Positioning

Sits in gamboozino’s Ninja Gaiden preservation lane beside OG Xbox [[ngbrecomp]] (xboxrecomp XBE lift) and in the README Xbox 360 **ReXGlue** cluster beside [[wwe-svr2009-recomp]], [[nhl-legacy-remaster]], and [[futari-recomp]]. Pair XEX analysis with [[idaxex]] and [[ida-vmx128-helper]]. (source: wiki/sources/README-categories.md)

## Links

- Repo: https://github.com/gamboozino/ng2recomp

## Related

[[ngbrecomp]] · [[wwe-svr2009-recomp]] · [[futari-recomp]] · [[nhl-legacy-remaster]] · [[mcla-pc]] · [[xenia]] · [[idaxex]] · [[static-runtime-evidence]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
