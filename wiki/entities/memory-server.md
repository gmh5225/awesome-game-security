---
title: memory-server
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__memory_server.md
updated: 2026-08-08
confidence: medium
---

# memory-server

Rust HTTP server for jailbroken iOS devices that exposes process memory operations—enumeration, region listing, reading, pattern scanning, and result filtering—through a REST API on port 3030. Enables remote memory analysis from a connected PC using the included Python sample client. Targets game-security researchers and reverse engineers in the Cheat / iOS memory explorer lane—userland remote scanning complementary to on-device editors and kernel explorers such as [[kfd-explorer]]. (source: wiki/sources/descriptions/gmh5225__memory_server.md)

Pairs with jailbreak/injection tooling ([[opainject]], [[dopamine]]) and mobile memory walkthroughs such as [[pubg-mobile-memory-hacking-examples]] when the workflow is PC-driven pattern scan and filter over Wi‑Fi/USB rather than kernel-level hooking via [[xnuspy]].

## Links

- Repo: https://github.com/gmh5225/memory_server

## Related

[[kfd-explorer]] · [[xnuspy]] · [[opainject]] · [[pubg-mobile-memory-hacking-examples]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
