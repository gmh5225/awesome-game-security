# Wiki Index

Compiled knowledge catalog for awesome-game-security.

> Maintained via `scripts/update-wiki-cli.py`. See [[AGENTS]] for schema.

## Overviews

- [Overview](overviews/overview.md) — project map; 40 README sections → skill topics (Cheat ~2551 / Anti Cheat ~595; Game Engine ~141; Image Codec; console Switch/Xbox/PS HV)
- [Anti-Cheat](overviews/anti-cheat.md) — layered AC; Detection:* + engine protection (~595); hybrid OS AC samples; Game Tools RCE + Windows Emulator AC
- [DMA Attack](overviews/dma-attack.md) — PCIe DMA via Cheat/Detection:DMA (~595) + WSF attestation
- [Game Engine](overviews/game-engine.md) — Unreal / Unity / Source / Godot / Lumix (~141); MCP/AI gamedev (~176); Image Codec + Testing/Tools/CI
- [Game Hacking](overviews/game-hacking.md) — Cheat taxonomy (~2551) + Some Tricks (~112); Launcher Abuser / console PS HV+BD-JB lanes
- [Graphics API](overviews/graphics-api.md) — DirectX (~33) / GL / Vulkan hooks, overlays, Image Codec
- [Mobile Security](overviews/mobile-security.md) — Android / iOS; memory-loading + App/Kernel CVE; WSA (~9), Gunyah/vphone emulators
- [Reverse Engineering](overviews/reverse-engineering.md) — RE tools, MBA/DBI, deobfuscation, packers; Windows Emulator + console/PS HV RE
- [Windows Kernel](overviews/windows-kernel.md) — callbacks, HVCI/CET/TPM attestation (~9), BYOVD, pool; Windows Emulator (~7) + WSL

## Concepts

- [BattlEye](concepts/battleye.md)
- [BYOVD](concepts/byovd.md)
- [DMA](concepts/dma.md)
- [Easy Anti-Cheat](concepts/easy-anti-cheat.md)
- [Frida](concepts/frida.md)
- [HVCI](concepts/hvci.md)
- [IL2CPP](concepts/il2cpp.md)
- [IOMMU](concepts/iommu.md)
- [Kernel Callbacks](concepts/kernel-callbacks.md)
- [PatchGuard](concepts/patchguard.md)
- [Present Hook](concepts/present-hook.md)
- [Vanguard](concepts/vanguard.md)

## Entities

- [2Pack](entities/2pack.md) — Rust PE & shellcode packer (EXE/DLL + raw; Anti Cheat → Binary Packer)
- [3D-Racing-Game](entities/3d-racing-game.md) — OpenGL racing game (M/N scene switch; Game Develop / OpenGL source)
- [BattleField-1-Internal](entities/battlefield-1-internal.md) — BF1 internal: DirectX / SDK generation / hooking (C++)
- [BE-Shellcode](entities/be-shellcode.md) — BattlEye UM shellcode dump/disasm (thread scan / VEH / modules)
- [android-proxy-mcp](entities/android-proxy-mcp.md) — Android HTTP/HTTPS capture MCP (mitmdump + SQLite + NL query)
- [apktool-mcp-server](entities/apktool-mcp-server.md) — MCP server wrapping apktool (Android RE suite)
- [AV-EDR-Killer](entities/av-edr-killer.md) — BYOVD via wsftprm.sys (IOCTL 0x22201C; PID kill)
- [awesome-educational-games](entities/awesome-educational-games.md) — curated educational games (editors / languages / programming; Game Develop Guide)
- [BlindEye](entities/blindeye.md) — BattlEye report-path pool-alloc drop (“Packet Fucker”)
- [BOOM](entities/boom.md) — hijack Beep.sys; stealth driver communication
- [BootBypass](entities/bootbypass.md) — Secure Boot / DSE / HVCI bypass (native; SeCiCallbacks / CI.dll)
- [BusterCall](entities/bustercall.md) — enumerate/patch kernel callbacks; HVCI PFN-swap research
- [CEDetector](entities/cedetector.md) — Cheat Engine detector (window/process/driver/debug; CE stealth test)

- [cet-research](entities/cet-research.md) — CET / shadow-stack research (C; Windows Security Features)
- [checkhv_um](entities/checkhv-um.md) — user-mode HV detection (CPUID / RDTSC / VMCS / signatures)
- [cheese](entities/cheese.md) — Quest 3/3S root via Adreno CVE-2025-21479 (Magisk, no boot rewrite)
- [Classroom](entities/classroom.md) — x64dbg OOP class docs (member funcs/vars; Cheat x64dbg Plugins)
- [CounterStrike2-Linux-Cheat](entities/counterstrike2-linux-cheat.md) — Linux external CS2 cheat (C++; memory analysis)
- [CS-2-Glow](entities/cs-2-glow.md) — external CS2 glow ESP (C++; entity / offsets / memory)
- [cs2-cheat-cpp](entities/cs2-cheat-cpp.md) — external CS2 cheat (C++; rendering / SDK generation)
- [CounterStrikeSource-Linux-Trainer](entities/counterstrikesource-linux-trainer.md) — Linux external CS:S trainer (movement / info display)
- [CVE-2026-43499-popsicle](entities/cve-2026-43499-popsicle.md) — Xiaomi popsicle Android 16 LPE (CVE-2026-43499; LD_PRELOAD; uid 0)
- [data-ptr-swap](entities/data-ptr-swap.md) — NtSetCompositionSurfaceAnalogExclusive kernel channel (C/C++)
- [DayZzz](entities/dayzzz.md) — DayZ cheat/modding: SDK generation + overlays (C/C++)
- [Demystifying-PatchGuard](entities/demystifying-patchguard.md) — educational C/C++ walkthrough of PatchGuard
- [deobf](entities/deobf.md) — libtprt.so OLLVM deobf / plugin hooks (Python)
- [DetectTpmSpoofing](entities/detect-tpm-spoofing.md) — KMDF: TPM 2.0 EK spoof detect (IOCTL vs TPM.sys cache)
- [DotX64Dbg](entities/dotx64dbg.md) — .NET 6 / C# x64dbg plugin framework (live edit; custom commands)
- [dpatch](entities/dpatch.md) — syscall dispatcher patching PoC (table copy + dispatcher jump)
- [eac-overlay](entities/eac-overlay.md) — EAC overlay PoC (ESP via alt surfaces / window manip; C++)
- [EfiTool](entities/efitool.md) — UEFI ExitBootServices in-RAM SYSTEM hive patch (SYSTEM shell; no disk/driver)
- [EtwExplorer](entities/etw-explorer.md) — GUI browse of ETW providers / event manifests
- [EvCommunication](entities/evcommunication.md) — named-event kernel↔UM channel (NtTokenManager; vs IOCTL)
- [FileRecoveryTool](entities/file-recovery-tool.md) — NTFS/FAT32/ExFAT disk forensics (MFT/USN/carving; Win32)

- [function-collections](entities/function-collections.md) — C PoCs for uncommon Ring3 paths (memory analysis; AC callback lane)
- [Fortnite-External-Source](entities/fortnite-external-source.md) — Fortnite external: driver / SDK generation (C++)
- [Fortnite-Fltokens-and-offsets](entities/fortnite-fltokens-and-offsets.md) — Fortnite FLToken/offset grabber (stale / offline)
- [GhidraMetrics](entities/ghidrametrics.md) — Ghidra native-code metrics (cyclomatic / size / call depth; headless JSON)
- [gta4-rtx](entities/gta4-rtx.md) — GTA IV RTX Remix compatibility (DirectX / ASI Loader remaster)
- [HijackLibs](entities/hijacklibs.md) — disclosed Windows DLL hijack DB (YAML + web UI; exports / conditions)
- [honor-of-kings-RE-research](entities/honor-of-kings-re-research.md) — Honor of Kings Android RE (ACE / libtersafe / IL2CPP / KernelPatch KPMs)
- [hv](entities/hv.md) — minimal Intel VT-x Type-2 hypervisor (VMX/VMCS learning)
- [ida-ios-helper](entities/ida-ios-helper.md) — IDA plugin for iOS reversing (vtable symbols required)
- [ida-jm-xorstr-decrypt-plugin](entities/ida-jm-xorstr-decrypt-plugin.md) — IDA Pro JM Xorstr decrypt (x64; Python)

- [IDADeflat](entities/idadeflat.md) — IDA Pro CFF deflatten (angr; OLLVM-style)
- [Il2cppSpy](entities/il2cpp-spy.md) — Unity IL2CPP APK disassembler / two-APK diff
- [imgui-ios-mod-menu](entities/imgui-ios-mod-menu.md) — iOS ImGui mod menu (cheat / render-draw)
- [Injectors](entities/injectors.md) — injection-testing harness (C/C++; AC stress)
- [InstrumentationCallbackSyscallLogger](entities/instrumentation-callback-syscall-logger.md) — Ring3 Instrumentation Callback on syscall return (AC / Windows)
- [Kagura](entities/kagura.md) — LLVM pass plugin: CFG/string obfuscation, anti-tamper, anti-debug (mobile/desktop/Wasm)
- [kevboy](entities/kevboy.md) — Rust Game Boy emulator (CPU / memory / graphics / input)
- [KeyboardKit](entities/keyboardkit.md) — kernel keyboard IRP filter keylogger (UDP exfil; ExplorerFrame DLL hijack)
- [KernelResearchKit](entities/kernel-research-kit.md) — Win11 25H2 boot-time DSE / SeCiCallbacks toolkit (manual map / IRP hijack / BYOVD)
- [kvc](entities/kvc.md) — DSE bypass via signed MS driver (`g_CiOptions` / skci / SeCiCallbacks; PP/PPL→LSASS)
- [KvcForensic](entities/kvcforensic.md) — LSASS credential forensics (MSV/WDigest/Kerberos/DPAPI; Win/Linux dumps)

- [lightsaber](entities/lightsaber.md) — iOS 18.4–18.6.2 userland exploit; JS inject SpringBoard (DarkSword-derived)
- [Lumina-Cheat](entities/lumina-cheat.md) — internal CS:GO; mutation for changing signature (cheat / game:csgo)
- [lsass-extend-mapper](entities/lsass-extend-mapper.md) — unsigned driver map via lsass address-space extend
- [magiskboot_ndk_on_linux](entities/magiskboot-ndk-on-linux.md) — NDK-on-Linux magiskboot (boot unpack/repack/ramdisk)
- [Mini-Launcher](entities/mini-launcher.md) — Steam-bypass game launcher (API stub / DLL inject / Lua; Launcher Abuser)
- [ModExMap](entities/modexmap.md) — user-mode PE manual-map DLL injector (x86/x64; TLS; Extend Manual Map)
- [mutaben](entities/mutaben.md) — Python MBA (mixed-boolean-arithmetic) expression generator
- [MoveCertificate](entities/move-certificate.md) — Magisk/KernelSU/APatch user→system CA module (Android 7–15)
- [ndisapi](entities/ndisapi.md) — user-mode Windows Packet Filter / NDIS packet inspect-modify API
- [NO_ACCESS_Protection](entities/no-access-protection.md) — PAGE_NOACCESS + VEH / single-step anti-tamper (vs external scanners)
- [NvidiaApi](entities/nvidiaapi.md) — undocumented NvAPI GPU serial / board fingerprint (HWID research)
- [NTMemory](entities/ntmemory.md) — kernel cross-process R/W (MDL / CR3 walk / physical translate)
- [NTSleuth](entities/ntsleuth.md) — Windows syscall extractor (ntdll/win32u PDB + disasm → JSON/C headers)
- [OFRP-device_xiaomi_mondrian](entities/ofrp-device-xiaomi-mondrian.md) — OFRP/TWRP device tree for Redmi K60 Pro (mondrian)
- [Obfusk8](entities/obfusk8.md) — C++17 compile-time/runtime obfuscation library (AC Compile Time)
- [opaque-predicates-detective](entities/opaque-predicates-detective.md) — Binary Ninja opaque-predicate detection (invariant / BB-local)
- [op7t](entities/op7t.md) — DIY Android kernel (cheat / Android kernel explorer)
- [OpenArk](entities/openark.md) — Qt anti-rootkit / kernel analysis (callbacks, SSDT, drivers)
- [Ophion](entities/ophion.md) — stealth Intel VT-x Type-2 HV (EPT; CPUID/CR4/TSC anti-detect)
- [PalworldSaved](entities/palworldsaved.md) — Palworld UE5 save/editor tooling (cheat / game:palworld [Save])
- [pe32-password](entities/pe32-password.md) — PE32 password binary packer (Anti Cheat → Binary Packer)
- [PresentHookDetection](entities/present-hook-detection.md) — BE-style IDXGISwapChain::Present hook check (dummy D3D11 + dxgi prologue)
- [PG1903](entities/pg1903.md) — Win10 1903 PatchGuard disable via context-page NX (Demo NX)

- [proxmox-ve-anti-detection](entities/proxmox-ve-anti-detection.md) — Hidden PVE / QEMU-KVM anti-detection (kernel)
- [qemu-anti-detection](entities/qemu-anti-detection.md) — Hidden QEMU (device-string / fingerprint spoof)
- [QuickAsm](entities/quickasm.md) — x86/x64 assemble-and-run GUI (Keystone)
- [reverse-engineering](entities/reverse-engineering.md) — curated RE awesome list (networking / editors; Cheat guide lane)
- [revert-mapper](entities/revert-mapper.md) — post-execution cleanup for manually mapped kernel drivers
- [ricochet-deobfuscator](entities/ricochet-deobfuscator.md) — Ricochet AC deobfuscator (C/C++; driver / memory analysis)
- [sbox](entities/sbox.md) — C++ compile-time AES-128 / S-box string obfuscation (Obfusk8 spin-off)
- [shredder-rs](entities/shredder-rs.md) — x86_64 polymorphic instruction shredding (Rust)
- [SkipHook](entities/skiphook.md) — trampoline skips first insn (bypass JMP/INT3 AC hooks; HDE)
- [SlothBP](entities/slothbp.md) — x64dbg collaborative breakpoint manager (Cheat x64dbg Plugins)
- [simpleperf_demo](entities/simpleperf-demo.md) — Android simpleperf / Perf demo (app profiling)
- [Static-Variables-Obfuscator-UE4](entities/static-variables-obfuscator-ue4.md) — UE4 static-variable obfuscation vs memory scanners
- [SteamAntiAntiDebug](entities/steam-anti-anti-debug.md) — bypass Steam anti-debug for debugger attach (x64dbg; Steam)
- [steam-overlay-x64](entities/steam-overlay-x64.md) — Steam overlay / modding research (C; memory analysis)
- [Symbridge](entities/symbridge.md) — live IDA ↔ x64dbg annotation/type sync (module+RVA; Python broker)
- [SymlinkCallback](entities/symlink-callback.md) — symlink LinkTarget → access callback (Ring0 / AC research)
- [System Informer](entities/systeminformer.md) — Process Hacker successor; Windows process/system explorer (kernel explorer lane)
- [SystemThreadFinder](entities/system-thread-finder.md) — detect hidden/manual-map system threads (NtQuerySystemInformation; BE-style)
- [The-Seed-Link-Future](entities/the-seed-link-future.md) — Unity VR (C#; OpenGL / shader / driver-dev; Game Develop)
- [Thetan_ArenaSDK](entities/thetan-arenasdk.md) — Thetan Arena SDK (rendering / audio / physics; cheat lane)
- [TiEtwAgent](entities/tietwagent.md) — ETW Threat-Intelligence injection-detection agent (krabsetw / Yara / PPL)
- [TotalPE2](entities/totalpe2.md) — WPF PE viewer (headers, imports/exports, .NET metadata)
- [Tracy](entities/tracy.md) — C++ real-time frame profiler (CPU/GPU; Game Testing)
- [tiny-csgo-client](entities/tiny-csgo-client.md) — minimal CS:GO client for dedicated servers (modding / SDK)
- [ts-ue4dumper](entities/ts-ue4dumper.md) — TypeScript + Frida UE4 dumper (modular; C++ offsets)
- [UniCli](entities/unicli.md) — Unity Editor terminal CLI (compile/test/build/inspect; AI-agent ready)
- [unity-mcp](entities/unity-mcp.md) — MCP server for Unity (Game Develop / MCP workflow)
- [unitySpeedTools](entities/unityspeedtools.md) — iOS Unity IL2CPP speed/modding tools (C/C++ / ObjC)
- [unflutter](entities/unflutter.md) — Flutter/Dart AOT snapshot static analyzer (symbol recovery)
- [vac3_inhibitor](entities/vac3-inhibitor.md) — VAC3 exploration via hooking / memory analysis (C++)
- [vac3-dumper](entities/vac3-dumper.md) — VAC3 multi-module dumper (timed loads; explore anticheat:vac)
- [valorant-dumper](entities/valorant-dumper.md) — Valorant UE offset/SDK dumper (GObjects/GNames; Vanguard research)
- [ValorantCC](entities/valorantcc.md) — Valorant crosshair setting (cheat / game:valorant)
- [VaultGuard](entities/vaultguard.md) — FSFilter minifilter + process access block (x64 MASM; anti-debug/tamper)
- [veh-dumper](entities/veh-dumper.md) — x64 VEH/VCH → synthetic PE64 dumps for IDA
- [VEN0m-Ransomware](entities/ven0m-ransomware.md) — BYOVD via iMFForceDelete.sys (IObit; AV/EDR evasion)
- [vermagic](entities/vermagic.md) — change Linux LKM vermagic / CRCs (cheat / RE tools)
- [vmdevirt-vtil](entities/vmdevirt-vtil.md) — broken VTIL VMP devirt demo (Fix VMP / IDA jmp-around-vmenter)
- [wda_monitor_trick](entities/wda-monitor-trick.md) — WDA/D3D9 monitor hook (display capture intercept; C++)

- [WProtect](entities/wprotect.md) — C/C++ obfuscation engine (Anti Cheat → Obfuscation Engine)
- [WDUTF](entities/wdutf.md) — Windows Driver Unit Test Framework (user-space MSTest for kernel drivers)
- [WinDbg_Scripts](entities/windbg-scripts.md) — JS WinDbg scripts for kernel debug/modding (WinDbg Plugins)
- [windows-dll-hijacking](entities/windows-dll-hijacking.md) — Windows DLL hijack DB (sideload / search-order / phantom DLL)
- [windows-kernel-exploits](entities/windows-kernel-exploits.md) — kernel exploit guide (Cheat / vulnerable driver)
- [WinDefCtl](entities/windefctl.md) — Defender / Tamper Protection control via kernel priv-esc (Win11 26H1)
- [WinVisor](entities/winvisor.md) — WHP hypervisor emulator for Windows x64 user-mode PE (Windows Emulator)
- [vt-debuuger](entities/vt-debuuger.md) — hacked hypervisor testing (C/C++ drivers / plugins)

- [x14.08-coverstory-blizzard](entities/x14-08-coverstory-blizzard.md) — WoW cheat / Warden bypass (loader hooks / RunScript; C++)
- [x260-lenovo-opencore](entities/x260-lenovo-opencore.md) — ThinkPad X260 Hackintosh OpenCore EFI (macOS research host)
- [x64-EXE-Packer](entities/x64-exe-packer.md) — PE X64 binary packer (Anti Cheat → Binary Packer)
- [x64dbg](entities/x64dbg.md) — Windows x86/x64 debugger (plugins; Cheat Debugging)
- [x64dbgbinja](entities/x64dbgbinja.md) — Binary Ninja plugin (Python; x64dbg org; BN ↔ x64dbg lane)

- [x670e-tomahawk-anticheat-update](entities/x670e-tomahawk-anticheat-update.md) — MSI X670E Tomahawk BIOS v1KB DXE anti-cheat (option-ROM strip / NX)
- [xemu](entities/xemu.md) — original Xbox LLE emulator (QEMU fork; NV2A/OpenGL; ISO/XISO)
- [xenia](entities/xenia.md) — Xbox 360 emulator (PowerPC recompiler; D3D12/Vulkan; XEX)
- [xenia-mac](entities/xenia-mac.md) — macOS port of Xbox 360 emulator Xenia
- [xigmapper](entities/xigmapper.md) — EFI manual map (non-USB payload; Vanguard early-load research)
- [xqemu](entities/xqemu.md) — original Xbox via QEMU (software full-machine; Cheat QEMU/KVM lane)
- [XrefsExt](entities/xrefsext.md) — IDA Pro extended-xrefs plugin (cheat / IDA Plugins)
- [ZeroThreadKernel](entities/zero-thread-kernel.md) — threadless kernel exec via existing contexts / timers (vs AC thread enum)





## Sources

- Projected category map: `sources/README-categories.md` (generated on scan; 40 top-level sections)
- Skill projections: `sources/skills/`
- Description projections: `sources/descriptions/` (incremental only)
