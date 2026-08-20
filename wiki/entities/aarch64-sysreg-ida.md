---
title: aarch64-sysreg-ida
kind: entity
topics: [reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/TrungNguyen1909__aarch64-sysreg-ida.md
updated: 2026-08-20
confidence: medium
---

# aarch64-sysreg-ida

IDA Pro plugin (**A IDA plugin to show ARM MSRs nicely**; TrungNguyen1909; cheat / IDA Plugins) that improves AArch64 system-register readability during disassembly. Python-based; hooks instruction display paths so cryptic **MSR** and **SYS** encodings render as meaningful register names. Ships with an embedded **ARMv8** register database and can load extra **Apple** register definitions from an external JSON file. Primary use case: **ARM OS and kernel reverse engineering**, where fast register interpretation is essential. (source: wiki/sources/descriptions/TrungNguyen1909__aarch64-sysreg-ida.md)

Complements Linux kernel symbol import via [[ida-kallsyms-symbol-renamer]] and [[import-kallsyms]], iOS kernelcache tooling such as [[ida-kernelcache-ng]] and [[ida-kcpp]], and standalone AArch64 decode via [[farm64]]—verify decoded register names against ARM architecture references per [[research-rigor]].

## Links

- Repo: https://github.com/TrungNguyen1909/aarch64-sysreg-ida

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[ida-kallsyms-symbol-renamer]] · [[import-kallsyms]] · [[ida-kernelcache-ng]] · [[ida-kcpp]] · [[farm64]] · [[list-of-ida-plugins]] · [[research-rigor]]
