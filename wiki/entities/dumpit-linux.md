---
title: DumpIt for Linux
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/MagnetForensics__dumpit-linux.md
updated: 2026-08-23
confidence: medium
---

# DumpIt for Linux

**Linux memory acquisition** utility that captures system memory into analysis-friendly dump files. Written in **Rust**; reads from `/proc/kcore` to produce **ELF core** output with optional **tar.zst** compressed packaging for easier storage and transfer. Resulting dumps work directly with **gdb**, **crash**, and **drgn** for incident response and Linux memory forensics without requiring a custom kernel module. (source: wiki/sources/descriptions/MagnetForensics__dumpit-linux.md)

## Links

- Repo: https://github.com/MagnetForensics/dumpit-linux

## Related

[[dumpit-mirror]] · [[memnixfs]] · [[volatility3]] · [[tracee]] · [[rootkit]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
