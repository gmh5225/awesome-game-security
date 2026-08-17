---
title: ThePerfectInjector
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/can1357__ThePerfectInjector.md
updated: 2026-08-17
confidence: medium
---

# ThePerfectInjector

Windows **DLL injector** in C++ that combines **`NtCreateThreadEx`** with a **thread-safe, position-independent shellcode stub** that resolves **`LdrLoadDll`** at runtime. The injector allocates PIC shellcode in the target process and starts a remote thread to load the payload DLL **without relying on `kernel32.LoadLibrary` at a fixed address**. Handles edge cases such as **WoW64 injection** and **process-creation flags**. Aimed at security researchers studying advanced DLL injection tradecraft and **anti-cheat evasion**. (source: wiki/sources/descriptions/can1357__ThePerfectInjector.md)

Contrasts with broader injection catalogs such as [[windows-process-injection]], `NtCreateThreadEx` training injectors such as [[guided-hacking-injector]], and TpAllocInject loaders such as [[tartarus-tp-alloc-inject]].

## Links

- Repo: https://github.com/can1357/ThePerfectInjector

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[windows-process-injection]] · [[guided-hacking-injector]] · [[tartarus-tp-alloc-inject]] · [[injectors]] · [[jektor]]
