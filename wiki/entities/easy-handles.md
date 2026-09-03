---
title: EasyHandles
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/AlSch092__EasyHandles.md
updated: 2026-09-03
confidence: medium
---

# EasyHandles

**Driver-plus-DLL** technique (AlSch092; C/C++) for obtaining **process handles while bypassing kernel handle callbacks**. A kernel driver uses **`ObOpenPointerToObject`** to open targets without traversing the normal `ObRegisterCallbacks`-filtered handle-creation path; a user-mode **`OpenProcess` hook** forwards requests through **IOCTLs** so tools like debuggers can attach to **callback-protected processes** where conventional handle creation is blocked. Documented **limitations** include **PPL (Protected Process Light)** targets. Primarily for **Windows security research** on anti-cheat or **EDR handle-protection** mechanisms. (source: wiki/sources/descriptions/AlSch092__EasyHandles.md)

README category: Elevating Handle.

## Architecture

| Component | Role |
|-----------|------|
| **Kernel driver** | `ObOpenPointerToObject` path bypassing Ob handle callbacks |
| **User-mode DLL** | Hooks `OpenProcess`; forwards handle requests via IOCTL |
| **Consumer tools** | Debuggers and similar attach workflows on protected targets |

Sits in the offensive **handle-elevation** lane beside [[libelevate]] and [[intraceptor]], opposite defensive **ObRegisterCallbacks** strip policies studied under [[kernel-callbacks]].

## Links

- Repo: https://github.com/AlSch092/EasyHandles

## Related

[[kernel-callbacks]] · [[libelevate]] · [[intraceptor]] · [[van1338]] · [[ultimate-anti-cheat]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
