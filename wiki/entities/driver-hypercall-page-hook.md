---
title: Driver-HypercallPageHook
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Driver-HypercallPageHook.md
updated: 2026-08-13
confidence: medium
---

# Driver-HypercallPageHook

Proof-of-concept kernel driver (gmh5225; README `[HvcallCodeVa]`) that hooks **`nt!HvcallCodeVa`** — the hypercall page pointer used for Hyper-V-related kernel hypercall transitions. The driver locates the hypercall page reference near `HvlInvokeHypercall`, replaces it with a custom dispatcher, and flips **`HvlEnlightenments`** so context-switch hypercalls such as **`HvlSwitchVirtualAddressSpace`** are routed through the hook. Implementation splits between a C++ driver entry layer and an assembly dispatcher that inspects the hypercall input code, forwards targeted operations to custom callbacks, and falls back to the original hypercall page for everything else. Mainly useful for low-level Windows and virtualization researchers studying how Hyper-V hypercall dispatch can be intercepted inside the kernel for tracing or experimentation. (source: wiki/sources/descriptions/gmh5225__Driver-HypercallPageHook.md)

## Links

- Repo: https://github.com/gmh5225/Driver-HypercallPageHook

## Related

[[overviews/windows-kernel]] · [[hook-hvl-switch-virtual-address-space]] · [[hyper-rev]] · [[voyager]] · [[go-detection-hyper-v]] · [[windows-kernel-pagehook]]
