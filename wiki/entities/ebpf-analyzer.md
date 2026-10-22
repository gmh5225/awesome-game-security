---
title: eBPF Analyzer
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/DoranekoSystems__ebpf-analyzer.md
  - wiki/sources/README-categories.md
updated: 2026-10-22
confidence: medium
---

# eBPF Analyzer

**eBPF Analyzer** (DoranekoSystems) is an experimental **PacketProxy** plugin that uses Linux **eBPF** on rooted **Android x86_64** devices to observe TCP traffic and syscall-related I/O **without** enabling a device-wide proxy. A Go host monitor drives an on-device **cilium/ebpf** collector; the Java plugin surfaces connections, packet copies, and per-package attribution in PacketProxy. Optional **Frida** scripts add native and Java stack traces for selected processes. (source: wiki/sources/descriptions/DoranekoSystems__ebpf-analyzer.md) (source: wiki/sources/README-categories.md)

Fits the Cheat **Android Network Explorer** lane beside VPN capture such as [[pcapdroid]] and kernel eBPF tooling such as [[peetch]].

## Links

- Repo: https://github.com/DoranekoSystems/ebpf-analyzer

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[pcapdroid]] · [[peetch]] · [[frida]] · [[mobile-network-trust-evidence]]
