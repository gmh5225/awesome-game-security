---
title: Windows-DLL-Injector
kind: entity
topics: [game-hacking, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/KooroshRZ__Windows-DLL-Injector.md
updated: 2026-08-23
confidence: medium
---

# Windows-DLL-Injector

C++ **Visual Studio** sample suite demonstrating multiple **Windows DLL injection** techniques for **32-bit and 64-bit** targets (KooroshRZ). Methods include **CreateRemoteThread**, native thread-creation variants, **QueueUserAPC**, **SetWindowsHookEx**, and **RtlCreateUserThread**. The repo splits **injector** and **payload DLL** projects so each technique can be exercised independently. The write-up emphasizes practical trade-offs among implementation simplicity, process compatibility, and detection surface — aimed at process-injection research and low-level Windows API experimentation. (source: wiki/sources/descriptions/KooroshRZ__Windows-DLL-Injector.md)

README lane: **Injection Testing** — multi-method user-mode DLL load study sample.

Complements broader injection corpora such as [[windows-process-injection]], focused PoCs such as [[thread-hijacking-injector]] and [[simple-setwindowshookexw-injector]], and multi-method injectors such as [[guided-hacking-injector]] and [[rust-dll-crab]].

## Links

- Repo: https://github.com/KooroshRZ/Windows-DLL-Injector

## Related

[[overviews/game-hacking]] · [[windows-process-injection]] · [[injectors]] · [[thread-hijacking-injector]] · [[simple-setwindowshookexw-injector]] · [[guided-hacking-injector]] · [[rust-dll-crab]] · [[process-injection-techniques]]
