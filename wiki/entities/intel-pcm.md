---
title: Intel PCM
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/intel__pcm.md
updated: 2026-08-04
confidence: medium
---

# Intel PCM

**Intel Performance Counter Monitor (PCM)** — official Intel tool suite for monitoring CPU performance metrics, memory bandwidth, PCIe throughput, and power consumption on Intel processors. The C++ codebase supports Docker deployment, CXL monitoring, and extensive documentation on custom compilation options and environment variables. Aimed at performance engineers and security researchers profiling system-level performance and hardware counter behavior. (source: wiki/sources/descriptions/intel__pcm.md)

Distinct from [[pcm]] (rand-tech; curated MCP for IDA Pro). Complements branch/IPT hardware-trace tooling such as [[branch-monitoring-project]], [[libiht]], [[winipt]], and [[processor-trace]] as a PMU / bandwidth / PCIe telemetry lane rather than control-flow capture.

## Links

- Repo: https://github.com/intel/pcm (README tag: Processor Counter Monitor)

## Related

[[pcm]] · [[branch-monitoring-project]] · [[libiht]] · [[winipt]] · [[processor-trace]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
