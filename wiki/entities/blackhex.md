---
title: BlackHex
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/areyougarou__BlackHex.md
  - wiki/sources/README-categories.md
updated: 2026-10-24
confidence: medium
---

# BlackHex

Free-tier Android runtime application self-protection (RASP) library: Kotlin SDK plus arm64 native checks for app tampering/repackaging, Frida and hooking, emulators, root and root-manager artifacts, and custom ROM or unlocked-bootloader signals. Policy toggles can allow or block emulator, instrumentation, root, and bootloader groups while app-integrity enforcement stays always on; each probe reports clean, detected, or inconclusive and rolls up to a local pass-or-block verdict without vendor-server telemetry. (source: wiki/sources/descriptions/areyougarou__BlackHex.md)

## Architecture

Gradle Android library module (API 26+); CMake/NDK scans include memory maps, GOT/PLT, opcode patterns, and JNI bridges for low-level integrity evidence.

## Integration

Suited to mobile games and fraud-sensitive apps needing lightweight on-device cheat/tamper signals for backend policy—not a substitute for server-side authorization or hardware attestation alone.

Sits in the mobile RASP lane beside [[rootect]], [[device-trust]], [[rootsentry]], and Talsec [[free-rasp-community]]—opposite instrumentation [[frida]] and root frameworks [[magisk]] / [[kernelsu]].

## Links

- Repo: https://github.com/areyougarou/BlackHex

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[mobile-trust-boundaries]] · [[rootect]] · [[securify]] · [[frida]]
