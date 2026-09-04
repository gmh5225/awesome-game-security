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

DEF CON research demo achieving native **SH-4 code execution** on Sega Dreamcast PlanetWeb Internet Browser v3.0 and running DOOM entirely on the emulated console without attaching a debugger. Intended for authorized console security research, vintage platform vulnerability analysis, and reverse engineering of legacy game-system browser attack surfaces. (source: wiki/sources/descriptions/piffd0s__Defcon-Dreamcast-Planetweb-Research.md)

## Exploit chain

Three chained browser flaws stage and trigger native code without debugger attachment:

1. **Eden service-subscription RCE** — rogue Eden HTTP server (with DNS redirection) delivers a Java payload through the PlanetWeb subscription path.
2. **`setRawDeviceID` memory write** — unbounded write primitive plants a native SH-4 loader stub in guest memory.
3. **MIME attachment stack overflow** — opening a crafted email triggers the stub and transfers control to native SH-4 code that runs a trimmed DOOM WAD.

The demo runs DOOM end-to-end on a patched Flycast emulator build for macOS. (source: wiki/sources/descriptions/piffd0s__Defcon-Dreamcast-Planetweb-Research.md)

## Stack

Python orchestration (DNS redirection, rogue Eden HTTP server, POP3 mail PoC), Java staging code, native SH-4 binaries, trimmed DOOM WAD, and patched Flycast emulator artifacts. Primary languages: Python and Java, with native SH-4 payloads and emulator patches supporting the chain. (source: wiki/sources/descriptions/piffd0s__Defcon-Dreamcast-Planetweb-Research.md)

## Links

- Repo: https://github.com/piffd0s/defcon-dreamcast-planetweb-research

## Related

[[xemu]] · [[xqemu]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[research-rigor]]
