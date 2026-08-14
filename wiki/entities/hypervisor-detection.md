---
title: Hypervisor-Detection
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/void-stack__Hypervisor-Detection.md
updated: 2026-08-14
confidence: medium
---

# Hypervisor-Detection

C++ research project that currently implements four techniques for detecting hacked / abusive hypervisors. Aimed at anti-cheat engineers and defensive researchers working the `Detection: Hacked Hypervisor` lane. (source: wiki/sources/descriptions/void-stack__Hypervisor-Detection.md)

Sits alongside Hyper-V VM environment probes such as [[go-detection-hyper-v]], kernel-mode KPCR/KPRCB Hyper-V guest probes such as [[detection-hyper-v]], ring-0 multi-heuristic test drivers such as [[detect-hypervisor-detect-ring-0]] (CPUID leaves, TSC/APERF/MPERF VM-exit timing, LBR/DEBUGCTL; manual-map print harness; gmh5225), IDT-based SIDT/LIDT probes such as [[hv-detect]], user-mode HV probes such as [[checkhv-um]], EPT hook detectors such as [[ept-hook-detection]] (timing / write-compare / cross-core consistency), HV construction / stealth stacks such as [[hv]] and [[ophion]], and hacked-hypervisor stress tooling such as [[vt-debuuger]].

## Links

- Repo: https://github.com/void-stack/Hypervisor-Detection

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[hv-detect]] · [[checkhv-um]] · [[hv]] · [[ophion]] · [[vt-debuuger]] · [[hvci]]
