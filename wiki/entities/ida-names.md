---
title: ida_names
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__ida_names.md
updated: 2026-08-08
confidence: medium
---

# ida_names

Python IDA Pro plugin for managing and manipulating function and symbol names in IDA databases. Supports batch renaming, name pattern matching, prefix/suffix operations, and name import/export to organize large disassembly projects. Also renames pseudocode window titles with the current function name—useful when many Hex-Rays tabs are open during game-client RE. (source: wiki/sources/descriptions/gmh5225__ida_names.md)

Workflow tooling in the symbol-naming lane: complements automated library-ID rename via [[renamaida]], linker `.MAP` import via [[ida-pro-loadmap]], and LLM-assisted rename via [[idassist]] / [[ida-llm-explainer]] when analysts need bulk manual curation rather than signature or MAP-driven recovery.

## Links

- Repo: https://github.com/gmh5225/ida_names

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[renamaida]] · [[ida-pro-loadmap]] · [[idassist]] · [[idaplugins-list]] · [[idawilli]]
