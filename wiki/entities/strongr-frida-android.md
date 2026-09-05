---
title: strongR-frida-android
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/CrackerCat__strongR-frida-android.md
updated: 2026-08-26
confidence: medium
---

# strongR-frida-android

Automation setup for building an anti-detection variant of `frida-server` for Android. Tracks upstream Frida releases and applies a sequence of core patches that alter recognizable strings, named pipes, symbols, and protocol behaviors so the resulting server evades common anti-instrumentation fingerprinting. The repository is lightweight and centered on patch workflow rather than a large standalone codebase—aimed at mobile reverse engineering and anti-instrumentation research where standard Frida signatures are blocked. (source: wiki/sources/descriptions/CrackerCat__strongR-frida-android.md)

Related patch/build lanes include [[florida]], [[phantom-frida]], [[morphida]], and hex-replace repacks such as [[fridare]].

## Links

- Repo: https://github.com/CrackerCat/strongR-frida-android

## Related

[[frida]] · [[florida]] · [[phantom-frida]] · [[morphida]] · [[fridare]] · [[florida-zygisk]] · [[antifrida]] · [[frida-detection]] · [[detect-frida]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
