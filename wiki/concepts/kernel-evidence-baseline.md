---
title: Kernel Evidence Baseline
kind: concept
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/skills/windows-kernel.md
updated: 2026-09-13
confidence: high
---

# Kernel Evidence Baseline

Discipline for matching kernel conclusions to the **exact Windows build** and separating **documented contracts**, **observed host state**, and **inferred internals** before generalizing PoCs, pool parsers, callback bypass claims, or forensic heuristics. Pair with [[driver-trust-boundaries]] for IOCTL/provenance threat modeling and [[research-rigor]] when README listings or wiki prose are turned into enforcement or attribution claims. (source: wiki/sources/skills/windows-kernel.md)

## Baseline before interpretation

| Dimension | Why it matters |
|-----------|----------------|
| Windows build and architecture | Undocumented structure layouts, globals, and allocator routing change per release and SKU |
| Configuration state | VBS/HVCI capability vs configuration vs **running state**; blocklist/policy version; verifier settings |
| Symbol identity | Public vs private PDB scope; a symbol name without sufficient type info does not establish a layout |
| Collection method and time | Live attach, crash dump, offline image — each has coverage gaps and retention limits |
| Calling context | **IRQL**, pool type, cancellation, and object lifetime constrain which APIs and buffers are valid |

Record these fields on every kernel report. A pattern scan or blog offset is not proof the structure or path exists on the tested host. (source: wiki/sources/skills/windows-kernel.md)

## Three evidence layers

1. **Documented contracts** — public WDK APIs, IOCTL contracts, Microsoft driver security checklists, published pool allocation parameters (`ExAllocatePool2`/`ExAllocatePool3` minimum versions, IRQL rules).
2. **Observed host state** — loaded-module inventory, HVCI/VBS running state, ETW/callback telemetry, crash artifacts, pool/dump parser output for the retained snapshot.
3. **Inferred internals** — undocumented table walks (`PiDDBCacheTable`, Segment Heap metadata), offset chains from reverse engineering — treat as **build-specific hypotheses** until verified with matching symbols and runtime for the exact target.

Keep allocation facts, ownership hypotheses, and security conclusions in separate sections. A negative scan or missing callback describes parser/collection coverage — not proof that all prior activity was absent. (source: wiki/sources/skills/windows-kernel.md)

## When to apply

| Query type | Pair with |
|------------|-----------|
| IOCTL reachability, signed-driver abuse, blocklist scope | [[driver-trust-boundaries]], [[byovd]] |
| Pool walks, PiDDBCache/MmUnloadedDrivers claims | [[kernel-pool-scanning]] |
| Callback/ETW blind or bypass claims | [[kernel-callbacks]], [[etw-threat-intelligence]] |
| Memory Integrity / hypervisor enforcement claims | [[hvci]], [[assurance-boundaries]] |
| External DMA vs host driver acquisition | [[memory-acquisition-path]], [[overviews/dma-attack]] |
| Disputed implementation or detectability claims | [[research-rigor]], [[overviews/windows-kernel]] |

## Related

[[driver-trust-boundaries]] · [[kernel-pool-scanning]] · [[kernel-callbacks]] · [[static-runtime-evidence]] · [[research-rigor]] · [[patchguard]] · [[hvci]] · [[byovd]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
