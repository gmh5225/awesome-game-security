---
title: Free-RASP-Android
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/talsec__Free-RASP-Android.md
updated: 2026-08-09
confidence: medium
---

# Free-RASP-Android

Talsec sample Android application demonstrating integration of the freeRASP SDK, a Runtime Application Self-Protection (RASP) library for in-app threat detection and security monitoring. Kotlin/Gradle demo shows `TalsecConfig` setup, `ThreatListener` callbacks, and responses to root/Magisk access, debuggers, emulators, hooking frameworks such as [[frida]], APK tampering, untrusted install sources, malware, screen capture, and location or WiFi spoofing. Optional screen protection, device state checks, signing certificate validation, and ProGuard-enabled release builds use the `TalsecSecurity-Community` Maven dependency. Targets native Android developers needing client-side shielding against reverse engineering, repackaging, and compromised environments—including games and fintech apps requiring anti-cheat and fraud protection. (source: wiki/sources/descriptions/talsec__Free-RASP-Android.md)

Sits in the mobile RASP / integrity lane as the native Android reference alongside cross-platform siblings [[free-rasp-unity-poc]], [[free-rasp-reactnative]], [[free-rasp-capacitor]], [[free-rasp-cordova]], [[free-rasp-flutter]], native iOS [[free-rasp-ios]], Android-only [[droidshield]], and device-fingerprint SDKs [[trustdevice-android]] / [[trustdevice-ios]].

## Links

- Repo: https://github.com/talsec/Free-RASP-Android

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[frida]] · [[free-rasp-ios]] · [[free-rasp-unity-poc]] · [[free-rasp-reactnative]] · [[free-rasp-capacitor]] · [[free-rasp-cordova]] · [[free-rasp-flutter]] · [[droidshield]]
