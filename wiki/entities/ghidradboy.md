---
title: ghidradboy
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Gekkio__GhidraBoy.md
updated: 2026-08-25
confidence: medium
---

# ghidradboy

Experimental **Ghidra extension** that adds **Nintendo Game Boy (DMG)** reverse-engineering support. Combines **Kotlin** and **Java** with custom **Sleigh** language definitions for the **Sharp SM83** CPU. Includes ROM loading for **banked and unbanked** cartridges, **boot ROM** variants, **memory map** blocks, and **hardware register** symbols. Primary use case is **retro game binary analysis** and **low-level firmware research**. (source: wiki/sources/descriptions/Gekkio__GhidraBoy.md)

Complements runtime GB emulators such as [[kevboy]] and [[feather-gb]] with static Ghidra analysis of DMG ROM images; peer to [[gba-ghidra-loader]] for GBA cartridge loading in the same README `Game Boy` / Cheat Ghidra Plugins lane.

## Links

- Repo: https://github.com/Gekkio/GhidraBoy (README tag: Sharp SM83 / Game Boy extension for Ghidra)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[gba-ghidra-loader]] · [[kevboy]] · [[feather-gb]] · [[openfpga-gbc-cheats-ui]]
