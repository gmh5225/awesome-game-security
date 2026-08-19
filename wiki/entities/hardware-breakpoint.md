---
title: hardware-breakpoint
kind: entity
topics: [mobile-security, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/Ylarod__hardware-breakpoint.md
updated: 2026-08-19
confidence: medium
---

# hardware-breakpoint

ARM64 **Linux kernel** project (Ylarod) that implements configurable **hardware breakpoints (HWBP)** through exported kernel APIs and **proc** interfaces. Supports adding and removing execution or watch breakpoints by symbol or address, listing active breakpoints, and collecting trigger statistics. Includes utilities to resolve symbol values and map physical I/O addresses to related virtual mappings. Primary use case: kernel-level debugging and security research on **Android or embedded** systems that need fine-grained runtime monitoring. (source: wiki/sources/descriptions/Ylarod__hardware-breakpoint.md)

Complements usermode Linux/Android HWBP process-watch tooling such as [[pwatch]] and [[pwatch-c]], and the broader ARM64 kernel memory/HWBP suite [[rw-proc-mem33]].

## Links

- Repo: https://github.com/Ylarod/hardware-breakpoint

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[pwatch]] · [[pwatch-c]] · [[rw-proc-mem33]] · [[rwmem]] · [[ida-android-breakpoint]] · [[florida-zygisk]]
