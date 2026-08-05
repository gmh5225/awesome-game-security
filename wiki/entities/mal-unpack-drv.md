---
title: mal_unpack_drv
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/hasherezade__mal_unpack_drv.md
updated: 2026-08-05
confidence: medium
---

# mal_unpack_drv

Experimental **Windows kernel driver** for malware sample unpacking in the Anti Cheat → Sample Unpacker lane. The driver is **test-signed**, so installation requires **Test Signing** enabled on the target machine. Intended for **anti-cheat engineers** and **defensive security researchers** studying packed or protected samples — use on a **virtual machine only**. (source: wiki/sources/descriptions/hasherezade__mal_unpack_drv.md)

Complements hasherezade usermode tooling such as [[pe-sieve]] (runtime injection scan / material collection) and [[pe-bear]] (PE structure editing); sits beside emulation unpackers such as [[xvolkolak]] and static lanes such as [[vmpunpacker]].

## Links

- Repo: https://github.com/hasherezade/mal_unpack_drv

## Related

[[pe-sieve]] · [[pe-bear]] · [[xvolkolak]] · [[vmpunpacker]] · [[android-unpacker]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
