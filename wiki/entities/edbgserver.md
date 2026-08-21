---
title: edbgserver
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/Satar07__edbgserver.md
updated: 2026-08-21
confidence: medium
---

# edbgserver

**eBPF-powered debugger server** for **Android** and **Linux** that avoids the traditional **ptrace** attachment path. Implemented as a **Rust** multi-crate workspace with separate **CLI**, shared logic, and **eBPF program** components for **Arm64** and **x86_64**. Provides breakpoints, stepping, memory and register operations, signal handling, and process library information in a **low-intrusion** model. Targets low-level debugging and security researchers who need alternative instrumentation in monitored or restricted environments. (source: wiki/sources/descriptions/Satar07__edbgserver.md)

Sits in the eBPF dynamic-analysis lane beside CLI debuggers such as [[edbg]] and [[stackplz]], syscall/trace corpora such as [[android-ebpf]], and uprobe hook frameworks such as [[ehook]]; complements user-mode DBI such as [[frida]] when kernel eBPF attach is available without ptrace.

## Links

- Repo: https://github.com/Satar07/edbgserver

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[android-ebpf]] · [[edbg]] · [[stackplz]] · [[ehook]] · [[fastdbg]] · [[frida]]
