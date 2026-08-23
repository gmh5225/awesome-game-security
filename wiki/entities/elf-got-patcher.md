---
title: elf-got-patcher
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/LeoChen-CoreMind__elf-got-patcher.md
updated: 2026-08-23
confidence: medium
---

# elf-got-patcher

**elf-got-patcher** (LeoChen-CoreMind) is an **ARM64 ELF static GOT hook patcher** for **Android native binaries**. It patches **Global Offset Table (GOT)** entries to redirect dynamic function calls, injecting custom shellcode via **code-cave** placement. Techniques include **`.init_array` RELA hijack** and **config-driven ASLR-safe patching** so hooks survive address-space layout randomization when applied offline. Targets hooking shared-library imports in ARM/ARM64 `.so` modules without runtime injectors. (source: wiki/sources/descriptions/LeoChen-CoreMind__elf-got-patcher.md)

Static/offline GOT redirection lane — complements runtime PLT/GOT hook libraries such as [[plthook]] and Python ARM inline patchers such as [[pyasm-patch]].

## Links

- Repo: https://github.com/LeoChen-CoreMind/elf-got-patcher

## Related

[[plthook]] · [[pyasm-patch]] · [[rel-fuscate]] · [[and64-inline-hook]] · [[dobby]] · [[adbi]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
