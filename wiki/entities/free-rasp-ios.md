---
title: Free-RASP-iOS
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/talsec__Free-RASP-iOS.md
updated: 2026-08-03
confidence: medium
---

# Free-RASP-iOS

Talsec freeRASP for native iOS: a free Runtime Application Self-Protection (RASP) SDK that adds in-app threat detection and security monitoring to Swift/Objective-C applications. Ships as the **TalsecRuntime** XCFramework via Swift Package Manager or Xcode, with a Swift demo app that scans the device and reports a security score from detected risks. Developers initialize protection through `TalsecConfig` and `Talsec.start`, then handle threat callbacks in app logic. Detection coverage includes jailbreak, debuggers, runtime hooking and manipulation frameworks (including [[frida]]), simulators, tampered or unofficial installs, invalid app signatures, Secure Enclave availability, passcode protection, device binding, system VPN use, screenshots, screen recording, and time spoofing. Aimed at iOS and mobile game developers needing lightweight runtime defenses against reverse engineering, cheating, fraud, and compromised devices without building security tooling from scratch. (source: wiki/sources/descriptions/talsec__Free-RASP-iOS.md)

Sits in the mobile RASP / integrity lane alongside cross-platform Talsec siblings [[free-rasp-unity-poc]], [[free-rasp-reactnative]], and [[free-rasp-capacitor]], Android-only [[droidshield]], and device-fingerprint SDKs [[trustdevice-ios]] / [[trustdevice-android]].

## Links

- Repo: https://github.com/talsec/Free-RASP-iOS

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[frida]] · [[free-rasp-unity-poc]] · [[free-rasp-reactnative]] · [[free-rasp-capacitor]] · [[droidshield]] · [[trustdevice-ios]] · [[trustdevice-android]]
