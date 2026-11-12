---
title: inject-hooks-android-rs
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/strazzere__inject-hooks-android-rs.md
updated: 2026-11-12
confidence: medium
---

# inject-hooks-android-rs

Rust Android remote shared-library injector (TinyInjector-based) plus hook library for in-process GOT rewrite and inline trampoline hooks on 32- and 64-bit ARM. Uses ptrace attach, remote `dlopen`, and cross-compiled payloads with adb push workflows for native mobile RE and game instrumentation study. (source: wiki/sources/descriptions/strazzere__inject-hooks-android-rs.md) (source: wiki/sources/README-categories.md)

Sits in the Cheat / injection:android lane beside [[android-ptrace-injector]], [[linjector-rs]], and [[android-dll-injector]].

## Links

- Repo: https://github.com/strazzere/inject-hooks-android-rs

## Related

[[android-ptrace-injector]] · [[linjector-rs]] · [[android-dll-injector]] · [[frida]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
