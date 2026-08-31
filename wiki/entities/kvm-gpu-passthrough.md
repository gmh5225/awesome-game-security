---
title: KVM-GPU-Passthrough
kind: entity
topics: [game-hacking, dma-attack, windows-kernel]
sources:
  - wiki/sources/descriptions/BigAnteater__KVM-GPU-Passthrough.md
updated: 2026-08-31
confidence: medium
---

# KVM-GPU-Passthrough

**KVM-GPU-Passthrough** (BigAnteater) is an **Arch Linux–focused setup project** for building a **GPU passthrough virtual machine** environment. It ships **shell scripts and config templates** for **GRUB**, **libvirt**, and **QEMU** host configuration, and documents **hardware virtualization prerequisites**—**IOMMU**, **VT-d**, and related **BIOS settings** for **AMD and Intel** systems. Intended for advanced users building **isolated gaming or security research labs** with **near-native graphics** in a guest VM. (source: wiki/sources/descriptions/BigAnteater__KVM-GPU-Passthrough.md)

Distinct from anti-detection lab orchestrators such as [[hypervisor-phantom]] (Bash automation with QEMU/EDK2/kernel/VFIO patches for VM fingerprint hiding): KVM-GPU-Passthrough focuses on **reproducible passthrough host bring-up** and **IOMMU group validation** rather than guest identifier spoofing. Complements DMA/KVM cheat stacks such as [[apex-dma-kvm-pub]] and [[cs2-kvm-dma]] that assume a working **VFIO passthrough** host.

Sits in the README **`GPU Passthrough`** lane and the broader `Cheat > QEMU/KVM/PVE/VBOX` research-host category.

## Links

- Repo: https://github.com/BigAnteater/KVM-GPU-Passthrough (README tag: GPU Passthrough)

## Related

[[iommu]] · [[hypervisor-phantom]] · [[kvm-performance]] · [[apex-dma-kvm-pub]] · [[cs2-kvm-dma]] · [[memflow-kvm]] · [[overviews/game-hacking]] · [[overviews/dma-attack]]
