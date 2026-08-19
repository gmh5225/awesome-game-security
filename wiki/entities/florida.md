---
title: Florida
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/Ylarod__Florida.md
updated: 2026-08-19
confidence: medium
---

# Florida

Automation project that patches upstream Frida and builds an anti-detection variant of `frida-server` for Android. Patch sets modify recognizable Frida strings, symbols, and artifact naming to reduce straightforward detection signatures; scripted workflows apply patches and reproduce builds around Frida core components. Targets mobile reverse-engineering research where analysts test anti-instrumentation and anti-detection techniques against apps and mobile anti-cheat checks. (source: wiki/sources/descriptions/Ylarod__Florida.md)

Downstream packaging includes boot-persistent Magisk/KernelSU modules such as [[florida-zygisk]] that ship Ylarod-patched Florida binaries. Hex-replace repacks such as [[fridare]] sit in the same stealth Frida lane with a different patching approach.

## Links

- Repo: https://github.com/Ylarod/Florida (anti-detection version of frida-server)

## Related

[[frida]] · [[fridare]] · [[florida-zygisk]] · [[antifrida]] · [[frida-detection]] · [[detect-frida]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
