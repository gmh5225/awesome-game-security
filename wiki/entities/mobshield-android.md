---
title: MobShield Android
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/Inforaam__MobShield-Android.md
  - wiki/sources/README-categories.md
updated: 2026-11-17
confidence: medium
---

# MobShield Android

Open-source **runtime application self-protection (RASP)** library for Android (Inforaam/MobShield-Android). Kotlin core with native C/C++ probes runs modular on-device detectors and aggregates results into **weighted threat events** reported through listeners, with optional process-termination policies and attested reports for server verification. Targets games and high-risk apps needing auditable client-side anti-tampering and anti-analysis signals as one layer of defense in depth alongside backend checks. (source: wiki/sources/descriptions/Inforaam__MobShield-Android.md)

## Detection modules

Optional modules cover root and platform integrity (Magisk, Zygisk, KernelSU), hook frameworks (Frida, LSPosed, Xposed), debuggers, emulators and automation, and APK or signature integrity.

## Architecture

| Layer | Role |
|-------|------|
| **Core engine** | Scores detector output, emits weighted threat events, listener callbacks |
| **Kotlin API** | Integration surface for host apps |
| **Native C/C++** | Per-module integrity and environment probes |
| **Gradle plugin** | Per-release native build personalization |

## Attestation and policy

Reports can be signed for server verification via **Android Keystore** or **Play Integrity**. Coverage is documented against **OWASP MASVS** resilience controls.

## Positioning

**Anti Cheat / Detection:Android root** and mobile RASP lane beside [[rootect]], [[blackhex]], [[device-trust]], and Talsec [[free-rasp-android]]—opposite instrumentation and root stacks such as [[magisk]], [[kernelsu]], [[frida]], and [[xposed-module-kit]].

## Links

- Repo: https://github.com/Inforaam/MobShield-Android

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[rootect]] · [[blackhex]] · [[free-rasp-android]] · [[frida]] · [[magisk]] · [[xposed-module-kit]]