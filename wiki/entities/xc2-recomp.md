---
title: Xenoblade Chronicles 2 Recomp
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/AksharDP__xc2-recomp.md
  - wiki/sources/README-categories.md
updated: 2026-11-04
confidence: medium
---

# xc2-recomp

**XC2 Recomp** ([AksharDP/xc2-recomp](https://github.com/AksharDP/xc2-recomp)) statically recompiles *Xenoblade Chronicles 2* from Nintendo Switch **ARM64** retail binaries into a native **Windows x86-64** application with a **Vulkan** graphics stack—without running a full Switch CPU emulator. It is a **fork of [[xcx-recomp]]** (XCX Recomp / TotK Recomp lineage). Users supply their own legally obtained **NSP** files and keys via a **Python installer**; the repository ships no game assets. (source: wiki/sources/descriptions/AksharDP__xc2-recomp.md)

## Lift pipeline

A **Python toolchain** lifts Switch **NSO modules** to **generated C**, applies **version-specific binary patches** for supported game updates, and validates behavior with **differential tests** against the **Unicorn** CPU emulator. (source: wiki/sources/descriptions/AksharDP__xc2-recomp.md)

## Runtime host

The **C runtime** implements host replacements for Switch **kernel services**, **NVN** graphics (Vulkan stack), **audio**, **input**, and **filesystem** access, with optional **mod and cheat overlays** built from user-supplied dumps. (source: wiki/sources/descriptions/AksharDP__xc2-recomp.md)

## Research use

Targets reverse engineers, porting researchers, and fans studying how commercial Switch titles translate to **PC-native execution** without a full emulator—not anti-cheat or live online security. Apply [[static-runtime-evidence]] the same way as [[totk-pc-recomp]], [[xcx-recomp]], [[smo-recomp]], and [[letsgo-recomp]]: separate lifted guest code from reimplemented Horizon/NVN host services before citing renderer or gameplay fidelity. (source: wiki/sources/descriptions/AksharDP__xc2-recomp.md)

## Links

- Repo: https://github.com/AksharDP/xc2-recomp

## Related

[[xcx-recomp]] · [[totk-pc-recomp]] · [[smo-recomp]] · [[letsgo-recomp]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
