---
title: KeUserModeCallBack
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/ExpLife0011__KeUserModeCallBack.md
updated: 2026-08-25
confidence: medium
---

# KeUserModeCallBack

**KeUserModeCallBack** (ExpLife0011) is a **Windows kernel demo** that invokes **user-mode routines through `KeUserModeCallback`**. The driver exposes a **device interface**, receives **IOCTL** requests, and prepares **callback arguments and shellcode stubs** for both **32-bit and 64-bit** paths. It walks process structures such as the **PEB** and **module export tables** to resolve **user32** and **MessageBoxA** before dispatching the callback. Intended for **kernel-to-user transition research** and understanding **callback-based code execution primitives** in the win32k GUI-subsystem lane. Listed under cheat / driver development with README tag `[KeUserModeCallBack]`. (source: wiki/sources/descriptions/ExpLife0011__KeUserModeCallBack.md)

Complements in-cheat **KeUserModeCallBack** notes such as those in [[eft]] (`usercallback.h` on Win10) with a **standalone driver scaffold** focused on the transition primitive rather than game-specific memory manipulation.

## Links

- Repo: https://github.com/ExpLife0011/KeUserModeCallBack

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[eft]] · [[ntcomparesigninglevel-hook]] · [[km-um-communication]] · [[win32khooker]]
