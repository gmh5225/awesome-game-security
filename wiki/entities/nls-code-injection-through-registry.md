---
title: NlsCodeInjectionThroughRegistry
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__NlsCodeInjectionThroughRegistry.md
updated: 2026-08-11
confidence: medium
---

# NlsCodeInjectionThroughRegistry

PoC demonstrating **code injection and persistence via Windows NLS (National Language Support) registry keys**. The technique modifies NLS-related registry entries to redirect loading of **code-page translation DLLs**, causing a custom DLL to load into processes that initialize the NLS subsystem — early in process startup, before many user-mode injectors run. Aimed at red-team and game-security researchers studying NLS-based injection and persistence tradecraft. (source: wiki/sources/descriptions/gmh5225__NlsCodeInjectionThroughRegistry.md)

Complements early-startup injection via **`AppInit_DLLs`** such as [[appinithook]], broader injection corpora such as [[injection]] and [[windows-process-injection]], and defensive DLL-load monitors in the AC stress-testing lane.

## Links

- Repo: https://github.com/gmh5225/NlsCodeInjectionThroughRegistry

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[appinithook]] · [[injection]] · [[windows-process-injection]] · [[dll-thread-injection-detector]]
