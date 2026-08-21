---
title: DoomSyscalls
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/SilentisVox__DoomSyscalls.md
updated: 2026-08-21
confidence: medium
---

# DoomSyscalls

Windows x64 **indirect syscall** technique that resolves **syscall numbers (SSN)** and the **`syscall` instruction site** at runtime from `ntdll`, then invokes via inline assembly to bypass user-mode API hooks. Adds **return-address spoofing** through `ntdll` gadgets so call-stack / RIP-return telemetry sees plausible module frames rather than cheat stubs — userland hook and RIP-return evasion research. (source: wiki/sources/descriptions/SilentisVox__DoomSyscalls.md)

Complements compile-time direct-syscall libraries such as [[syscalls-cpp]] and [[inline-syscall]], PIC indirect-syscall shellcode such as [[tabby]], Tartarus' Gate injectors such as [[tartarus-tp-alloc-inject]], and syscall-origin detectors such as [[syscall-detect]]. Return-path spoofing overlaps [[callstackspoofer]] and the [[stack-spoofing]] concept.

## Links

- Repo: https://github.com/SilentisVox/DoomSyscalls

## Related

[[syscalls-cpp]] · [[inline-syscall]] · [[syscall-detect]] · [[tabby]] · [[tartarus-tp-alloc-inject]] · [[callstackspoofer]] · [[stack-spoofing]] · [[rs-ldr]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
