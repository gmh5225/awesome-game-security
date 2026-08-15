---
title: Android Overlay Protection
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/geeksonsecurity__android-overlay-protection.md
updated: 2026-08-15
confidence: medium
---

# Android Overlay Protection

Java library for detecting and mitigating **overlay attacks (tapjacking)** on Android. It scans for visible overlay windows drawn above the app that could intercept touches or obscure sensitive UI, implements `TYPE_APPLICATION_OVERLAY` detection, and handles `filterTouchesWhenObscured` so obscured views reject input. Callback-based notifications alert the app when overlays are present—aimed at developers and security engineers hardening login, payment, and permission flows. (source: wiki/sources/descriptions/geeksonsecurity__android-overlay-protection.md)

Defensive counterpart to offensive floating-overlay cheat menus such as [[android-native-surface]] and [[external-imgui-android]]; complements broader RASP samples ([[droidshield]], freeRASP) that may include screen-capture or overlay-adjacent signals.

## Links

- Repo: https://github.com/geeksonsecurity/android-overlay-protection

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[android-native-surface]] · [[external-imgui-android]] · [[droidshield]] · [[free-rasp-android]]
