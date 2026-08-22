---
title: Android_bpf_sys
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/PShocker__Android_bpf_sys.md
updated: 2026-08-22
confidence: medium
---

# Android_bpf_sys

Minimal **Android eBPF** example for monitoring **kernel syscall** events. Defines a BPF **tracepoint** program on `raw_syscalls/sys_enter`, stores observed **PID** and **syscall** identifiers in a BPF map, and pairs with a **C++** user-space tool that attaches the program and reads map contents through Android **bpf** libraries. Intended for low-level Android security monitoring and syscall behavior analysis. (source: wiki/sources/descriptions/PShocker__Android_bpf_sys.md)

Educational bring-up beside syscall/trace corpora such as [[android-ebpf]] and production tracers such as [[stackplz]] / [[edbg]]; complements user-mode DBI such as [[frida]] when kernel tracepoint attach is available.

## Links

- Repo: https://github.com/PShocker/Android_bpf_sys

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[android-ebpf]] · [[stackplz]] · [[edbg]] · [[btrace]] · [[frida]]
