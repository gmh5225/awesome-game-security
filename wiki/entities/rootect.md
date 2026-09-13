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

Zero-dependency Android RASP library (Kotlin + native C++) that gathers environment-integrity evidence for rooted devices, runtime instrumentation, repackaging, debuggers, and emulators. Native detectors use raw syscalls and obfuscated strings, then aggregate findings into scored risk reports rather than emitting a single on-device verdict. Targets mobile games and security-sensitive apps needing tamper/cheat telemetry for backend policy. (source: wiki/sources/descriptions/SloMR__Rootect.md)

## Detection signals

Probes Magisk, KernelSU, Frida, Xposed, repackaging, debuggers, and emulators across root, instrumentation, integrity, and unsafe runtime conditions.

## Architecture

Kotlin API surface with native C++ detectors; no third-party dependencies. Syscall-level checks and string obfuscation reduce trivial hook/patch surface on native probes.

## Integration

Optional Android Key Attestation produces hardware-signed certificate chains for backend verification alongside on-device signals. Ships sample app and reference attestation server for integration workflows.

Sits in the mobile RASP lane beside [[device-trust]], [[rootsentry]], and [[duck-detector-refactoring]]—opposite root frameworks [[magisk]] / [[kernelsu]] and instrumentation [[frida]] / [[xposed-module-kit]].

## Links

- Repo: https://github.com/SloMR/Rootect

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[mobile-trust-boundaries]] · [[rootsentry]] · [[device-trust]] · [[frida]] · [[magisk]]
