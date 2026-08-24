---
title: peinjector
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/JonDoNym__peinjector.md
updated: 2026-08-24
confidence: medium
---

# peinjector

**PE patching and infection framework** that injects custom payloads into **Windows executables** while **preserving original behavior**. Ships a **C core** for PE parsing and modification, plus **Python and Java** control and interception components. Supports **multiple infection methods**, **patch generation for transfer-time modification**, and **web-based remote configuration**. Intended for executable research, red-team simulations, and analysis of defensive mechanisms around **PE tampering**—not an AC product. (source: wiki/sources/descriptions/JonDoNym__peinjector.md)

Complements import-table staging via [[hintinject]], parasitic shellcode loaders such as [[super-mega]], and polymorphic encoding tooling such as [[shoggoth]].

## Links

- Repo: https://github.com/JonDoNym/peinjector

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[hintinject]] · [[super-mega]] · [[shoggoth]] · [[windows-process-injection]] · [[awesome-injection]] · [[injectors]]
