---
title: ShellcodeFluctuation
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mgeeky__ShellcodeFluctuation.md
updated: 2026-07-30
confidence: medium
---

# ShellcodeFluctuation

PoC for **shellcode fluctuation** — an in-memory evasion technique that cyclically encrypts and decrypts shellcode contents so pages alternate between **RW** (or **NoAccess**) and **RX** protection. Demystifies commercial-framework “magic” against memory scanners that flag persistent executable private regions. Aimed at anti-cheat engineers and defensive researchers studying page-protection / memory-integrity detection. (source: wiki/sources/descriptions/mgeeky__ShellcodeFluctuation.md)

Pairs with related page-protection samples such as [[deepsleep]] (ROP/PIC sleep-hide), [[death-sleep]] (thread terminate/restore sleep obfuscation), [[voidmaw]] (`PAGE_GUARD`), and [[no-access-protection]] (`PAGE_NOACCESS` + VEH). Same-author in-memory evasion PoC: [[thread-stack-spoofer]] (call-stack spoofing).

## Links

- Repo: https://github.com/mgeeky/ShellcodeFluctuation

## Related

[[deepsleep]] · [[death-sleep]] · [[voidmaw]] · [[no-access-protection]] · [[thread-stack-spoofer]] · [[scfw]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
