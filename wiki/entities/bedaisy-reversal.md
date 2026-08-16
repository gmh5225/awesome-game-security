---
title: bedaisy-reversal
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/dllcrt0__bedaisy-reversal.md
updated: 2026-08-16
confidence: medium
---

# bedaisy-reversal

Comprehensive reverse-engineering write-up of BattlEye's kernel-mode anti-cheat driver **`BEDaisy.sys`** (dllcrt0). Educational security research only—documents driver architecture and detection/reporting mechanisms rather than shipping bypass or cheat code. Covers integrity validation, kernel callback enumeration, HAL table verification, and manual-mapped driver detection; object handle protection, filesystem minifilter checks, physical memory scanning, CSRSS integrity validation, graphics component verification, and thread/image notification callbacks—the full scope of BEDaisy kernel-level checks and how findings are reported upstream. Primary audience: anti-cheat researchers mapping BattlEye's kernel driver design. (source: wiki/sources/descriptions/dllcrt0__bedaisy-reversal.md)

Complements [[battleye-re]] (experienceds; IOCTL/API surfaces, anti-DMA, VM obfuscation corpus) with a mechanism-oriented catalog of BEDaisy detection paths. Pairs with offensive samples such as [[bedaisy-bypass]] (report suppression) and [[goodeye]] (APC instrumentation) for end-to-end kernel AC study.

## Links

- Repo: https://github.com/dllcrt0/bedaisy-reversal

## Related

[[battleye]] · [[battleye-re]] · [[bedaisy-bypass]] · [[goodeye]] · [[kernel-callbacks]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
