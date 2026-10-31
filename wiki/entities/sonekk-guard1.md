---
title: Sonekk Guard
kind: entity
topics: [anti-cheat, mobile-security, game-engine]
sources:
  - wiki/sources/descriptions/sonekkdev__sonekk-guard1.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: high
---

# Sonekk Guard

**Sonekk Guard** ([sonekkdev/sonekk-guard1](https://github.com/sonekkdev/sonekk-guard1)) is a free **client-server anti-cheat** stack aimed at standalone **VR** titles on Quest- and Pico-class **Android** headsets. PolyForm-licensed; listed under README **Anti Cheat** as an open-source mobile VR integrity layer without kernel drivers or third-party telemetry. (source: wiki/sources/descriptions/sonekkdev__sonekk-guard1.md)

## Client (native + Unity)

A **C++17** native library embedded in the game APK collects evidence of rooting, **Frida** and other hooking frameworks, active debuggers, and tampering with APK signature, pinned library hashes, in-memory code, and function prologues. It ships a privacy-conscious **signed JSON** report to the operator backend. A **Unity** runtime package drives periodic collection and upload. (source: wiki/sources/descriptions/sonekkdev__sonekk-guard1.md)

## Reference server

Optional dependency-free **Node.js** reference server issues single-use challenges, verifies **HMAC** signatures, optionally validates hardware **Keystore** attestation chains, and scores findings into **watch**, **review**, or **block** verdicts. Ban and enforcement logic stay **server-side only** so patched clients cannot silently self-clear. (source: wiki/sources/descriptions/sonekkdev__sonekk-guard1.md)

## Design intent

Targets small studios that want mod and cheat resistance without kernel drivers or commercial RASP telemetry—practical integrity for standalone VR rather than kernel-level or platform-AC replacement. (source: wiki/sources/descriptions/sonekkdev__sonekk-guard1.md)

## Links

- Repo: https://github.com/sonekkdev/sonekk-guard1

## Related

[[overviews/anti-cheat]] · [[overviews/mobile-security]] · [[mobile-anti-cheat]] · [[com-sipvlib-anticheat]] · [[free-rasp-unity-poc]] · [[mira]] · [[frida]] · [[keyattestation]]
