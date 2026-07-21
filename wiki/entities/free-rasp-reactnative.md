---
title: Free-RASP-ReactNative
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/talsec__Free-RASP-ReactNative.md
updated: 2026-07-21
confidence: medium
---

# Free-RASP-ReactNative

Talsec freeRASP plugin for React Native: mobile in-app RASP and application shielding on Android and iOS. TypeScript/JavaScript APIs (including `useFreeRasp`) bridge native Kotlin and Swift to the Talsec runtime for threat callbacks and optional screen-capture protection. Detection coverage includes root/jailbreak (Magisk, KernelSU, Dopamine, and similar), hooking frameworks such as [[frida]], app tampering / untrusted installs, device unbinding, malware and suspicious apps, time spoofing, and missing code obfuscation. Aimed at React Native developers needing lightweight, low-latency runtime monitoring against reverse engineering, compromised devices, and fraud, with optional weekly security reporting. (source: wiki/sources/descriptions/talsec__Free-RASP-ReactNative.md)

Sits in the mobile RASP / integrity lane alongside Unity sibling [[free-rasp-unity-poc]], Android-only [[droidshield]], and device-fingerprint SDKs [[trustdevice-android]] / [[trustdevice-ios]].

## Links

- Repo: https://github.com/talsec/Free-RASP-ReactNative

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[frida]] · [[free-rasp-unity-poc]] · [[droidshield]] · [[trustdevice-android]] · [[trustdevice-ios]] · [[magisk]] · [[kernelsu]]
