---
title: Rootect
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/SloMR__Rootect.md
  - wiki/sources/README-categories.md
updated: 2026-09-13
confidence: medium
---

# Rootect

Zero-dependency Android RASP library (Kotlin + native C++) that gathers environment-integrity evidence for rooted devices, runtime instrumentation, repackaging, debuggers, and emulators. Native detectors use raw syscalls and obfuscated strings to probe Magisk, KernelSU, Frida, and Xposed, then aggregate findings into scored risk reports. Optional Android Key Attestation produces hardware-signed certificate chains for backend verification alongside on-device signals. Ships sample app and reference attestation server. Targets mobile games and security-sensitive apps needing tamper/cheat telemetry rather than a single on-device verdict. (source: wiki/sources/descriptions/SloMR__Rootect.md)

## Links

- Repo: https://github.com/SloMR/Rootect

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[mobile-trust-boundaries]] · [[rootsentry]] · [[device-trust]] · [[frida]] · [[magisk]]
