---
title: Detect-Any
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/lotty520__Detect-Any.md
updated: 2026-11-11
confidence: medium
---

# Detect-Any

**Detect-Any** (lotty520) is an open-source **Android environment integrity** framework that scans devices for compromise and tampering, then emits a **weighted risk score** with **replayable evidence**. Implemented primarily in **Kotlin** as a multi-module **Gradle** project with **JNI**-backed native probes, a **parallel collector** pipeline, **JSON rules**, and a **Jetpack Compose** app exposing **quick**, **full**, and **deep** (L1–L3) scan tiers. Signal coverage spans root and hook stacks (**Magisk**, **KernelSU**, **Zygisk**, **LSPosed**), **attestation spoofing** (incl. **TrickyStore**-class checks), **emulators** and cloud phones, dynamic instrumentation such as **Frida**, and behavioral channels (VPN, overlays, screen sharing), backed by a hot-updatable **Ed25519-signed** signature database. Confidence grading and parallel orchestration target auditability and low false-positive rates for security engineers, mobile anti-fraud teams, and game or app integrity research on Android. (source: wiki/sources/descriptions/lotty520__Detect-Any.md)

Complements modular inspectors [[duck-detector-refactoring]], offline multi-check [[advanced-root-checker]], RASP libraries [[device-trust]] and [[rootect]], and attestation tooling [[keyattestation]]—opposite root frameworks [[magisk]] and [[kernelsu]].

## Links

- Repo: https://github.com/lotty520/Detect-Any

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[duck-detector-refactoring]] · [[advanced-root-checker]] · [[device-trust]] · [[rootect]] · [[trickystore]] · [[detect-frida]] · [[magisk]] · [[kernelsu]] · [[zygisk]]
