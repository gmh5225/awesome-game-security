---
title: AERoot
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/quarkslab__AERoot.md
updated: 2026-07-25
confidence: medium
---

# AERoot

Quarkslab **Python tool for rooting Android Emulator instances at runtime** without rewriting the system image. Uses the emulator debug pipe or ADB root to remount `/system` read-write, install a custom `su` binary, and establish persistent root across multiple Android API levels. Aimed at mobile security researchers and Android developers who need rooted emulator hosts for testing and reverse engineering. (source: wiki/sources/descriptions/quarkslab__AERoot.md)

Sits in the Cheat `[Root]` / `Android Emulator` lane beside device-scoped root paths such as [[magisk]] / [[kernelsu]] / [[dirtypiperoot]], and opposite emulator-detection samples such as [[anti-emulator]] / [[android-emulator-detection]].

## Links

- Repo: https://github.com/quarkslab/AERoot (README tag: Root)

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[magisk]] · [[kernelsu]] · [[dirtypiperoot]] · [[gunyah-hypervisor]] · [[anti-emulator]] · [[android-emulator-detection]] · [[termux-app]]
