---
title: DeviceTrust
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/Xheghun__DeviceTrust.md
updated: 2026-08-19
confidence: medium
---

# DeviceTrust

Android library that collects local device-integrity signals to assess whether a handset may be rooted, hooked, emulated, or otherwise compromised. Kotlin coroutine API plus native NDK C++ checks scan for root artifacts, runtime instrumentation such as [[frida]] and Xposed, emulator fingerprints, and weakened system integrity (bootloader state, SELinux enforcement). Assessments yield a weighted risk score with categorized evidence; apps can apply configurable review and high-risk thresholds or export raw signals for server-side scoring. Native binaries ship for ARM64, ARMv7, x86, and x86_64. Intended for mobile developers building fraud prevention, authentication hardening, or game anti-cheat controls on Android. (source: wiki/sources/descriptions/Xheghun__DeviceTrust.md)

Sits in the mobile RASP / integrity lane alongside [[duck-detector-refactoring]], [[android-native-root-detector]], [[droidshield]], freeRASP family, and [[trustdevice-android]]—opposite root frameworks [[magisk]] / [[kernelsu]] and instrumentation tooling [[frida]] / [[xposed-module-kit]].

## Links

- Repo: https://github.com/Xheghun/DeviceTrust

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[android-native-root-detector]] · [[duck-detector-refactoring]] · [[detection]] · [[frida-detection]] · [[android-emulator-detection]] · [[droidshield]] · [[trustdevice-android]] · [[magisk]] · [[frida]]
