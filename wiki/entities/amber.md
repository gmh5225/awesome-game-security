---
title: Amber
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/EgeBalci__amber.md
updated: 2026-08-25
confidence: medium
---

# Amber

**Amber** is a **reflective PE loader and payload generator** for **in-memory execution** of native Windows binaries. The project combines **Go tooling** with **low-level assembly loader** components to map and run **EXE, DLL, or SYS** payloads without standard disk-based loading. Features include **payload encoding**, **API resolution obfuscation**, **staged delivery** options, and **memory cleanup** behavior aimed at reducing scanner visibility. Primary use: offensive security research and defense testing where understanding **reflective loading** and **evasion techniques** matters. (source: wiki/sources/descriptions/EgeBalci__amber.md)

Sits in the reflective-loader / in-memory PE execution lane beside encoders such as [[shoggoth]], CET-aware loaders such as [[bingusldr]], and injection technique catalogs such as [[process-injection-techniques]].

## Links

- Repo: https://github.com/EgeBalci/amber

## Related

[[shoggoth]] · [[bingusldr]] · [[windows-process-injection]] · [[process-injection-techniques]] · [[modexmap]] · [[memject]] · [[scfw]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
