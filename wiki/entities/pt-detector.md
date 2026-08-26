---
title: pt-detector
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/DProvinciani__pt-detector.md
updated: 2026-08-26
confidence: medium
---

# pt-detector

**pt-detector** is a Windows research prototype for detecting code-reuse exploits using **Intel Processor Trace (PT)** data. It combines kernel- and user-mode components to collect trace packets, then decodes execution streams to identify suspicious control-flow behavior associated with techniques like ROP or JOP. Capture infrastructure is implemented in C/C++; Python tooling supports interpretation and analysis. Targeted at exploit detection research and control-flow integrity experimentation. (source: wiki/sources/descriptions/DProvinciani__pt-detector.md)

Sits beside Windows IPT capture stacks such as [[winipt]], [[windows-intel-pt]], and [[libipt-rs]], and decode layers such as [[processor-trace]] (libipt), as an application-oriented PT pipeline focused on anomalous control-flow detection rather than coverage or fuzzing alone.

## Links

- Repo: https://github.com/DProvinciani/pt-detector (README tag: Intel PT)

## Related

[[processor-trace]] · [[winipt]] · [[windows-intel-pt]] · [[libipt-rs]] · [[pmi-hpc]] · [[branch-monitoring-project]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
