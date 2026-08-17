---
title: NtLua
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/can1357__NtLua.md
updated: 2026-08-17
confidence: medium
---

# NtLua

Proof-of-concept for **running Lua 5.4 scripts inside the Windows kernel**. A C/C++ WDK driver embeds a Lua interpreter and exposes NT kernel primitives — **physical and virtual memory access**, **process enumeration**, and **MSR read/write** — to Lua executing at ring 0. A user-mode client sends Lua source for kernel-side evaluation over the driver IOCTL channel. Aimed at kernel researchers and exploit developers studying **scripted kernel introspection** and the security implications of interpreted languages in privileged contexts. (source: wiki/sources/descriptions/can1357__NtLua.md)

Sits in the same dynamic-script / rapid-probe lane as [[pawnio]] (Pawn AMX VM) and [[ntphp]] (PHP in kernel drivers), but uses Lua syntax and a UM script-dispatch model rather than signed bytecode modules or in-driver PHP.

## Links

- Repo: https://github.com/can1357/NtLua

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[pawnio]] · [[ntphp]] · [[hvdetecc]] · [[the-perfect-injector]]
