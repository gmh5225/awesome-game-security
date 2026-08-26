---
title: BamExtensionTableHook
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/Dor00tkit__BamExtensionTableHook.md
updated: 2026-08-26
confidence: medium
---

# BamExtensionTableHook

Windows kernel proof of concept (Dor00tkit) for hooking **process notifications through the BAM extension table** instead of the standard `PsSetCreateProcessNotifyRoutine` callback array. The driver targets the extension-host path and swaps the **`bam!BampCreateProcessCallback`** pointer with a custom routine. Sample code demonstrates ntoskrnl offset-based lookup, callback pointer replacement, and temporary notify-mask handling. Intended for advanced anti-cheat and EDR research on callback bypasses, defensive visibility, and undocumented kernel internals. (source: wiki/sources/descriptions/Dor00tkit__BamExtensionTableHook.md)

Sits in the same offensive [[kernel-callbacks]] lane as notify-array hijacks such as [[notify-routine-hijack-thread]], selective unloaders such as [[ps-notif-routine-unloader]], and offset-free callback discovery such as [[dcmb]]—but routes through the BAM extension table rather than `PspCreateProcessNotifyRoutine` directly.

## Links

- Repo: https://github.com/Dor00tkit/BamExtensionTableHook [bam!BampCreateProcessCallback]

## Related

[[kernel-callbacks]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[notify-routine-hijack-thread]] · [[ps-notif-routine-unloader]] · [[mapped-callback]] · [[dcmb]] · [[bustercall]]
