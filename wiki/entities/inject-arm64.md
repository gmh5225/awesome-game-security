---
title: InjectARM64
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/NepMods__InjectARM64.md
updated: 2026-08-22
confidence: medium
---

# InjectARM64

**Non-root cheat injection platform** for ARM Android devices (NepMods). Combines **Java/Kotlin** Android components with **C/C++** native modules and hooking code to inject payloads inside a **virtualized app space**. Advertises **ARM32 and ARM64** support, **configurable injection flows**, and compatibility with **newer Android releases**. Targets game-hacking researchers prototyping **mobile injection without root**. README tag: `[Non-root injection]`. (source: wiki/sources/descriptions/NepMods__InjectARM64.md)

Sits in the same no-root Virtual Space / container inject lane as [[android-virtual-inject]] and [[virtual-app]], contrasting with ptrace/Zygote paths such as [[android-super-inject]] and [[android-ptrace-injector]]. Complements ARM64 hook libraries such as [[and64-inline-hook]] and [[dobby]] when building native payload hooks inside the injected process.

## Links

- Repo: https://github.com/NepMods/InjectARM64

## Related

[[android-virtual-inject]] · [[virtual-app]] · [[android-super-inject]] · [[android-ptrace-injector]] · [[and64-inline-hook]] · [[dobby]] · [[android-cheat-template]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
