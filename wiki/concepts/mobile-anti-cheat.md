---
title: Mobile Anti-Cheat
kind: concept
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/skills/mobile-security.md
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/venkata-ram__DroidShield.md
  - wiki/sources/descriptions/rushiranpise__detection.md
  - wiki/sources/descriptions/wwweeeqqu__honor-of-kings-RE-research.md
  - wiki/sources/descriptions/phajmvawnsix__com.sipvlib.anticheat.md
  - wiki/sources/descriptions/smithluke874__Android-VirtualCam-Manager.md
  - wiki/sources/descriptions/libtersafe__dfm_android_unicorn.md
  - wiki/sources/descriptions/libtersafe__KPM-MemReader.md
  - wiki/sources/descriptions/gmh5225__PUBGM1.6-DeadGame.md
  - wiki/sources/descriptions/gmh5225__freedom.md
  - wiki/sources/descriptions/okhsunrog__vpnhide.md
  - wiki/sources/descriptions/rathorekrishna401-NeuroVoid__ApexSU.md
  - wiki/sources/descriptions/salvogiangri__KnoxPatch.md
  - wiki/sources/descriptions/quarkslab__android-hardware-attestation-demo.md
  - wiki/sources/descriptions/geeksonsecurity__android-overlay-protection.md
  - wiki/sources/descriptions/geeksonsecurity__android-overlay-malware-example.md
  - wiki/sources/descriptions/fynks__awesome-android-root.md
  - wiki/sources/descriptions/eltavine__Duck-Detector-Refactoring.md
  - wiki/sources/descriptions/canyie__Riru-MomoHider.md
  - wiki/sources/descriptions/canyie__MagiskKiller.md
  - wiki/sources/descriptions/canyie__MagiskEoP.md
  - wiki/sources/descriptions/apkunpacker__RootAppDetector.md
  - wiki/sources/descriptions/apkunpacker__MagiskDetection.md
  - wiki/sources/descriptions/apkunpacker__DetectZygisk.md
  - wiki/sources/descriptions/Xheghun__DeviceTrust.md
  - wiki/sources/descriptions/WsttXm__RiskEngine.md
  - wiki/sources/descriptions/VisionR1__KeyAttestation.md
  - wiki/sources/descriptions/cognis-digital__rootsentry.md
  - wiki/sources/descriptions/Solaree__pairipcore.md
  - wiki/sources/descriptions/NPC2000__AppPealing-new.md
  - wiki/sources/descriptions/cxOrz__AnyWhere.md
  - wiki/sources/descriptions/Rem01Gaming__meowna_detector.md
  - wiki/sources/descriptions/NoobDigital__react-native-shieldscan.md
  - wiki/sources/descriptions/AfanasievN__react-native-device-risk-signals.md
  - wiki/sources/descriptions/Mrack__MemDetection.md
  - wiki/sources/descriptions/Lazenca__Lazenca-S.md
  - wiki/sources/descriptions/Laert-Android__Advanced-Root-Checker.md
  - wiki/sources/descriptions/LSPosed__DirtySepolicy.md
  - wiki/sources/descriptions/JingMatrix__Demo.md
  - wiki/sources/descriptions/Dr-TSNG__ApplistDetector.md
  - wiki/sources/descriptions/Binuka97__cordova-plugin-rootguard.md
  - wiki/sources/descriptions/Xposed-Modules-Repo__com.wowsoftware.hidemyandroid.md
  - wiki/sources/descriptions/AtawurRahmanTanvir__NEXUS.md
  - wiki/sources/descriptions/Android1500__AndroidFaker.md
  - wiki/sources/descriptions/AlirezaParsi__COPG.md
  - wiki/sources/descriptions/zelect0r__zamr.md
  - wiki/sources/descriptions/Lixense__ff-ace-anticheat-analysis.md
updated: 2026-09-03
confidence: medium
---

# Mobile Anti-Cheat

Client-side integrity and environment checks on Android/iOS game clients, often combined with server-side validation, attestation, and regional commercial protectors. Overlaps README `Anti Cheat > Detection:*` mobile lanes (Android root, Magisk, Frida) and title-specific native SDKs. (source: wiki/sources/skills/mobile-security.md)

## Common systems

- **Tencent ACE** — Chinese-market native protector; title RE such as [[honor-of-kings-re-research]] (`libtersafe`, IL2CPP, KernelPatch modules). Free Fire byte-level post-mortem [[ff-ace-anticheat-analysis]] (Lixense; `libanogs.so`/`libanort.so` on armeabi-v7a; IDA decompilation + Python/JS automation; APK hash, cert parsing, inline-hook scans, self-integrity checksum catalog + SQLite findings index; defensive ACE client study). (source: wiki/sources/descriptions/Lixense__ff-ace-anticheat-analysis.md) Historical PUBG Mobile 1.6 decompiled `libtersafe.so` archives such as [[pubgm1.6-deadgame]] preserve ACE native symbols/functions from a dead client build for offline static RE. (source: wiki/sources/descriptions/gmh5225__PUBGM1.6-DeadGame.md) ARM64 coordinate-decryption emulation via [[dfm-android-unicorn]] (Unicorn replay of protected crypto paths). KernelPatch KPM cross-process memory read via ioctl hook via [[kpm-memreader]]. (source: wiki/sources/descriptions/libtersafe__dfm_android_unicorn.md) (source: wiki/sources/descriptions/libtersafe__KPM-MemReader.md)
- **NetEase Protection** — NetEase titles; similar native + server mix.
- **Per-game / SDK RASP** — [[droidshield]], Talsec freeRASP ([[free-rasp-unity-poc]], [[free-rasp-reactnative]], [[free-rasp-capacitor]], [[free-rasp-cordova]]), Cordova plugin [[cordova-plugin-rootguard]] (Binuka97; Java/ObjC + JS bridge; Magisk/KernelSU/APatch, Frida/Gum/debugger; SAFE/COMPROMISED/UNKNOWN tri-state; source: wiki/sources/descriptions/Binuka97__cordova-plugin-rootguard.md), [[react-native-shieldscan]] (NoobDigital; TS + Kotlin/Swift; root/jailbreak, Frida, debugger, emulator, Xposed/Substrate hooks, developer mode; weighted risk score + screen blur/screenshot/recording protection; source: wiki/sources/descriptions/NoobDigital__react-native-shieldscan.md), [[react-native-device-risk-signals]] (AfanasievN; TurboModule; raw typed root/jailbreak, emulator, Frida/debugger, VPN/proxy, hardware/locale/app/runtime probes; no client score or upload; backend fraud/device-risk enrichment; source: wiki/sources/descriptions/AfanasievN__react-native-device-risk-signals.md), [[rs-native-kit-security]], [[rootsentry]] (Python CLI/library; root/jailbreak, emulator, hook, tamper scoring → TRUSTED→CRITICAL; fleet analysis + MITRE ATT&CK for Mobile; source: wiki/sources/descriptions/cognis-digital__rootsentry.md), Unity UPM [[com-sipvlib-anticheat]] (server-verified GameTime + IntegrityChecker), open-source hybrid Java/JNI engine [[lazenca-s]] (Lazenca; debugging, root, speed-hack, binary tamper, VM signals; mobile AC study; source: wiki/sources/descriptions/Lazenca__Lazenca-S.md).
- **Commercial packers** — AppSealing, DexGuard/ProGuard, Arxan on APK/DEX/native layers; Google's **pairipcore** on first-party and Play-distributed apps (integrity checks, pseudo-VM native injection, control-flow obfuscation, dynamic symbol resolution, anti-debug, optional root gates)—documented for researchers via [[pairipcore]] (source: wiki/sources/descriptions/Solaree__pairipcore.md). Offensive AppSealing bypass and decrypted-DEX dump via LSPosed module [[apppealing-new]] (Java Xposed hooks + native [[dobby]] components; root/cheat-detection disable; Magisk workflow; source: wiki/sources/descriptions/NPC2000__AppPealing-new.md).

## Detection methods

| Signal | Examples |
|--------|----------|
| Root / jailbreak | `su` paths, build tags, Magisk mounts, Xposed/LSPosed, KernelSU/APatch artifacts, installed root-manager apps (launch probes such as [[root-app-detector]]; source: wiki/sources/descriptions/apkunpacker__RootAppDetector.md); Kotlin + native library [[applist-detector]] (Dr-TSNG; package inspection, FS artifacts, syscall file probes, Xposed status, dual/work-profile checks; source: wiki/sources/descriptions/Dr-TSNG__ApplistDetector.md); logging-service disruption artifacts (missing logd sockets, package traces) such as [[meowna-detector]] (source: wiki/sources/descriptions/Rem01Gaming__meowna_detector.md); Magisk `su`-daemon flaws such as [[magisk-eop]] (unprivileged app → root without grant UI; source: wiki/sources/descriptions/canyie__MagiskEoP.md) show root frameworks can fail closed on authorization |
| Instrumentation | Frida server/gadget, inline hooks, Zygisk modules ([[zygisk]]); ptrace-based Zygisk-style injection probes such as [[detect-zygisk]] (fork + `PTRACE_GETEVENTMSG`; source: wiki/sources/descriptions/apkunpacker__DetectZygisk.md); user-space library injection checks such as [[demo]] (JingMatrix; soinfo linked-list, virtual memory map inspection, module unload counters; Kotlin + native C++; source: wiki/sources/descriptions/JingMatrix__Demo.md) |
| Emulator / VM | Build fingerprint, sensors, FS signatures ([[anti-emulator]], [[android-emulator-detection]], [[conbeerlib]]) |
| Integrity | APK/signature hash, native `.so` checksums, in-memory vs on-disk CRC of `libc.so`/`libart.so` such as [[memdetection]] (Mrack; Java + Rust/JNI demo; Frida/Xposed/cloning signals; source: wiki/sources/descriptions/Mrack__MemDetection.md), Play Integrity / Key Attestation ([[keyattestation]]; VisionR1 fork adds RSA attestation, certificate-chain persistence, and local/remote revocation-list checks — source: wiki/sources/descriptions/VisionR1__KeyAttestation.md) — stricter on Android 14/15 per curated root research notes [[awesome-android-root]] (source: wiki/sources/descriptions/fynks__awesome-android-root.md); relay PoCs such as [[android-hardware-attestation-demo]] show genuine TEE/StrongBox chains can be proxied from a clean device via Frida Keystore hooks—server validation must bind beyond the attestation nonce (source: wiki/sources/descriptions/quarkslab__android-hardware-attestation-demo.md) |
| Debugger | `TracerPid`, JDWP, ptrace |
| Hooks | PLT/GOT integrity, `/proc/self/maps` anomalies |
| IAP / billing | Client-side Play Billing API trust; local purchase-confirmation spoofing such as [[freedom]] (billing-service hook; server receipt validation is the primary defense) (source: wiki/sources/descriptions/gmh5225__freedom.md) |
| Camera / liveness | Camera1 preview/callback integrity, face/liveness SDK probes; rooted virtual-camera injection such as [[android-virtualcam-manager]] (ArtHook + NV21 frame replace; no LSPosed) (source: wiki/sources/descriptions/smithluke874__Android-VirtualCam-Manager.md) |
| VPN / proxy | `ConnectivityManager`/`NetworkCapabilities`, `/proc/net`, ioctl/netlink routes, localhost daemon port scans (Clash/sing-box); RASP SDKs such as [[rs-native-kit-security]]; per-app hide tooling such as [[vpnhide]] (Binder + kernel/Zygisk path filtering; no target-process hooks) (source: wiki/sources/descriptions/okhsunrog__vpnhide.md) |
| Overlay / tapjacking | `TYPE_APPLICATION_OVERLAY` windows above sensitive views; `filterTouchesWhenObscured` input blocking; callback alerts via [[android-overlay-protection]] (Java library for overlay detection on login/payment flows) (source: wiki/sources/descriptions/geeksonsecurity__android-overlay-protection.md); offensive PoC [[android-overlay-malware-example]] (foreground-app monitor + credential-phishing overlay mimicking banking/social apps) (source: wiki/sources/descriptions/geeksonsecurity__android-overlay-malware-example.md) |

Multi-check collections: [[detection]], [[android-native-root-detector]], [[meowna-detector]], [[root-app-detector]], [[applist-detector]] (Dr-TSNG; Kotlin + native C++ library/demo; package/FS/syscall/Xposed/work-profile probes; source: wiki/sources/descriptions/Dr-TSNG__ApplistDetector.md), [[magisk-detection]] (apkunpacker; archive of root/Magisk POC APKs with Zygisk, hook, bootloader, and root-app checks plus sample hashes; source: wiki/sources/descriptions/apkunpacker__MagiskDetection.md), [[detect-zygisk]] (apkunpacker; C++/JNI Zygisk-style injection POC via ptrace event messages; source: wiki/sources/descriptions/apkunpacker__DetectZygisk.md), [[duck-detector-refactoring]] (local Compose inspector with native probe cards for root/hook/mount/attestation/VM evidence; source: wiki/sources/descriptions/eltavine__Duck-Detector-Refactoring.md), [[advanced-root-checker]] (Laert-Android; offline Java app; su/Magisk/KernelSU/APatch/Zygisk/Xposed/LSPosed, root cloaking, SELinux, Frida/debugger/hook anti-tamper, risk score; source: wiki/sources/descriptions/Laert-Android__Advanced-Root-Checker.md), [[dirty-sepolicy]] (LSPosed; App Zygote SELinux access-check probe for userspace `su`; runtime permissive policy injection via AIDL without root; source: wiki/sources/descriptions/LSPosed__DirtySepolicy.md), [[device-trust]] (Xheghun; Kotlin coroutine API + NDK C++ root/hook/emulator/bootloader/SELinux probes; weighted risk score + categorized evidence; configurable thresholds or raw signal export for server-side scoring; source: wiki/sources/descriptions/Xheghun__DeviceTrust.md), [[risk-engine]] (WsttXm; Android risk-control SDK + management platform; JNI + system-property checks for root, emulator, Frida/Xposed, debugger, VPN, sandbox; device fingerprinting; source: wiki/sources/descriptions/WsttXm__RiskEngine.md), [[magisk-killer]] (canyie; forked subprocess + pipe IPC; Magisk/MagiskHide tracer, bootloader, property-area, and PTS probes outside caller trace scope; source: wiki/sources/descriptions/canyie__MagiskKiller.md), archived [[magiskdetector]].

## Bypass strategies (research framing)

1. Static RE of detection routines in DEX/native code.
2. Hook or patch check functions ([[frida]], [[locusmimic]] / [[anywhere]] for mock-location edge cases—LSPosed hide modules bypass `isFromMockProvider` and related spoofing checks; source: wiki/sources/descriptions/cxOrz__AnyWhere.md). Profile-based identifier and environment spoofing via [[hidemyandroid]] intercepts Android ID, GAID, IMEI, Widevine, and root/LSPosed/VPN/proxy/dev-options probes per app profile. (source: wiki/sources/descriptions/Xposed-Modules-Repo__com.wowsoftware.hidemyandroid.md) Focused hardware-identifier spoofing via [[android-faker]] (IMEI, Android ID, MAC, SIM; Xposed/LSPosed; randomization and manual edit) masks tracking-relevant metadata on rooted devices. (source: wiki/sources/descriptions/Android1500__AndroidFaker.md) Zygisk per-app hardware-profile spoofing via [[copg]] (build props, CPU/GPU, IMEI, Widevine, SIM, GAID; stealth CoW/unload-before-launch vs detectable resident GPU/DRM hooks; WebUI device libraries) targets hardware-gated FPS/graphics tier checks and device fingerprint probes on rooted Magisk/Zygisk hosts. (source: wiki/sources/descriptions/AlirezaParsi__COPG.md) Root-level orchestration via [[nexus]] rotates Android ID/MAC/IMEI/`build.prop`, resets network/DNS, purges caches, and scrubs Google telemetry through privileged `su` engines—anti-ban identity rotation outside app-scoped hooking. (source: wiki/sources/descriptions/AtawurRahmanTanvir__NEXUS.md)
3. Reduce injection footprint (stealth Frida [[fridare]], WXSHADOW/RECOMP tiers, root-hide DenyList/Shamiko, KernelSU process isolation). Curated MMRL module catalog [[zamr]] bundles maintained Play Integrity Fix, Zygisk runtimes, TEESimulator, and root-hide modules (HMA-OSS Zygisk, SUSFS) for Magisk/KernelSU/APatch hosts—hourly refreshed JSON manifests for researchers testing integrity gates on rooted hardware. (source: wiki/sources/descriptions/zelect0r__zamr.md) Riru Zygote-injection hide modules such as [[riru-momo-hider]] hook syscalls and Java root-check APIs (mount spoof, Magisk artifact hide, property-query block) to evade libraries like [[magiskdetector]]/RootBeer. (source: wiki/sources/descriptions/canyie__Riru-MomoHider.md) Hardened KernelSU forks such as [[apex-su]] study reduced root artifacts—IOCTL over anonymous `io_uring`-disguised inodes with no proc/sys/dev entries—against FS and process-based root probes. (source: wiki/sources/descriptions/rathorekrishna401-NeuroVoid__ApexSU.md) OEM Knox integrity on Samsung Galaxy: [[knoxpatch]] hooks target Samsung apps to bypass root detection and disable Knox SDK / Samsung Attestation Key checks, with companion Magisk/KernelSU system patches for Secure Folder on legacy One UI—useful for studying how Samsung apps gate features on rooted hardware. (source: wiki/sources/descriptions/salvogiangri__KnoxPatch.md)
4. Timing — checks may run once at launch vs periodically.
5. Environment emulation — hide emulator props or use physical devices with clean attestation; attestation relay from a second clean device via [[android-hardware-attestation-demo]] (no crypto forgery; backend nonce forwarded to an oracle) passes hardware-backed checks on rooted analysis hardware. (source: wiki/sources/descriptions/quarkslab__android-hardware-attestation-demo.md)

Apply [[research-rigor]]—detectors and bypasses vary by build, OEM, and server policy; README samples are not universal recipes.

## Related

[[research-rigor]] · [[frida]] · [[memdetection]] · [[lazenca-s]] · [[pairipcore]] · [[apppealing-new]] · [[freedom]] · [[vpnhide]] · [[android-overlay-protection]] · [[android-overlay-malware-example]] · [[android-native-surface]] · [[zygisk]] · [[magisk]] · [[kernelsu]] · [[apex-su]] · [[knoxpatch]] · [[riru-momo-hider]] · [[magisk-killer]] · [[magisk-eop]] · [[keyattestation]] · [[android-hardware-attestation-demo]] · [[droidshield]] · [[react-native-shieldscan]] · [[react-native-device-risk-signals]] · [[free-rasp-reactnative]] · [[detection]] · [[antifrida]] · [[android-virtualcam-manager]] · [[locusmimic]] · [[anywhere]] · [[hidemyandroid]] · [[android-faker]] · [[copg]] · [[nexus]] · [[zamr]] · [[spoofing-collection]] · [[honor-of-kings-re-research]] · [[ff-ace-anticheat-analysis]] · [[dfm-android-unicorn]] · [[kpm-memreader]] · [[pubgm1.6-deadgame]] · [[overviews/mobile-security]] · [[overviews/anti-cheat]]
