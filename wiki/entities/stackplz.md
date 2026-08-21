---
title: stackplz
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/SeeFlowerX__stackplz.md
updated: 2026-08-21
confidence: medium
---

# stackplz

**Android-focused** stack tracing and hook analysis tool built on **eBPF**. Combines a **Go** userland controller with **eBPF C** programs to trace **syscalls**, **user-space probes**, and **hardware breakpoints** on **ARM64**. Captures arguments, registers, and call stacks; supports filtering, structured output, and optional **Frida RPC** integration. Aimed at mobile security and game protection research where deep runtime telemetry is needed on **rooted devices**. (source: wiki/sources/descriptions/SeeFlowerX__stackplz.md)

Sits in the Android eBPF dynamic-analysis lane beside CLI debuggers such as [[edbg]], uprobe hook frameworks such as [[ehook]], and syscall/trace corpora such as [[android-ebpf]]; complements user-mode DBI such as [[frida]] when kernel eBPF attach is available.

## Links

- Repo: https://github.com/SeeFlowerX/stackplz

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[android-ebpf]] · [[edbg]] · [[ehook]] · [[btrace]] · [[frida]]
