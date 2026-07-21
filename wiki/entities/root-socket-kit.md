---
title: RootSocketKit
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/systemnb__RootSocketKit.md
updated: 2026-07-21
confidence: medium
---

# RootSocketKit

Android kernel module plus companion app that exposes root-level process memory read/write over a custom Unix-socket IPC protocol. Ships a JNI client compatible with Magisk / [[kernelsu]] / APatch and a GUI for memory search, edit, and game-value modification — positioned as reinforcement-proof, low-latency root ops (`OpenProcess`, `ReadMemory`). (source: wiki/sources/descriptions/systemnb__RootSocketKit.md)

Sits in the same Android root / memory-explorer lane as CLI scanners such as [[mypower]] and LKM research kits such as [[android-kernel-hacking-toolkit]].

## Links

- Repo: https://github.com/systemnb/RootSocketKit

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[magisk]] · [[kernelsu]] · [[mypower]] · [[android-kernel-hacking-toolkit]] · [[compile-android-driver]]
