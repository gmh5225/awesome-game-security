---
title: Xenoblade Chronicles X Recomp
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/jmars125__xcx-recomp.md
  - wiki/sources/README-categories.md
updated: 2026-11-02
confidence: medium
---

# xcx-recomp

**XCX Recomp** ([jmars125/xcx-recomp](https://github.com/jmars125/xcx-recomp)) statically recompiles *Xenoblade Chronicles X: Definitive Edition* from Nintendo Switch **ARM64** retail binaries into a native **Windows x86-64** program with a **Vulkan** renderer—without running a full Switch CPU emulator. Users supply their own game dumps via an included setup tool; the repository ships no copyrighted assets. The project is a **fork of TotK Recomp** and inherits techniques from **LAS Recomp** and related large-title porting work. (source: wiki/sources/descriptions/jmars125__xcx-recomp.md)

## Lift pipeline

A **Python lifter and code generator** translate **NSO modules** into **C** that is not hand-edited, with **jumptable** handling and **version-specific patch tables**. Changes are verified with **differential tests** against the **Unicorn** CPU emulator. (source: wiki/sources/descriptions/jmars125__xcx-recomp.md)

## Runtime host

The **C/C++ host runtime** emulates Nintendo SDK services, maps **NVN** graphics to **Vulkan** (including Maxwell-oriented behavior documented for debugging), and covers **audio**, **input**, **filesystem**, and **configuration**. (source: wiki/sources/descriptions/jmars125__xcx-recomp.md)

## Research use

Targets reverse engineers and preservation-minded developers studying **static binary translation**, **console module layout**, and **API re-hosting**—not anti-cheat or live online security. Apply [[static-runtime-evidence]] the same way as [[totk-pc-recomp]], [[smo-recomp]], and [[letsgo-recomp]]: separate lifted guest code from reimplemented Horizon/NVN host services before citing renderer or gameplay fidelity. (source: wiki/sources/descriptions/jmars125__xcx-recomp.md)

## Links

- Repo: https://github.com/jmars125/xcx-recomp

## Related

[[totk-pc-recomp]] · [[smo-recomp]] · [[letsgo-recomp]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
