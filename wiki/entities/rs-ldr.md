---
title: rs-ldr
kind: entity
topics: [windows-kernel, reverse-engineering, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/alfarom256__rs-ldr.md
updated: 2026-08-18
confidence: medium
---

# rs-ldr

Rust **no_std** library for **hash-based dynamic WinAPI resolution** on Windows x86_64 without an import table, visible API strings, or a **kernel32** dependency for loading. Walks the **PEB** to locate loaded modules by hashed name, parses export directories (including forwarded exports), and can load DLLs via ntdll **`LdrLoadDll`** through a **DynApi** interface. Compile-time **XOR string obfuscation** macros decode to stack buffers that zero themselves on drop to evade static string and signature scanning. Optional features include a pluggable **syscall SSN resolver** (with a **DirectResolver** reference for Hell's Gate-style techniques), a process-wide DynApi behind a spinlock, per-build salted **djb2** hashes, and pure-Rust memory intrinsics for **NODEFAULTLIB** builds. Targets no_std Windows red-team, reverse-engineering, and game-security tooling that needs stealthy API resolution. (source: wiki/sources/descriptions/alfarom256__rs-ldr.md)

Complements C PIC shellcode frameworks such as [[tabby]] (FNV-1a PEB/EAT + indirect syscalls), C++ lazy-import libraries such as [[blitz]] / [[kli]], compile-time string crypters such as [[crystr]], and syscall stub libraries such as [[syscalls-cpp]] / [[inline-syscall]]. Defensive counterpart: [[syscall-detect]] flags custom syscall stubs vs ntdll.

## Links

- Repo: https://github.com/alfarom256/rs-ldr

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[tabby]] · [[blitz]] · [[crystr]] · [[syscalls-cpp]] · [[syscall-detect]] · [[windows-process-injection]]
