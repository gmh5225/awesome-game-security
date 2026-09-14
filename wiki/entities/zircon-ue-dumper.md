---
title: Zircon UE Dumper
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/TheHolyOneZ__Zircon-UE-Dumper.md
  - wiki/sources/README-categories.md
updated: 2026-09-14
confidence: medium
---

# Zircon UE Dumper

**Runtime Unreal Engine reflection extraction and analysis toolkit** (TheHolyOneZ). Written in C++20 for Windows, Zircon reconstructs a title's full type system from a live process, memory dump, or on-disk binary. It auto-detects engine versions from UE 4.22 through 5.7 and derives layout offsets without hardcoded version tables, then emits C++ SDK headers, USMAP mappings, IDA/Ghidra/Binary Ninja type imports, Frida JavaScript bindings, Python stubs, ReClass projects, and other formats from a shared intermediate representation. Acquisition modes include internal injection, external read-only attachment, offline minidump analysis, and static PE scanning through a unified memory abstraction; a GUI browser supports live object inspection, property editing, and Blueprint script decompilation. Listed under cheat / SDK Dump. (source: wiki/sources/descriptions/TheHolyOneZ__Zircon-UE-Dumper.md)

Sits in the multi-format Unreal SDK-generation lane beside in-process inject dumpers such as [[dumper-7]], all-in-one editors such as [[uedumper]], MemProcFS-backed external dumpers such as [[uedumper-memprocfs]], and live-script generators such as [[re-ue4ss]]—all feeding the same [[unreal-object-model]] research surface.

## Audience

Reverse engineers, mod developers, and game security researchers use Zircon when they need accurate reflection data, **cross-build diffing** between UE patches, and **multi-tool export pipelines** from one shared intermediate representation. (source: wiki/sources/descriptions/TheHolyOneZ__Zircon-UE-Dumper.md)

## Links

- Repo: https://github.com/TheHolyOneZ/Zircon-UE-Dumper

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[unreal-object-model]] · [[dumper-7]] · [[uedumper]] · [[uedumper-memprocfs]] · [[re-ue4ss]] · [[frida]]
