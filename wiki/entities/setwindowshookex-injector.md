---
title: SetWindowsHookEx-Injector
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__SetWindowsHookEx-Injector.md
updated: 2026-08-10
confidence: medium
---

# SetWindowsHookEx-Injector

C/C++ **SetWindowsHookExW injection-testing** PoC from gmh5225 (README: Injection Testing:SetWindowsHookExW). Demonstrates loading a DLL into a target process via the Windows message-hook API — a classic user-mode injection vector that anti-cheat engineers and defensive researchers use to stress-test hook-based load detection, message-queue monitoring, and module-enumeration coverage. (source: wiki/sources/descriptions/gmh5225__SetWindowsHookEx-Injector.md)

Centers on modding, Unreal Engine, and hooking workflows where SetWindowsHookEx is a common overlay and inject path. Complements the broader [[injection]] corpus, message-hook overlay samples such as [[overlay]], preinjected-DLL SetWindowHookEx research such as [[setwindowhookex]] (ekknod), sibling Skengdo [[simple-setwindowshookexw-injector]] (PE parsing + registry helpers + optional cert spoofing; window-class workflow), and other injection-testing harnesses such as [[injectors]] and [[rust-dll-crab]].

## Links

- Repo: https://github.com/gmh5225/SetWindowsHookEx-Injector

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[injection]] · [[overlay]] · [[injectors]] · [[windows-process-injection]]
