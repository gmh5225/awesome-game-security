---
title: Kernel Callbacks
kind: concept
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/skills/windows-kernel.md
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/zer0condition__BusterCall.md
  - wiki/sources/descriptions/yyl-20020115__OpenArk.md
  - wiki/sources/descriptions/yardenshafir__SymlinkCallback.md
  - wiki/sources/descriptions/wesmar__VaultGuard.md
  - wiki/sources/descriptions/wavestone-cdt__EDRSandblast.md
  - wiki/sources/descriptions/sbsbsbssbsbs__boundcallback.md
  - wiki/sources/descriptions/vovasicidk__sentinelac.md
updated: 2026-07-24
confidence: high
---

# Kernel Callbacks

Windows notify/object registration APIs used by anti-cheat and EDR to observe process/thread creation, image loads, handle operations, registry, and file I/O. (source: wiki/sources/skills/windows-kernel.md)

## Common APIs

- `PsSetCreateProcessNotifyRoutine(Ex/2)`, `PsSetCreateThreadNotifyRoutine(Ex)`
- `PsSetLoadImageNotifyRoutine(Ex)`
- `ObRegisterCallbacks` (handle create/duplicate) — defensive AC skeletons such as [[sentinelac]] use Ob + load-image notify for process protection and unauthorized-driver detection (source: wiki/sources/descriptions/vovasicidk__sentinelac.md)
- `CmRegisterCallback(Ex)`, minifilter `FltRegisterFilter`
- `KeRegisterBoundCallback` — research sample [[boundcallback]] (cheat / driver-communication lane) (source: wiki/sources/descriptions/sbsbsbssbsbs__boundcallback.md)

## Attack / defense

Attackers with kernel R/W ([[byovd]]) may try to unlink or patch callback lists; hypervisor EPT write-protection is a modern counter. EFI/bootkits can avoid some load-image signals entirely. Research tooling such as [[bustercall]] enumerates process/thread/image/registry callbacks by owning driver and can selectively remove or patch them. (source: wiki/sources/descriptions/zer0condition__BusterCall.md) EDR-evasion toolkits such as [[edrsandblast]] patch/remove process and thread notify callbacks (plus ETW TI and ntdll unhook) via BYOVD. (source: wiki/sources/descriptions/wavestone-cdt__EDRSandblast.md) Defensive anti-rootkit GUIs such as [[openark]] also enumerate callbacks (plus SSDT/drivers/objects) for rootkit hunting and system analysis. (source: wiki/sources/descriptions/yyl-20020115__OpenArk.md) Object-level research such as [[symlink-callback]] replaces a symlink `LinkTarget` with a callback fired on access—relevant to Ring0 callback / AC defensive study. (source: wiki/sources/descriptions/yardenshafir__SymlinkCallback.md) Defensive FSFilter / process-access blockers such as [[vaultguard]] (x64 MASM minifilter + driver; hide/lock/RO/block-exec; anti-debug) illustrate the same Flt/Ob surfaces from the protection side. (source: wiki/sources/descriptions/wesmar__VaultGuard.md)

## Related

[[byovd]] · [[hvci]] · [[bustercall]] · [[boundcallback]] · [[edrsandblast]] · [[openark]] · [[symlink-callback]] · [[vaultguard]] · [[sentinelac]] · [[vanguard]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
