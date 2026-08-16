---
title: battleye-shellcode
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/dllcrt0__battleye-shellcode.md
updated: 2026-08-16
confidence: medium
---

# battleye-shellcode

Collection of reverse-engineered and decompiled BattlEye **user-mode shellcode modules** (dllcrt0). Documents runtime integrity checks the anti-cheat streams into protected game processes: **AutoHotKey detection**, **Present hook scanning** on the swap chain, and **stack-walking** routines that validate return addresses for suspicious frames. Primary audience: anti-cheat researchers studying BattlEye shellcode-based detection and runtime scanning strategies. README category: `[shellcode]`. (source: wiki/sources/descriptions/dllcrt0__battleye-shellcode.md)

Complements dump-and-reimplement tooling such as [[be-shellcode]], [[be-battleye-shellcode]], and [[battleye-shellcode-dumper]] with decompiled source for specific BE scan stages. Pairs with [[bedaisy-reversal]] (dllcrt0 kernel driver RE) and [[present-hook-detection]] / [[present-hook]] for graphics-path integrity study.

## Links

- Repo: https://github.com/dllcrt0/battleye-shellcode

## Related

[[battleye]] · [[bedaisy-reversal]] · [[be-shellcode]] · [[be-battleye-shellcode]] · [[battleye-shellcode-dumper]] · [[be-shellcode-tester]] · [[present-hook]] · [[present-hook-detection]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
