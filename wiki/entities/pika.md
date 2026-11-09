---
title: pika
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/delfianto__pika.md
updated: 2026-11-09
confidence: medium
---

# pika

Rust daemon/CLI memory scanner and value patcher for Windows games running under Wine and Proton on Linux. Uses `process_vm_readv` / `process_vm_writev` instead of ptrace attach so scanning and writes avoid freezing DXVK/VKD3D or deadlocking the wineserver. SIMD-accelerated multi-type scans, safe region classification from proc maps, filter passes, value freezing, AOB signature search, pointer-chain discovery, and Capstone-based disassembly are exposed through a JSON-RPC daemon and CLI client—for modders, reverse engineers, and security researchers who need stable live memory work on Linux gaming setups. (source: wiki/sources/descriptions/delfianto__pika.md)

Complements ptrace-based [[ferret]] and GDB-front-end [[pince]] when Proton/Wine titles need non-stopping cross-process I/O; overlaps feature-wise with [[archmod]] and [[pymemory-editor]] on the Linux memory-editing lane.

## Links

- Repo: https://github.com/delfianto/pika

## Related

[[ferret]] · [[pince]] · [[pymemory-editor]] · [[mempeek]] · [[archmod]] · [[proton]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
