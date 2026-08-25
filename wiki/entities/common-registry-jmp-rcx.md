---
title: Common-Registry-Jmp-RCX
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__Common-Registry-Jmp-RCX.md
updated: 2026-08-14
confidence: medium
---

# Common-Registry-Jmp-RCX

Kernel-mode communication research sample that registers a **`CmRegisterCallback`** registry callback whose routine address resolves to a **`JMP RCX`** gadget found in **`nvraid.sys`**, hijacking the registry-callback dispatch path to redirect execution to a custom handler for covert Ring0↔Ring3 I/O without a conventional IOCTL device surface. (source: wiki/sources/descriptions/gmh5225__Common-Registry-Jmp-RCX.md)

Sits in the same stealth driver-communication and [[kernel-callbacks]] lane as [[boundcallback]], [[mapped-callback]], and [[evcommunication]].

## Links

- Repo: https://github.com/gmh5225/Common-Registry-Jmp-RCX

## Related

[[kernel-callbacks]] · [[common-registry]] · [[boundcallback]] · [[mapped-callback]] · [[evcommunication]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
