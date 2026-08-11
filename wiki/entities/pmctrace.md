---
title: pmctrace
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__pmctrace.md
updated: 2026-08-07
confidence: medium
---

# pmctrace

**pmctrace** is a C tool for collecting **Intel PMC (Performance Monitoring Counter)** data on Windows. It configures and reads CPU performance counters to measure cache hits/misses, branch predictions, instruction counts, and other micro-architectural events for program profiling. The tool exposes low-level PMC register access and streams real-time counter collection via **ETW**. Aimed at performance engineers and security researchers using hardware performance counters for program analysis and side-channel research. (source: wiki/sources/descriptions/gmh5225__pmctrace.md)

Complements official PMU telemetry stacks such as [[intel-pcm]] and hardware-trace tooling ([[branch-monitoring-project]], [[libiht]], [[winipt]], [[windows-intel-pt]]) as a lightweight ETW-backed PMC lane rather than IPT control-flow capture. Interrupt-driven security monitoring via [[pmi-hpc]] (PMI + HPC; branch misprediction / cache-miss events; code injection / ROP anomaly detection) sits in the same PMU lane with a defensive detection focus. Background reference material on x86 PMC/PMI appears in [[pdf-pmc-x86]] (PDF study; documentation archive).

## Links

- Repo: https://github.com/gmh5225/pmctrace (README tag: Real-time collection of PMCs via ETW)

## Related

[[intel-pcm]] · [[pmi-hpc]] · [[pdf-pmc-x86]] · [[branch-monitoring-project]] · [[libiht]] · [[winipt]] · [[windows-intel-pt]] · [[processor-trace]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
