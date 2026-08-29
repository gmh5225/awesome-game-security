---
title: Free-RASP-Community
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/talsec__Free-RASP-Community.md
updated: 2026-08-29
confidence: medium
---

# Free-RASP-Community

Main community repository for **freeRASP**, Talsec's mobile Runtime Application Self-Protection (RASP) SDK for in-app threat detection and security monitoring at runtime. Aggregates platform-specific integrations for native Android and iOS, cross-platform frameworks (Flutter, React Native, Capacitor, Cordova, Kotlin Multiplatform), and game engines (Unity, Unreal Engine). Detects rooted or jailbroken devices, hooking frameworks such as [[frida]] and Xposed, reverse-engineering and repackaging attempts, untrusted installs, screen capture, device spoofing, and unsafe network or OS environments; optional Android malware scanning via freeMalwareDetection. Threats are reported through a callback API with minimal performance overhead; aligns with OWASP MASVS V8 resiliency requirements against reverse engineering. Targets mobile and game developers needing client-side application shielding against tampering, cheating, and compromised device environments. (source: wiki/sources/descriptions/talsec__Free-RASP-Community.md)

Platform integration siblings: native Android [[free-rasp-android]], native iOS [[free-rasp-ios]], Unity [[free-rasp-unity-poc]], React Native [[free-rasp-reactnative]], Capacitor [[free-rasp-capacitor]], Cordova [[free-rasp-cordova]], Flutter [[free-rasp-flutter]], and KMP [[free-rasp-kmp]]. Offensive evaluation tooling such as [[ultimate-frida-bypass]] documents layered bypass against Talsec/freeRASP-class RASP on Android.

## Links

- Repo: https://github.com/talsec/Free-RASP-Community

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[frida]] · [[droidshield]] · [[free-rasp-android]] · [[free-rasp-ios]] · [[free-rasp-unity-poc]] · [[free-rasp-reactnative]] · [[free-rasp-capacitor]] · [[free-rasp-cordova]] · [[free-rasp-flutter]] · [[free-rasp-kmp]]
