---
title: RiskEngine
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/WsttXm__RiskEngine.md
updated: 2026-08-19
confidence: medium
---

# RiskEngine

Android risk-control SDK and management platform that fingerprints devices and runs runtime environment checks through native JNI probes and system-property analysis. Detects rooted handsets, emulators, hooking frameworks such as [[frida]] and Xposed, debuggers, VPN connections, sandbox environments, and related tamper signals. Intended for fraud prevention, authentication hardening, and game anti-cheat on Android. (source: wiki/sources/descriptions/WsttXm__RiskEngine.md)

Sits in the mobile RASP / integrity lane alongside [[device-trust]], [[droidshield]], [[trustdevice-android]], and [[duck-detector-refactoring]]—opposite root frameworks [[magisk]] / [[kernelsu]] and instrumentation tooling [[frida]] / [[xposed-module-kit]].

## Links

- Repo: https://github.com/WsttXm/RiskEngine

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[device-trust]] · [[droidshield]] · [[trustdevice-android]] · [[frida-detection]] · [[android-emulator-detection]] · [[detection]] · [[magisk]] · [[frida]]
