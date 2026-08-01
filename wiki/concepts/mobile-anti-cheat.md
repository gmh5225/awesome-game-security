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
updated: 2026-08-01
confidence: medium
---

# Mobile Anti-Cheat

Client-side integrity and environment checks on Android/iOS game clients, often combined with server-side validation, attestation, and regional commercial protectors. Overlaps README `Anti Cheat > Detection:*` mobile lanes (Android root, Magisk, Frida) and title-specific native SDKs. (source: wiki/sources/skills/mobile-security.md)

## Common systems

- **Tencent ACE** — Chinese-market native protector; title RE such as [[honor-of-kings-re-research]] (`libtersafe`, IL2CPP, KernelPatch modules). ARM64 coordinate-decryption emulation via [[dfm-android-unicorn]] (Unicorn replay of protected crypto paths). (source: wiki/sources/descriptions/libtersafe__dfm_android_unicorn.md)
- **NetEase Protection** — NetEase titles; similar native + server mix.
- **Per-game / SDK RASP** — [[droidshield]], Talsec freeRASP ([[free-rasp-unity-poc]], [[free-rasp-reactnative]], [[free-rasp-capacitor]]), [[rs-native-kit-security]], Unity UPM [[com-sipvlib-anticheat]] (server-verified GameTime + IntegrityChecker).
- **Commercial packers** — AppSealing, DexGuard/ProGuard, Arxan on APK/DEX/native layers.

## Detection methods

| Signal | Examples |
|--------|----------|
| Root / jailbreak | `su` paths, build tags, Magisk mounts, Xposed/LSPosed, KernelSU/APatch artifacts |
| Instrumentation | Frida server/gadget, inline hooks, Zygisk modules ([[zygisk]]) |
| Emulator / VM | Build fingerprint, sensors, FS signatures ([[anti-emulator]], [[android-emulator-detection]], [[conbeerlib]]) |
| Integrity | APK/signature hash, native `.so` checksums, Play Integrity / Key Attestation ([[keyattestation]]) |
| Debugger | `TracerPid`, JDWP, ptrace |
| Hooks | PLT/GOT integrity, `/proc/self/maps` anomalies |
| Camera / liveness | Camera1 preview/callback integrity, face/liveness SDK probes; rooted virtual-camera injection such as [[android-virtualcam-manager]] (ArtHook + NV21 frame replace; no LSPosed) (source: wiki/sources/descriptions/smithluke874__Android-VirtualCam-Manager.md) |

Multi-check collections: [[detection]], [[android-native-root-detector]], archived [[magiskdetector]].

## Bypass strategies (research framing)

1. Static RE of detection routines in DEX/native code.
2. Hook or patch check functions ([[frida]], [[locusmimic]] for mock-location edge cases).
3. Reduce injection footprint (stealth Frida [[fridare]], WXSHADOW/RECOMP tiers, root-hide DenyList/Shamiko, KernelSU process isolation).
4. Timing — checks may run once at launch vs periodically.
5. Environment emulation — hide emulator props or use physical devices with clean attestation.

Apply [[research-rigor]]—detectors and bypasses vary by build, OEM, and server policy; README samples are not universal recipes.

## Related

[[research-rigor]] · [[frida]] · [[zygisk]] · [[magisk]] · [[kernelsu]] · [[keyattestation]] · [[droidshield]] · [[detection]] · [[antifrida]] · [[android-virtualcam-manager]] · [[honor-of-kings-re-research]] · [[dfm-android-unicorn]] · [[overviews/mobile-security]] · [[overviews/anti-cheat]]
