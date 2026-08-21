---
title: eHook
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ShinoLeah__eHook.md
updated: 2026-08-21
confidence: medium
---

# eHook

Framework for building **Android ARM64 uprobe hooks** with **eBPF** modules. **Go** orchestrates loading and lifecycle; **C** implements eBPF hook logic. Wrappers cover memory read/write, logging, and custom event submission. Users configure target package and library offsets, then implement **on-enter** and **on-leave** handlers for instrumentation or behavior modification. Aimed at rooted-device dynamic analysis, mobile game research, and lightweight runtime tracing. (source: wiki/sources/descriptions/ShinoLeah__eHook.md)

Sits in the Android eBPF hook lane beside syscall/trace corpora such as [[android-ebpf]] and behavior tracers such as [[btrace]], and complements user-mode DBI such as [[frida]] when kernel uprobe attach is available.

## Links

- Repo: https://github.com/ShinoLeah/eHook

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[android-ebpf]] · [[btrace]] · [[peetch]] · [[frida]]
