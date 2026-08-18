---
title: cs2-kvm-dma
kind: entity
topics: [dma-attack, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/atombottle__cs2_kvm_dma.md
updated: 2026-08-18
confidence: medium
---

# cs2-kvm-dma

**Counter-Strike 2** cheat that runs cheat logic from a **KVM virtual machine** or separate host OS, reading game memory through **DMA hardware** or **KVM memory mapping** and rendering **radar or ESP** outside the guest where CS2 and its anti-cheat execute. Because no cheat code runs inside the gaming VM, in-guest AC has no local process, module, or hook surface to inspect — useful for studying KVM/DMA hybrid cheat architectures and their detection challenges. (source: wiki/sources/descriptions/atombottle__cs2_kvm_dma.md)

Bridges PCIe **below-OS DMA** CS2 samples such as [[cs2-dma]], [[cs2-dma-radar]], and [[cs2-dma-cheat]] with **hypervisor-host** lanes such as [[cs16-trigger-kvm]] and [[kvm-csgo-cheat]]; complements KVM introspection tooling such as [[memflow-kvm]] and transport-agnostic [[vm]] backends.

## Links

- Repo: https://github.com/atombottle/cs2_kvm_dma

## Related

[[cs2-dma]] · [[cs2-dma-radar]] · [[cs2-dma-cheat]] · [[cs16-trigger-kvm]] · [[kvm-csgo-cheat]] · [[memflow-kvm]] · [[vm]] · [[dma]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
