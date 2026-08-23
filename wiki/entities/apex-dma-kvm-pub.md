---
title: apex-dma-kvm-pub
kind: entity
topics: [dma-attack, game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/MisterY52__apex_dma_kvm_pub.md
updated: 2026-08-23
confidence: medium
---

# apex-dma-kvm-pub

**External Apex Legends cheat framework** built for **QEMU or KVM** memory-access workflows (MisterY52/apex_dma_kvm_pub). The codebase combines **C++ gameplay modules** with **Rust-based memflow** components and **C FFI bindings** to read game memory through **virtualization-focused connectors**. Feature modules include **ESP**, **aiming logic**, **math**, and **prediction** routines, with supporting **build scripts for Linux-style environments**. Intended for studying **DMA or VM-assisted game hacking** techniques and related **anti-cheat detection surfaces** under [[easy-anti-cheat]]. (source: wiki/sources/descriptions/MisterY52__apex_dma_kvm_pub.md)

Sits in the Apex Legends below-OS lane beside FPGA PCILeech samples such as [[apex-dma-cheat-updated]] and KVM-host readers such as [[ez-apex-dma-aimbot]], and complements QEMU/KVM title frameworks such as [[escape-from-tuxkov]] with memflow-backed guest physical-memory access via [[memflow-kvm]].

## Architecture

| Layer | Role |
|-------|------|
| C++ gameplay modules | ESP, aim, math, prediction |
| Rust memflow + C FFI | Virtualization-focused memory connectors |
| QEMU/KVM host | External memory reads outside guest OS |
| Linux build scripts | Host-side compile and deployment |

## Links

- Repo: https://github.com/MisterY52/apex_dma_kvm_pub

## Related

[[easy-anti-cheat]] · [[dma]] · [[memflow-kvm]] · [[vm]] · [[apex-dma-cheat-updated]] · [[ez-apex-dma-aimbot]] · [[cs2-kvm-dma]] · [[escape-from-tuxkov]] · [[world-to-screen]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
