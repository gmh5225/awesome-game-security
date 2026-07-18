---
title: Game Hacking
kind: overview
topics: [game-hacking]
sources:
  - wiki/sources/skills/game-hacking.md
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/zyhp__vac3_inhibitor.md
  - wiki/sources/descriptions/x1tan__vac3-dumper.md
  - wiki/sources/descriptions/zodiacon__TotalPE2.md
  - wiki/sources/descriptions/zodiacon__QuickAsm.md
  - wiki/sources/descriptions/zoand__Injectors.md
  - wiki/sources/descriptions/zoand__BOOM.md
  - wiki/sources/descriptions/zinx-YT__Fortnite-Fltokens-and-offsets.md
  - wiki/sources/descriptions/zhuzhu-Top__deobf.md
  - wiki/sources/descriptions/zhuowei__cheese.md
  - wiki/sources/descriptions/zhitkur__DayZzz.md
  - wiki/sources/descriptions/zhaodice__proxmox-ve-anti-detection.md
  - wiki/sources/descriptions/zhaodice__qemu-anti-detection.md
  - wiki/sources/descriptions/xqemu__xqemu.md
  - wiki/sources/descriptions/xkevio__kevboy.md
  - wiki/sources/descriptions/zer0condition__NTMemory.md
  - wiki/sources/descriptions/zengfr__XrefsExt.md
  - wiki/sources/descriptions/za233__IDADeflat.md
  - wiki/sources/descriptions/z1ko__mutaben.md
  - wiki/sources/descriptions/yubie-re__ida-jm-xorstr-decrypt-plugin.md
  - wiki/sources/descriptions/ys1231__MoveCertificate.md
  - wiki/sources/descriptions/yourmnbbn__tiny-csgo-client.md
  - wiki/sources/descriptions/whereisr0da__Lumina-Cheat.md
  - wiki/sources/descriptions/younasiqw__BattleField-1-Internal.md
  - wiki/sources/descriptions/yoshisaac__CounterStrikeSource-Linux-Trainer.md
  - wiki/sources/descriptions/yoshisaac__CounterStrike2-Linux-Cheat.md
  - wiki/sources/descriptions/ymdzq__OFRP-device_xiaomi_mondrian.md
  - wiki/sources/descriptions/yinleiCoder__cs2-cheat-cpp.md
  - wiki/sources/descriptions/xvorost__CS-2-Glow.md
  - wiki/sources/descriptions/yhnu__op7t.md
  - wiki/sources/descriptions/yabinc__simpleperf_demo.md
  - wiki/sources/descriptions/yellowbyte__opaque-predicates-detective.md
  - wiki/sources/descriptions/yaxinsn__vermagic.md
  - wiki/sources/descriptions/xtremegamer1__vmdevirt-vtil.md
  - wiki/sources/descriptions/xp987__symbridge.md
  - wiki/sources/descriptions/xoxor4d__gta4-rtx.md
  - wiki/sources/descriptions/xo1337__steam-overlay-x64.md
  - wiki/sources/descriptions/xmmword__dpatch.md
  - wiki/sources/descriptions/xkp95175333__Thetan_ArenaSDK.md
  - wiki/sources/descriptions/xiaoxindada__magiskboot_ndk_on_linux.md
  - wiki/sources/descriptions/xetzzy__Fortnite-External-Source.md
  - wiki/sources/descriptions/xenia-project__xenia.md
  - wiki/sources/descriptions/wmarti__xenia-mac.md
  - wiki/sources/descriptions/xemu-project__xemu.md
  - wiki/sources/descriptions/xan105__Mini-Launcher.md
  - wiki/sources/descriptions/xakepru__x14.08-coverstory-blizzard.md
  - wiki/sources/descriptions/xPasters__.data-ptr-swap.md
  - wiki/sources/descriptions/x64dbg__x64dbgbinja.md
  - wiki/sources/descriptions/x64dbg__x64dbg.md
  - wiki/sources/descriptions/x64dbg__SlothBP.md
  - wiki/sources/descriptions/x64dbg__DotX64Dbg.md
  - wiki/sources/descriptions/x64dbg__Classroom.md
  - wiki/sources/descriptions/x-spy__CVE-2026-43499-popsicle.md
  - wiki/sources/descriptions/wtsxDev__reverse-engineering.md
  - wiki/sources/descriptions/wiresock__ndisapi.md
  - wiki/sources/descriptions/wilszdev__SteamAntiAntiDebug.md
  - wiki/sources/descriptions/wietze__windows-dll-hijacking.md
  - wiki/sources/descriptions/wietze__HijackLibs.md
  - wiki/sources/descriptions/westfox-5__GhidraMetrics.md
  - wiki/sources/descriptions/wesmar__KeyboardKit.md
  - wiki/sources/descriptions/wesmar__EfiTool.md
  - wiki/sources/descriptions/weizhking__PalworldSaved.md
  - wiki/sources/descriptions/weedeej__ValorantCC.md
  - wiki/sources/descriptions/weak1337__SkipHook.md
  - wiki/sources/descriptions/weak1337__NvidiaApi.md
  - wiki/sources/descriptions/weak1337__ModExMap.md
  - wiki/sources/descriptions/weak1337__EvCommunication.md
  - wiki/sources/descriptions/weak1337__CEDetector.md
updated: 2026-07-18
confidence: high
---





# Game Hacking

Offensive technique taxonomy and threat model: how cheats escalate from user-mode memory/injection to kernel drivers, hypervisors, EFI, and [[dma]] as defenders raise the bar. (source: wiki/sources/skills/game-hacking.md)

## Escalation model

1. **User-mode** — RPM/WPM, DLL/shellcode injection, graphics/input hooks
2. **Kernel-mode** — signed/vulnerable drivers ([[byovd]]), callback/page-table work; cross-process R/W via MDL/CR3 helpers such as [[ntmemory]] (source: wiki/sources/descriptions/zer0condition__NTMemory.md)
3. **Below the OS** — hypervisor, PCIe DMA, external devices / second machines

## Key sub-areas

- Memory, injection, hooking (inline/IAT/VTable/HWBP); injection-testing samples such as [[injectors]] for AC stress evaluation. (source: wiki/sources/descriptions/zoand__Injectors.md) User-mode PE manual-map injectors such as [[modexmap]] (VirtualAllocEx/WPM + import/reloc/TLS; CreateRemoteThread entry stub; x86/x64) sit in the Extend Manual Map lane. (source: wiki/sources/descriptions/weak1337__ModExMap.md) Trampoline-based prologue skip (first-instruction bypass of JMP/INT3 AC hooks) via [[skiphook]] (HDE length decode; local trampoline → `instruction+1`). (source: wiki/sources/descriptions/weak1337__SkipHook.md) Cheat Engine stealth configs can be checked against multi-vector detectors such as [[cedetector]] (window class / process / driver / debug artifacts). (source: wiki/sources/descriptions/weak1337__CEDetector.md) DLL Hijack surface catalogs such as [[windows-dll-hijacking]] and [[hijacklibs]] map relative-path / sideload / phantom-DLL load paths and disclosed hijack opportunities (DLL names, required exports, conditions) across Windows binaries. (source: wiki/sources/descriptions/wietze__windows-dll-hijacking.md) (source: wiki/sources/descriptions/wietze__HijackLibs.md) Kernel keyboard-filter / IRP-hook keylog research such as [[keyboardkit]] (UDP log exfil + ExplorerFrame DLL-hijack persistence) sits in the input-filter and DLL Hijack persistence lanes. (source: wiki/sources/descriptions/wesmar__KeyboardKit.md)
- Packet sniff/filter at NDIS via user-mode libs such as [[ndisapi]] (Windows Packet Filter driver interface; inspect/modify raw packets with low overhead). (source: wiki/sources/descriptions/wiresock__ndisapi.md)
- Launcher Abuser / platform-bypass launchers such as [[mini-launcher]] (Steam API stub + env/SteamAppID setup; DLL injection + Lua scripting) for out-of-client game start. (source: wiki/sources/descriptions/xan105__Mini-Launcher.md)
- Visual ESP / aim / movement cheats; AI visual pipelines (OBS + YOLO + HID)
- Overlays via [[present-hook]] and external/DWM/Steam windows; Steam-overlay samples such as [[steam-overlay-x64]] (C; modding / memory analysis). (source: wiki/sources/descriptions/xo1337__steam-overlay-x64.md)
- HWID spoofing, stack spoofing, driver communication channels (e.g. [[boom]] hijacks `Beep.sys` and alters hide/comm paths; [[data-ptr-swap]] studies `NtSetCompositionSurfaceAnalogExclusive` as a kernel-side channel; [[evcommunication]] uses named events + `NtTokenManager` hook instead of IOCTL). GPU serial / board fingerprinting via undocumented NvAPI is illustrated by [[nvidiaapi]] (`nvapi64.dll` + `NvAPI_QueryInterface`). (source: wiki/sources/descriptions/zoand__BOOM.md) (source: wiki/sources/descriptions/xPasters__.data-ptr-swap.md) (source: wiki/sources/descriptions/weak1337__EvCommunication.md) (source: wiki/sources/descriptions/weak1337__NvidiaApi.md)
- EFI boot-time mappers and pre-kernel privilege demos such as [[efitool]] (`ExitBootServices` in-RAM `SYSTEM` hive patch → SYSTEM `cmd.exe`; no disk writes / no kernel driver); engine-specific paths (Unreal/Unity/Source). (source: wiki/sources/descriptions/wesmar__EfiTool.md)
- AC-system exploration repos (e.g. [[vac3-inhibitor]] for VAC3 hooking/memory work; [[vac3-dumper]] for timed multi-module VAC dumps) sit in the user-mode lane of cheat research. (source: wiki/sources/descriptions/zyhp__vac3_inhibitor.md) (source: wiki/sources/descriptions/x1tan__vac3-dumper.md)
- Blizzard / WoW Warden research samples such as [[x14-08-coverstory-blizzard]] (C++; memory scan / code patch / Warden loader hooks / RunScript via HacksController) sit in the same user-mode AC-exploration lane. (source: wiki/sources/descriptions/xakepru__x14.08-coverstory-blizzard.md)

- Curated RE learning indexes such as [[reverse-engineering]] (reversing / networking / editors) sit in the Cheat guide lane for offensive technique study. (source: wiki/sources/descriptions/wtsxDev__reverse-engineering.md)
- PE triage of game/client modules (imports, TLS, .NET metadata) via viewers such as [[totalpe2]] before deeper RE. (source: wiki/sources/descriptions/zodiacon__TotalPE2.md)
- Rapid x86/x64 shellcode/asm prototyping with [[quickasm]] (assemble via Keystone, execute in-process). (source: wiki/sources/descriptions/zodiacon__QuickAsm.md)
- Title-specific offset/token dumps (e.g. Fortnite FLTokens via [[fortnite-fltokens-and-offsets]]) illustrate ephemeral cheat-research artifacts that rot quickly. (source: wiki/sources/descriptions/zinx-YT__Fortnite-Fltokens-and-offsets.md)
- External Fortnite samples such as [[fortnite-external-source]] (C++; driver development / SDK generation) sit in the cheat / game:fortnite lane. (source: wiki/sources/descriptions/xetzzy__Fortnite-External-Source.md)
- MBA expression generators such as [[mutaben]] (Python) sit in the Cheat Mixed boolean-arithmetic lane. (source: wiki/sources/descriptions/z1ko__mutaben.md)
- Fix OLLVM / deobfuscation plugins targeting `libtprt.so` (e.g. [[deobf]]) sit in the Cheat Fix OLLVM lane. (source: wiki/sources/descriptions/zhuzhu-Top__deobf.md)
- IDA CFF deflattening via [[idadeflat]] (angr-backed semi-auto CFG recover/patch) also sits in that Fix OLLVM / deflat lane. (source: wiki/sources/descriptions/za233__IDADeflat.md)
- Fix VMP / VTIL demos such as [[vmdevirt-vtil]] (broken VTIL compile path; multi-`vmenter` → jmp into compiled VTIL for IDA) sit in the Cheat Fix VMP lane. (source: wiki/sources/descriptions/xtremegamer1__vmdevirt-vtil.md)
- Opaque-predicate detection via [[opaque-predicates-detective]] (invariant-expression / BB-local damage) sits in the Cheat Binary Ninja Plugins lane. (source: wiki/sources/descriptions/yellowbyte__opaque-predicates-detective.md)
- Windows x86/x64 debugging via [[x64dbg]] (feature-rich debugger + plugin system) is a core Cheat Debugging lane tool for offensive RE. (source: wiki/sources/descriptions/x64dbg__x64dbg.md)
- Steam anti-anti-debug helpers such as [[steam-anti-anti-debug]] (patch Steam debug detection so [[x64dbg]] can attach to protected game processes) sit in the Steam / Cheat Debugging research lane. (source: wiki/sources/descriptions/wilszdev__SteamAntiAntiDebug.md)
- Binary Ninja ↔ x64dbg plugin work such as [[x64dbgbinja]] (Python BN plugin from the x64dbg org) sits in the Cheat Binary Ninja / x64dbg Plugins lane. (source: wiki/sources/descriptions/x64dbg__x64dbgbinja.md)
- Collaborative breakpoint management via [[slothbp]] (x64dbg plugin; C/C++) sits in the Cheat x64dbg Plugins lane. (source: wiki/sources/descriptions/x64dbg__SlothBP.md)
- Managed .NET 6 / C# x64dbg plugin authoring via [[dotx64dbg]] (live edit/debug; custom commands/expressions) sits in the same Cheat x64dbg Plugins lane. (source: wiki/sources/descriptions/x64dbg__DotX64Dbg.md)
- OOP analysis via [[classroom]] (define member functions/variables while debugging; persisted class docs) sits in the Cheat x64dbg Plugins lane. (source: wiki/sources/descriptions/x64dbg__Classroom.md)
- IDA Plugins such as [[xrefsext]] (extended xrefs) and [[ida-jm-xorstr-decrypt-plugin]] (JM Xorstr decrypt on some x64 binaries) support cheat-side static RE workflows. (source: wiki/sources/descriptions/zengfr__XrefsExt.md) (source: wiki/sources/descriptions/yubie-re__ida-jm-xorstr-decrypt-plugin.md)
- Ghidra Plugins such as [[ghidrametrics]] (cyclomatic complexity / function size / call depth; headless + JSON) support native-code metric triage in the Cheat Ghidra Plugins lane. (source: wiki/sources/descriptions/westfox-5__GhidraMetrics.md)
- Live IDA ↔ x64dbg annotation/type sync via [[symbridge]] (names/comments/structs; module+RVA; Python broker) bridges static and dynamic RE on the same binary. (source: wiki/sources/descriptions/xp987__symbridge.md)
- Magisk-style root on Android VR (Quest 3/3S) via [[cheese]] (Adreno CVE-2025-21479; temporary root, no boot rewrite) sits in the Cheat Magisk lane. (source: wiki/sources/descriptions/zhuowei__cheese.md)
- Magisk/KernelSU/APatch modules such as [[move-certificate]] (user→system CA trust, Android 7–15) support MITM-oriented mobile cheat research. (source: wiki/sources/descriptions/ys1231__MoveCertificate.md)
- Boot-image tooling such as [[magiskboot-ndk-on-linux]] (standalone NDK-on-Linux magiskboot for unpack/repack/ramdisk) sits in the Cheat Magisk / Boot Image Modification Tool lane. (source: wiki/sources/descriptions/xiaoxindada__magiskboot_ndk_on_linux.md)
- Custom recovery / ROM device trees such as [[ofrp-device-xiaomi-mondrian]] (OFRP for Redmi K60 Pro / mondrian) sit in the Android bootloader/ROM/root lane. (source: wiki/sources/descriptions/ymdzq__OFRP-device_xiaomi_mondrian.md)
- DIY Android kernel explorers such as [[op7t]] sit in the Cheat Android kernel explorer lane. (source: wiki/sources/descriptions/yhnu__op7t.md)
- Android Kernel CVE PoCs such as [[cve-2026-43499-popsicle]] (Xiaomi popsicle LPE via CVE-2026-43499; LD_PRELOAD; uid 0 + SELinux disabled) sit in the Cheat Android Kernel CVE lane. (source: wiki/sources/descriptions/x-spy__CVE-2026-43499-popsicle.md)
- Syscall dispatcher patching PoCs such as [[dpatch]] (writable syscall-table copy + dispatcher jump to custom handler) sit in the Cheat Hook syscall / Android kernel explorer lane. (source: wiki/sources/descriptions/xmmword__dpatch.md)
- Android app perf profiling demos such as [[simpleperf-demo]] (simpleperf / Perf) sit adjacent to that Android explorer / cheat research lane. (source: wiki/sources/descriptions/yabinc__simpleperf_demo.md)
- Linux LKM vermagic/CRC rewriting via [[vermagic]] sits in the Cheat Linux / RE tools lane (load modules across mismatched kernel builds). (source: wiki/sources/descriptions/yaxinsn__vermagic.md)
- Title-specific DayZ cheat/modding samples such as [[dayzzz]] (SDK generation + overlays) illustrate game:dayz offensive research surface. (source: wiki/sources/descriptions/zhitkur__DayZzz.md)
- Palworld save / editor tooling such as [[palworldsaved]] (rendering + editor; UE5) sits in the cheat / game:palworld [Save] lane. (source: wiki/sources/descriptions/weizhking__PalworldSaved.md)
- Minimal CS:GO dedicated-server clients such as [[tiny-csgo-client]] (C++; modding / SDK generation) sit in the cheat / game:csgo lane. (source: wiki/sources/descriptions/yourmnbbn__tiny-csgo-client.md)
- Internal CS:GO samples such as [[lumina-cheat]] emphasize mutation for a changing signature (Internal tag). (source: wiki/sources/descriptions/whereisr0da__Lumina-Cheat.md)
- Linux external CS:S trainers such as [[counterstrikesource-linux-trainer]] (movement automation + info display) sit in the cheat / game:css lane. (source: wiki/sources/descriptions/yoshisaac__CounterStrikeSource-Linux-Trainer.md)
- Linux external CS2 cheats such as [[counterstrike2-linux-cheat]] (C++; memory analysis) sit in the cheat / game:cs2 lane. (source: wiki/sources/descriptions/yoshisaac__CounterStrike2-Linux-Cheat.md)
- External CS2 samples such as [[cs2-cheat-cpp]] (C++; rendering / asset pipelines / SDK generation) also sit in the cheat / game:cs2 lane. (source: wiki/sources/descriptions/yinleiCoder__cs2-cheat-cpp.md)
- External CS2 glow ESP such as [[cs-2-glow]] (C++; entity parse / offsets / external memory glow) sits in the same cheat / game:cs2 visual lane. (source: wiki/sources/descriptions/xvorost__CS-2-Glow.md)
- Title-specific Battlefield 1 internals such as [[battlefield-1-internal]] (C++; DirectX / SDK generation / hooking) illustrate the cheat / game:battlefield 1 lane. (source: wiki/sources/descriptions/younasiqw__BattleField-1-Internal.md)
- Valorant crosshair-setting utilities such as [[valorantcc]] sit in the cheat / game:valorant lane (client config; Riot-owned assets/endpoints). (source: wiki/sources/descriptions/weedeej__ValorantCC.md)
- Title-specific Thetan Arena SDKs such as [[thetan-arenasdk]] (rendering / audio / physics) illustrate the cheat / game:thetan lane. (source: wiki/sources/descriptions/xkp95175333__Thetan_ArenaSDK.md)
- ASI Loader–based remaster bridges such as [[gta4-rtx]] (GTA IV Complete Edition → RTX Remix; custom runtime / light / wetness) illustrate DirectX compatibility tooling adjacent to graphics-mod research. (source: wiki/sources/descriptions/xoxor4d__gta4-rtx.md)
- Hidden-PVE / QEMU-KVM anti-detection (e.g. [[proxmox-ve-anti-detection]], [[qemu-anti-detection]] device-string spoof such as QEMU→ASUS keyboard) sits in the `Cheat > QEMU/KVM/PVE/VBOX` lane. (source: wiki/sources/descriptions/zhaodice__proxmox-ve-anti-detection.md) (source: wiki/sources/descriptions/zhaodice__qemu-anti-detection.md)
- Original Xbox software emulation via [[xqemu]] (full-machine QEMU, no hardware VT required) also sits in that QEMU/KVM research lane for title playback / RE. (source: wiki/sources/descriptions/xqemu__xqemu.md)
- Original Xbox LLE via [[xemu]] (QEMU fork; NV2A/MCPX/NForce/Pentium III; OpenGL + SDL2; ISO/XISO) sits in the console `Xbox` lane for hardware-internals / preservation study. (source: wiki/sources/descriptions/xemu-project__xemu.md)
- Game Boy hardware emulation via [[kevboy]] (Rust; CPU/memory/graphics/input + ROM formats) sits in the console `Game Boy` lane for emulator architecture study. (source: wiki/sources/descriptions/xkevio__kevboy.md)
- Xbox 360 emulation via [[xenia]] (C++; PowerPC recompiler, D3D12/Vulkan GPU, XAM/kernel/XEX) sits in the console `Xbox` lane for hardware-abstraction / binary-translation research. (source: wiki/sources/descriptions/xenia-project__xenia.md)
- macOS port [[xenia-mac]] extends that Xbox 360 HLE stack to Apple hosts for emulator / Xbox research. (source: wiki/sources/descriptions/wmarti__xenia-mac.md)

## Related concepts

[[dma]] · [[byovd]] · [[present-hook]] · [[il2cpp]] · [[kernel-callbacks]] · [[ndisapi]] · [[nvidiaapi]] · [[ntmemory]] · [[vac3-inhibitor]] · [[vac3-dumper]] · [[x14-08-coverstory-blizzard]] · [[reverse-engineering]] · [[totalpe2]] · [[quickasm]] · [[xrefsext]] · [[symbridge]] · [[x64dbg]] · [[x64dbgbinja]] · [[slothbp]] · [[dotx64dbg]] · [[classroom]] · [[steam-anti-anti-debug]] · [[ida-jm-xorstr-decrypt-plugin]] · [[ghidrametrics]] · [[injectors]] · [[modexmap]] · [[skiphook]] · [[cedetector]] · [[windows-dll-hijacking]] · [[hijacklibs]] · [[keyboardkit]] · [[mini-launcher]] · [[boom]] · [[data-ptr-swap]] · [[efitool]] · [[fortnite-fltokens-and-offsets]] · [[fortnite-external-source]] · [[mutaben]] · [[deobf]] · [[idadeflat]] · [[vmdevirt-vtil]] · [[opaque-predicates-detective]] · [[cheese]] · [[move-certificate]] · [[magiskboot-ndk-on-linux]] · [[ofrp-device-xiaomi-mondrian]] · [[op7t]] · [[dpatch]] · [[simpleperf-demo]] · [[vermagic]] · [[dayzzz]] · [[palworldsaved]] · [[tiny-csgo-client]] · [[lumina-cheat]] · [[counterstrikesource-linux-trainer]] · [[counterstrike2-linux-cheat]] · [[cs2-cheat-cpp]] · [[cs-2-glow]] · [[battlefield-1-internal]] · [[valorantcc]] · [[thetan-arenasdk]] · [[gta4-rtx]] · [[steam-overlay-x64]] · [[proxmox-ve-anti-detection]] · [[qemu-anti-detection]] · [[xqemu]] · [[xemu]] · [[kevboy]] · [[xenia]] · [[xenia-mac]] · [[overviews/anti-cheat]]




## README map

`Cheat` is the largest category (~2551 links): guides, debugging, packet sniff/capture, speedhack, RE tools, MBA/VMP/Themida/OLLVM fix lanes, DBI, Launcher Abuser, PatchGuard/DSE, Windows/Linux/Android kernel explorers, Magisk/Xposed/Frida/ART-syscall hooks, Android memory loading + App/Kernel CVE lanes, bootloader/ROM/root trees, Cellular/SIM + IoT, iOS jailbreak/network, plus `Some Tricks` (~112; Ring0/Ring3/Linux/Android). Adjacent console/emulator cats: `Nintendo Switch` (~7), `Xbox` (~7), `PlayStation` (~5; PS5 HV exploit / BD-JB / drive-clone research), `Game Boy` (~3), `Nintendo 3DS` / `GameCube/Wii`, plus `Linux Emulator` (~1). (source: wiki/sources/README-categories.md)
