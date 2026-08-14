---
title: CE Remap Plugin
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__CE-remap-plugin.md
updated: 2026-08-14
confidence: medium
---

# CE Remap Plugin

**Delphi Cheat Engine plugin** that hooks the **Cheat Engine plugin SDK** to **remap disassembler memory pages** for a chosen address. When a target hides or obfuscates executable bytes from CE's disassembler view, remapping the underlying page lets researchers inspect code that would otherwise appear blank, stale, or misleading. Tested on **Cheat Engine 7.4**. Listed under cheat / Remap. (source: wiki/sources/descriptions/gmh5225__CE-remap-plugin.md)

Complements CE static-analysis bridges such as [[ce-tracer-ida]] and runtime dumpers such as [[gddumper]] when the research bottleneck is disassembler page visibility rather than live value tracing or engine object enumeration.

## Links

- Repo: https://github.com/gmh5225/CE-remap-plugin

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[ce-tracer-ida]] · [[gddumper]] · [[wasm-ceserver]] · [[cheat-engine-dma-plugin]]
