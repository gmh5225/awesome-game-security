---
title: kernel-hook-framework
kind: entity
topics: [reverse-engineering, game-hacking, mobile-security]
sources:
  - wiki/sources/descriptions/WeiJiLab__kernel-hook-framework.md
updated: 2026-08-19
confidence: medium
---

# kernel-hook-framework

**Linux kernel inline-hook framework** (WeiJiLab) for intercepting, replacing, and restoring kernel functions at runtime. Ships a core loadable module plus sample modules; supports **x86**, **x86_64**, **ARM**, **ARM64**, and **RISC-V 64** with **proc** interfaces for live control. Uses **trampoline-based patching** and extended **kallsyms** symbol resolution to hook a broader set of kernel targets. Aimed at kernel debugging, live experimentation, and low-level security research—including anti-cheat-related kernel studies on Linux and embedded/Android hosts. (source: wiki/sources/descriptions/WeiJiLab__kernel-hook-framework.md)

Complements Android-oriented Linux kernel tooling such as [[kernelpatch]] and [[hardware-breakpoint]], offensive LKM hook samples such as [[venom]], and kallsyms-centric static RE helpers such as [[vmlinux-to-elf]] and [[import-kallsyms]].

## Links

- Repo: https://github.com/WeiJiLab/kernel-hook-framework

## Related

[[kernelpatch]] · [[venom]] · [[hardware-breakpoint]] · [[vmlinux-to-elf]] · [[import-kallsyms]] · [[klldb]] · [[kernel-development]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/mobile-security]]
