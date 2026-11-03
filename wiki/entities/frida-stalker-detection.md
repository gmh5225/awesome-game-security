---
title: Frida Stalker Detection
kind: entity
topics: [mobile-security, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/romainthomas__frida-stalker-detection.md
  - wiki/sources/README-categories.md
updated: 2026-11-03
confidence: medium
---

# Frida Stalker Detection

Proof-of-concept that detects when Frida’s **Stalker** engine is actively tracing the current thread on **Android ARM64** and **Linux x86-64**. Inline assembly plants canary values in stack slots beyond the red zone where Stalker saves backup registers, forces a control-flow transition that triggers Stalker’s context switch, and checks whether canaries were overwritten across repeated rounds. C/CMake code links the Frida Gum devkit for embedded Stalker tests; a justfile automates Linux and Android builds and on-device runs. Useful for game security and mobile hardening teams that need Stalker-specific instrumentation signals beyond generic Frida presence checks. (source: wiki/sources/descriptions/romainthomas__frida-stalker-detection.md)

## Links

- Repo: https://github.com/romainthomas/frida-stalker-detection

## Related

[[frida]] · [[veridiff]] · [[mira]] · [[overviews/mobile-security]] · [[overviews/anti-cheat]]
