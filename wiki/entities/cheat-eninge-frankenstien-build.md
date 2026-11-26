---
title: Cheat Engine Frankenstein Build
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/lolidroid86__Cheat-Eninge-Frankenstien-Build.md
updated: 2026-11-26
confidence: medium
---

# Cheat Engine Frankenstein Build

**Cheat Engine Frankenstein** (lolidroid86/Cheat-Eninge-Frankenstien-Build) is a **custom compile of Cheat Engine 7.5** from the public Pascal source tree that **backports newer Auto-Assembler and scripting syntax** onto the older engine core. Patches target `autoassembler.pas` and `SynHighlighterAA.pas`, built with **Lazarus and Free Pascal**. (source: wiki/sources/descriptions/lolidroid86__Cheat-Eninge-Frankenstien-Build.md)

Added Auto-Assembler directives include **`HOOK` / `UNHOOK`** for inline code hooks, conditional **`{$ifdef}` / `{$else}` / `{$endif}`** blocks, and **`AOBSCANFUNCTION`** for symbol-scoped pattern scans. **Version 3** pairs the patched 7.5 executable with **CE 7.7.3 support files** plus a **Lua compatibility layer** so modern autorun scripts load without missing-function errors. The repo ships **Inno Setup** installer scripts, example Auto-Assembler tables, and optional extension loading for tools such as [[aitools]].

Targets memory editing, game modding, and reverse-engineering workflows where developers want **CE 7.7-style scripting** on a **self-built** fork—not AC evasion research like [[cheat-engine-undetectable]].

## Links

- Repo: https://github.com/lolidroid86/Cheat-Eninge-Frankenstien-Build

## Related

[[cheat-engine]] · [[aitools]] · [[ce-lua-extensions]] · [[ce-extensions]] · [[cheat-engine-undetectable]] · [[intro-to-gamehacking]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]