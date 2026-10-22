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

**eBPF Analyzer** (DoranekoSystems) is an experimental **PacketProxy** plugin that uses Linux **eBPF** on rooted **Android x86_64** devices to observe TCP traffic and syscall-related I/O **without** enabling a device-wide proxy. A Go host monitor drives an on-device **cilium/ebpf** collector; the Java plugin surfaces connections, packet copies, and per-package attribution in PacketProxy. Optional **Frida** integration (companion scripts plus eBPF helpers) adds native and Java stack traces for selected processes so analysts can correlate live connections with call sites while **TLS payloads stay encrypted on the wire**. (source: wiki/sources/descriptions/DoranekoSystems__ebpf-analyzer.md) (source: wiki/sources/README-categories.md)

Targets mobile security researchers, reverse engineers, and analysts who need attribution and syscall context without MITM trust changes. Development has emphasized **controlled emulator testing** rather than production-ready deployment. (source: wiki/sources/descriptions/DoranekoSystems__ebpf-analyzer.md)

Fits the Cheat **Android Network Explorer** lane beside VPN capture such as [[pcapdroid]] and kernel eBPF tooling such as [[peetch]], [[stackplz]], and the [[android-ebpf]] example corpus.

## Links

- Repo: https://github.com/DoranekoSystems/ebpf-analyzer

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[pcapdroid]] · [[peetch]] · [[frida]] · [[mobile-network-trust-evidence]]
