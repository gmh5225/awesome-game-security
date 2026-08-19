---
title: cs2-dumper
kind: entity
topics: [game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/a2x__cs2-dumper.md
updated: 2026-08-19
confidence: medium
---

# cs2-dumper

**External offset and interface dumper** for **Counter-Strike 2** (a2x; cheat / game:cs2 `[Dump]`). Core written in **Rust** with **memflow**-based memory access on **Windows and Linux**. Emits structured outputs in **C#**, **C++**, **Rust**, and **JSON** for downstream automation. Used by game security researchers, cheat developers, and anti-cheat analysts who need current CS2 schema, netvar, and offset data after patches. (source: wiki/sources/descriptions/a2x__cs2-dumper.md)

Widely consumed as an offset bootstrap by CS2 externals such as [[cs2-dma]], [[titled-gui-cs2]], [[overlayai]], and [[cs2-cheat]]; complements maintained header dumps such as [[cs2-offsets]] and [[cs2-offsets-ro0ti]].

## Links

- Repo: https://github.com/a2x/cs2-dumper

## Related

[[cs2-offsets]] · [[cs2-offsets-ro0ti]] · [[cs2-dma]] · [[cs2-cheat]] · [[titled-gui-cs2]] · [[overlayai]] · [[gh-offset-dumper]] · [[dezlock-dump]] · [[source2gen]] · [[source-netvars]] · [[memflow-kvm]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
