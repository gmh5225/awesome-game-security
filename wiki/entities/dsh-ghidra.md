---
title: DSH Ghidra
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/spix18__dsh-ghidra.md
  - wiki/sources/README-categories.md
updated: 2026-10-08
confidence: medium
---

# DSH Ghidra

**dsh-ghidra** (spix18/dsh-ghidra) is a **DeepSeek Harness (DSH) plugin** that connects AI agents to Ghidra for interactive binary reverse engineering. JavaScript and Python expose 219 DSH tools for import/decompile, strings/segments/imports/exports, cross-references, call graphs, persistent renames/comments/prototypes, composite analysis, and malware triage (crypto constants, behavioral API heuristics, IOC extraction, anti-analysis patterns). Optional GhidraMCP REST integration extends the tool surface. Cross-platform via PyGhidra on Windows, Linux, and macOS. (source: wiki/sources/descriptions/spix18__dsh-ghidra.md)

README category: Cheat / RE Tools.

## Positioning

Complements [[dsh-plugins]] PyGhidra bridge and [[ghidra-skill-for-dsh]] scenario skills as a broader DSH-native Ghidra automation stack with malware-triage and memory-edit tooling. Pair agent summaries with [[research-rigor]] before enforcement conclusions.

## Links

- Repo: https://github.com/spix18/dsh-ghidra

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[dsh-plugins]] · [[ghidra-skill-for-dsh]] · [[ghidra-mcp]] · [[research-rigor]]
