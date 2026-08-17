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
  - wiki/sources/descriptions/hfiref0x__WinObjEx64.md
  - wiki/sources/descriptions/gmh5225__kernel-callback-functions-list.md
  - wiki/sources/descriptions/gmh5225__KernelSnippets.md
  - wiki/sources/descriptions/gmh5225__RToolZ.md
  - wiki/sources/descriptions/gmh5225__PsNotifRoutineUnloader.md
  - wiki/sources/descriptions/ch3rn0byl__WinDbg-Extensions.md
  - wiki/sources/descriptions/br-sn__CheekyBlinder.md
updated: 2026-08-17
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

## Reference

Documentation catalogs such as [[kernel-callback-functions-list]] list Windows Ring0 callback registration APIs for anti-cheat engineers and defensive researchers—not a live enumeration or patch tool. (source: wiki/sources/descriptions/gmh5225__kernel-callback-functions-list.md) Live attach enumeration during kernel debugging via [[windbg-extensions]] walks `PspCreateProcessNotifyRoutine`, `PspCreateThreadNotifyRoutine`, and `PspLoadImageNotifyRoutine` with per-type filters (process/thread/image/all) and resolving driver modules—useful for rootkit and AC driver inspection. (source: wiki/sources/descriptions/ch3rn0byl__WinDbg-Extensions.md) Reusable kernel-mode code patterns such as [[kernel-snippets]] collect copy-paste callback registration, memory, and process-manipulation snippets for driver development—not a full framework. (source: wiki/sources/descriptions/gmh5225__KernelSnippets.md)

## Attack / defense

Attackers with kernel R/W ([[byovd]]) may try to unlink or patch callback lists; hypervisor EPT write-protection is a modern counter. EFI/bootkits can avoid some load-image signals entirely. Research tooling such as [[bustercall]] enumerates process/thread/image/registry callbacks by owning driver and can selectively remove or patch them. (source: wiki/sources/descriptions/zer0condition__BusterCall.md) BYOVD callback PoCs such as [[cheeky-blinder]] enumerate and modify kernel callbacks via a signed vulnerable MSI driver. (source: wiki/sources/descriptions/br-sn__CheekyBlinder.md) EDR-evasion toolkits such as [[edrsandblast]] patch/remove process and thread notify callbacks (plus ETW TI and ntdll unhook) via BYOVD. (source: wiki/sources/descriptions/wavestone-cdt__EDRSandblast.md) Defensive anti-rootkit GUIs such as [[openark]] also enumerate callbacks (plus SSDT/drivers/objects) for rootkit hunting and system analysis. (source: wiki/sources/descriptions/yyl-20020115__OpenArk.md) Object Manager explorer [[winobjex64]] adds namespace inspection and callback enumeration for anti-cheat / Ring0 callback research (admin required for much of the namespace and object security editing). (source: wiki/sources/descriptions/hfiref0x__WinObjEx64.md) Object-level research such as [[symlink-callback]] replaces a symlink `LinkTarget` with a callback fired on access—relevant to Ring0 callback / AC defensive study. (source: wiki/sources/descriptions/yardenshafir__SymlinkCallback.md) Defensive FSFilter / process-access blockers such as [[vaultguard]] (x64 MASM minifilter + driver; hide/lock/RO/block-exec; anti-debug) illustrate the same Flt/Ob surfaces from the protection side. (source: wiki/sources/descriptions/wesmar__VaultGuard.md) Hide-callback research such as [[mapped-callback]] plants a JMP in a legit-module codecave (e.g. APCI, outside [[patchguard]]) so the registered routine’s start address resolves inside a valid image. (source: wiki/sources/descriptions/nlepleux__MappedCallback.md) Offensive callback/process manipulation utilities such as [[rtoolz]] (gmh5225; driver-backed hide/unhide processes, callback enumeration/removal, notification-routine removal, process protection-level manipulation; rootkit-technique study) sit in the same offensive Ring0 lane. (source: wiki/sources/descriptions/gmh5225__RToolZ.md) Focused notify-routine unloaders such as [[ps-notif-routine-unloader]] (gmh5225; enumerate `PsSetCreateProcessNotifyRoutine` and selectively remove process/thread/image notify entries from AC/security drivers; `RTCore64.sys` backend) target the same blind-callback evasion surface. (source: wiki/sources/descriptions/gmh5225__PsNotifRoutineUnloader.md)

## Related

[[byovd]] · [[hvci]] · [[bustercall]] · [[cheeky-blinder]] · [[boundcallback]] · [[mapped-callback]] · [[edrsandblast]] · [[openark]] · [[winobjex64]] · [[windbg-extensions]] · [[rtoolz]] · [[ps-notif-routine-unloader]] · [[kernel-callback-functions-list]] · [[kernel-snippets]] · [[function-collections]] · [[symlink-callback]] · [[vaultguard]] · [[sentinelac]] · [[libelevate]] · [[van1338]] · [[vanguard]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
