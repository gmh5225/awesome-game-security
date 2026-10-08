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

## Capabilities

Over 200 DSH tools cover executable import and analysis, function decompilation, browsing strings/segments/imports/exports, cross-references and call graphs, and persisting edits such as renames, comments, prototypes, and function labels. Composite analysis and malware triage add crypto-constant detection, behavioral API heuristics, IOC extraction, and anti-analysis pattern scanning. Environment diagnostics and an bundled agent skill guide when Ghidra is the appropriate analysis backend. (source: wiki/sources/descriptions/spix18__dsh-ghidra.md)

## Architecture

DSH-native JavaScript plugin surface with Python/PyGhidra backend bridges Ghidra to the harness agent loop. Optional integration with the GhidraMCP REST surface extends tooling beyond the built-in DSH tool catalog. Runs headless or interactive on Windows, Linux, and macOS without platform-specific Ghidra UI dependencies in the agent path. (source: wiki/sources/descriptions/spix18__dsh-ghidra.md)

## Target use cases

Reverse engineers, malware analysts, and game security researchers who want LLM-driven workflows over native binaries — game clients, anti-cheat modules, packed crackmes, and triage samples where scripted Ghidra commands plus agent orchestration beat manual GUI clicking. (source: wiki/sources/descriptions/spix18__dsh-ghidra.md)

## Positioning

Complements [[dsh-plugins]] PyGhidra bridge and [[ghidra-skill-for-dsh]] scenario skills as a broader DSH-native Ghidra automation stack with malware-triage and memory-edit tooling. Optional [[ghidra-mcp]] REST extends the same agent lane. Pair agent summaries with [[research-rigor]] before enforcement conclusions.

## Links

- Repo: https://github.com/spix18/dsh-ghidra

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[dsh-plugins]] · [[ghidra-skill-for-dsh]] · [[ghidra-mcp]] · [[research-rigor]]
