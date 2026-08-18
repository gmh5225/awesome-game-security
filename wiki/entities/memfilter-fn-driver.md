---
title: memfilter-fn-driver
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/zensenzay__memfilter-fn-driver-.md
updated: 2026-08-18
confidence: medium
---

# memfilter-fn-driver

**MemFilter** is a Windows kernel minifilter driver with a C++ user-mode client aimed at game security research, anti-cheat evasion, and kernel-level reverse engineering. It combines stealth and cross-process memory access for protected processes. (source: wiki/sources/descriptions/zensenzay__memfilter-fn-driver-.md)

The driver uses the Filter Manager framework to hide files and directories by scrubbing directory-query buffers, `CmRegisterCallback` to hide registry keys, and Object Manager callbacks to strip virtual-memory read and write access from handles targeting protected processes. Cross-process memory read and write use MDL mapping. User-mode communication goes through a Filter Manager port (`FltCreateCommunicationPort`) rather than a conventional device object or IOCTL interface. Demo code targets live game process memory inspection.

Sits in the cheat / hide + RPM lane beside offensive file-hide samples such as [[hide-file]], defensive minifilter references such as [[vaultguard]], AC minifilter IPC probes such as [[neacsafe-analysis]], and other zensenzay kernel research such as [[eac-spoofer-meme]].

## Links

- Repo: https://github.com/zensenzay/memfilter-fn-driver-

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[kernel-callbacks]] · [[hide-file]] · [[vaultguard]] · [[neacsafe-analysis]] · [[eac-spoofer-meme]] · [[ntmemory]]
