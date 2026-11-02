---
title: Harvest Moon SNES Decomp
kind: entity
topics: [game-engine, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/RodoLy__HarvestMoonSnesDecomp.md
updated: 2026-11-02
confidence: medium
---

# harvest-moon-snes-decomp

Readable **decompilation** of SNES *Harvest Moon* that rewrites literal **65816** recompiler output into clear **C** while keeping behavior **byte-identical** to the retail cartridge baseline from **HM-Decomp**. **Python** tooling imports community routine names, applies decomp overrides at build time, and tracks rewrite progress with automated check scripts against the recompiled baseline. (source: wiki/sources/descriptions/RodoLy__HarvestMoonSnesDecomp.md)

The tree pairs decomp sources with a **native C host** embedding SNES **CPU**, **PPU**, and **audio** components, **cross-platform** launchers (Windows, macOS, Linux), optional **Android** builds, **save states**, and non-destructive **IPS/BPS** mod loading. Guides document console registers, farm and weather systems, event scripting, and interpreter vs compiled-path differences for per-routine validation. README notes in-game cheat hooks for local experimentation; users supply their own ROM (**BYO ROM**). (source: wiki/sources/descriptions/RodoLy__HarvestMoonSnesDecomp.md)

Targets reverse engineers, preservationists, and mod developers who need **source-level** classic SNES game logic—not live anti-cheat or online security research. Sit beside other Game Develop / source SNES work ([[zelda3]], [[devilution]]) and apply [[static-runtime-evidence]] when separating decomp game logic from embedded emulator host services. (source: wiki/sources/descriptions/RodoLy__HarvestMoonSnesDecomp.md)

## Links

- Repo: https://github.com/RodoLy/HarvestMoonSnesDecomp (README: Harvest Moon (SNES) rewritten in byte-verified C from HM-Decomp, with native Windows/macOS/Linux/Android builds, save states, and in-game cheats; BYO ROM)

## Related

[[zelda3]] · [[devilution]] · [[static-runtime-evidence]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
