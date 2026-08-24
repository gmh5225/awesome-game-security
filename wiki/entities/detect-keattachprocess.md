---
title: Detect-KeAttachProcess
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/KANKOSHEV__Detect-KeAttachProcess.md
updated: 2026-08-24
confidence: medium
---

# Detect-KeAttachProcess

**Kernel research sample** for detecting **`KeAttachProcess` usage** on Windows (KANKOSHEV). Enumerates processes and their threads, then inspects **thread context data** to identify **unexpected attached target processes**. Packaged as a **continuously running kernel driver** built with Visual Studio C/C++ tooling. Primarily relevant to **anti-cheat** and **security monitoring** scenarios where **covert process attachment** is a threat—not a production enforcement stack. (source: wiki/sources/descriptions/KANKOSHEV__Detect-KeAttachProcess.md)

Complements offensive cross-process attach and hook lanes such as [[driver-kdtour]] (sample `KeAttachProcess` inline hook), MDL/CR3 cross-process R/W helpers such as [[ntmemory]], and KANKOSHEV driver-backed injection samples such as [[face-injector-v2]] when threat-modeling covert kernel memory access paths.

## Links

- Repo: https://github.com/KANKOSHEV/Detect-KeAttachProcess

## Related

[[driver-kdtour]] · [[ntmemory]] · [[face-injector-v2]] · [[detect-mouseclassservicecallback]] · [[windows-kernel-rs]] · [[driver-read-write]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
