---
title: ModExMap
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/weak1337__ModExMap.md
updated: 2026-07-18
confidence: medium
---

# ModExMap

User-mode DLL injector that **manually maps** a DLL into a target process: parse PE headers, `VirtualAllocEx` + `WriteProcessMemory` for sections, resolve imports, apply relocations, then run the entry point via a shellcode stub on `CreateRemoteThread`. Supports x86/x64, TLS callbacks, and PE structure helpers (`pestruct.h`) for section/import/reloc walks. Useful for studying user-mode manual-map injection and PE loading internals that anti-cheat scanners target. (source: wiki/sources/descriptions/weak1337__ModExMap.md)

README lane: Extend Manual Map.

## Links

- Repo: https://github.com/weak1337/ModExMap

## Related

[[injectors]] · [[skiphook]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
