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

Proof-of-concept ([romainthomas/frida-stalker-detection](https://github.com/romainthomas/frida-stalker-detection)) that detects when Frida Gum **Stalker** is actively tracing the **current thread**, not merely when Frida libraries or hooks are present. Listed under README **Anti Cheat → Detection:Frida**. (source: wiki/sources/descriptions/romainthomas__frida-stalker-detection.md) (source: wiki/sources/README-categories.md)

## Mechanism

Inline assembly plants **canary values** in stack slots **beyond the red zone** where Stalker saves backup registers during its context switch. The PoC forces a **control-flow transition** that triggers Stalker’s save/restore path, then checks whether canaries were overwritten across **repeated rounds**. A positive signal implies Stalker is instrumenting execution on that thread. (source: wiki/sources/descriptions/romainthomas__frida-stalker-detection.md)

## Platforms and build

Targets **Android ARM64** and **Linux x86-64**. Implementation is **C** with **CMake**, linking the **Frida Gum devkit** for embedded Stalker self-tests on each platform. A **justfile** automates Linux builds, Android cross-builds, and on-device runs. (source: wiki/sources/descriptions/romainthomas__frida-stalker-detection.md)

## Positioning

Complements hook- and artifact-oriented Detection:Frida research such as [[frida-detection]] and [[detect-frida]] by surfacing **active Stalker tracing**—relevant when analysts rely on Stalker for coverage, branch logging, or dual-trace diff tooling (e.g. [[veridiff]]) and stealth builds hide generic Frida fingerprints. (source: wiki/sources/descriptions/romainthomas__frida-stalker-detection.md)

## Links

- Repo: https://github.com/romainthomas/frida-stalker-detection

## Related

[[frida]] · [[frida-detection]] · [[detect-frida]] · [[veridiff]] · [[mira]] · [[overviews/mobile-security]] · [[overviews/anti-cheat]]
