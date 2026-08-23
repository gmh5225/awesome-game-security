---
title: PerfMon (KelvinMsft)
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/KelvinMsft__PerfMon.md
updated: 2026-08-23
confidence: medium
---

# PerfMon (KelvinMsft)

**PerfMon** is a **Windows kernel research driver** that uses **hardware performance monitoring** for low-level control and observation. It works with **PMU** and **PMI** flows, **APIC** handling, and related interrupt paths to explore techniques connected to **SSDT monitoring** and **hook-style interception** on modern Windows systems. Implementation is mainly **C/C++**; the repository includes reference papers and a small test program for experimentation. Aimed at kernel security and anti-cheat researchers studying **hardware-assisted monitoring** on Windows 10–era platforms. (source: wiki/sources/descriptions/KelvinMsft__PerfMon.md)

README lane: **PMI Callback** — foundational PMU/PMI/APIC research for monitoring and interception rather than a turnkey cheat or detector.

Complements detection-oriented PMI/HPC samples such as [[pmi-hpc]] and offensive PMI callback work such as [[thread-spy]] in the same KelvinMsft Windows kernel lane. Background on x86 PMC/PMI appears in [[pdf-pmc-x86]].

## Links

- Repo: https://github.com/KelvinMsft/PerfMon

## Related

[[pmi-hpc]] · [[thread-spy]] · [[pdf-pmc-x86]] · [[branch-monitoring-project]] · [[pmctrace]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
