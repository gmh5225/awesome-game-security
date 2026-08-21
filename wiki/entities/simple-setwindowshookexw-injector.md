---
title: simple-SetWindowsHookExW-injector
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Skengdo__simple-SetWindowsHookExW-injector.md
updated: 2026-08-21
confidence: medium
---

# simple-SetWindowsHookExW-injector

C++ **SetWindowsHookExW** DLL injector from Skengdo (README: Injection Testing:SetWindowsHookExW). Workflow: select a payload DLL, set a target **window class**, and run against the chosen process. Includes portable-executable parsing helpers, registry-related utilities, and optional **certificate spoofing** workflows — aimed at learning and testing user-mode injection pipelines in game-security research. (source: wiki/sources/descriptions/Skengdo__simple-SetWindowsHookExW-injector.md)

Complements other SetWindowsHookExW injection-testing PoCs such as [[setwindowshookex-injector]], preinjected-DLL message-hook research such as [[setwindowhookex]] (ekknod), and broader [[injection]] / [[windows-process-injection]] corpora for AC stress evaluation of hook-based DLL load coverage.

## Links

- Repo: https://github.com/Skengdo/simple-SetWindowsHookExW-injector

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[setwindowshookex-injector]] · [[setwindowhookex]] · [[injection]] · [[overlay]] · [[injectors]] · [[windows-process-injection]]
