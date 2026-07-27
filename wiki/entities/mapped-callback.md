---
title: MappedCallback
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/nlepleux__MappedCallback.md
updated: 2026-07-27
confidence: medium
---

# MappedCallback

Kernel research sample for **hide callback**: find a codecave in a legitimate loaded module (here the APCI driver, noted as outside [[patchguard]] protection), write a JMP to custom routines, and register the callback so its start address appears inside a valid module—useful for offensive cheat / hide study of [[kernel-callbacks]] surfaces. (source: wiki/sources/descriptions/nlepleux__MappedCallback.md)

Adjacent to general kernel codecave planting such as [[kernel-codecave-poc]] and to callback enum/patch tooling such as [[bustercall]].

## Links

- Repo: https://github.com/nlepleux/MappedCallback

## Related

[[kernel-callbacks]] · [[kernel-codecave-poc]] · [[bustercall]] · [[patchguard]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
