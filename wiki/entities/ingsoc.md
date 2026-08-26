---
title: ingsoc
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/CristiNacu__ingsoc.md
updated: 2026-08-26
confidence: medium
---

# ingsoc

**ingsoc** is a Windows **Intel Processor Trace (PT)** toolkit that combines a kernel driver, a user-mode controller, and a Python trace decoder. The driver configures Intel PT collection; the client sends control commands and can stream captured trace packets to Kafka. The companion decoder parses packet streams, reconstructs execution behavior, and generates visual analytics for trace timing and control-flow events. Aimed at exploit and malware behavior research — especially low-level execution patterns and potential code-reuse activity. (source: wiki/sources/descriptions/CristiNacu__ingsoc.md)

Sits beside Windows IPT capture stacks such as [[winipt]], [[windows-intel-pt]], and [[libipt-rs]], decode layers such as [[processor-trace]] (libipt), and ROP/JOP-oriented detection research such as [[pt-detector]] as a full-stack PT pipeline with optional Kafka streaming and visual analytics.

## Links

- Repo: https://github.com/CristiNacu/ingsoc (README tag: Intel PT)

## Related

[[processor-trace]] · [[winipt]] · [[windows-intel-pt]] · [[pt-detector]] · [[libipt-rs]] · [[winafl]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
