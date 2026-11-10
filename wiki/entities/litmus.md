---
title: Litmus
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/xunyyds__litmus.md
updated: 2026-11-10
confidence: medium
---

# Litmus

**Litmus** (xunyyds) is an open **Android resilience benchmark** that ships a canary app so developers can patch, repack, or instrument it and measure how much tampering still evades detection. The stack combines a Java Android probe runner, C++ native ELF and memory forensics, and a **Python CLI** that records baselines, runs experiments, and emits reproducible **JSON scores** plus **HTML reports**. It exercises dozens of cataloged detection vectors across package integrity, code injection, runtime hooks, privilege elevation, virtualization, and environment signals, with scoring that highlights blind spots and false positives against a clean baseline. The project deliberately avoids third-party runtime dependencies and targets developers validating anti-tamper and anti-cheat-style hardening under **OWASP MASVS** resilience assumptions on real devices from Android 8 through current releases. (source: wiki/sources/descriptions/xunyyds__litmus.md)

Complements offline multi-check inspectors such as [[advanced-root-checker]] and scored runtime-risk tools [[security-risk-android]]; Frida, **Xposed**, **Zygisk**, repack, and emulator vectors align with [[mobile-anti-cheat]] signal families.

## Links

- Repo: https://github.com/xunyyds/litmus

## Related

[[overviews/mobile-security]] · [[mobile-anti-cheat]] · [[advanced-root-checker]] · [[security-risk-android]] · [[rootsentry]] · [[duck-detector-refactoring]] · [[frida]] · [[zygisk]] · [[memdetection]]
