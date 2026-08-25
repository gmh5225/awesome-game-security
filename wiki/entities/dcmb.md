---
title: DCMB
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/GetRektBoy724__DCMB.md
updated: 2026-08-25
confidence: medium
---

# DCMB

Windows kernel driver project for **dynamically locating callback lists** without hardcoded offsets or signature scans. Written in C for the Windows driver toolchain; targets process, thread, image, registry, object, and minifilter notification categories. Learning-focused implementation that reports findings through debug output rather than a polished product API. Primary use case: kernel internals research for anti-cheat, EDR, and callback inspection. (source: wiki/sources/descriptions/GetRektBoy724__DCMB.md)

Sits in the offset-free callback-discovery lane beside [[kpdb]] and [[win32khooker]] from the same author, and callback-removal/offensive enumeration tools such as [[bustercall]], [[ps-notif-routine-unloader]], and [[kernel-callback-removal]] on [[kernel-callbacks]].

## Links

- Repo: https://github.com/GetRektBoy724/DCMB [Removing kernel callbacks]

## Related

[[kernel-callbacks]] · [[kpdb]] · [[win32khooker]] · [[bustercall]] · [[ps-notif-routine-unloader]] · [[kernel-callback-removal]] · [[rtoolz]] · [[openark]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
