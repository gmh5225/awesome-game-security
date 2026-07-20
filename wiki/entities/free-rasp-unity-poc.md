---
title: Free-RASP-Unity-POC
kind: entity
topics: [mobile-security, anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/talsec__Free-RASP-Unity-POC.md
updated: 2026-07-20
confidence: medium
---

# Free-RASP-Unity-POC

Talsec Unity plugin wrapping the freeRASP runtime application self-protection SDK for mobile in-app protection. C# APIs bridge native Android (Java) and iOS (Swift/Objective-C++) so Unity games can initialize Talsec, receive threat callbacks, and react to runtime attacks. Detection coverage includes root/jailbreak, hooking frameworks such as [[frida]], emulators/simulators, app integrity / unofficial installs, debugging, screenshots or screen recording, and device-state risks (time/location spoofing). Ships a sample Unity test app for integration checks. Aimed at Unity mobile developers needing freemium RASP against RE, tampering, and compromised OS environments on Android and iOS. (source: wiki/sources/descriptions/talsec__Free-RASP-Unity-POC.md)

Sits in the mobile RASP / integrity lane alongside Android-only [[droidshield]] and device-fingerprint SDKs [[trustdevice-android]] / [[trustdevice-ios]].

## Links

- Repo: https://github.com/talsec/Free-RASP-Unity-POC

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[frida]] · [[droidshield]] · [[trustdevice-android]] · [[trustdevice-ios]] · [[il2cpp]]
