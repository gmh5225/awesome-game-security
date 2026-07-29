---
title: rs-native-kit-security
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/rajssinde__rs-native-kit-security.md
updated: 2026-07-29
confidence: medium
---

# rs-native-kit-security

Enterprise-grade runtime application self-protection (RASP) SDK for React Native on Android and iOS. TypeScript-first APIs expose native Kotlin and Swift checks through Nitro Modules on React Native's New Architecture, enabling JSI-direct calls without bridge serialization. Detection coverage includes root/jailbreak, emulator/simulator, Frida/Xposed/Magisk hooking, app signature and APK integrity, VPN/proxy and screen-capture monitoring, plus SSL pinning helpers. A configurable device risk engine emits real-time security events. Aimed at security-sensitive mobile apps — banking, fintech, and games needing client-side anti-tamper and anti-cheat protections. (source: wiki/sources/descriptions/rajssinde__rs-native-kit-security.md)

Sits in the mobile RASP / integrity lane alongside Talsec [[free-rasp-reactnative]] / [[free-rasp-capacitor]], Unity sibling [[free-rasp-unity-poc]], Android-only [[droidshield]], and device-fingerprint SDKs [[trustdevice-android]] / [[trustdevice-ios]].

## Links

- Repo: https://github.com/rajssinde/rs-native-kit-security

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[frida]] · [[free-rasp-reactnative]] · [[free-rasp-capacitor]] · [[free-rasp-unity-poc]] · [[droidshield]] · [[magisk]] · [[trustdevice-android]] · [[trustdevice-ios]]
