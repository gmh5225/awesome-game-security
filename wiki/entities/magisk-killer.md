---
title: MagiskKiller
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/canyie__MagiskKiller.md
updated: 2026-08-17
confidence: medium
---

# MagiskKiller

Android app that detects **Magisk root** and **MagiskHide** through multiple vectors: active tracers (MagiskHide), unlocked bootloader state, modified system properties via property-area inspection, and active Magisk `su` sessions through PTS detection. Java/JNI/C++ runs checks in a **forked subprocess** with **pipe-based IPC** so MagiskHide cannot intercept probes on the calling process—complementing AppZygote-isolated designs like archived [[magiskdetector]]. Useful for mobile security researchers studying Magisk detection and anti-root-hiding on Android. (source: wiki/sources/descriptions/canyie__MagiskKiller.md)

Sits in the Anti Cheat `Detection:Magisk` lane opposite [[magisk]] hide modules ([[magiskhide]], [[riru-momo-hider]]) and alongside [[android-native-root-detector]] / [[detection]] multi-check collections.

## Links

- Repo: https://github.com/canyie/MagiskKiller

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[magisk]] · [[magiskhide]] · [[magiskdetector]] · [[riru-momo-hider]] · [[android-native-root-detector]] · [[detection]] · [[canyie-pine]]
