---
title: vmdtstr
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/cryotb__VmdtStr.md
updated: 2026-08-16
confidence: medium
---

# vmdtstr

Research project that **detects VMMs with faulty handling of STR (store task register) VM exits** — exercises guest `STR` instruction paths that should trap to the hypervisor and flags VMMs that mishandle register state or exit semantics. Uses **HVPP as a nested VMM** test harness to stress Type-2 hypervisor implementations from a controlled outer layer. Aimed at anti-cheat engineers and defensive security researchers working the `Detection: Hacked Hypervisor` lane. (source: wiki/sources/descriptions/cryotb__VmdtStr.md)

Complements IDT SIDT/LIDT probes such as [[hv-detect]], ring-0 multi-heuristic test drivers such as [[detect-hypervisor-detect-ring-0]], multi-technique C++ detectors such as [[hypervisor-detection]], REP MOV / ERMSB EPT side-channel probes such as [[ermsb-meme]], and hypervisor VM-detection benchmarking such as [[nohv]].

## Links

- Repo: https://github.com/cryotb/VmdtStr

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[hv-detect]] · [[hypervisor-detection]] · [[detect-hypervisor-detect-ring-0]] · [[ermsb-meme]] · [[nohv]] · [[checkhv-um]] · [[ept-hook-detection]] · [[hv]] · [[hypervisor]] · [[hvci]]
