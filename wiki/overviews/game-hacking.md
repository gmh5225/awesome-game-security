---
title: Game Hacking
kind: overview
topics: [game-hacking]
sources:
  - wiki/sources/skills/game-hacking.md
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/zyhp__vac3_inhibitor.md
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
  - wiki/sources/descriptions/zer0condition__NTMemory.md
  - wiki/sources/descriptions/zengfr__XrefsExt.md
  - wiki/sources/descriptions/za233__IDADeflat.md
  - wiki/sources/descriptions/z1ko__mutaben.md
  - wiki/sources/descriptions/yubie-re__ida-jm-xorstr-decrypt-plugin.md
  - wiki/sources/descriptions/ys1231__MoveCertificate.md
  - wiki/sources/descriptions/yourmnbbn__tiny-csgo-client.md
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
updated: 2026-07-17
confidence: high
---



# Game Hacking

Offensive technique taxonomy and threat model: how cheats escalate from user-mode memory/injection to kernel drivers, hypervisors, EFI, and [[dma]] as defenders raise the bar. (source: wiki/sources/skills/game-hacking.md)

## Escalation model

1. **User-mode** — RPM/WPM, DLL/shellcode injection, graphics/input hooks
2. **Kernel-mode** — signed/vulnerable drivers ([[byovd]]), callback/page-table work; cross-process R/W via MDL/CR3 helpers such as [[ntmemory]] (source: wiki/sources/descriptions/zer0condition__NTMemory.md)
3. **Below the OS** — hypervisor, PCIe DMA, external devices / second machines

## Key sub-areas

- Memory, injection, hooking (inline/IAT/VTable/HWBP); injection-testing samples such as [[injectors]] for AC stress evaluation. (source: wiki/sources/descriptions/zoand__Injectors.md)
- Visual ESP / aim / movement cheats; AI visual pipelines (OBS + YOLO + HID)
- Overlays via [[present-hook]] and external/DWM windows
- HWID spoofing, stack spoofing, driver communication channels (e.g. [[boom]] hijacks `Beep.sys` and alters hide/comm paths). (source: wiki/sources/descriptions/zoand__BOOM.md)
- EFI boot-time mappers; engine-specific paths (Unreal/Unity/Source)
- AC-system exploration repos (e.g. [[vac3-inhibitor]] for VAC3 hooking/memory work) sit in the user-mode lane of cheat research. (source: wiki/sources/descriptions/zyhp__vac3_inhibitor.md)
- PE triage of game/client modules (imports, TLS, .NET metadata) via viewers such as [[totalpe2]] before deeper RE. (source: wiki/sources/descriptions/zodiacon__TotalPE2.md)
- Rapid x86/x64 shellcode/asm prototyping with [[quickasm]] (assemble via Keystone, execute in-process). (source: wiki/sources/descriptions/zodiacon__QuickAsm.md)
- Title-specific offset/token dumps (e.g. Fortnite FLTokens via [[fortnite-fltokens-and-offsets]]) illustrate ephemeral cheat-research artifacts that rot quickly. (source: wiki/sources/descriptions/zinx-YT__Fortnite-Fltokens-and-offsets.md)
- MBA expression generators such as [[mutaben]] (Python) sit in the Cheat Mixed boolean-arithmetic lane. (source: wiki/sources/descriptions/z1ko__mutaben.md)
- Fix OLLVM / deobfuscation plugins targeting `libtprt.so` (e.g. [[deobf]]) sit in the Cheat Fix OLLVM lane. (source: wiki/sources/descriptions/zhuzhu-Top__deobf.md)
- IDA CFF deflattening via [[idadeflat]] (angr-backed semi-auto CFG recover/patch) also sits in that Fix OLLVM / deflat lane. (source: wiki/sources/descriptions/za233__IDADeflat.md)
- Fix VMP / VTIL demos such as [[vmdevirt-vtil]] (broken VTIL compile path; multi-`vmenter` → jmp into compiled VTIL for IDA) sit in the Cheat Fix VMP lane. (source: wiki/sources/descriptions/xtremegamer1__vmdevirt-vtil.md)
- Opaque-predicate detection via [[opaque-predicates-detective]] (invariant-expression / BB-local damage) sits in the Cheat Binary Ninja Plugins lane. (source: wiki/sources/descriptions/yellowbyte__opaque-predicates-detective.md)
- IDA Plugins such as [[xrefsext]] (extended xrefs) and [[ida-jm-xorstr-decrypt-plugin]] (JM Xorstr decrypt on some x64 binaries) support cheat-side static RE workflows. (source: wiki/sources/descriptions/zengfr__XrefsExt.md) (source: wiki/sources/descriptions/yubie-re__ida-jm-xorstr-decrypt-plugin.md)
- Magisk-style root on Android VR (Quest 3/3S) via [[cheese]] (Adreno CVE-2025-21479; temporary root, no boot rewrite) sits in the Cheat Magisk lane. (source: wiki/sources/descriptions/zhuowei__cheese.md)
- Magisk/KernelSU/APatch modules such as [[move-certificate]] (user→system CA trust, Android 7–15) support MITM-oriented mobile cheat research. (source: wiki/sources/descriptions/ys1231__MoveCertificate.md)
- Custom recovery / ROM device trees such as [[ofrp-device-xiaomi-mondrian]] (OFRP for Redmi K60 Pro / mondrian) sit in the Android bootloader/ROM/root lane. (source: wiki/sources/descriptions/ymdzq__OFRP-device_xiaomi_mondrian.md)
- DIY Android kernel explorers such as [[op7t]] sit in the Cheat Android kernel explorer lane. (source: wiki/sources/descriptions/yhnu__op7t.md)
- Android app perf profiling demos such as [[simpleperf-demo]] (simpleperf / Perf) sit adjacent to that Android explorer / cheat research lane. (source: wiki/sources/descriptions/yabinc__simpleperf_demo.md)
- Linux LKM vermagic/CRC rewriting via [[vermagic]] sits in the Cheat Linux / RE tools lane (load modules across mismatched kernel builds). (source: wiki/sources/descriptions/yaxinsn__vermagic.md)
- Title-specific DayZ cheat/modding samples such as [[dayzzz]] (SDK generation + overlays) illustrate game:dayz offensive research surface. (source: wiki/sources/descriptions/zhitkur__DayZzz.md)
- Minimal CS:GO dedicated-server clients such as [[tiny-csgo-client]] (C++; modding / SDK generation) sit in the cheat / game:csgo lane. (source: wiki/sources/descriptions/yourmnbbn__tiny-csgo-client.md)
- Linux external CS:S trainers such as [[counterstrikesource-linux-trainer]] (movement automation + info display) sit in the cheat / game:css lane. (source: wiki/sources/descriptions/yoshisaac__CounterStrikeSource-Linux-Trainer.md)
- Linux external CS2 cheats such as [[counterstrike2-linux-cheat]] (C++; memory analysis) sit in the cheat / game:cs2 lane. (source: wiki/sources/descriptions/yoshisaac__CounterStrike2-Linux-Cheat.md)
- External CS2 samples such as [[cs2-cheat-cpp]] (C++; rendering / asset pipelines / SDK generation) also sit in the cheat / game:cs2 lane. (source: wiki/sources/descriptions/yinleiCoder__cs2-cheat-cpp.md)
- External CS2 glow ESP such as [[cs-2-glow]] (C++; entity parse / offsets / external memory glow) sits in the same cheat / game:cs2 visual lane. (source: wiki/sources/descriptions/xvorost__CS-2-Glow.md)
- Title-specific Battlefield 1 internals such as [[battlefield-1-internal]] (C++; DirectX / SDK generation / hooking) illustrate the cheat / game:battlefield 1 lane. (source: wiki/sources/descriptions/younasiqw__BattleField-1-Internal.md)
- Hidden-PVE / QEMU-KVM anti-detection (e.g. [[proxmox-ve-anti-detection]], [[qemu-anti-detection]] device-string spoof such as QEMU→ASUS keyboard) sits in the `Cheat > QEMU/KVM/PVE/VBOX` lane. (source: wiki/sources/descriptions/zhaodice__proxmox-ve-anti-detection.md) (source: wiki/sources/descriptions/zhaodice__qemu-anti-detection.md)
- Original Xbox software emulation via [[xqemu]] (full-machine QEMU, no hardware VT required) also sits in that QEMU/KVM research lane for title playback / RE. (source: wiki/sources/descriptions/xqemu__xqemu.md)

## Related concepts

[[dma]] · [[byovd]] · [[present-hook]] · [[il2cpp]] · [[kernel-callbacks]] · [[ntmemory]] · [[vac3-inhibitor]] · [[totalpe2]] · [[quickasm]] · [[xrefsext]] · [[ida-jm-xorstr-decrypt-plugin]] · [[injectors]] · [[boom]] · [[fortnite-fltokens-and-offsets]] · [[mutaben]] · [[deobf]] · [[idadeflat]] · [[vmdevirt-vtil]] · [[opaque-predicates-detective]] · [[cheese]] · [[move-certificate]] · [[ofrp-device-xiaomi-mondrian]] · [[op7t]] · [[simpleperf-demo]] · [[vermagic]] · [[dayzzz]] · [[tiny-csgo-client]] · [[counterstrikesource-linux-trainer]] · [[counterstrike2-linux-cheat]] · [[cs2-cheat-cpp]] · [[cs-2-glow]] · [[battlefield-1-internal]] · [[proxmox-ve-anti-detection]] · [[qemu-anti-detection]] · [[xqemu]] · [[overviews/anti-cheat]]



## README map

`Cheat` is the largest category (~2544 links): guides, debugging, packet sniff/capture, speedhack, RE tools, MBA/VMP/Themida/OLLVM fix lanes, DBI, Launcher Abuser, PatchGuard/DSE, Windows/Linux/Android kernel explorers, Magisk/Xposed/Frida/ART-syscall hooks, Android memory loading + App/Kernel CVE lanes, bootloader/ROM/root trees, Cellular/SIM + IoT, iOS jailbreak/network, plus `Some Tricks` (~112; Ring0/Ring3/Linux/Android). (source: wiki/sources/README-categories.md)
