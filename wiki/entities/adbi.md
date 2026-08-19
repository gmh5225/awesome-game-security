---
title: ADBI
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/crmulliner__adbi.md
  - wiki/sources/descriptions/WaterlooBridge__adbi.md
updated: 2026-08-19
confidence: medium
---

# ADBI

**Android Dynamic Binary Instrumentation** — native instrumentation toolkit for Android **ARM** and **Thumb** targets. Combines a **hijack injector** with a base hooking library to load instrumentation into running processes and **inline-hook function entry points**. Built with C/C++ and the Android NDK; includes sample instruments for runtime logging and behavior interception. Intended for mobile reverse engineering, runtime analysis, and security research on Android applications. (source: wiki/sources/descriptions/WaterlooBridge__adbi.md)

Original lineage: crmulliner’s Android native instrumentation toolkit in the Cheat / dynamic binary instrumentation lane (library injection + inline entry hooking). (source: wiki/sources/descriptions/crmulliner__adbi.md)

Historical predecessor to modern Frida-, ptrace-, and Zygote-based Android inject stacks; complements [[frida]], [[dobby]], [[qbdi-tracer-android]], and [[android-super-inject]].

## Links

- Repo (WaterlooBridge fork): https://github.com/WaterlooBridge/adbi
- Repo (original): https://github.com/crmulliner/adbi

## Related

[[frida]] · [[dobby]] · [[qbdi-tracer-android]] · [[android-super-inject]] · [[dynamic-binary-instrumentation]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
