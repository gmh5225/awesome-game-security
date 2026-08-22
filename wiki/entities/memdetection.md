---
title: MemDetection
kind: entity
topics: [anti-cheat, mobile-security]
sources:
  - wiki/sources/descriptions/Mrack__MemDetection.md
updated: 2026-08-22
confidence: medium
---

# MemDetection

Android anti-tampering demo that detects abnormal runtime environments by comparing in-memory and on-disk CRC checksums of critical system libraries (`libc.so`, `libart.so`). Combines a Java Android app with a Rust native component integrated through Gradle and JNI. Checks target signs of instrumentation or modification frameworks such as [[frida]], Xposed, and cloning environments. Main use case is mobile security hardening and runtime integrity validation for Android applications, including games. (source: wiki/sources/descriptions/Mrack__MemDetection.md)

## Links

- Repo: https://github.com/Mrack/MemDetection

## Related

[[frida]] · [[detect-frida]] · [[mobile-anti-cheat]] · [[xposed-module-kit]] · [[overviews/mobile-security]] · [[overviews/anti-cheat]]
