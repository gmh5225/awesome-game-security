---
title: DeathSleep
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/janoglezcampos__DeathSleep.md
updated: 2026-08-03
confidence: medium
---

# DeathSleep

PoC for a sleep/evasion technique that **terminates the current thread** and restores it before resuming execution, applying **page protection changes during the no-execution window**. Extends the maldev sleep-obfuscation lane (page protection flips, optional shellcode encryption) by also hiding the active execution thread from scanners. Aimed at anti-cheat engineers and defensive researchers studying page-protection / memory-integrity detection. (source: wiki/sources/descriptions/janoglezcampos__DeathSleep.md)

Pairs with related sleep/page-protection samples such as [[deepsleep]] (ROP/PIC Gargoyle variant), [[shellcode-fluctuation]] (RW/NoAccess↔RX fluctuation), [[voidmaw]] (`PAGE_GUARD`), and [[no-access-protection]] (`PAGE_NOACCESS` + VEH).

## Links

- Repo: https://github.com/janoglezcampos/DeathSleep

## Related

[[deepsleep]] · [[shellcode-fluctuation]] · [[voidmaw]] · [[no-access-protection]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
