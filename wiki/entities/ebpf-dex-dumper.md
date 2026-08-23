---
title: eBPFDexDumper
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/LLeavesG__eBPFDexDumper.md
updated: 2026-08-23
confidence: medium
---

# eBPFDexDumper

**Android in-memory DEX dumping** tool from LLeavesG that uses **eBPF probes** to capture runtime bytecode with a **low-intrusion** workflow. Implemented primarily in **Go** for **rooted ARM64 Android** devices. Supports filtering by **UID** or **package name**, streaming **method execution traces**, dumping **DEX files from ART activity**, and **automatic repair** of dumped files for easier static analysis. Targets Android reverse engineering and mobile game security research when dynamically loaded or packed DEX must be recovered at runtime. (source: wiki/sources/descriptions/LLeavesG__eBPFDexDumper.md)

Complements Zygisk hook-based dumpers such as [[zygisk-dump-dex]] and static decode lanes ([[jadx]], [[apktool]], [[dex2jar]]) with kernel-assisted eBPF capture—similar low-intrusion philosophy to [[edbg]], [[stackplz]], and [[ehook]] when analysts need ART-visible DEX without in-process hook modules.

## Links

- Repo: https://github.com/LLeavesG/eBPFDexDumper (README tag: DexDumper based eBPF on Android Platform)

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[android-ebpf]] · [[edbg]] · [[stackplz]] · [[ehook]] · [[zygisk-dump-dex]] · [[dexkit-android]] · [[dexbuilder]] · [[jadx]] · [[frida]]
