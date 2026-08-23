---
title: ape-ex-abominations
kind: entity
topics: [dma-attack, game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/LWSS__Ape-ex-Abominations.md
updated: 2026-08-23
confidence: medium
---

# ape-ex-abominations

**Ape-ex Abominations** is a **DMA-oriented cheat project** from **LWSS** aimed at **Apex Legends** workflows in **QEMU and VFIO** environments. The codebase combines **C++ feature modules** with **shell-based tooling** that automates **gdb injection**, extraction, and fast reload cycles. It includes **interface discovery** and **pattern-scanning** components and expects auxiliary input support from an **evdev-mirror kernel module**. Intended for advanced game security researchers experimenting with **virtualized or hardware-assisted cheating setups** under [[easy-anti-cheat]]. (source: wiki/sources/descriptions/LWSS__Ape-ex-Abominations.md)

README category: **Apex**.

Sits in the Apex Legends below-OS lane beside QEMU/KVM frameworks such as [[apex-dma-kvm-pub]] and [[ez-apex-dma-aimbot]], FPGA PCILeech samples such as [[apex-dma-cheat-updated]], and other QEMU title stacks such as [[escape-from-tuxkov]]. Complements LWSS Linux tooling such as [[mcdota]] on a different title and engine.

## Architecture

| Layer | Role |
|-------|------|
| C++ feature modules | Gameplay / memory-facing cheat logic |
| Shell automation | gdb inject, extract, fast reload cycles |
| Interface discovery + pattern scan | Offset and vtable recovery |
| evdev-mirror kernel module | Auxiliary host-side input path |
| QEMU / VFIO host | Guest isolation + passthrough research setup |

## Links

- Repo: https://github.com/LWSS/Ape-ex-Abominations

## Related

[[easy-anti-cheat]] · [[dma]] · [[hardware-input-injection]] · [[apex-dma-kvm-pub]] · [[apex-dma-cheat-updated]] · [[ez-apex-dma-aimbot]] · [[escape-from-tuxkov]] · [[memflow-kvm]] · [[mcdota]] · [[world-to-screen]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
