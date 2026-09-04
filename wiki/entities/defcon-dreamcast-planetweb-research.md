---
title: DEF CON Dreamcast PlanetWeb Research
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/piffd0s__Defcon-Dreamcast-Planetweb-Research.md
  - wiki/sources/README-categories.md
updated: 2026-09-04
confidence: medium
---

# DEF CON Dreamcast PlanetWeb Research

DEF CON research demo achieving native **SH-4 code execution** on Sega Dreamcast PlanetWeb Internet Browser v3.0 and running DOOM entirely on the emulated console without a debugger. Chains three browser flaws — Eden service-subscription remote code execution, an unbounded `setRawDeviceID` memory write, and a MIME attachment stack overflow — to stage Java, plant a native loader stub, and trigger it via crafted email. Python orchestration covers DNS redirection, rogue Eden HTTP server, and POP3 mail PoC; includes Java staging, native SH-4 binaries, trimmed DOOM WAD, and patched Flycast emulator build for macOS. Intended for authorized console security research and vintage browser attack-surface analysis. (source: wiki/sources/descriptions/piffd0s__Defcon-Dreamcast-Planetweb-Research.md)

## Links

- Repo: https://github.com/piffd0s/defcon-dreamcast-planetweb-research

## Related

[[xemu]] · [[xqemu]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[research-rigor]]
