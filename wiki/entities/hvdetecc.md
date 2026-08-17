---
title: hvdetecc
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/can1357__hvdetecc.md
updated: 2026-08-17
confidence: medium
---

# hvdetecc

C++ **collection of hypervisor / VMM detection techniques** for x86-64 — processor behavior tests, performance-monitoring counter (PMC) analysis, memory-management and TLB anomaly checks, multi-source timing analysis (including DRAM power-utilization side channels), MSR behavior probes, and interrupt-handling tests. Targets **Intel VMX** and **AMD SVM**, and also flags **Type-1 hypervisors** via SMBIOS, ACPI tables, and PCI enumeration. Aimed at anti-cheat engineers and hypervisor-security researchers studying VM detection and virtualization evasion. (source: wiki/sources/descriptions/can1357__hvdetecc.md)

Complements multi-technique C++ detectors such as [[hypervisor-detection]], IDT SIDT/LIDT probes such as [[hv-detect]], ring-0 multi-heuristic test drivers such as [[detect-hypervisor-detect-ring-0]], STR-exit VMM fault probes such as [[vmdtstr]], REP MOV / ERMSB EPT side-channel probes such as [[ermsb-meme]], and hypervisor VM-detection benchmarking such as [[nohv]].

## Links

- Repo: https://github.com/can1357/hvdetecc

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[hypervisor-detection]] · [[hv-detect]] · [[detect-hypervisor-detect-ring-0]] · [[vmdtstr]] · [[ermsb-meme]] · [[nohv]] · [[checkhv-um]] · [[awesome-anti-virtualization]] · [[hvci]]
