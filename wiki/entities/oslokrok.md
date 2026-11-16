---
title: Oslokrok
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Ascen1ty__oslokrok.md
updated: 2026-11-16
confidence: medium
---

# Oslokrok

**Oslokrok** is an Android **Xposed-style** module for **LSPosed** or **Vector** that keeps the **PayPal** mobile app from **kill-on-launch** when on-device **RASP / anti-tamper** runs on **rooted** phones. Implemented as a **Gradle** Java application module, it hooks PayPal’s in-process integrity checks: **no-op** startup **AppVerifier** logic on newer builds and the **legacy root-detection signal path** on older ones. Hook targets are discovered at runtime with **DexKit** using package and method-shape anchors, with **hardcoded class and method fallbacks** when dynamic search fails. Requires **arm64-v8a**, root, a working Xposed framework, and separate **root-hiding** setup. Aimed at **reverse engineering** and mobile **client-protection** research around RASP and anti-tamper bypass—not **server-side attestation**. (source: wiki/sources/descriptions/Ascen1ty__oslokrok.md)

Listed under **Cheat → Xposed** beside LSPosed research modules such as [[io-mo-glassmic]] and [[com-fuck-iab]].

## Links

- Repo: https://github.com/Ascen1ty/oslokrok (README tag: LSPosed/Vector PayPal RASP DexKit hooks)

## Related

[[dexkit-android]] · [[xposed-module-kit]] · [[lsposed-universal-template]] · [[appsealing-reversal]] · [[com-fuck-iab]] · [[mobile-anti-cheat]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]