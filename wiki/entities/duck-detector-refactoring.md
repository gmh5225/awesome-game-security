---
title: Duck-Detector-Refactoring
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/eltavine__Duck-Detector-Refactoring.md
updated: 2026-08-15
confidence: medium
---

# Duck-Detector-Refactoring

Refactored **DuckDetector**: local Android device-integrity inspector covering root tampering, runtime hooking, mount anomalies, attestation trust, and virtualization evidence. Jetpack Compose UI with modular Kotlin feature packages and native C++ / assembly probes surfaces detector cards with structured findings, method coverage, and scan-state summaries. Useful for game security researchers and reverse engineers studying offensive techniques in the cheat / Android root lane. (source: wiki/sources/descriptions/eltavine__Duck-Detector-Refactoring.md)

Complements multi-check environment probes [[detection]], native root detector [[android-native-root-detector]], Magisk-focused [[magiskdetector]], attestation tooling [[keyattestation]], and emulator/VM probes [[android-emulator-detection]] / [[conbeerlib]]—opposite root frameworks [[magisk]] and [[kernelsu]].

## Links

- Repo: https://github.com/eltavine/Duck-Detector-Refactoring

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[detection]] · [[android-native-root-detector]] · [[magiskdetector]] · [[keyattestation]] · [[android-emulator-detection]] · [[magisk]] · [[kernelsu]]
