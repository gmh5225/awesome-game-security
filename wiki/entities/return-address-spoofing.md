---
title: Return-address-spoofing
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Apex-master__return-address-spoofing.md
updated: 2026-09-02
confidence: medium
---

# Return-address-spoofing

Compact **return-address spoofing** implementation for **native function invocation bypass** scenarios. Uses **C++ templates** and **x64 assembly stubs** to redirect control flow while preserving expected calling behavior. Lightweight and intended to integrate into an existing **invoker pipeline** rather than stand alone as a full framework. Primary audience: low-level game security researchers exploring **anti-detection evasion** and stack-walk bypass patterns. (source: wiki/sources/descriptions/Apex-master__return-address-spoofing.md)

Sits in the `Cheat > Spoof Stack` lane beside minimal x64 samples such as [[ret-spoofing]] and [[spoof-ret-addr]], educational illustrations such as [[return-address-spoofer]], and x64 trampoline libraries such as [[callstackspoofer-2]].

## Links

- Repo: https://github.com/Apex-master/return-address-spoofing

## Related

[[stack-spoofing]] · [[ret-spoofing]] · [[spoof-ret-addr]] · [[return-address-spoofer]] · [[callstackspoofer-2]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
