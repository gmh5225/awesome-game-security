---
title: uwpinject
kind: entity
topics: [game-hacking, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/Francesco149__uwpinject.md
updated: 2026-08-25
confidence: medium
---

# uwpinject

**Command-line injector** for launching **UWP applications** and injecting **DLLs at a very early startup stage**. Implemented in **C** with **Win32** and **AppModel APIs**, using a **debugger-like suspended launch flow** to gain early process control before the app fully initializes. Includes build and environment scripts for Windows toolchains and a straightforward **DLL drop-in workflow**. Primary use cases: **UWP reverse engineering**, **runtime instrumentation**, and **debugging support** for Microsoft Store / WinRT titles. (source: wiki/sources/descriptions/Francesco149__uwpinject.md)

README lane: Explore UWP (dll injector for uwp apps).

## Links

- Repo: https://github.com/Francesco149/uwpinject

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[uwpspy]] · [[uwp-dumper]] · [[windows-process-injection]]
