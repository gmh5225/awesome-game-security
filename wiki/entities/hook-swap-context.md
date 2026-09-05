---
title: HookSwapContext
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/1401199262__HookSwapContext.md
updated: 2026-09-05
confidence: medium
---

# HookSwapContext

**HookSwapContext** (1401199262) is a Windows kernel **proof of concept** for hooking **context-switch–related execution paths**. It uses an **ETW/CKCL-based hook path** and **custom stack-frame checks** to invoke a handler during selected **thread scheduling flow**. Implemented in C++ with low-level modules for trace control, syscall-facing hooks, and kernel utility routines. Primary use case: experimenting with **thread scheduling interception** techniques for kernel security research. README category: cheat / SwapContext hook. (source: wiki/sources/descriptions/1401199262__HookSwapContext.md)

Complements **SwapContext** snippet references in [[kernel-snippets]], hypervisor-assisted address-space hooks such as [[hook-hvl-switch-virtual-address-space]] and [[driver-hypercall-page-hook]], CR3 switch monitoring in [[hook-guard]], and context-switch–scoped memory concealment such as [[yumekage]] — plus sibling 1401199262 kernel PoCs [[nmi-stack-walk]] and [[remote-call]].

## Links

- Repo: https://github.com/1401199262/HookSwapContext [SwapContext hook]

## Related

[[kernel-snippets]] · [[hook-hvl-switch-virtual-address-space]] · [[driver-hypercall-page-hook]] · [[hook-guard]] · [[yumekage]] · [[nmi-stack-walk]] · [[remote-call]] · [[etw-threat-intelligence]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
