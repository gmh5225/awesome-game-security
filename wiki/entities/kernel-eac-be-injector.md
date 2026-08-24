---
title: kernel-eac-be-injector
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/JGonz1337__kernel-eac-be-injector.md
updated: 2026-08-24
confidence: medium
---

# kernel-eac-be-injector

**Kernel-assisted manual mapper** for injecting a DLL into a target game process (JGonz1337). A **kernel hook-based command handler** pairs with a **user-mode mapper** that performs relocation, import resolution, section writing, and remote `DllMain` execution. The kernel component includes memory allocation and exposure routines, pointer-swap hooks, and cleanup steps for mapped payloads. Primarily intended for advanced research into **anti-cheat-resistant injection workflows** on Windows under [[easy-anti-cheat]] and [[battleye]]-protected titles—not a maintained bypass product. (source: wiki/sources/descriptions/JGonz1337__kernel-eac-be-injector.md)

README lane: PTE.User.

## Links

- Repo: https://github.com/JGonz1337/kernel-eac-be-injector

## Related

[[kernelmode-dll-injector]] · [[face-injector-v2]] · [[stealthy-kernelmode-injector]] · [[memmap]] · [[eac-injector-driver]] · [[simple-manual-map-injector]] · [[easy-anti-cheat]] · [[battleye]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
