---
title: ObjectFlow
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/thecommenter297__ObjectFlow.md
updated: 2026-11-27
confidence: medium
---

# ObjectFlow

IDA Pro / Hex-Rays IDAPython plugin that adds **semantic cross-references** on top of ordinary static xrefs by analyzing decompiler microcode. Surfaces local and interprocedural xrefs, stable variable selection, reaching definitions, pointer and memory relationships, and trace-style evidence; inferred links are labeled as static **MAY** relationships rather than proven data flow. Implemented as a single Python module on IDAPython with a PyQt5 UI and hot reload for iterative plugin development. Aimed at reverse engineers who need richer navigation and data-flow context when dissecting compiled game clients, anti-cheat modules, and other native binaries where Hex-Rays pseudocode is the primary view. (source: wiki/sources/descriptions/thecommenter297__ObjectFlow.md)

Complements [[xrefxpert]], [[xrefgen]], and [[find-xrefs]] (xref navigation and materialization) with microcode-backed semantic tracing in the decompiler; parallels variable data-flow views in [[ida-better-reverse]] on stripped native targets.

## Links

- Repo: https://github.com/thecommenter297/ObjectFlow

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[xrefxpert]] · [[xrefgen]] · [[find-xrefs]] · [[ida-better-reverse]]