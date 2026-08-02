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
  - wiki/sources/descriptions/notscimmy__libelevate.md
  - wiki/sources/descriptions/nlepleux__MappedCallback.md
  - wiki/sources/descriptions/kkent030315__Van1338.md
updated: 2026-08-02
confidence: high
---

# Kernel Callbacks

Windows notify/object registration APIs used by anti-cheat and EDR to observe process/thread creation, image loads, handle operations, registry, and file I/O. (source: wiki/sources/skills/windows-kernel.md)

## Common APIs

- `PsSetCreateProcessNotifyRoutine(Ex/2)`, `PsSetCreateThreadNotifyRoutine(Ex)`
- `PsSetLoadImageNotifyRoutine(Ex)`
- `ObRegisterCallbacks` (handle create/duplicate) — defensive AC skeletons such as [[sentinelac]] use Ob + load-image notify for process protection and unauthorized-driver detection (source: wiki/sources/descriptions/vovasicidk__sentinelac.md); offensive handle-elevation research such as [[libelevate]] studies obtaining full-access process handles past AC/security strip restrictions for memory R/W (source: wiki/sources/descriptions/notscimmy__libelevate.md); timing-attack handle-elevation PoC [[van1338]] explores object-callback design complexity for AC engineers / stress testing (source: wiki/sources/descriptions/kkent030315__Van1338.md)
- `CmRegisterCallback(Ex)`, minifilter `FltRegisterFilter`
- `KeRegisterBoundCallback` — research sample [[boundcallback]] (cheat / driver-communication lane) (source: wiki/sources/descriptions/sbsbsbssbsbs__boundcallback.md)

## Attack / defense

Attackers with kernel R/W ([[byovd]]) may try to unlink or patch callback lists; hypervisor EPT write-protection is a modern counter. EFI/bootkits can avoid some load-image signals entirely. Research tooling such as [[bustercall]] enumerates process/thread/image/registry callbacks by owning driver and can selectively remove or patch them. (source: wiki/sources/descriptions/zer0condition__BusterCall.md) EDR-evasion toolkits such as [[edrsandblast]] patch/remove process and thread notify callbacks (plus ETW TI and ntdll unhook) via BYOVD. (source: wiki/sources/descriptions/wavestone-cdt__EDRSandblast.md) Defensive anti-rootkit GUIs such as [[openark]] also enumerate callbacks (plus SSDT/drivers/objects) for rootkit hunting and system analysis. (source: wiki/sources/descriptions/yyl-20020115__OpenArk.md) Object-level research such as [[symlink-callback]] replaces a symlink `LinkTarget` with a callback fired on access—relevant to Ring0 callback / AC defensive study. (source: wiki/sources/descriptions/yardenshafir__SymlinkCallback.md) Defensive FSFilter / process-access blockers such as [[vaultguard]] (x64 MASM minifilter + driver; hide/lock/RO/block-exec; anti-debug) illustrate the same Flt/Ob surfaces from the protection side. (source: wiki/sources/descriptions/wesmar__VaultGuard.md) Hide-callback research such as [[mapped-callback]] plants a JMP in a legit-module codecave (e.g. APCI, outside [[patchguard]]) so the registered routine’s start address resolves inside a valid image. (source: wiki/sources/descriptions/nlepleux__MappedCallback.md)

## Related

[[byovd]] · [[hvci]] · [[bustercall]] · [[boundcallback]] · [[mapped-callback]] · [[edrsandblast]] · [[openark]] · [[symlink-callback]] · [[vaultguard]] · [[sentinelac]] · [[libelevate]] · [[van1338]] · [[vanguard]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
