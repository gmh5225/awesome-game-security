---
title: ValveGen
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/CallumCVM__ValveGen.md
updated: 2026-08-29
confidence: medium
---

# ValveGen

**Source Engine SDK generator** (CallumCVM) implemented in C++. Parses networked **ClientClass**, **RecvTable**, and data-table structures from client metadata and emits usable **class definitions and offsets** for Source 1 titles. Project files and supporting code build generated structures from live client layout data rather than hand-maintained header dumps. README tag: `[SDK Generator]`. (source: wiki/sources/descriptions/CallumCVM__ValveGen.md)

Complements offset dumpers ([[gh-offset-dumper]], [[hazedumper]]), scaffold generators ([[csf-w]], [[csf]]), and maintained SDK headers ([[csgo-sdk]], [[sdk]]) when analysts need **automated Source-engine SDK codegen** after game updates. Pairs with [[source-netvars]] for RecvTable-driven layout workflows.

## Links

- Repo: https://github.com/CallumCVM/ValveGen

## Related

[[source-netvars]] · [[gh-offset-dumper]] · [[hazedumper]] · [[csgo-sdk]] · [[csf-w]] · [[csf]] · [[sdk]] · [[source-engine]] · [[source-sdk-2013]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
