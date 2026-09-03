---
title: Zygisk_mod
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Admirepowered__Zygisk_mod.md
updated: 2026-09-03
confidence: medium
---

# Zygisk_mod

**Zygisk_mod** is a standalone implementation of the **Zygisk runtime interface** for rooted Android environments. It targets compatibility across **KernelSU**, **APatch**, and **Magisk** setups, offering an alternative module-loading path when built-in or closed Zygisk implementations are unavailable. The codebase uses Android build tooling with **Kotlin** and native components to provide API-level behavior expected by Zygisk modules. Primary audience: Android security and modding researchers who need flexible process injection and module experimentation on rooted devices. (source: wiki/sources/descriptions/Admirepowered__Zygisk_mod.md)

Sits beside other transparent Zygisk API runtimes such as [[rezygisk]] and [[zygisk-on-kernelsu]] and enables [[zygisk]] module ecosystems without relying on Magisk-bundled Zygisk alone.

## Links

- Repo: https://github.com/Admirepowered/Zygisk_mod (Standalone implementation of Zygisk)

## Related

[[zygisk]] · [[magisk]] · [[kernelsu]] · [[apatch]] · [[rezygisk]] · [[zygisk-on-kernelsu]] · [[zamr]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
