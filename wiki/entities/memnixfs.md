---
title: MemNixFS
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/MemNixFS__MemNixFS.md
updated: 2026-08-23
confidence: medium
---

# MemNixFS

**Linux memory forensics** tool that mounts offline RAM dumps as a virtual filesystem so investigators can browse processes, open files, sockets, loaded modules, and forensic timelines with ordinary shell and file tools. Accepts **AVML**, **LiME**, raw, and **kdump** images and brings the **MemProcFS** memory-as-filesystem workflow to Linux dumps on both Windows and Linux analysis hosts. Written in **C++17**; centers on kernel-level memory forensics and threat-hunting workflows for anti-cheat engineers and defensive security researchers. (source: wiki/sources/descriptions/MemNixFS__MemNixFS.md)

## Links

- Repo: https://github.com/MemNixFS/MemNixFS

## Related

[[memprocfs-analyzer]] · [[volatility3]] · [[volatility]] · [[pcileech]] · [[tracee]] · [[procmap]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
