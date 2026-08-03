---
title: AMD IBS Toolkit
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/jlgreathouse__AMD_IBS_Toolkit.md
updated: 2026-08-03
confidence: medium
---

# AMD IBS Toolkit

Toolkit for **AMD Instruction-Based Sampling (IBS)** — a hardware mechanism that samples a subset of instructions flowing through the processor. Aimed at game-security researchers and reverse engineers studying offensive techniques in the cheat / Windows kernel explorer lane, where low-overhead execution profiling can reveal hot paths without software instrumentation patches. (source: wiki/sources/descriptions/jlgreathouse__AMD_IBS_Toolkit.md)

Complements Intel-side hardware tracing ([[branch-monitoring-project]], [[libiht]]) and software DBI ([[dynamic-binary-instrumentation]], [[vmtrace]]) as an AMD CPU sampling lane beside LBR/BTS and Intel PT workflows.

## Links

- Repo: https://github.com/jlgreathouse/AMD_IBS_Toolkit (README tag: AMD Sampling)

## Related

[[branch-monitoring-project]] · [[libiht]] · [[dynamic-binary-instrumentation]] · [[vmtrace]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
