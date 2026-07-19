---
title: Mobile Security
kind: overview
topics: [mobile-security]
sources:
  - wiki/sources/skills/mobile-security.md
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/zinja-coder__apktool-mcp-server.md
  - wiki/sources/descriptions/zhuowei__cheese.md
  - wiki/sources/descriptions/zhizhuodemao__android_proxy_mcp.md
  - wiki/sources/descriptions/zeroxjf__lightsaber.md
  - wiki/sources/descriptions/zboralski__unflutter.md
  - wiki/sources/descriptions/yukiarrr__Il2cppSpy.md
  - wiki/sources/descriptions/xxzzddxzd__unitySpeedTools.md
  - wiki/sources/descriptions/ys1231__MoveCertificate.md
  - wiki/sources/descriptions/yoavst__ida-ios-helper.md
  - wiki/sources/descriptions/ymdzq__OFRP-device_xiaomi_mondrian.md
  - wiki/sources/descriptions/yhnu__op7t.md
  - wiki/sources/descriptions/yabinc__simpleperf_demo.md
  - wiki/sources/descriptions/xmmword__dpatch.md
  - wiki/sources/descriptions/xiaoxindada__magiskboot_ndk_on_linux.md
  - wiki/sources/descriptions/xProHackerx__imgui-ios-mod-menu.md
  - wiki/sources/descriptions/x-spy__CVE-2026-43499-popsicle.md
  - wiki/sources/descriptions/wwweeeqqu__honor-of-kings-RE-research.md
  - wiki/sources/descriptions/walzer__game-engine-detector.md
  - wiki/sources/descriptions/vvb2060__MagiskDetector.md
  - wiki/sources/descriptions/vvb2060__KeyAttestation.md
updated: 2026-07-19
confidence: high
---




# Mobile Security

Android and iOS game security: APK/IPA analysis, native/IL2CPP reversing, root/jailbreak ecosystems, dynamic instrumentation ([[frida]]), and mobile anti-cheat (root/Frida/emulator detection). (source: wiki/sources/skills/mobile-security.md)

## Key sub-areas

**Android:** apktool/jadx (agent-facing apktool via [[apktool-mcp-server]] MCP tools) (source: wiki/sources/descriptions/zinja-coder__apktool-mcp-server.md), Magisk / KernelSU / APatch (e.g. [[cheese]] Magisk install on Quest 3/3S via Adreno CVE-2025-21479, no boot-partition rewrite; [[move-certificate]] user→system CA module for Android 7–15; NDK-on-Linux magiskboot builds via [[magiskboot-ndk-on-linux]] for boot-image unpack/repack; Magisk artifact / mount-namespace detection via archived [[magiskdetector]] AppZygote+AIDL isolated checks; hardware-backed key attestation / bootloader integrity via [[keyattestation]] Keymaster/KeyMint AIDL cert checks) (source: wiki/sources/descriptions/zhuowei__cheese.md) (source: wiki/sources/descriptions/ys1231__MoveCertificate.md) (source: wiki/sources/descriptions/xiaoxindada__magiskboot_ndk_on_linux.md) (source: wiki/sources/descriptions/vvb2060__MagiskDetector.md) (source: wiki/sources/descriptions/vvb2060__KeyAttestation.md), custom recovery device trees such as [[ofrp-device-xiaomi-mondrian]] (OFRP/TWRP for Redmi K60 Pro / Snapdragon 8 Gen 2) (source: wiki/sources/descriptions/ymdzq__OFRP-device_xiaomi_mondrian.md), DIY Android kernel explorers such as [[op7t]] (source: wiki/sources/descriptions/yhnu__op7t.md), Android Kernel CVE PoCs such as [[cve-2026-43499-popsicle]] (Xiaomi 17 Pro Max / popsicle LPE; LD_PRELOAD; uid 0 + SELinux off on 6.12 kernels) (source: wiki/sources/descriptions/x-spy__CVE-2026-43499-popsicle.md), syscall dispatcher patching PoCs such as [[dpatch]] (writable syscall-table copy + dispatcher jump) (source: wiki/sources/descriptions/xmmword__dpatch.md), Android app perf profiling demos such as [[simpleperf-demo]] (simpleperf / Perf) (source: wiki/sources/descriptions/yabinc__simpleperf_demo.md), Zygisk modules, ART/syscall hooks, eBPF tracers, kernel drivers, ACE/AppSealing-class protectors; Honor of Kings (sgame) RE workspace [[honor-of-kings-re-research]] (Frida/IL2CPP/`libtersafe` + KernelPatch acepeek KPMs vs Tencent ACE) (source: wiki/sources/descriptions/wwweeeqqu__honor-of-kings-RE-research.md); agent-facing HTTP/HTTPS capture via [[android-proxy-mcp]] (mitmdump + SQLite + NL query) (source: wiki/sources/descriptions/zhizhuodemao__android_proxy_mcp.md).

**iOS:** jailbreak tooling, class-dump, Logos hooks, sideloading / AltStore for non-jailbreak paths; userland exploit chains such as [[lightsaber]] (iOS 18.4–18.6.2 JS injection into SpringBoard / other processes; derived from DarkSword) (source: wiki/sources/descriptions/zeroxjf__lightsaber.md); IDA iOS reversing helper [[ida-ios-helper]] (needs vtable symbols) (source: wiki/sources/descriptions/yoavst__ida-ios-helper.md); ImGui mod-menu samples such as [[imgui-ios-mod-menu]] (cheat / render-draw research) (source: wiki/sources/descriptions/xProHackerx__imgui-ios-mod-menu.md).


**Unity/Unreal mobile:** Engine triage for packages via [[game-engine-detector]] (Python; which engine an `.apk` / `.ipa` uses) before deeper dumps. (source: wiki/sources/descriptions/walzer__game-engine-detector.md) [[il2cpp]] (`libil2cpp.so` / UnityFramework + metadata), SDK dumps, memory editors (GameGuardian, H5GG); APK IL2CPP disassembly/diff via [[il2cpp-spy]] (select two APKs → show differences). (source: wiki/sources/descriptions/yukiarrr__Il2cppSpy.md) iOS Unity speed/modding tooling such as [[unityspeedtools]] (C/C++ / Objective-C; IL2CPP analysis) sits in the same explorer:Unity lane. (source: wiki/sources/descriptions/xxzzddxzd__unitySpeedTools.md)


**Flutter/Dart:** AOT snapshot symbol recovery via [[unflutter]] (Dart VM snapshot metadata → class/function/type names from Flutter APKs/iOS apps) (source: wiki/sources/descriptions/zboralski__unflutter.md).

## Related concepts

[[frida]] · [[il2cpp]] · [[game-engine-detector]] · [[il2cpp-spy]] · [[unityspeedtools]] · [[unflutter]] · [[apktool-mcp-server]] · [[android-proxy-mcp]] · [[honor-of-kings-re-research]] · [[cheese]] · [[magiskdetector]] · [[keyattestation]] · [[cve-2026-43499-popsicle]] · [[move-certificate]] · [[magiskboot-ndk-on-linux]] · [[ofrp-device-xiaomi-mondrian]] · [[op7t]] · [[dpatch]] · [[simpleperf-demo]] · [[lightsaber]] · [[ida-ios-helper]] · [[imgui-ios-mod-menu]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]


## README map

Cheat Magisk/Xposed/Frida/ART-syscall hooks/Android kernel*/driver/Network Explorer/bootloader bypass/ROM/root/memory-loading/App+Kernel CVE/Cellular-SIM/IoT trees; iOS jailbreak+network; Anti Cheat Detection:Android root; platform cats `WSA` (~9), `Android Emulator` (~9; Genymotion/Anbox + Snapdragon/Gunyah DroidVM with VirGL/GfxStream), `IOS Emulator` (~3; qemu-apple-silicon + Virtualization.framework vphone-cli/aio). (source: wiki/sources/README-categories.md)
