---
title: android-ebpf
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__android_ebpf.md
  - wiki/sources/descriptions/PShocker__Android_bpf_sys.md
updated: 2026-08-22
confidence: medium
---

# android-ebpf

Demonstration project for **eBPF** (extended Berkeley Packet Filter) on **Android**: examples for writing and loading eBPF programs to trace syscalls, monitor network traffic, track process activity, and collect kernel-level performance data. Aimed at Android kernel developers and security researchers using eBPF for runtime system analysis. (source: wiki/sources/descriptions/gmh5225__android_ebpf.md)

Educational corpus for Android eBPF bring-up—not a full production tracer. Minimal syscall tracepoint sample [[android-bpf-sys]] (PShocker; `raw_syscalls/sys_enter` → BPF map; C++ userland via Android bpf libs; syscall monitoring / security analysis; cheat / EBPF) illustrates tracepoint+map readback patterns beside this corpus. (source: wiki/sources/descriptions/PShocker__Android_bpf_sys.md) Complements behavior-focused [[btrace]] and packet/TLS tooling such as [[peetch]].

## Links

- Repo: https://github.com/gmh5225/android_ebpf

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[android-bpf-sys]] · [[btrace]] · [[peetch]]
