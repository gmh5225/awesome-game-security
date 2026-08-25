---
title: zam64-zemina
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__zam64-zemina.md
updated: 2026-08-07
confidence: medium
---

# zam64-zemina

BYOVD research PoC targeting Zemana anti-malware **`zam64.sys`**. The signed driver’s IOCTL interface exposes process termination and cross-process memory access—typical primitives for killing security/AC processes from an unprivileged client. Useful for studying how third-party security-product drivers become LOLdriver targets in game-security and kernel RE work. (source: wiki/sources/descriptions/gmh5225__zam64-zemina.md)

## Links

- Repo: https://github.com/gmh5225/zam64-zemina

## Related

[[byovd]] · [[terminator]] · [[edr-xdr-av-killer]] · [[ven0m-ransomware]] · [[av-edr-killer]] · [[watchdog-killer]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
