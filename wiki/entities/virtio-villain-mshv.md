---
title: Virtio Villain MSHV
kind: entity
topics: [game-hacking, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/weltling__virtio-villain-mshv.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: high
---

# Virtio Villain MSHV

**virtio-villain-mshv** ([weltling/virtio-villain-mshv](https://github.com/weltling/virtio-villain-mshv)) is a **Linux Microsoft Hypervisor (MSHV) userspace API test suite** focused on **partition lifecycle** and **virtual processor (VP) behavior**. It targets virtualization and platform security researchers who need repeatable, appliance-based validation of **MSHV root-partition support** and **hypervisor UAPI correctness** on x86-64. README category: Cheat (Guest introspection / KVM-adjacent lane). (source: wiki/sources/descriptions/weltling__virtio-villain-mshv.md)

## Stack and orchestration

Plugs into the **Virtio Villain** framework to boot a custom Linux kernel and initramfs under **nested Hyper-V**, using **Cloud Hypervisor with MSHV** or **OpenVMM with KVM and nested virtualization**. **C** implements in-guest test cases; **Python** builds boot images, fetches ESP and OpenVMM firmware components, and **Make** drives orchestration. Host-side selftests cover the build pipeline. (source: wiki/sources/descriptions/weltling__virtio-villain-mshv.md)

## Test coverage

Structured cases exercise lifecycle edge cases, **isolation**, **guest memory**, **IRQ eventfds**, and **VP register or CPUID operations**. (source: wiki/sources/descriptions/weltling__virtio-villain-mshv.md)

## Research use

Complements guest-introspection libraries such as [[introvirt]] and KVM-host memory bridges such as [[memflow-kvm]] in the QEMU/KVM research-host lane beside [[better-timing]] and [[rdtsc-kvm-handler]]. On the Windows side, nested-Hyper-V stacks such as [[aleph0-virtualization-hypervisor]] and Hyper-V introspection tooling such as [[hyper-rev]] share the same hypervisor-behavior research axis from different host OSes. (source: wiki/sources/descriptions/weltling__virtio-villain-mshv.md)

## Links

- Repo: https://github.com/weltling/virtio-villain-mshv

## Related

[[introvirt]] · [[memflow-kvm]] · [[aleph0-virtualization-hypervisor]] · [[hyper-rev]] · [[better-timing]] · [[rdtsc-kvm-handler]] · [[hypervisor-phantom]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
