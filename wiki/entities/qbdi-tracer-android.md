---
title: qbdi-tracer-android
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/g2wfw__qbdi-tracer-android.md
updated: 2026-08-15
confidence: medium
---

# qbdi-tracer-android

Android native code tracing framework built on **QBDI** (QuarkslaB Dynamic Binary Instrumentation) and the **[[dobby]]** inline hooking library. Intercepts shared-library loading through Android linker hooks, instruments target functions for per-instruction tracing with backtrace capture, and ships memory scanning and pattern-matching utilities. CMake toolchain files support cross-compilation for Android, iOS, and other ARM64 targets. Cheat / Android assembly instruction tracing lane. (source: wiki/sources/descriptions/g2wfw__qbdi-tracer-android.md)

## Links

- Repo: https://github.com/g2wfw/qbdi-tracer-android

## Related

[[dobby]] · [[dynamic-binary-instrumentation]] · [[btrace]] · [[frida]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
