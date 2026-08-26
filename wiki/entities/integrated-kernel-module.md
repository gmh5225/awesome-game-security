---
title: integrated-kernel-module
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Dispa1r__Integrated_kernel_module.md
updated: 2026-08-26
confidence: medium
---

# integrated-kernel-module

Android **ARM64** toolkit (Dispa1r) that combines a custom **kernel driver** with a **Zygisk** injection module for rooted mobile game reverse engineering and anti-cheat research. The **lsdriver** loadable kernel module exposes process memory read/write via **PTE remapping** (AT S1E0R), hardware and PTE breakpoints, single-step debugging, **`do_el0_svc` system-call monitoring**, and virtual **touch**, **gyroscope**, and **GNSS** injection. It integrates **W^X Shadow Hook (wxshadow)**, which uses shadow page tables so integrity checks see original code while execution runs on a modified shadow page. The **rfrida_zygisk** component loads a Frida-compatible agent through a custom ELF linker with anonymous `mmap`, avoiding `ptrace` and `dlopen` traces. A userspace tooling layer and optional MCP server wrappers complete the stack. (source: wiki/sources/descriptions/Dispa1r__Integrated_kernel_module.md)

Complements ARM64 kernel HWBP tooling such as [[hardware-breakpoint]] and eBPF debug stacks such as [[stackplz]]. Stealth Frida/Zygisk lanes include [[florida-zygisk]], [[zygisk-frida]], and [[ksu-rust-frida]]. Framework home: [[kernelsu]] · [[magisk]] · [[zygisk]] · [[frida]].

## Links

- Repo: https://github.com/Dispa1r/Integrated_kernel_module (Android ARM64 kernel module + Zygisk injector for game RE)

## Related

[[zygisk]] · [[frida]] · [[hardware-breakpoint]] · [[stackplz]] · [[florida-zygisk]] · [[zygisk-frida]] · [[ksu-rust-frida]] · [[kernelsu]] · [[magisk]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[mobile-anti-cheat]]
