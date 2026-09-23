---
title: Securify
kind: entity
topics: [anti-cheat, mobile-security]
sources:
  - wiki/sources/descriptions/RabehX__Securify.md
  - wiki/sources/README-categories.md
updated: 2026-09-23
confidence: medium
---

# Securify

**Securify** (RabehX/Securify) is an open-source Android security verification and hardware attestation utility that audits whether a device is rooted, tampered with, or running in an emulator. Listed under README **Anti Cheat > Detection:Android root**. (source: wiki/sources/descriptions/RabehX__Securify.md)

## Detection engine

The native **Rei 2.0.0** engine runs multi-threaded on-device audits across root, injection, framework, emulator, and system-integrity domains. Targets include **Magisk**, **KernelSU**, **Frida** hooks, and **Xposed**-style bytecode manipulation.

## Attestation and reporting

Verifies **Google Play Integrity** attestation through a configured backend and reports kernel version, supported ABIs, build fingerprint, and security patch level. Optional diagnostic log export uses the Android Storage Access Framework.

## Stack and audience

Kotlin with **Jetpack Compose** and a modular Gradle architecture. Targets developers and security researchers who need mobile device integrity checks for anti-cheat, fraud prevention, and reverse-engineering research.

## Links

- Repo: https://github.com/RabehX/Securify

## Related

[[rootect]] · [[advanced-root-checker]] · [[mobile-anti-cheat]] · [[mobile-trust-boundaries]] · [[jerrymanager]] · [[overviews/anti-cheat]] · [[overviews/mobile-security]]
