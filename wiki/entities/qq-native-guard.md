---
title: QQ Native Guard
kind: entity
topics: [mobile-security, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/KIDA-Nya__QQNativeGuard.md
updated: 2026-11-24
confidence: medium
---

# QQ Native Guard

**LSPosed** module that extends a Java-layer Tencent **QQ** detection bypass with **native ByteHook** inline hooks aimed at QQ’s environment and device-integrity checks. Gradle builds pair Java/Kotlin app code with C++ **NDK** hooks across **libc** and QQ-specific libraries (**fekit**, **MSF**, **Turing**), with coordinated spoofing of system properties, `/proc` and sysfs reads, identifiers, and HTTP user-agent strings so multi-channel reports stay aligned (QsecEst, HTTP UA, MSF, VOD). (source: wiki/sources/descriptions/KIDA-Nya__QQNativeGuard.md)

Configuration-driven identity profiles, observation modes for traffic and risk telemetry, verification scripts, and audits of detection surfaces and data exposure support authorized study of mobile client anti-tamper, root and Xposed detection, and **multi-channel device fingerprinting** on Android.

## Links

- Repo: https://github.com/KIDA-Nya/QQNativeGuard

## Related

[[overviews/mobile-security]] · [[concepts/mobile-anti-cheat]] · [[spoofing-collection]] · [[device-reset-spoofer]] · [[hidemyandroid]] · [[lsposed-universal-template]] · [[xposed-module-kit]] · [[trustdevice-android]] · [[memdetection]]