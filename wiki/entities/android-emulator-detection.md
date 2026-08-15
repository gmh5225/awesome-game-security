---
title: Android-Emulator-Detection
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__Android-Emulator-Detection.md
  - wiki/sources/descriptions/reveny__Android-Emulator-Detection.md
updated: 2026-08-15
confidence: medium
---

# Android-Emulator-Detection

Wiki slug for README **Android Anti-Emulator** / Anti Cheat `Detection:Virtual Environments` samples named **Android-Emulator-Detection**.

## gmh5225 (Java/Kotlin library)

Android library implementing multiple emulator detection techniques with a **scoring system** combining heuristics: QEMU-specific files, Genymotion markers, BlueStacks artifacts, build property anomalies, hardware sensor absence, telephony service inconsistencies, and known emulator MAC/IMEI patterns. Aimed at mobile game developers and security engineers implementing emulator detection for anti-cheat or anti-fraud. (source: wiki/sources/descriptions/gmh5225__Android-Emulator-Detection.md)

## reveny (Java + C++ plugin)

Java/C++ Anti-Emulator project oriented toward plugin development and emulation research. (source: wiki/sources/descriptions/reveny__Android-Emulator-Detection.md)

Sits alongside classic Java artifact heuristics [[anti-emulator]], container·VM probes [[conbeerlib]], and broader RASP samples such as [[droidshield]] / freeRASP that include emulator signals.

## Links

- gmh5225: https://github.com/gmh5225/Android-Emulator-Detection
- reveny: https://github.com/reveny/Android-Emulator-Detection

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[anti-emulator]] · [[conbeerlib]] · [[droidshield]] · [[android-native-root-detector]] · [[anticuckoo]] · [[awesome-anti-virtualization]]
