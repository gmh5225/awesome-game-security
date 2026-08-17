---
title: access
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/btbd__access.md
updated: 2026-08-17
confidence: medium
---

# access

**access** (btbd/access) is a **kernel-mode syscall wrapper** that grants **PROCESS_ALL_ACCESS** operations on protected processes **without creating real handles**. It hooks a syscall via **`.data` section modification** in the kernel and ships a **user-mode DLL wrapper** that transparently redirects privileged operations through the driver. The implementation avoids structured exception handling (SEH) while still performing safe operations, and was tested against protected game processes such as Fortnite. Aimed at researchers studying handleless kernel-mode process access and syscall-hooking techniques for bypassing process protection. (source: wiki/sources/descriptions/btbd__access.md)

Contrasts with handle-based elevation such as [[libelevate]] and usermode NT-call redirection such as [[intraceptor]]. Shares the BTBD research lane with [[umap]], [[smap]], [[modmap]], and [[wpp]].

## Links

- Repo: https://github.com/btbd/access

## Related

[[intraceptor]] · [[libelevate]] · [[kernel-callbacks]] · [[umap]] · [[wpp]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
