---
title: x86RetSpoof
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/danielkrupinski__x86RetSpoof.md
updated: 2026-08-16
confidence: medium
---

# x86RetSpoof

**x86RetSpoof** is a **header-only C++ library** for **32-bit (x86) Windows** that invokes functions with a **spoofed return address** by routing calls through a **`JMP DWORD PTR [EBX]`** gadget located in a target module's code section. Supports **stdcall, cdecl, fastcall, and thiscall** calling conventions so the callee sees the gadget address as its return address instead of the true caller—useful for game-security researchers studying **return-address spoofing** used to evade call-stack analysis. (source: wiki/sources/descriptions/danielkrupinski__x86RetSpoof.md)

Sits in the `Cheat > Spoof Stack` lane beside x64 trampoline implementations such as [[callstackspoofer-2]], reusable libraries such as [[spoof-stack-safecall]], and illustrative samples such as [[return-address-spoofer]].

## Links

- Repo: https://github.com/danielkrupinski/x86RetSpoof

## Related

[[stack-spoofing]] · [[callstackspoofer-2]] · [[spoof-stack-safecall]] · [[return-address-spoofer]] · [[proxy-api-call]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
