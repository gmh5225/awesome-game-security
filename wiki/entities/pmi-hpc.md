---
title: PMI-hpc
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__PMI-hpc.md
updated: 2026-08-11
confidence: medium
---

# PMI-hpc

Windows research project demonstrating **Performance Monitoring Interrupts (PMI)** with **hardware performance counters (HPC)** for security monitoring. Configures CPU performance counters to fire interrupts on micro-architectural events such as branch mispredictions and cache misses, enabling detection of anomalous execution patterns that may indicate code injection or ROP attacks. Aimed at security researchers exploring hardware-assisted detection techniques. (source: wiki/sources/descriptions/gmh5225__PMI-hpc.md)

Complements passive PMC profiling via [[pmctrace]] and branch-trace collection via [[branch-monitoring-project]] as an interrupt-driven HPC lane oriented toward exploit-pattern detection rather than ETW streaming or LBR/BTS control-flow capture. Background reference material on x86 PMC/PMI appears in [[pdf-pmc-x86]] (PDF study; documentation archive).

## Links

- Repo: https://github.com/gmh5225/PMI-hpc (README tag: PMI)

## Related

[[pmctrace]] · [[pdf-pmc-x86]] · [[perfmon]] · [[thread-spy]] · [[branch-monitoring-project]] · [[intel-pcm]] · [[libiht]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
