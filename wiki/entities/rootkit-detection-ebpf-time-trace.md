---
title: rootkit-detection-ebpf-time-trace
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/ait-aecid__rootkit-detection-ebpf-time-trace.md
updated: 2026-08-18
confidence: medium
---

# rootkit-detection-ebpf-time-trace

**Linux research framework** for **behavior-based rootkit detection** by analyzing **timing anomalies** in kernel execution paths. Uses **eBPF probes** to collect fine-grained timing data from functions in the **getdents** flow—including paths manipulated by **file-hiding rootkits**. Bundled **Python tooling** supports experiment orchestration, dataset handling, and **semi-supervised statistical anomaly detection** with evaluation outputs. Primary audience: kernel security researchers studying anti-stealth telemetry and timing-side-channel detection rather than production endpoint agents. (source: wiki/sources/descriptions/ait-aecid__rootkit-detection-ebpf-time-trace.md)

Complements Windows hidden-process PoCs such as [[rootkit-2]], Linux hidden-module detectors such as [[modreveal]], and broader eBPF runtime-security platforms such as [[tracee]].

## Links

- Repo: https://github.com/ait-aecid/rootkit-detection-ebpf-time-trace [Detection of rootkit file hiding activities through analysis of shifts in kernel function execution times]

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[rootkit-2]] · [[modreveal]] · [[tracee]] · [[blanket]]
