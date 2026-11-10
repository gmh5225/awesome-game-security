---
title: UC.Zone API docs (Umbrella Dota 2)
kind: entity
topics: [game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/Nerve11__uczone-docs-UmbrellaDota2.md
updated: 2026-11-10
confidence: medium
---

# UC.Zone API docs (Umbrella Dota 2)

**uczone-docs-UmbrellaDota2** (Nerve11) aggregates **UCZONE API v2.0** documentation for the **Umbrella** Dota 2 scripting platform into a single offline reference. A Python utility crawls curated GitBook Markdown pages and merges them into one structured document with a table of contents for search and LLM-assisted reading. The material documents the Lua 5.4 cheat API: script callbacks, menu and UI widgets, game entity and engine accessors, rendering and Panorama hooks, and networking helpers (HTTP, Steam, protobuf). It is aimed at developers and security researchers who need a portable guide to how third-party Dota 2 automation and overlay tools interact with in-game state and client systems. (source: wiki/sources/descriptions/Nerve11__uczone-docs-UmbrellaDota2.md)

Contrast with implementation samples such as [[mcdota]] (Linux injection + Panorama/protobuf RE) and layout dumps such as [[dota2dumped]]; this repo is **API reference + doc scraper**, not a cheat binary.

## Links

- Repo: https://github.com/Nerve11/uczone-docs-UmbrellaDota2

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[mcdota]] · [[dota2-cheat]] · [[dota-cheat]] · [[dota2dumped]] · [[umbrella-hwid-resp-tool]]
