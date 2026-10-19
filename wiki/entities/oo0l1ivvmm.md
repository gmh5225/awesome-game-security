---
title: Oo0l1IVvMm
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/woye969__Oo0l1IVvMm.md
  - wiki/sources/README-categories.md
updated: 2026-10-19
confidence: medium
---

# Oo0l1IVvMm

Opt-in **IDA Pro 9.x Hex-Rays** plugin (woye969; Python) for **OLLVM-style control-flow flattening** and encoded dispatch recovery. **MIN** mode targets classic central-dispatcher flattening via unflat valrange unflattening, instruction materialization, and **D-810** simplification. **MAX** mode resolves encoded inline jmp-reg dispatch with concrete chain walking, microcode edge rewriting, and dead-dispatcher removal. Disarmed by default so F5 stays at vanilla speed until a mode is chosen from the menu or hotkey; optional Capstone decoding and runtime snapshots support table-based dispatch. Bundled **seagull_core** supports standalone chain analysis outside IDA. (source: wiki/sources/descriptions/woye969__Oo0l1IVvMm.md)

## Positioning

Complements decompilation-time rule engines such as [[d810]] and [[d810-ng]] with explicit MIN/MAX orchestration for heavy CFF—useful when protected game clients or packers flatten control flow before manual RE.

## Links

- Repo: https://github.com/woye969/Oo0l1IVvMm

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[concepts/control-flow-flattening]] · [[d810]] · [[d810-ng]] · [[idadeflat]] · [[ollvm-unflattener]]
