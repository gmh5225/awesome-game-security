---
title: AppInitHook
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/mrexodia__AppInitHook.md
updated: 2026-07-29
confidence: medium
---

# AppInitHook

Windows **DLL injection and API hooking framework** that loads custom modules via the **`AppInit_DLLs` registry** mechanism at process startup. A dispatcher DLL reads an INI configuration to select process-specific modules; a **HookDll** helper wraps **MinHook** with macros for hooking exported APIs or process entry points. Built with C/C++, **CMake**, and **cmkr** for MSVC; ships example modules for process control and behavior tweaks. Aimed at reverse engineers and developers who need early, configurable process injection and hooking for debugging, research, or game-security work. (source: wiki/sources/descriptions/mrexodia__AppInitHook.md)

Contrasts with runtime injectors such as [[windows-process-injection]], [[modexmap]], and [[tartarus-tp-alloc-inject]]; hook libraries such as [[polyhook-2-0]] and [[detoursnt]]; and AC stress harnesses such as [[injectors]].

## Links

- Repo: https://github.com/mrexodia/AppInitHook

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[windows-process-injection]] · [[injectors]] · [[polyhook-2-0]] · [[detoursnt]] · [[skiphook]]
