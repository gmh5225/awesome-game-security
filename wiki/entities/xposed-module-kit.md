---
title: Xposed Module Kit
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/mabbcoll13__xposed-module-kit.md
updated: 2026-07-31
confidence: medium
---

# Xposed Module Kit

Batteries-included **Android scaffold** for building **Xposed** and **LSPosed** modules. Gradle Android app (Java; Xposed API 82–93) with reusable hook helpers and small CLI utilities for finding hook targets. (source: wiki/sources/descriptions/mabbcoll13__xposed-module-kit.md)

**Components:** `HookTemplate`, `MethodHook`, and `PackageHook` helpers; logcat-friendly logger; Python class scanner that parses compiled `.class` or JAR files and emits ready-to-use `MethodHook` stubs. Ships an example module that neutralizes common root-detection checks.

**Use cases:** authorized Android security research, reverse engineering, and lawful testing of apps—including game and anti-cheat analysis—on devices you own or are authorized to test.

## Links

- Repo: https://github.com/mabbcoll13/xposed-module-kit

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[locusmimic]] · [[frida]] · [[detection]] · [[mobile-anti-cheat]]
