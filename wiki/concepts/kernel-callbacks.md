---
title: Kernel Callbacks
kind: concept
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/skills/windows-kernel.md
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/zer0condition__BusterCall.md
updated: 2026-07-17
confidence: high
---

# Kernel Callbacks

Windows notify/object registration APIs used by anti-cheat and EDR to observe process/thread creation, image loads, handle operations, registry, and file I/O. (source: wiki/sources/skills/windows-kernel.md)

## Common APIs

- `PsSetCreateProcessNotifyRoutine(Ex/2)`, `PsSetCreateThreadNotifyRoutine(Ex)`
- `PsSetLoadImageNotifyRoutine(Ex)`
- `ObRegisterCallbacks` (handle create/duplicate)
- `CmRegisterCallback(Ex)`, minifilter `FltRegisterFilter`

## Attack / defense

Attackers with kernel R/W ([[byovd]]) may try to unlink or patch callback lists; hypervisor EPT write-protection is a modern counter. EFI/bootkits can avoid some load-image signals entirely. Research tooling such as [[bustercall]] enumerates process/thread/image/registry callbacks by owning driver and can selectively remove or patch them. (source: wiki/sources/descriptions/zer0condition__BusterCall.md)

## Related

[[byovd]] · [[hvci]] · [[bustercall]] · [[vanguard]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
