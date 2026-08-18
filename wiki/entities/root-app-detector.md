---
title: RootAppDetector
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/apkunpacker__RootAppDetector.md
updated: 2026-08-18
confidence: medium
---

# RootAppDetector

Small Android proof-of-concept that detects known root-management applications by **app presence**. Written in Java; iterates target package/activity pairs, attempts activity launches, and interprets `SecurityException` outcomes to infer installed root managers. Ships as a minimal Gradle project with a simple UI to rescan and display findings. Useful for mobile anti-cheat and integrity teams validating package-manager–visible root-app detection. (source: wiki/sources/descriptions/apkunpacker__RootAppDetector.md)

Sits in the Anti Cheat `Detection:Android root` lane beside broader environment probes such as [[android-native-root-detector]], [[magiskdetector]], [[magisk-detection]] (same author; archive of root/Magisk POC APK samples), and [[detection]]—opposite root-hide tooling such as [[hideroot]] and [[riru-momo-hider]] that conceal Magisk artifacts from package and mount checks.

## Links

- Repo: https://github.com/apkunpacker/RootAppDetector

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[android-native-root-detector]] · [[magiskdetector]] · [[magisk-detection]] · [[detection]] · [[magisk]] · [[kernelsu]] · [[hideroot]]
