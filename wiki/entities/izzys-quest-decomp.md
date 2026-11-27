---
title: Izzy's Quest decomp
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/ironsniper1__izzys-quest-decomp.md
updated: 2026-11-27
confidence: medium
---

# Izzy's Quest decomp

**Source-level decompilation** of the 1995 Windows 3.1 CD-ROM title *Izzy's Quest for Olympic Gold*, rebuilt as **portable C99** and shipped as a **64-bit Windows** native client. The work lifts the original **16-bit StoryGame Engine** executable into readable C with traceable function labels, decodes proprietary **asset and script** formats, and reimplements a **scene player**, **VET script VM**, renderer, and audio stack. The tree includes a **Ghidra-oriented** decompilation workspace, asset extractors, **VET compiler/decompiler** tooling, stress and self-test harnesses, and a built-in **Indeo 3.2** video decoder to replace codecs disabled on current Windows. Targets reverse engineers, game preservationists, and researchers studying legacy interactive multimedia engines and binary-to-source recovery—**bring your own** retail game assets; not live anti-cheat or online security tooling. (source: wiki/sources/descriptions/ironsniper1__izzys-quest-decomp.md)

README lane: Win16 StoryGame Engine→portable C99 with Windows 10/11 port, script toolchain, and regression tests—BYO game assets; Game Engine / source.

## Links

- Repo: https://github.com/ironsniper1/izzys-quest-decomp

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[linnut1-6-2-decomp]] · [[harvest-moon-snes-decomp]] · [[legacy-game-launcher]] · [[static-runtime-evidence]]