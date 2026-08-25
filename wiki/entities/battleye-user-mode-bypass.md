---
title: BattlEye User-Mode Bypass
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/HadockKali__battleye-user-mode-bypass.md
updated: 2026-08-25
confidence: medium
---

# BattlEye User-Mode Bypass

C++ **Visual Studio** proof-of-concept for a historical **user-mode [[battleye]] bypass** that demonstrates a previously vulnerable loading path. Includes an implanter plus sample DLL workflow that hooks **CreateFileW** and manipulates file checks so a payload masquerades as a trusted module, with example usage for injecting into a target game process and handling exported hook callbacks. Primary use is anti-cheat vulnerability research and study of user-mode trust-validation weaknesses—not a maintained bypass for current BE builds. (source: wiki/sources/descriptions/HadockKali__battleye-user-mode-bypass.md)

Complements Ring-3 BE injection research such as [[splendid-implanter]] and service-layer bypass samples such as [[noeye]]; differs by focusing on **CreateFileW**-mediated file-integrity masquerade during module loading rather than kernel handle maintenance or service emulation.

## Links

- Repo: https://github.com/HadockKali/battleye-user-mode-bypass
- README tag: SetWindowsHookExW

## Related

[[battleye]] · [[splendid-implanter]] · [[noeye]] · [[beclient]] · [[beservice-intcallbacks]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
