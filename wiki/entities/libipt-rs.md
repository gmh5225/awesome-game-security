---
title: libipt-rs
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/australeo__libipt-rs.md
updated: 2026-08-18
confidence: medium
---

# libipt-rs

**libipt-rs** is a Rust library for interacting with the Windows built-in **Intel Processor Trace (IPT)** driver (`ipt.sys`) from user mode. It exposes APIs to start, stop, and retrieve IPT traces via `DeviceIoControl`, based on reverse engineering of the current Windows IPT driver interface. The scope is driver interaction only — it does not include IPT trace parsing or coverage analysis. Aimed at security researchers and anti-cheat analysts studying hardware-assisted code tracing on Windows via Intel PT. (source: wiki/sources/descriptions/australeo__libipt-rs.md)

Sits beside C `ipt.sys` wrappers such as [[winipt]] and own-driver IPT stacks such as [[windows-intel-pt]] as a Rust-native Windows IPT capture option. Pair with [[processor-trace]] (libipt) or other decoders for packet/instruction reconstruction from raw trace buffers.

## Links

- Repo: https://github.com/australeo/libipt-rs (README tag: `ipt.sys`)

## Related

[[winipt]] · [[windows-intel-pt]] · [[processor-trace]] · [[libiht]] · [[branch-monitoring-project]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
