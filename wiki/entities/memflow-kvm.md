---
title: memflow-kvm
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/memflow__memflow-kvm.md
updated: 2026-07-30
confidence: medium
---

# memflow-kvm

**memflow** connector implemented as a **Linux kernel module** that maps **KVM virtual-machine physical pages** directly into userspace, enabling fast **cross-VM memory introspection** without standard KVM APIs. The module uses **page-table walking** and **vmtools** to expose guest memory through **ioctl-based character-device** interfaces with **Rust userspace bindings** — useful on Linux/KVM lab hosts for live guest RAM reads (including Windows guests) adjacent to offline dump forensics and the broader memflow ecosystem ([[dma-speedtest-memflow-rs]] uses other memflow connectors for DMA benchmarking). (source: wiki/sources/descriptions/memflow__memflow-kvm.md)

## Links

- Repo: https://github.com/memflow/memflow-kvm

## Related

[[dma-speedtest-memflow-rs]] · [[volatility3]] · [[ephemera]] · [[panda]] · [[mvisor]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
