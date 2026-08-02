---
title: VMAware
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/kernelwernel__VMAware.md
updated: 2026-08-02
confidence: medium
---

# VMAware

Cross-platform **header-only C++** library for virtual-machine detection. Implements **100+** techniques: hypervisor CPUID leaves, known VM artifacts in registry/filesystem/MAC addresses, timing-based side channels, hardware fingerprints, and driver signatures to classify VMware, VirtualBox, Hyper-V, QEMU/KVM, and other hypervisors. Exposes a simple API returning **confidence scores**. Aimed at anti-cheat developers, malware researchers, and security engineers implementing VM detection or studying VM evasion. (source: wiki/sources/descriptions/kernelwernel__VMAware.md)

README lane: `[VM detection library]` under `Detection:Virtual Environments`. Complements narrower probes such as [[checkhv-um]] and [[hypervisor-detection]], sandbox demos such as [[anticuckoo]], curated technique lists such as [[awesome-anti-virtualization]], and guest fingerprint spoof research such as [[qemu-patched]] / [[proxmox-ve-anti-detection]].

## Links

- Repo: https://github.com/kernelwernel/VMAware

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[checkhv-um]] · [[hypervisor-detection]] · [[anticuckoo]] · [[awesome-anti-virtualization]] · [[qemu-patched]] · [[conbeerlib]] · [[makin]]
