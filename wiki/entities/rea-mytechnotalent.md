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

## Static analysis

One-shot scans inventory **ELF, Mach-O, and PE** layouts and symbols through standard host tooling without executing the sample, and walks packaged **JavaScript/Electron** trees without running the app. Output is meant as a readable **first-pass** map before deeper work in Ghidra, IDA, or dynamic instrumentation. (source: wiki/sources/descriptions/mytechnotalent__rea.md)

## Agent workflow

Local **RAG** grounds narrative summaries in analyst-supplied documents. A **multi-agent propose–review–gate** harness separates draft findings from reviewer gates so each claim carries traceable evidence rather than undifferentiated model prose—aligned with [[binary-evidence]] finding granularity. (source: wiki/sources/descriptions/mytechnotalent__rea.md)

## Interfaces

**CLI** and **MCP** share one tool catalog so terminal triage and IDE agents (Cursor, Claude Code, etc.) drive the same offline analysis surface. (source: wiki/sources/descriptions/mytechnotalent__rea.md)

## Audience

Reverse engineers, **malware analysts**, and security researchers who need quick assessment of unknown executables and packaged apps—including **game clients and anti-cheat-related binaries**—with offline defaults. (source: wiki/sources/descriptions/mytechnotalent__rea.md)

## Positioning

Distinct from morluto/[[rea]] (TypeScript cross-format MCP orchestrator listed under **Game Develop → MCP server**). Pair agent summaries with [[research-rigor]]; use [[reverify]] when conclusions must be byte-verified.

## Links

- Repo: https://github.com/mytechnotalent/rea [Offline-first RE assistant with one-shot binary scan, native PE/ELF/Mach-O and JavaScript/Electron static inventory, local RAG, multi-agent harness, and MCP server]

## Related

[[reverify]] · [[pymemory-editor]] · [[open-reverselab]] · [[skid-factory]] · [[binary-evidence]] · [[research-rigor]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
