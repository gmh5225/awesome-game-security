---
title: Wizard-Loader
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__Wizard-Loader.md
updated: 2026-08-09
confidence: medium
---

# Wizard-Loader

Windows **PE loader/injector** that **manually maps** DLLs into target processes with anti-detection measures: PE section mapping, import resolution, relocation fixups, TLS callbacks, and exception-handler registration, plus **PE header erasure** and **thread hiding** to evade anti-cheat scanners. README lane abuses **Xwizard.exe** for **DLL side-loading**—a signed Microsoft binary used as a load host rather than direct remote injection. Aimed at kernel and game-security researchers studying advanced DLL loading and injection-detection evasion. (source: wiki/sources/descriptions/gmh5225__Wizard-Loader.md)

## Links

- Repo: https://github.com/gmh5225/Wizard-Loader

## Related

[[modexmap]] · [[shtreeba]] · [[guided-hacking-injector]] · [[windows-dll-hijacking]] · [[faultline]] · [[system-thread-finder]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
