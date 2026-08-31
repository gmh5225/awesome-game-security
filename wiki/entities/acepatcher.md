---
title: ACEPatcher
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/BataBo__ACEPatcher.md
updated: 2026-08-31
confidence: medium
---

# ACEPatcher

**ACEPatcher** (BataBo/ACEPatcher) is a **GUI-based patching tool** for modifying **.NET assemblies**. Written in C#, it uses **dnlib** for assembly manipulation and **Harmony** to map patch methods to target methods across many method types. The application supports importing and exporting patch sets, optional password protection for patch files, and workflows for packed or obfuscated managed binaries. Primary use case is reverse-engineering research and repeatable .NET patch automation. Listed under Cheat → [.NET Patcher]. (source: wiki/sources/descriptions/BataBo__ACEPatcher.md)

Complements interactive [[dnspy]] editing and headless agent workflows via [[dnspymcp]] with a dedicated GUI for batch, reusable patch sets—useful when patching obfuscated game clients or automating Harmony-style method redirection outside a live plugin host such as [[bepinex]].

## Links

- Repo: https://github.com/BataBo/ACEPatcher

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[dnspy]] · [[dnspymcp]] · [[bepinex]] · [[ilspy]] · [[obfuscation-methods]]
