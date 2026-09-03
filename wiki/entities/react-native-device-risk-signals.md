---
title: React Native Device Risk Signals
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/AfanasievN__react-native-device-risk-signals.md
updated: 2026-09-03
confidence: medium
---

# React Native Device Risk Signals

Open-source React Native TurboModule (New Architecture) that collects raw device intelligence and fraud-prevention signals on Android and iOS. Kotlin, Objective-C/C++, and TypeScript probes return typed outcomes for root and jailbreak indicators, emulator detection, debugger and [[frida]] traces, VPN and proxy state, hardware, locale, application, and runtime data—without computing a client-side risk score or uploading results. Probe failures are isolated; the host app controls consent, timeouts, and which signals to collect. Primary use case: enriching backend fraud-prevention, device-risk, and mobile security models for login, checkout, payments, and other high-risk actions. (source: wiki/sources/descriptions/AfanasievN__react-native-device-risk-signals.md)

Sits in the mobile RASP / device-intel lane beside [[react-native-shieldscan]], [[free-rasp-reactnative]], and [[rs-native-kit-security]]—emphasizing raw signal export for server-side scoring rather than embedded threat callbacks or vendor backends.

## Links

- Repo: https://github.com/AfanasievN/react-native-device-risk-signals

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[frida]] · [[react-native-shieldscan]] · [[free-rasp-reactnative]] · [[rs-native-kit-security]] · [[droidshield]] · [[detection]]
