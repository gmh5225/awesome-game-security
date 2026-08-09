---
title: ceserver-ios
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__ceserver-ios.md
updated: 2026-08-09
confidence: medium
---

# ceserver-ios

Cheat Engine **ceserver** port for **jailbroken iOS**: runs on-device and exposes process memory through the **ceserver network protocol** so a desktop Cheat Engine client can connect remotely for memory search, value editing, and pointer scanning on iOS game processes. Targets iOS game-security researchers who want standard CE workflows on mobile rather than REST-only or Frida-backed servers. (source: wiki/sources/descriptions/gmh5225__ceserver-ios.md)

Complements [[frida-ceserver]] when attach-based Frida is unavailable or a native jailbreak ceserver stack is preferred, and [[memory-server]] when the workflow is desktop CE over ceserver rather than REST pattern scan on port 3030.

## Links

- Repo: https://github.com/gmh5225/ceserver-ios

## Related

[[frida-ceserver]] · [[memory-server]] · [[wasm-ceserver]] · [[cheap-engine]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
