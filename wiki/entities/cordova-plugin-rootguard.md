---
title: Cordova Plugin RootGuard
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/Binuka97__cordova-plugin-rootguard.md
updated: 2026-08-30
confidence: medium
---

# Cordova Plugin RootGuard

**cordova-plugin-rootguard** (Binuka97) is a Cordova plugin that provides best-effort **root**, **jailbreak**, and **runtime instrumentation** detection for hybrid **Android** and **iOS** apps. Native checks in **Java** and **Objective-C** bridge to JavaScript, probing for `su` binaries and root managers such as **Magisk**, **KernelSU**, and **APatch**, plus **Frida**, **Frida Gadget**, **Gum**, debugger state, and related process artifacts. Results use a three-state model of **SAFE**, **COMPROMISED**, and **UNKNOWN** so timeouts and restricted OS capabilities are not treated as proof of compromise, with optional detailed evidence telemetry. Intended as a local risk sensor for mobile app security and anti-tamper workflows—typically paired with server-side platform attestation rather than used alone for high-value authorization. (source: wiki/sources/descriptions/Binuka97__cordova-plugin-rootguard.md)

Sits in the Cordova RASP lane beside commercial [[free-rasp-cordova]] and open-source multi-check tools such as [[advanced-root-checker]] and [[android-native-root-detector]]—opposite root frameworks [[magisk]], [[kernelsu]], and [[apatch]], and instrumentation stacks probed via [[detect-frida]].

## Links

- Repo: https://github.com/Binuka97/cordova-plugin-rootguard

## Related

[[overviews/mobile-security]] · [[mobile-anti-cheat]] · [[free-rasp-cordova]] · [[advanced-root-checker]] · [[android-native-root-detector]] · [[detect-frida]] · [[frida]] · [[magisk]] · [[kernelsu]] · [[apatch]]
