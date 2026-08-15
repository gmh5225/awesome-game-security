---
title: HintInject
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/frkngksl__HintInject.md
updated: 2026-08-15
confidence: medium
---

# HintInject

**PE injection technique** that conceals shellcode inside **Hint/Name Table** entries of **fabricated Import Directory** records. Splits a raw shellcode payload into chunks sized for each fake imported DLL's export-name slots, writes them into the PE **import lookup table**, and **reconstructs the shellcode at load time** through the Windows loader's normal **IAT resolution** path. Parses target PE section headers, manipulates **RVA-to-offset** translations, and randomly selects export names from system DLLs to populate the fake entries. Listed under Cheat → Hint/Name Table; aimed at game-security researchers and reverse engineers studying PE import-table abuse and stealthy in-process payload staging—not an AC product. (source: wiki/sources/descriptions/frkngksl__HintInject.md)

Useful as a PE import-table / loader-behavior reference alongside [[windows-process-injection]], [[modexmap]], and [[shoggoth]].

## Links

- Repo: https://github.com/frkngksl/HintInject

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[windows-process-injection]] · [[injectors]] · [[awesome-injection]] · [[modexmap]] · [[shoggoth]] · [[huan]]
