---
title: idaxex
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/emoose__idaxex.md
updated: 2026-08-15
confidence: medium
---

# idaxex

IDA Pro loader plugin for Xbox 360 XEX (Xenon Executable) files (C++): parses the XEX container, extracts embedded PE, resolves imports/exports, and applies Xbox 360 kernel function names for annotated static analysis in IDA Pro 9. (source: wiki/sources/descriptions/emoose__idaxex.md)

Useful for reverse engineers analyzing Xbox 360 game binaries and console security researchers in the README `Xbox` lane—adjacent to HLE playback via [[xenia]] / [[xenia-mac]], emulator work via [[xbox360-emu]], and executable porting via [[recompiler]], but focused on static XEX disassembly in IDA rather than runtime emulation.

## Links

- Repo: https://github.com/emoose/idaxex (README tag: Xbox360/Xenon loader plugin for IDA 9)

## Related

[[xenia]] · [[xenia-mac]] · [[xbox360-emu]] · [[recompiler]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
