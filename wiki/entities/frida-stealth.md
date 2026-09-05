---
title: frida-stealth
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/AsenOsen__frida-stealth.md
updated: 2026-09-01
confidence: medium
---

# frida-stealth

Patch set that modifies Frida to reduce common runtime detection fingerprints on Android targets. The patches alter identifying traits such as default ports, socket names, thread names, loop labels, and related Frida markers in `frida-core` and `frida-gum`. The repository provides patch files and build instructions for producing custom instrumented binaries—aimed at mobile reverse engineering and anti-instrumentation bypass research where stock Frida signatures are blocked. (source: wiki/sources/descriptions/AsenOsen__frida-stealth.md)

Related Android anti-detection build lanes include [[strongr-frida-android]], [[florida]], [[phantom-frida]], [[morphida]], and hex-replace repacks such as [[fridare]].

## Links

- Repo: https://github.com/AsenOsen/frida-stealth

## Related

[[frida]] · [[strongr-frida-android]] · [[florida]] · [[phantom-frida]] · [[morphida]] · [[fridare]] · [[antifrida]] · [[frida-detection]] · [[detect-frida]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
