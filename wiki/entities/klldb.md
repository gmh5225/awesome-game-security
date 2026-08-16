---
title: kLLDB
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/djolertrk__kLLDB.md
updated: 2026-08-16
confidence: medium
---

# kLLDB

LLDB-based **Linux kernel debugger** built on LLVM-19 infrastructure. Custom LLDB plugins plus Python scripting support both live attach and offline post-mortem workflows — an LLDB-native alternative to traditional GDB-based Linux kernel debugging. (source: wiki/sources/descriptions/djolertrk__kLLDB.md)

**kLLDBLive** handles running-kernel sessions; a separate offline plugin supports crash-dump analysis with automated bug-reporting scripts. Primarily aimed at kernel developers and security researchers stepping through Linux kernel internals with LLDB tooling rather than KGDB/GDB stacks.

## Links

- Repo: https://github.com/djolertrk/kLLDB (README tag: LLDB based debugger for Linux Kernel)

## Related

[[kernel-development]] · [[vmlinux-to-elf]] · [[ida-kallsyms-symbol-renamer]] · [[venom]] · [[modreveal]] · [[kernel-hack]] · [[lldbext-dump]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
