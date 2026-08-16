---
title: SetWindowHookEx (ekknod)
kind: entity
topics: [game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/ekknod__SetWindowHookEx.md
updated: 2026-08-16
confidence: medium
---

# SetWindowHookEx (ekknod)

**SetWindowHookEx** is offensive research focused on using **`SetWindowHookEx`** to load **preinjected DLLs** into target processes. It is written in **C** and centers on **hooking** for low-level Windows researchers working in the **Some Tricks / Windows Ring3** lane — the classic user-mode message-hook path that anti-cheat and modding engineers study beside conventional injectors and overlay hooks. (source: wiki/sources/descriptions/ekknod__SetWindowHookEx.md)

Complements injection-testing PoCs such as [[setwindowshookex-injector]], message-hook overlay samples such as [[overlay]], and broader [[injection]] / [[windows-process-injection]] corpora for AC stress evaluation of hook-based DLL load coverage.

## Links

- Repo: https://github.com/ekknod/SetWindowHookEx

## Related

[[setwindowshookex-injector]] · [[overlay]] · [[injection]] · [[present-hook]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
