---
title: Detection-Hyper-v
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__Detection-Hyper-v.md
updated: 2026-08-14
confidence: medium
---

# Detection-Hyper-v

Minimal **kernel-mode Hyper-V detection driver** that reads hypervisor state directly from **KPCR / KPRCB** structures rather than user-mode CPUID probes. Targets Windows 10 build **17763** headers: calls `KeGetPcr`, walks to `CurrentPrcb`, and inspects `PowerState.Hypervisor` plus `PowerState.HvTargetState` to decide whether the machine is a Hyper-V guest. Reports via debug prints and exits with `STATUS_VIRUS_INFECTED` — a focused kernel experiment, not a reusable anti-cheat module. README category `[Hyper-v]`. (source: wiki/sources/descriptions/gmh5225__Detection-Hyper-v.md)

Mainly useful for defensive researchers studying **build-specific kernel structure checks** for Hyper-V presence. Complements user-mode Go probes such as [[go-detection-hyper-v]], IDT SIDT/LIDT hypervisor probes such as [[hv-detect]], and multi-technique C++ detectors such as [[hypervisor-detection]].

## Links

- Repo: https://github.com/gmh5225/Detection-Hyper-v

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[go-detection-hyper-v]] · [[hv-detect]] · [[hypervisor-detection]] · [[checkhv-um]] · [[disabling-hyper-v]] · [[hvci]]
