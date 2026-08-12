---
title: iOS Jailbreak — Fugu15
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__IOS-jailbreak--Fugu15.md
updated: 2026-08-12
confidence: medium
---

# iOS Jailbreak — Fugu15

**Untethered jailbreak** for **iOS 15** built on the **Fugu15** kernel exploit chain. Chains kernel vulnerabilities for arbitrary kernel read/write, grants **root access**, bypasses **code signing**, and enables **arbitrary code execution** with full system privileges after a one-time exploit run. (source: wiki/sources/descriptions/gmh5225__IOS-jailbreak--Fugu15.md)

Sits in the modern iOS 15 jailbreak lane beside semi-untethered [[dopamine]] and checkm8 [[palera1n]], and upstream of userland cheat/inject stacks ([[opainject]], [[ceserver-ios]], [[memory-server]]) that assume jailbreak-grade `tfp0`/root.

## Links

- Repo: https://github.com/gmh5225/IOS-jailbreak--Fugu15

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[dopamine]] · [[dopamine2-roothide]] · [[palera1n]] · [[xnu-1day-practice]] · [[kfd-explorer]] · [[opainject]] · [[ceserver-ios]] · [[memory-server]]
