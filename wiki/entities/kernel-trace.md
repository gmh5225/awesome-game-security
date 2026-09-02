---
title: Kernel-Trace
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/AndroidReverser-Test__Kernel-Trace.md
updated: 2026-09-02
confidence: medium
---

# Kernel-Trace

**KPM (KernelPatch Module)** for Linux and Android that uses **uprobes** to hook large numbers of user-space functions simultaneously. Written in C/C++; exposes userspace headers and helper components for configuring target libraries, offsets, and hook metadata. Supports **tracefs**-based output and APIs to register and clear probe points across supported kernel versions. Intended for dynamic analysis, reverse engineering, and low-level behavior tracing on Android systems. (source: wiki/sources/descriptions/AndroidReverser-Test__Kernel-Trace.md)

Sits in the KPM uprobe hook lane beside [[apatch-kpm]] / [[kernelpatch]] module collections and complements eBPF uprobe frameworks such as [[ehook]] and [[stackplz]] when a loadable kernel module path is preferred over eBPF attach.

## Links

- Repo: https://github.com/AndroidReverser-Test/Kernel-Trace

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[apatch-kpm]] · [[kernelpatch]] · [[ehook]] · [[stackplz]] · [[android-kernel-hacking-toolkit]]
