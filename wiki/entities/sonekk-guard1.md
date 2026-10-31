---
title: Sonekk Guard
kind: entity
topics: [anti-cheat, mobile-security]
sources:
  - wiki/sources/descriptions/sonekkdev__sonekk-guard1.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: medium
---

# Sonekk Guard

Free **client-server anti-cheat** stack for standalone **VR** titles on Quest- and Pico-class **Android** headsets. **C++17** native library in the game APK collects root, **Frida**/hooking, debugger, APK signature, pinned library hash, in-memory code, and prologue tampering evidence; ships privacy-conscious **signed JSON** reports to operator backends. **Unity** runtime package drives periodic collection; optional dependency-free **Node.js** reference server issues single-use challenges, verifies **HMAC** signatures, optional hardware **Keystore** attestation chains, and scores findings into watch/review/block verdicts applied **server-side only** (PolyForm license). (source: wiki/sources/descriptions/sonekkdev__sonekk-guard1.md)

Listed under **Anti Cheat** as an open-source mobile VR integrity layer without kernel drivers.

## Links

- Repo: https://github.com/sonekkdev/sonekk-guard1

## Related

[[overviews/anti-cheat]] · [[overviews/mobile-security]] · [[mobile-anti-cheat]] · [[mira]] · [[frida]]
