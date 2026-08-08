---
title: ntminhook
kind: entity
topics: [game-hacking, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__ntminhook.md
updated: 2026-08-08
confidence: medium
---

# ntminhook

Modified **MinHook** fork that depends **only on the Windows Native API** (`NTDLL`-level interfaces), without higher-level Win32 imports. Written in C/C++; centers on asset pipelines, modding, and inline hooking for game-security researchers and reverse engineers studying offensive user-mode hook/trampoline techniques in the cheat / hook lane. (source: wiki/sources/descriptions/gmh5225__ntminhook.md)

Mirrors the NTDLL-only adaptation pattern of [[detoursnt]] beside standard MinHook consumers such as [[appinithook]], [[dwmhook]], and [[holodori-kernel-bypass]].

## Links

- Repo: https://github.com/gmh5225/ntminhook

## Related

[[detoursnt]] · [[polyhook-2-0]] · [[subhook]] · [[appinithook]] · [[skiphook]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
