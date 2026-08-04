---
title: processor-trace
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/intelpt__processor-trace.md
updated: 2026-08-04
confidence: medium
---

# processor-trace

**libipt** — Intel's open-source reference **Intel Processor Trace (PT) decoder library**. It decodes raw PT trace packets into instruction-level execution traces, handling timing, control flow, and packet formats across multiple trace encodings. The C library exposes APIs for both packet-level and instruction-level decoding. Aimed at debugger authors, performance tool developers, and security researchers building Intel PT-based tracing and coverage tools. (source: wiki/sources/descriptions/intelpt__processor-trace.md)

Complements Windows IPT capture via [[winipt]] and [[windows-intel-pt]], Intel hardware-trace libraries such as [[libiht]], and Intel-PT hypervisor fuzzing stacks such as [[qemu-nyx]] as the standard decode layer for raw PT buffers.

## Links

- Repo: https://github.com/intelpt/processor-trace (README tag: Intel PT Decoder)

## Related

[[winipt]] · [[windows-intel-pt]] · [[libiht]] · [[qemu-nyx]] · [[branch-monitoring-project]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
