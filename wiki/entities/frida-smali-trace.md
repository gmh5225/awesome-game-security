---
title: frida-smali-trace
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/SeeFlowerX__frida-smali-trace.md
updated: 2026-08-21
confidence: medium
---

# frida-smali-trace

**Frida-based** tracing toolkit for observing **Android smali instruction execution** at runtime. Uses **JavaScript/TypeScript** Frida agents to hook **ART interpreter** paths and emit detailed execution logs. Documentation covers locating architecture-specific offsets and registers with static analysis tools such as **IDA** before running traces. Intended for Android reverse engineering and mobile security research focused on **runtime behavior analysis**. (source: wiki/sources/descriptions/SeeFlowerX__frida-smali-trace.md)

Complements static smali/DEX lanes ([[apktool]], [[jadx]]) with interpreter-level dynamic tracing; sits beside other SeeFlowerX Android telemetry such as [[stackplz]] and general [[frida]] hooking workflows.

## Links

- Repo: https://github.com/SeeFlowerX/frida-smali-trace

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[frida]] · [[stackplz]] · [[apktool]] · [[jadx]] · [[qbdi-tracer-android]]
