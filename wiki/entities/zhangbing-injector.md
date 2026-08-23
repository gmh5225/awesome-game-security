---
title: ZhangBing-Injector
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/M3351AN__ZhangBing-Injector.md
updated: 2026-08-23
confidence: medium
---

# ZhangBing-Injector

Windows **DLL injector** from **M3351AN** that uses **vulnerable kernel drivers** to inject into **protected processes**. Bundles multiple `.sys` driver files and ships a C++ user-mode application that communicates with loaded drivers to perform cross-process **memory operations** and **DLL injection**. README credits [[kdmapper]] and notes use of a **WHQL-signed driver** backend. Primarily useful for game-security researchers studying kernel-assisted DLL injection and vulnerable-driver exploitation for process manipulation. (source: wiki/sources/descriptions/M3351AN__ZhangBing-Injector.md)

Sits in the BYOVD-assisted protected-process injection lane beside [[kernelmode-dll-injector]], [[mminject]], [[present-injector]], and [[meme-rw]].

## Links

- Repo: https://github.com/M3351AN/ZhangBing-Injector (README: WHQL-signed driver; credits kdmapper)

## Related

[[kdmapper]] · [[byovd]] · [[kernel-dll-injector]] · [[kernelmode-dll-injector]] · [[mminject]] · [[present-injector]] · [[meme-rw]] · [[injectors]] · [[windows-process-injection]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
