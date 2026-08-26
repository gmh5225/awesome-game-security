---
title: KernelForge
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/Cr4sh__KernelForge.md
updated: 2026-08-26
confidence: medium
---

# KernelForge

**KernelForge** (Cr4sh) is a **Windows C++ library** for **invoking kernel routines from user mode** on systems hardened by **VBS** and **HVCI**. Its split design pairs a component that exposes **kernel-memory primitives through a signed driver wrapper** with another that builds **higher-level kernel function-call** capabilities. The repository ships headers, static libraries, DLL bindings, and an example demonstrating **kernel-to-user DLL injection**. Primary use cases include **advanced kernel security research** and **exploit prototyping under modern platform defenses**. (source: wiki/sources/descriptions/Cr4sh__KernelForge.md)

README category: **[Hijack ROP]** — user-mode orchestration of kernel execution without classic unsigned shellcode mapping paths.

From the same author as firmware/DMA research stacks [[pico-dma]], [[s6-pcie-microblaze]], and [[smm-backdoor-ng]], but focused on **runtime VBS/HVCI-era kernel invocation** rather than pre-boot or Ring -2 persistence.

## Links

- Repo: https://github.com/Cr4sh/KernelForge

## Related

[[hvci]] · [[byovd]] · [[goodmans-kernel]] · [[bustercall]] · [[kernel-dll-injector]] · [[pico-dma]] · [[smm-backdoor-ng]] · [[overviews/windows-kernel]]
