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
  - wiki/sources/descriptions/V-i-x-x__kernel-callback-removal.md
  - wiki/sources/descriptions/GetRektBoy724__DCMB.md
  - wiki/sources/descriptions/zensenzay__wnf-driver-meme.md
  - wiki/sources/descriptions/UCFoxi__NotifyRoutineHijackThread.md
  - wiki/sources/descriptions/SurgeGotTappedAgain__Pink-Eye.md
  - wiki/sources/descriptions/Staatsgeheim__PsImageNotifyRoutineSpamFilter.md
  - wiki/sources/descriptions/Rycooop__Bloom-Anticheat.md
updated: 2026-08-25
confidence: high
---

# Kernel Callbacks

Windows notify/object registration APIs used by anti-cheat and EDR to observe process/thread creation, image loads, handle operations, registry, and file I/O. (source: wiki/sources/skills/windows-kernel.md)

## Common APIs

- `PsSetCreateProcessNotifyRoutine(Ex/2)`, `PsSetCreateThreadNotifyRoutine(Ex)`
- `PsSetLoadImageNotifyRoutine(Ex)`
- `ObRegisterCallbacks` (handle create/duplicate) — defensive AC skeletons such as [[sentinelac]] use Ob + load-image notify for process protection and unauthorized-driver detection (source: wiki/sources/descriptions/vovasicidk__sentinelac.md); offensive handle-elevation research such as [[libelevate]] studies obtaining full-access process handles past AC/security strip restrictions for memory R/W (source: wiki/sources/descriptions/notscimmy__libelevate.md); timing-attack handle-elevation PoC [[van1338]] explores object-callback design complexity for AC engineers / stress testing (source: wiki/sources/descriptions/kkent030315__Van1338.md); WNF-backed process-hardening drivers such as [[wnf-driver-meme]] (zensenzay; strip VM read/write, duplicate, suspend/resume on protected processes; covert KM↔UM comm without device objects) (source: wiki/sources/descriptions/zensenzay__wnf-driver-meme.md); multi-component AC prototypes such as [[bloom-anticheat]] (Rycooop; ObRegisterCallbacks protects AC + target processes from hostile handle ops; kernel+UM Windows x64 research scaffold) (source: wiki/sources/descriptions/Rycooop__Bloom-Anticheat.md)
- `CmRegisterCallback(Ex)`, minifilter `FltRegisterFilter`
- `KeRegisterBoundCallback` — research sample [[boundcallback]] (cheat / driver-communication lane) (source: wiki/sources/descriptions/sbsbsbssbsbs__boundcallback.md)

## Reference

Documentation catalogs such as [[kernel-callback-functions-list]] list Windows Ring0 callback registration APIs for anti-cheat engineers and defensive researchers—not a live enumeration or patch tool. (source: wiki/sources/descriptions/gmh5225__kernel-callback-functions-list.md) Live attach enumeration during kernel debugging via [[windbg-extensions]] walks `PspCreateProcessNotifyRoutine`, `PspCreateThreadNotifyRoutine`, and `PspLoadImageNotifyRoutine` with per-type filters (process/thread/image/all) and resolving driver modules—useful for rootkit and AC driver inspection. (source: wiki/sources/descriptions/ch3rn0byl__WinDbg-Extensions.md) Reusable kernel-mode code patterns such as [[kernel-snippets]] collect copy-paste callback registration, memory, and process-manipulation snippets for driver development—not a full framework. (source: wiki/sources/descriptions/gmh5225__KernelSnippets.md) Load-image notify hygiene samples such as [[ps-image-notify-routine-spam-filter]] (Staatsgeheim; filters noisy `PsImageNotifyRoutine` callbacks via `RtlWalkFrameChain` stack walking; practical callback hygiene for kernel monitoring and AC telemetry pipelines) complement enumeration catalogs. (source: wiki/sources/descriptions/Staatsgeheim__PsImageNotifyRoutineSpamFilter.md)

## Attack / defense

Attackers with kernel R/W ([[byovd]]) may try to unlink or patch callback lists; hypervisor EPT write-protection is a modern counter. EFI/bootkits can avoid some load-image signals entirely. Research tooling such as [[bustercall]] enumerates process/thread/image/registry callbacks by owning driver and can selectively remove or patch them. (source: wiki/sources/descriptions/zer0condition__BusterCall.md) BYOVD callback PoCs such as [[cheeky-blinder]] enumerate and modify kernel callbacks via a signed vulnerable MSI driver. (source: wiki/sources/descriptions/br-sn__CheekyBlinder.md) EDR-evasion toolkits such as [[edrsandblast]] patch/remove process and thread notify callbacks (plus ETW TI and ntdll unhook) via BYOVD. (source: wiki/sources/descriptions/wavestone-cdt__EDRSandblast.md) Defensive anti-rootkit GUIs such as [[openark]] also enumerate callbacks (plus SSDT/drivers/objects) for rootkit hunting and system analysis. (source: wiki/sources/descriptions/yyl-20020115__OpenArk.md) Object Manager explorer [[winobjex64]] adds namespace inspection and callback enumeration for anti-cheat / Ring0 callback research (admin required for much of the namespace and object security editing). (source: wiki/sources/descriptions/hfiref0x__WinObjEx64.md) Object-level research such as [[symlink-callback]] replaces a symlink `LinkTarget` with a callback fired on access—relevant to Ring0 callback / AC defensive study. (source: wiki/sources/descriptions/yardenshafir__SymlinkCallback.md) Defensive FSFilter / process-access blockers such as [[vaultguard]] (x64 MASM minifilter + driver; hide/lock/RO/block-exec; anti-debug) illustrate the same Flt/Ob surfaces from the protection side. (source: wiki/sources/descriptions/wesmar__VaultGuard.md) Hide-callback research such as [[mapped-callback]] plants a JMP in a legit-module codecave (e.g. APCI, outside [[patchguard]]) so the registered routine’s start address resolves inside a valid image. (source: wiki/sources/descriptions/nlepleux__MappedCallback.md) Anti-cheat callback and integrity-hook PoCs such as [[pink-eye]] (SurgeGotTappedAgain; KMDF-style driver; object-callback redirect via code caves plus selected integrity-check path tampering; AC research / defensive testing) extend the same offensive manipulation surface. (source: wiki/sources/descriptions/SurgeGotTappedAgain__Pink-Eye.md) Offensive callback/process manipulation utilities such as [[rtoolz]] (gmh5225; driver-backed hide/unhide processes, callback enumeration/removal, notification-routine removal, process protection-level manipulation; rootkit-technique study) sit in the same offensive Ring0 lane. (source: wiki/sources/descriptions/gmh5225__RToolZ.md) Dynamic callback-list discovery drivers such as [[dcmb]] (GetRektBoy724; C kernel driver; locates process/thread/image/registry/object/minifilter notify lists without hardcoded offsets or signature scans; debug-output learning PoC; AC/EDR callback inspection; README [Removing kernel callbacks]) complement offset-free enumeration beside PDB parsers such as [[kpdb]]. (source: wiki/sources/descriptions/GetRektBoy724__DCMB.md) Focused notify-routine unloaders such as [[ps-notif-routine-unloader]] (gmh5225; enumerate `PsSetCreateProcessNotifyRoutine` and selectively remove process/thread/image notify entries from AC/security drivers; `RTCore64.sys` backend) target the same blind-callback evasion surface. (source: wiki/sources/descriptions/gmh5225__PsNotifRoutineUnloader.md) Dedicated-thread hijack PoCs such as [[notify-routine-hijack-thread]] (UCFoxi; compact Visual Studio C++ driver; hijacks `PspCreateThreadNotifyRoutine` callback dispatch for AC/EDR evasion study; README [Hijack PspCreateThreadNotifyRoutine]) illustrate an alternate offensive lane beside bulk removal. (source: wiki/sources/descriptions/UCFoxi__NotifyRoutineHijackThread.md) ETW-TI provider enable-flag manipulation from kernel memory such as [[kernel-callback-removal]] (V-i-x-x; toggles provider state with an existing R/W primitive; WinDbg/IDA structure/offset discovery; README [Removing kernel callbacks]) extends the same Ring0 blind-telemetry research lane toward [[etw-threat-intelligence]]. (source: wiki/sources/descriptions/V-i-x-x__kernel-callback-removal.md)

## Related

[[byovd]] · [[hvci]] · [[bustercall]] · [[cheeky-blinder]] · [[boundcallback]] · [[mapped-callback]] · [[pink-eye]] · [[edrsandblast]] · [[kernel-callback-removal]] · [[dcmb]] · [[kpdb]] · [[openark]] · [[winobjex64]] · [[windbg-extensions]] · [[rtoolz]] · [[ps-notif-routine-unloader]] · [[ps-image-notify-routine-spam-filter]] · [[notify-routine-hijack-thread]] · [[kernel-callback-functions-list]] · [[kernel-snippets]] · [[function-collections]] · [[symlink-callback]] · [[vaultguard]] · [[sentinelac]] · [[bloom-anticheat]] · [[libelevate]] · [[van1338]] · [[wnf-driver-meme]] · [[vanguard]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
