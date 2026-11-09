---
title: flutter-tamper-detector
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/kauemurakami__flutter_tamper_detector.md
updated: 2026-11-09
confidence: medium
---

# flutter-tamper-detector

Flutter plugin for **client-side tamper and runtime-risk detection** on Android and iOS. Dart APIs wrap native Kotlin and Swift probes so apps can block or exit before sensitive logic runs. Checks cover rooted or jailbroken hosts, hooking frameworks (Frida, Xposed, Cydia Substrate), emulators and simulators, debug builds, and installs outside official stores. Optional responses include automatic process termination, self-uninstall on rooted compromise, window hardening against screenshots and recents preview, and **early native checks before the Flutter engine starts** (`onCreate`-time gates). Targets Flutter games, fintech, and other security-sensitive mobile clients needing in-app RASP-style integrity controls. (source: wiki/sources/descriptions/kauemurakami__flutter_tamper_detector.md)

Defensive complement to Flutter offensive RE lanes ([[unflutter]], [[flutter-re-demo]]); overlaps commercial Flutter freeRASP ([[free-rasp-flutter]]) on signal coverage but emphasizes native pre-engine gating and optional self-uninstall.

## Links

- Repo: https://github.com/kauemurakami/flutter_tamper_detector

## Related

[[overviews/mobile-security]] · [[mobile-anti-cheat]] · [[free-rasp-flutter]] · [[frida]] · [[unflutter]] · [[flutter-re-demo]]
