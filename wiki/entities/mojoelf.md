---
title: mojoelf
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/icculus__mojoelf.md
updated: 2026-08-04
confidence: medium
---

# mojoelf

In-process **ELF binary loader** that runs inside the host application instead of relying on the C runtime's `dlopen()`. Unlike standard `dlopen()`, it can load ELF images from buffers or other non-filesystem sources — useful for game-security researchers and reverse engineers studying offensive **Android memory loading** and cheat injection tradecraft. (source: wiki/sources/descriptions/icculus__mojoelf.md)

Complements Android `.so` loaders such as [[so-loader]], ptrace injectors such as [[android-ptrace-injector]], and Linux ELF injection tooling such as [[mandibule]].

## Links

- Repo: https://github.com/icculus/mojoelf

## Related

[[so-loader]] · [[android-ptrace-injector]] · [[mandibule]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
