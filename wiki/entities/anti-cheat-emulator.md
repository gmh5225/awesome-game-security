---
title: anti-cheat-emulator
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/ApexLegendsUC__anti-cheat-emulator.md
updated: 2026-09-02
confidence: medium
---

# anti-cheat-emulator

Windows kernel **anti-cheat simulation driver** from ApexLegendsUC that runs multiple heuristic detection routines to emulate practical anti-cheat telemetry pipelines. Written in C++, it is aimed at researchers studying how kernel-level AC detection and testing workflows can be built without a commercial product. (source: wiki/sources/descriptions/ApexLegendsUC__anti-cheat-emulator.md)

## Detection routines

| Area | Technique |
|------|-----------|
| **System threads** | Start-address / thread heuristics |
| **Stack traces** | Suspicious call-stack inspection |
| **BigPool** | Large-pool allocation scanning |
| **Mapper artifacts** | PiDDB cache entry checks |
| **Driver surface** | Driver dispatch-table inspection |
| **Physical memory** | Suspicious physical-memory handle usage |
| **Environment** | Hypervisor presence + kernel mapping checks |

Complements experimental multi-telemetry sandboxes such as [[kernel-anti-cheat]] (NMI stack walks) and evaluation harnesses such as [[anti-cheat-testbench]] by focusing on breadth of heuristic checks rather than a single detector path.

## Links

- Repo: https://github.com/ApexLegendsUC/anti-cheat-emulator

## Related

[[kernel-anti-cheat]] · [[anti-cheat-testbench]] · [[anti-cheat-testing-framework]] · [[kernel-pool-scanning]] · [[system-thread-finder]] · [[nomad]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
