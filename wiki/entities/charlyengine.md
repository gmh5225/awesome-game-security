---
title: charlyengine
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/andoridcharlyroot-debug__charlyengine.md
  - wiki/sources/README-categories.md
updated: 2026-08-26
confidence: medium
---

# charlyengine

**CharlyEngine** is a minimal Cheat Engine–style memory scanner and modifier for rooted **Android** devices. It pairs a **Kotlin** + **Jetpack Compose** UI with a native **C** daemon that reads and writes target process memory via `/proc`, supporting classic scan, rescan, inject, and freeze workflows. (source: wiki/sources/descriptions/andoridcharlyroot-debug__charlyengine.md)

The app can attach to running games or launch and hook them automatically, persist scan sessions and frozen addresses per title, and stream live value changes to an integrated terminal. Supported value types include integers, floats, longs, words, and bytes. The root daemon exposes a text protocol drivable from **Termux** or other shells.

Sits in the Cheat **Android Memory Explorer** lane beside CE-style debuggers such as [[memdbg]] and full-stack editors such as [[ace-the-game]], but with a lighter Compose UI + `/proc` daemon split aimed at modders and game-security researchers studying rooted Android memory tampering.

## Links

- Repo: https://github.com/andoridcharlyroot-debug/charlyengine

## Related

[[memdbg]] · [[ace-the-game]] · [[cheap-engine]] · [[writemem]] · [[android-memory-tool]] · [[termux-app]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
