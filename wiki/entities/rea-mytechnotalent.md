---
title: REA (Reverse Engineering Assistant)
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mytechnotalent__rea.md
  - wiki/sources/README-categories.md
updated: 2026-10-11
confidence: medium
---

# REA (Reverse Engineering Assistant)

**REA** (mytechnotalent/rea) is an **offline-first** Python reverse-engineering assistant that triages unknown native binaries and JavaScript or Electron application trees from a single scan command, then explains findings in plain language. It combines static PE/ELF/Mach-O inventory via host utilities (`readelf`, `objdump`, `nm`, `strings`), non-executing JavaScript tree walks, **local retrieval-augmented generation** over analyst documents, and a **propose–review–gate** multi-agent workflow that records evidence per claim. The same tool catalog is exposed through a CLI and **Model Context Protocol** server for IDE agents. Default operation needs no API key; optional hosted LLM backends can be configured. (source: wiki/sources/descriptions/mytechnotalent__rea.md)

README category: **Cheat → RE Tools**.

## Positioning

Distinct from morluto/[[rea]] (TypeScript cross-format MCP orchestrator listed under **Game Develop → MCP server**). This repo targets **fast, readable first-pass triage** of game clients, packers, and anti-cheat-related binaries with offline defaults. Pair agent summaries with [[research-rigor]]; use [[reverify]] when conclusions must be byte-verified.

## Links

- Repo: https://github.com/mytechnotalent/rea

## Related

[[reverify]] · [[pymemory-editor]] · [[open-reverselab]] · [[skid-factory]] · [[research-rigor]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
