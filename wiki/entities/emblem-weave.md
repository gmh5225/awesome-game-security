---
title: EmblemWeave
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/XiONDiGiTaL__EmblemWeave.md
updated: 2026-11-10
confidence: medium
---

# emblem-weave

**EmblemWeave** ([XiONDiGiTaL/EmblemWeave](https://github.com/XiONDiGiTaL/EmblemWeave)) is a **Rust**-based Windows launcher and **static recompilation** stack that runs *Fire Emblem: Fortune's Weave* (Nintendo **Switch 2**) natively from a user-supplied game dump—without a full Switch CPU emulator. It targets reverse engineers, preservationists, and game-security researchers studying AArch64 binary analysis, static translation, and host-side runtime replacement for modern console titles. Users must bring their own dump; the repository ships no retail assets. (source: wiki/sources/descriptions/XiONDiGiTaL__EmblemWeave.md)

## Lift pipeline

The toolchain decodes compressed **NSO** modules, performs control-flow recovery on **AArch64** machine code, and lifts it into portable **C** compiled for Windows x64. (source: wiki/sources/descriptions/XiONDiGiTaL__EmblemWeave.md)

## Runtime host

A high-level emulation layer reimplements console **SDK services**; graphics go through an **NVN**-backed layer on **Vulkan**. Verification layers include a reference interpreter and independent **CPU models** beside normal execution. (source: wiki/sources/descriptions/XiONDiGiTaL__EmblemWeave.md)

## Modding and cheat surfaces

Bundled tooling covers save editing, **RomFS** mod installation, in-game menus, and cheat support—including **Atmosphere** codes and **Cheat Engine** tables mapped to live game memory—which makes the port useful for studying how static-recomp hosts expose the same mod/cheat attack surface as emulators or native PC builds. (source: wiki/sources/descriptions/XiONDiGiTaL__EmblemWeave.md)

## Research use

Apply [[static-runtime-evidence]] like [[dkb-pc-recomp]], [[mkw-thwomp]], [[totk-pc-recomp]], and [[smo-recomp]]: separate lifted guest AArch64 from reimplemented Horizon services and NVN host paths before citing renderer, gameplay, or preservation fidelity. (source: wiki/sources/descriptions/XiONDiGiTaL__EmblemWeave.md)

## Links

- Repo: https://github.com/XiONDiGiTaL/EmblemWeave

## Related

[[dkb-pc-recomp]] · [[mkw-thwomp]] · [[totk-pc-recomp]] · [[smo-recomp]] · [[letsgo-recomp]] · [[xcx-recomp]] · [[xc2-recomp]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
