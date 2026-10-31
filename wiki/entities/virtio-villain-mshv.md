---
title: Virtio Villain MSHV
kind: entity
topics: [game-hacking, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/weltling__virtio-villain-mshv.md
updated: 2026-10-31
confidence: medium
---

# Virtio Villain MSHV

**virtio-villain-mshv** (weltling) is a **Linux Microsoft Hypervisor (MSHV) userspace API test suite** focused on **partition lifecycle** and **virtual processor (VP) state**. It plugs into the **Virtio Villain** framework to boot a custom Linux kernel and initramfs under **nested Hyper-V**, using **Cloud Hypervisor with MSHV** or **OpenVMM with KVM and nested virtualization**. Implementation is mainly **C** for in-guest cases and **Python** for boot-image build, ESP/OpenVMM firmware fetch, and **Make** orchestration. Structured cases cover lifecycle edge cases, isolation, guest memory, IRQ eventfds, and VP register/CPUID operations, with host-side selftests for the build pipeline. Targets **virtualization and platform security researchers** who need repeatable appliance-based validation of MSHV root-partition support and hypervisor UAPI correctness on x86-64. README category: Cheat (Guest introspection / KVM-adjacent lane). (source: wiki/sources/descriptions/weltling__virtio-villain-mshv.md)

Complements guest-introspection libraries such as [[introvirt]] and KVM-host memory bridges such as [[memflow-kvm]] in the QEMU/KVM research-host lane beside [[better-timing]] and [[rdtsc-kvm-handler]].

## Links

- Repo: https://github.com/weltling/virtio-villain-mshv

## Related

[[introvirt]] · [[memflow-kvm]] · [[better-timing]] · [[rdtsc-kvm-handler]] · [[hypervisor-phantom]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
