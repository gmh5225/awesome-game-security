---
title: Frida
kind: concept
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/skills/mobile-security.md
  - wiki/sources/skills/reverse-engineering.md
  - wiki/sources/descriptions/yring-me__ts-ue4dumper.md
  - wiki/sources/descriptions/vfsfitvnm__frida-il2cpp-bridge.md
  - wiki/sources/descriptions/synacktiv__thats_no_pipe.md
  - wiki/sources/descriptions/suifei__fridare.md
  - wiki/sources/descriptions/smartdone__Frida-Scripts.md
  - wiki/sources/descriptions/rednaga__frida-stack.md
  - wiki/sources/descriptions/qtfreet00__AntiFrida.md
  - wiki/sources/descriptions/muellerberndt__frida-detection.md
  - wiki/sources/descriptions/piotrbania__frida_usb_dump.md
  - wiki/sources/descriptions/noobpk__frida-android-hook.md
  - wiki/sources/descriptions/miticollo__xpc-tracer.md
  - wiki/sources/descriptions/thelok1s__florida-zygisk.md
  - wiki/sources/descriptions/lico-n__ZygiskFrida.md
  - wiki/sources/descriptions/kkkbbb__rustFrida.md
  - wiki/sources/descriptions/kkkbbb__mkpms.md
  - wiki/sources/descriptions/moaaz01__nightowl.md
  - wiki/sources/descriptions/jcalabres__hook-updater.md
  - wiki/sources/descriptions/infosecrajesh__Auto-generate-Frida-bypass-scripts-for-SSL-pinning-root-detection-on-Android-iOS.md
  - wiki/sources/descriptions/hackcatml__frida-watchpoint-tutorial.md
  - wiki/sources/descriptions/hackcatml__frida-findJNINativeMethods.md
  - wiki/sources/descriptions/gmh5225__frinet.md
  - wiki/sources/descriptions/gmh5225__frida-ue4dump.md
  - wiki/sources/descriptions/gmh5225__frida-ceserver.md
  - wiki/sources/descriptions/gmh5225__frida-boot.md
  - wiki/sources/descriptions/gmh5225__FridaScript.md
  - wiki/sources/descriptions/mitros123__DragonHook.md
updated: 2026-08-13
confidence: high
---

# Frida

Cross-platform dynamic instrumentation toolkit widely used on Android/iOS (and desktop) to attach/spawn processes, intercept native/Java/ObjC APIs, and script runtime behavior without static patching. (source: wiki/sources/skills/mobile-security.md)

## Game-security uses

Hook game/[[il2cpp]] natives, bypass SSL pinning, probe root/jailbreak checks, trace anti-cheat detectors. APK triage CLI [[nightowl]] profiles RASP/Frida-detection stacks (RootBeer, SafetyNet, hooking checks) and can emit tailored bypass scripts per profile for mobile assessment workflows. (source: wiki/sources/descriptions/moaaz01__nightowl.md) Static-analysis generators such as [[auto-generate-frida-bypass-scripts-for-ssl-pinning-root-detection-on-android-ios]] scan APK/IPA binary signatures (OkHttp, TrustKit, Flutter, gRPC; RootBeer, Play Integrity, commercial SDKs) and emit targeted Frida hooks for SSL pinning and root/jailbreak bypass without manual class hunting. (source: wiki/sources/descriptions/infosecrajesh__Auto-generate-Frida-bypass-scripts-for-SSL-pinning-root-detection-on-Android-iOS.md) Mobile ACs often ship Frida/ Magisk detection; hide stacks (DenyList/Shamiko, KernelSU isolation) appear in the same research space. Defensive Detection:Frida samples such as [[antifrida]] and hooking-oriented [[frida-detection]] (Java/C++; muellerberndt) sit on the AC side of that lane. (source: wiki/sources/descriptions/qtfreet00__AntiFrida.md) (source: wiki/sources/descriptions/muellerberndt__frida-detection.md) Stealth mobile Frida deployments (hex-replace of server strings/symbols/artifacts; rooted and rootless iOS install scripts) use [[fridare]]. (source: wiki/sources/descriptions/suifei__fridare.md) Boot-persistent anti-detection server modules such as [[florida-zygisk]] (Magisk/KernelSU/APatch; Ylarod-patched Florida `frida-server`; random port; magisk-frida-derived) auto-start hardened Frida on device boot for dynamic analysis against anti-Frida checks. (source: wiki/sources/descriptions/thelok1s__florida-zygisk.md) Zygisk gadget injectors such as [[zygisk-frida]] load the in-process Frida agent via Magisk Zygisk into app processes during specialization for early hooking without external attach. (source: wiki/sources/descriptions/lico-n__ZygiskFrida.md) Script collections such as [[frida-scripts]] (JS/Python; editor tooling and hooking) sit in the same cheat / Frida research lane. (source: wiki/sources/descriptions/smartdone__Frida-Scripts.md) Cross-platform game/app hook libraries such as [[fridascript]] (gmh5225; JavaScript call intercept, API trace, runtime modify; Android/iOS/desktop; iOS low-level scripting) complement that lane. (source: wiki/sources/descriptions/gmh5225__FridaScript.md) Python hook-maintenance helpers such as [[hook-updater]] automate refreshing Frida hook scripts when targets change. (source: wiki/sources/descriptions/jcalabres__hook-updater.md) Class/function-trace and return-value-modify helpers such as [[frida-android-hook]] (iOS-oriented scripts noted) sit in that same lane. (source: wiki/sources/descriptions/noobpk__frida-android-hook.md) Stack/backtrace helpers such as [[frida-stack]] reuse unwind helpers for clearer Frida traces. (source: wiki/sources/descriptions/rednaga__frida-stack.md) Unreal explorers also script Frida dumpers in TypeScript (e.g. [[ts-ue4dumper]], with C++ offset helpers) or as standalone Frida scripts such as [[frida-ue4dump]] (Android UE4 reflection hook; `UObject` enum / property offsets / SDK headers at runtime). (source: wiki/sources/descriptions/yring-me__ts-ue4dumper.md) (source: wiki/sources/descriptions/gmh5225__frida-ue4dump.md) For Unity IL2CPP dumps across a wide version range, [[frida-il2cpp-bridge]] is a common Frida-side bridge. (source: wiki/sources/descriptions/vfsfitvnm__frida-il2cpp-bridge.md) On Windows desktop, [[thats-no-pipe]] uses Frida to intercept named-pipe I/O (`NtReadFile`/`NtWriteFile` and related waits) and relay IPC to an HTTP proxy over WebSocket for protocol analysis and fuzzing. (source: wiki/sources/descriptions/synacktiv__thats_no_pipe.md) On macOS, [[frida-usb-dump]] sniffs and dumps USB traffic (Big Sur-era offsets). (source: wiki/sources/descriptions/piotrbania__frida_usb_dump.md) On iOS and macOS, [[xpc-tracer]] traces XPC IPC messages (xpcspy variant). (source: wiki/sources/descriptions/miticollo__xpc-tracer.md) On Android ARM64, [[rust-frida]] offers a Frida-like injector/agent stack (QuickJS, Java/native/stealth hooks, QBDI) that pairs with [[mkpms]] wxshadow KPM stealth (R^X page-split hook; bypass self-read integrity). (source: wiki/sources/descriptions/kkkbbb__rustFrida.md) (source: wiki/sources/descriptions/kkkbbb__mkpms.md) Hardware data watchpoints via Frida's `setHardwareWatchpoint` — what-writes/accesses tracing without software breakpoints — are documented in [[frida-watchpoint-tutorial]] (trial-and-error walkthrough; cheat / Frida). (source: wiki/sources/descriptions/hackcatml__frida-watchpoint-tutorial.md) Runtime JNI native-method discovery — mapping Java `native` stubs to loaded `.so` symbols via hooking and memory analysis — is supported by [[frida-find-jni-native-methods]] (JavaScript; cheat / Frida). (source: wiki/sources/descriptions/hackcatml__frida-findJNINativeMethods.md) Static+dynamic RE bridge via [[frinet]] (IDA Pro plugin; run Frida on a live target while navigating corresponding code in IDA; sync runtime memory values, function args, and return values into the static analysis view) complements standalone Frida scripting for combined workflows. (source: wiki/sources/descriptions/gmh5225__frinet.md) Ghidra-side counterpart [[dragonhook]] exposes Ghidra database functions, comments, and xrefs to Frida agents via localhost HTTP API with in-Ghidra session GUI (runtime indirect-call resolution, live xref/comment updates, symbol backtraces, call tracing; mitros123). (source: wiki/sources/descriptions/mitros123__DragonHook.md) Cheat Engine remote memory via [[frida-ceserver]] implements the ceserver protocol through Frida attach on mobile and desktop (non-rooted Android supported where Frida can attach). (source: wiki/sources/descriptions/gmh5225__frida-ceserver.md) Beginner streamed DBI workshops such as [[frida-boot]] (gmh5225; YouTube; binary instrumentation fundamentals for cheat / Frida newcomers) complement targeted tutorials like [[frida-watchpoint-tutorial]]. (source: wiki/sources/descriptions/gmh5225__frida-boot.md)

## Related

[[il2cpp]] · [[nightowl]] · [[auto-generate-frida-bypass-scripts-for-ssl-pinning-root-detection-on-android-ios]] · [[frida-il2cpp-bridge]] · [[frida-android-hook]] · [[frida-find-jni-native-methods]] · [[frida-scripts]] · [[fridascript]] · [[frida-watchpoint-tutorial]] · [[hook-updater]] · [[frida-stack]] · [[frida-usb-dump]] · [[xpc-tracer]] · [[fridare]] · [[florida-zygisk]] · [[zygisk-frida]] · [[rust-frida]] · [[mkpms]] · [[antifrida]] · [[frida-detection]] · [[ts-ue4dumper]] · [[frida-ue4dump]] · [[thats-no-pipe]] · [[frinet]] · [[dragonhook]] · [[frida-ceserver]] · [[frida-boot]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
