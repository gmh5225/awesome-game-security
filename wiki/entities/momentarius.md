---
title: momentarius
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/staturnzz__momentarius.md
updated: 2026-08-18
confidence: medium
---

# momentarius

C library that bypasses Apple's **Page Protection Layer (PPL)** on A12 and A13 Apple Silicon devices by exploiting **IOMobileFramebuffer** GPU firmware. Maps physical memory through **IOSurface**, manipulates ARM64 page tables and PTEs, injects AArch64 shellcode into GPU firmware, and hooks kernel register reads to gain controlled kernel read/write primitives. Separate initialization paths target A12 (Vortex/Tempest) and A13 (Lightning/Thunder) CPU families via IOMFB suspend/resume and patchfinding against GPU binary signatures. Intended for iOS kernel security researchers and exploit developers studying PPL bypass and low-level Apple platform protections. (source: wiki/sources/descriptions/staturnzz__momentarius.md)

Complements static PPL gate-call tracing via [[pplorer]] (kernelcache IDA) and historical `tfp0` study via [[oob-entry]] from the same author—this project delivers runtime PPL bypass and kernel R/W on A12/A13 hardware rather than RE annotation or legacy jailbreak primitives alone.

## Links

- Repo: https://github.com/staturnzz/momentarius

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[pplorer]] · [[oob-entry]] · [[dopamine]] · [[xnu-1day-practice]]
