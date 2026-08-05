---
title: page_no_access
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/hotline1337__page_no_access.md
updated: 2026-08-05
confidence: medium
---

# page_no_access

C++ modding sample implementing **lazy page protection**: protected pages stay encrypted (or otherwise inaccessible) until their **very first access**, when they are decrypted for execution. README lane: **Anti Cheat → Page Protection**; aimed at anti-cheat engineers and defensive security researchers studying on-demand page decrypt / memory-integrity evasion patterns. (source: wiki/sources/descriptions/hotline1337__page_no_access.md)

Contrasts with VEH + `PAGE_NOACCESS` trampoline samples such as [[no-access-protection]] and [[bincon]], and with cyclic RW/NoAccess↔RX fluctuation PoCs such as [[shellcode-fluctuation]] — here decryption is tied to first touch rather than exception-driven re-protect or periodic permission flips.

## Links

- Repo: https://github.com/hotline1337/page_no_access

## Related

[[no-access-protection]] · [[bincon]] · [[voidmaw]] · [[shellcode-fluctuation]] · [[count-hook]] · [[umium]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
