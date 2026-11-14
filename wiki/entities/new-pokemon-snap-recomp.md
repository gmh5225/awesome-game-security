---
title: New Pokémon Snap Recomp
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/finalpantasy__new-pokemon-snap-recomp.md
  - wiki/sources/README-categories.md
updated: 2026-11-14
confidence: medium
---

# new-pokemon-snap-recomp

Native Windows port of *New Pokémon Snap* (Switch **2.0.1**) from [finalpantasy/new-pokemon-snap-recomp](https://github.com/finalpantasy/new-pokemon-snap-recomp) via **ahead-of-time static recompilation**: retail AArch64 machine code lifts to C and links into a standalone x86-64 executable—**not** a runtime CPU emulator. Users supply their own dump; the repository ships **no game assets**. (source: wiki/sources/descriptions/finalpantasy__new-pokemon-snap-recomp.md)

## Stack

- **Lift / build:** C++ host code plus Python tooling; **LLVM/clang** compile generated C.
- **Runtime:** Hand-written **Horizon OS** high-level emulation for system services.
- **Graphics:** **NVN→Vulkan** bridge with shader translation; optional **DLSS** and **FSR** upscalers.
- **Validation:** **Ghidra**-based binary analysis, deterministic function maps, **Unicorn** instruction differential fuzzing, and automated route tests across CPU, graphics, audio, saves, and gameplay.
- **Extras:** Mod loading, in-game PC settings, and porter-focused documentation. (source: wiki/sources/descriptions/finalpantasy__new-pokemon-snap-recomp.md)

## Research use

Targets reverse engineers studying Switch binary translation, console GPU API shimming, and rehosting boundaries. Apply [[static-runtime-evidence]]: separate lifted guest code from reimplemented Horizon/NVN host services before citing renderer or gameplay fidelity—same discipline as [[letsgo-recomp]], [[smo-recomp]], and [[totk-pc-recomp]]. (source: wiki/sources/descriptions/finalpantasy__new-pokemon-snap-recomp.md)

## Links

- Repo: https://github.com/finalpantasy/new-pokemon-snap-recomp

## Related

[[letsgo-recomp]] · [[smo-recomp]] · [[totk-pc-recomp]] · [[xc2-recomp]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
