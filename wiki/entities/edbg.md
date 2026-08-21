---
title: eDBG
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Sh11no__eDBG.md
updated: 2026-08-21
confidence: medium
---

# eDBG

Lightweight **command-line debugger** for **Android ARM64** built on **eBPF** rather than traditional **ptrace** attachment. Implemented mainly in **Go** with supporting **C** and eBPF components. Provides a **GDB-like** interactive workflow with breakpoint, memory, register, and thread inspection commands. Its **file-plus-offset breakpoint** model is designed for fast startup and stronger resistance to anti-debug interference in protected apps. Targets mobile reverse engineering and game security analysis on **rooted devices** with modern kernels. (source: wiki/sources/descriptions/Sh11no__eDBG.md)

Sits in the Android eBPF dynamic-analysis lane beside syscall/trace corpora such as [[android-ebpf]], debugger servers such as [[edbgserver]], uprobe hook frameworks such as [[ehook]], and complements user-mode DBI such as [[frida]] when kernel eBPF attach is available without ptrace.

## Links

- Repo: https://github.com/Sh11no/eDBG

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[android-ebpf]] · [[edbgserver]] · [[ehook]] · [[fastdbg]] · [[frida]]
