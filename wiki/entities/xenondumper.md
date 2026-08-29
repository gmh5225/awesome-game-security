---
title: xenondumper
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Byrom90__XenonDumper.md
updated: 2026-08-29
confidence: medium
---

# xenondumper

Custom **Xbox 360** dumping utility (C/C++) that collects console data required by low-level emulation workflows: fuses, bootloader content, and NAND-related artifacts. Targets modified retail or developer environments where privileged access is available—primarily console reverse engineering, preservation, and emulator preparation research. (source: wiki/sources/descriptions/Byrom90__XenonDumper.md)

Sits in the README `Xbox` lane beside HLE playback via [[xenia]] / [[xenia-mac]], emulator work via [[xbox360-emu]], static XEX analysis via [[idaxex]], live modded-console patching via [[x360gamehack2025]], and network memory RE via [[toastylink]]—but focused on **hardware artifact extraction** (fuses/bootloader/NAND) for Xenon LLE emulator prep rather than runtime emulation, IDA static analysis, backup deployment, or live XBDM scanning.

## Links

- Repo: https://github.com/Byrom90/XenonDumper (README tag: Dumps files & data required to use the Xenon Xbox 360 Low Level Emulator)

## Related

[[xenia]] · [[xenia-mac]] · [[xbox360-emu]] · [[idaxex]] · [[x360gamehack2025]] · [[toastylink]] · [[recompiler]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
