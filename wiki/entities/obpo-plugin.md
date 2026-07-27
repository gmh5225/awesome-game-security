---
title: obpo-plugin
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/obpo-project__obpo-plugin.md
updated: 2026-07-27
confidence: medium
---

# obpo-plugin

Open-source IDA client / Go backend for OBPO deobfuscation. The OBPO core is closed source; the plugin side is free and open. A simple Golang server receives requests, feeds input into IDA with obpo-core, and returns deobfuscated results to the plugin client. Aimed at game-security researchers and reverse engineers in the cheat / Fix OLLVM lane. (source: wiki/sources/descriptions/obpo-project__obpo-plugin.md)

Not a standalone unpacker—scoped as an IDA-facing client/server bridge to closed-source OBPO deobfuscation.

## Links

- Repo: https://github.com/obpo-project/obpo-plugin

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[d810-ng]] · [[idadeflat]] · [[deobf]] · [[ida-easy-life]]
