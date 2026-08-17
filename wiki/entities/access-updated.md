---
title: access-updated
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/bromoket__access_updated.md
updated: 2026-08-17
confidence: medium
---

# access-updated

**access_updated** (bromoket/access_updated) is an updated fork of [[access]] (btbd/access) that provides **handle-free kernel-mode process operations** by hooking the **`xKdEnumerateDebuggingDevices`** pointer for kernel–usermode communication. It replaces hardcoded offsets with **Zydis-based dynamic pattern finding** for runtime discovery of kernel functions, supporting **Windows 10 (1607+) through Windows 11 (24H2)** in a single binary. The kernel driver performs **`PROCESS_ALL_ACCESS`** operations without creating real handles, using a clean **`.data` section hook** with no inline patches. Aimed at kernel security researchers studying handleless process access, syscall hooking, and version-independent Windows kernel techniques. (source: wiki/sources/descriptions/bromoket__access_updated.md)

Extends the upstream BTBD [[access]] lane with Zydis pattern scanning for cross-build compatibility. Contrasts with handle-based elevation such as [[libelevate]] and usermode NT-call redirection such as [[intraceptor]]. Shares the BTBD research ecosystem with [[umap]], [[smap]], [[modmap]], and [[wpp]].

## Links

- Repo: https://github.com/bromoket/access_updated

## Related

[[access]] · [[intraceptor]] · [[libelevate]] · [[kernel-callbacks]] · [[umap]] · [[wpp]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
