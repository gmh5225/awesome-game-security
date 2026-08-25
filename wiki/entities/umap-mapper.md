---
title: umap-mapper
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/FarmEquipment69__umap-mapper.md
updated: 2026-08-25
confidence: medium
---

# umap-mapper

**umap-mapper** (FarmEquipment69/umap-mapper) is a **Windows kernel-mode manual mapper** proof of concept in **C**. It hooks a **kernel function pointer** to receive mapping requests, copies PE images into **executable kernel memory**, resolves imports and relocations, then calls the entry point. The Visual Studio driver project includes helper utilities for **pattern scanning** and **protected memory writes**. Primary use case: low-level research into **driver loading techniques** used in anti-cheat evasion experiments. (source: wiki/sources/descriptions/FarmEquipment69__umap-mapper.md)

README lane: **`NtConvertBetweenAuxiliaryCounterAndPerformanceCounter`** — syscall-dispatch hook channel for covert map requests from user mode, distinct from BYOVD usermode mappers such as [[umap]] and [[kdmapper]].

Complements other function-pointer hook mappers and load-path research such as [[iocreatedriver]], [[driver-session-mapper]], and [[known-driver-mappers]].

## Links

- Repo: https://github.com/FarmEquipment69/umap-mapper

## Related

[[umap]] · [[kdmapper]] · [[iocreatedriver]] · [[known-driver-mappers]] · [[kernel-pool-scanning]] · [[nullmap]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
