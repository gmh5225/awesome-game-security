---
title: Blackbone
kind: entity
topics: [game-hacking, windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/DarthTon__Blackbone.md
updated: 2026-08-26
confidence: medium
---

# Blackbone

Windows **memory hacking library** (DarthTon) for advanced process manipulation and code injection. Supports x86 and x64 targets with APIs for memory allocation, read/write, protection changes, module enumeration, manual PE mapping, and thread control across WOW64 boundaries. Includes both user-mode and kernel-related capabilities for low-level internals work. Widely used in reverse engineering, game security research, and anti-cheat tooling experiments. (source: wiki/sources/descriptions/DarthTon__Blackbone.md)

Consumes manual-map and injection research lanes alongside [[modexmap]], [[simple-manual-map-injector]], and [[windows-process-injection]]. Downstream tools such as [[pevisor]] build on Blackbone for process control, hooking, and mapping in PE instrumentation workflows.

## Links

- Repo: https://github.com/DarthTon/Blackbone

## Related

[[pevisor]] · [[modexmap]] · [[windows-process-injection]] · [[libmem]] · [[memwars]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
