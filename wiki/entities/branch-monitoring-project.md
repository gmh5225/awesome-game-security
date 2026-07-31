---
title: Branch Monitoring Project
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/marcusbotacin__BranchMonitoringProject.md
updated: 2026-07-31
confidence: medium
---

# Branch Monitoring Project

Research framework for **hardware-assisted program execution monitoring** using Intel **Last Branch Record (LBR)** and **Branch Trace Store (BTS)**. A C kernel driver accesses CPU branch-recording registers from kernel mode; companion usermode tools collect and analyze branch-level execution traces from running programs — fine-grained control-flow visibility **without software instrumentation** (no `.text` patches or trap-and-emulate hooks). Aimed at security researchers studying malware analysis and integrity checking. (source: wiki/sources/descriptions/marcusbotacin__BranchMonitoringProject.md)

Complements software DBI ([[cpp-veh-dbi]], [[w1tn3ss]]) and hypervisor/Intel-PT tracing ([[qemu-nyx]]) as a CPU PMU / PMI lane for branch coverage and control-flow forensics.

## Links

- Repo: https://github.com/marcusbotacin/BranchMonitoringProject (README tag: PMI)

## Related

[[dynamic-binary-instrumentation]] · [[cpp-veh-dbi]] · [[w1tn3ss]] · [[qemu-nyx]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
