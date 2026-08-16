---
title: DetectFrida
kind: entity
topics: [anti-cheat, mobile-security]
sources:
  - wiki/sources/descriptions/darvincisec__DetectFrida.md
updated: 2026-08-16
confidence: medium
---

# DetectFrida

Android native library under Anti Cheat → Detection:Frida that implements multiple [[frida]] presence checks and native anti-instrumentation hardening. Detection paths include named-pipe scanning, Frida-specific thread-name probes, and `.text` section integrity comparison between in-memory mappings and on-disk ELF images. The sample also demonstrates defensive native hardening—syscall-based libc replacement, custom string/memory helpers, and O-LLVM obfuscation—to resist hooking and tampering. Useful for mobile game security engineers studying anti-instrumentation and native code hardening on Android. (source: wiki/sources/descriptions/darvincisec__DetectFrida.md)

## Links

- Repo: https://github.com/darvincisec/DetectFrida

## Related

[[frida]] · [[antifrida]] · [[frida-detection]] · [[mobile-anti-cheat]] · [[droidshield]] · [[overviews/mobile-security]] · [[overviews/anti-cheat]]
