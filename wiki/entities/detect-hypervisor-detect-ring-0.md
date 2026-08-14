---
title: Detect-Hypervisor_detect_ring_0
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__Detect-Hypervisor_detect_ring_0.md
updated: 2026-08-14
confidence: medium
---

# Detect-Hypervisor_detect_ring_0

**Ring-0 hypervisor detection test driver** built for **manual-mapped kernel deployment**. From `DriverEntry` it runs a battery of kernel-mode heuristics and **prints each result** — a comparison harness, not an enforcement pipeline. Checks combine the **CPUID hypervisor bit**, comparisons between **invalid and hypervisor CPUID leaves**, **timing attacks** around VM-exit behavior using **TSC**, **APERF**, and **MPERF** MSRs, and **Intel LBR / DEBUGCTL consistency** probes. The README credits **Secret Club** hypervisor-detection research. Mainly useful for anti-cheat and low-level security researchers comparing multiple kernel-mode heuristics for spotting emulation or custom hypervisors. (source: wiki/sources/descriptions/gmh5225__Detect-Hypervisor_detect_ring_0.md)

Complements IDT SIDT/LIDT probes such as [[hv-detect]], Hyper-V KPCR/KPRCB guest probes such as [[detection-hyper-v]], user-mode Go Hyper-V checks such as [[go-detection-hyper-v]], and multi-technique C++ detectors such as [[hypervisor-detection]]. Benchmark suites such as [[nohv]] stress custom hypervisors against common vm-detection heuristics in the same `Detection: Hacked Hypervisor` lane.

## Links

- Repo: https://github.com/gmh5225/Detect-Hypervisor_detect_ring_0

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[hv-detect]] · [[detection-hyper-v]] · [[go-detection-hyper-v]] · [[hypervisor-detection]] · [[nohv]] · [[checkhv-um]] · [[hvci]]
