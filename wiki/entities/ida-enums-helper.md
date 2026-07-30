---
title: ida-enums-helper
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/milankovo__ida_enums_helper.md
updated: 2026-07-30
confidence: medium
---

# ida-enums-helper

IDA Pro plugin that streamlines enum management in the Hex-Rays pseudocode view. Hotkey-driven actions rename enum members (**N**), add numeric operands to existing or new enums (**A**), and append to the last-used enum (**Shift-A**). Uses `idaapi.tinfo_t` ordinal iteration and chooser dialogs to match numeric operands against existing enum definitions. (source: wiki/sources/descriptions/milankovo__ida_enums_helper.md)

Hex-Rays enum workflow helper—not a decompiler, unpacker, or SDK generator.

## Links

- Repo: https://github.com/milankovo/ida_enums_helper

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[source2gen]] · [[cs2-offsets]] · [[idaplugins]] · [[yarascan-ida]] · [[big5-decode-ida]]
