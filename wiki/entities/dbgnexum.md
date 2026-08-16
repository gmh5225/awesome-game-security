---
title: DbgNexum
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/dis0rder0x00__DbgNexum.md
updated: 2026-08-16
confidence: medium
---

# DbgNexum

**Proof-of-concept shellcode injector** that uses the **Windows Debugging API** and **shared memory (file mapping)** to deliver and execute payloads **without** calling `WriteProcessMemory`, `VirtualAllocEx`, or `ReadProcessMemory`. Attaches to the target as a debugger, sets **hardware breakpoints (HWBP)**, and manipulates **thread context registers** to orchestrate a chain of API calls inside the target process that map and run the shellcode. Primarily useful for security researchers studying **advanced injection techniques** that evade EDR detection by avoiding traditional cross-process memory manipulation APIs. (source: wiki/sources/descriptions/dis0rder0x00__DbgNexum.md)

Sits in the Debug API / HWBP injection lane beside broader technique catalogs such as [[windows-process-injection]] and shellcode execution samples such as [[jektor]].

## Links

- Repo: https://github.com/dis0rder0x00/DbgNexum

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[windows-process-injection]] · [[injectors]] · [[jektor]] · [[hintinject]] · [[mmf-code-injection]] · [[veh]]
