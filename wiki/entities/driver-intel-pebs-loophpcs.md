---
title: Driver-intel-PEBs-LoopHPCs
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Driver-intel-PEBs-LoopHPCs.md
updated: 2026-08-13
confidence: medium
---

# Driver-intel-PEBs-LoopHPCs

**LoopHPCs** is a Windows **filter-driver** framework for loop-centric profiling built on Intel hardware performance features — **PEBS** (Processor Event-Based Sampling) and **Last Branch Record (LBR)**. The source tree combines PEBS helpers, branch-record processing, and loop-tracking logic. Core code consumes PEBS records, correlates eventing IPs, next IPs, and data addresses with LBR-derived control-flow context, then builds **loop-oriented telemetry** instead of only collecting raw counter values. Archived README positions it for finding hot loops in running binaries, especially **unpacking-oriented malware**. Aimed at low-level Windows and reverse-engineering researchers studying hardware-assisted runtime profiling of tight loops and unpacker behavior. (source: wiki/sources/descriptions/gmh5225__Driver-intel-PEBs-LoopHPCs.md)

Complements branch-trace drivers such as [[branch-monitoring-project]], PMI counter stacks such as [[pmi-hpc]] and [[pmctrace]], and Intel PT capture such as [[windows-intel-pt]] as a PEBS+LBR loop-profiling lane rather than full control-flow trace or raw PMC dumps.

## Links

- Repo: https://github.com/gmh5225/Driver-intel-PEBs-LoopHPCs (README tag: Intel PEBs)

## Related

[[branch-monitoring-project]] · [[pmi-hpc]] · [[pmctrace]] · [[intel-pcm]] · [[windows-intel-pt]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
