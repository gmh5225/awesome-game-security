---
title: epthookdetection
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/IntelSDM__EPTHookDetection.md
updated: 2026-11-19
confidence: medium
---

# epthookdetection

**EPTHookDetection** (IntelSDM/EPTHookDetection) is an **LLVM 19** compiler-pass plugin for **Windows x64** that instruments application code at **build time** to detect hypervisor-based **EPT memory hooks** without separate runtime JIT stubs. It injects three complementary probes: a customized **ERMSB**-based check that catches shadow debug-register behavior missed by older detectors, **in-page LODSD-style** gadgets that execute only on the real physical pages, and optional **HyperDOS** inline pause loops that severely slow execution on hooked pages while barely affecting normal machines. Developers opt functions in or out and register a detection callback via **LLVM function annotations**; the pass is designed to work alongside obfuscation so probes live next to protected code on the same pages. Primary use case: game security, anti-cheat, and anti-tamper tooling that must spot EPT hooking from usermode binaries against stacks such as HyperDbg or DBVM. (source: wiki/sources/descriptions/IntelSDM__EPTHookDetection.md)

Distinct from runtime usermode EPT detectors such as [[ept-hook-detection]] (timing / write-compare / cross-core) and standalone REP MOV side-channel PoCs such as [[ermsb-meme]] and [[rep-mov-ept-detecc]]; complements VPGATHER probes such as [[bloodhound]]. Opposite stealth Type-2 hook stacks such as [[ophion]] and [[hypervisor]]. Same author lane as [[7dtd]] and [[rust-dma-cheat]].

## Links

- Repo: https://github.com/IntelSDM/EPTHookDetection

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[ept-hook-detection]] · [[ermsb-meme]] · [[rep-mov-ept-detecc]] · [[bloodhound]] · [[hypervisor-detection]] · [[ophion]] · [[hypervisor]] · [[hvci]] · [[7dtd]]