---
title: Magisk
kind: entity
topics: [mobile-security, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/topjohnwu__Magisk.md
  - wiki/sources/descriptions/ri-char__zygisk-dump-dex.md
updated: 2026-07-24
confidence: medium
---

# Magisk

Widely used Android root solution and **systemless** modification framework. Provides root via a `su` daemon, module-based changes without altering the system partition, MagiskHide for root-detection bypass, and an app for modules / superuser grants. Canonical Cheat Magisk / Android-root reference for mobile security and anti-cheat research on root frameworks, systemless mods, and root-hide tradeoffs. (source: wiki/sources/descriptions/topjohnwu__Magisk.md)

Adjacent tooling: kernel-level root peer [[kernelsu]]; boot-image tools [[magiskboot]] and [[magiskboot-ndk-on-linux]]; Magisk modules such as [[move-certificate]], Pixel-prop disguise [[easypixel]] (source: wiki/sources/descriptions/the-dise__EasyPixel.md), and Zygisk DEX dump [[zygisk-dump-dex]] (`libdexfile.so` hook; Android 14/15) (source: wiki/sources/descriptions/ri-char__zygisk-dump-dex.md); install paths such as [[cheese]]; detection samples such as [[magiskdetector]].

## Links

- Repo: https://github.com/topjohnwu/Magisk

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[kernelsu]] · [[magiskdetector]] · [[magiskboot]] · [[magiskboot-ndk-on-linux]] · [[move-certificate]] · [[easypixel]] · [[zygisk-dump-dex]] · [[cheese]] · [[keyattestation]] · [[frida]]
