---
title: GH Injector Library
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Broihon__GH-Injector-Library.md
updated: 2026-08-30
confidence: medium
---

# GH Injector Library

Feature-rich **Windows DLL injection library** (Broihon) for **x86, x64, and WOW64** targets. Written in C++, it implements multiple loading strategies—including several **Ldr-based** paths and **manual mapping**—plus many shellcode execution methods: **NtCreateThreadEx**, **APC**, **thread hijacking**, **SetWindowsHookEx**, and **kernel callback** techniques. Additional components for **cloaking**, **hook handling**, and **.NET assembly loading** make it useful for advanced game-hacking workflows and anti-cheat behavior research. (source: wiki/sources/descriptions/Broihon__GH-Injector-Library.md)

README lane: **inject library and tool**.

Complements Guided Hacking tooling such as [[guided-hacking-injector]], [[gh-offset-dumper]], and [[gh-d3d11-hook]], memory libraries such as [[blackbone]], educational technique samples such as [[inject-all-the-things]], and broader injection corpora such as [[windows-process-injection]].

## Links

- Repo: https://github.com/Broihon/GH-Injector-Library

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[guided-hacking-injector]] · [[blackbone]] · [[inject-all-the-things]] · [[windows-process-injection]] · [[process-injection-techniques]] · [[injectors]]
