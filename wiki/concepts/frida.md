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
updated: 2026-08-03
confidence: high
---

# Frida

Cross-platform dynamic instrumentation toolkit widely used on Android/iOS (and desktop) to attach/spawn processes, intercept native/Java/ObjC APIs, and script runtime behavior without static patching. (source: wiki/sources/skills/mobile-security.md)

## Game-security uses

Hook game/[[il2cpp]] natives, bypass SSL pinning, probe root/jailbreak checks, trace anti-cheat detectors. APK triage CLI [[nightowl]] profiles RASP/Frida-detection stacks (RootBeer, SafetyNet, hooking checks) and can emit tailored bypass scripts per profile for mobile assessment workflows. (source: wiki/sources/descriptions/moaaz01__nightowl.md) Mobile ACs often ship Frida/ Magisk detection; hide stacks (DenyList/Shamiko, KernelSU isolation) appear in the same research space. Defensive Detection:Frida samples such as [[antifrida]] and hooking-oriented [[frida-detection]] (Java/C++; muellerberndt) sit on the AC side of that lane. (source: wiki/sources/descriptions/qtfreet00__AntiFrida.md) (source: wiki/sources/descriptions/muellerberndt__frida-detection.md) Stealth mobile Frida deployments (hex-replace of server strings/symbols/artifacts; rooted and rootless iOS install scripts) use [[fridare]]. (source: wiki/sources/descriptions/suifei__fridare.md) Boot-persistent anti-detection server modules such as [[florida-zygisk]] (Magisk/KernelSU/APatch; Ylarod-patched Florida `frida-server`; random port; magisk-frida-derived) auto-start hardened Frida on device boot for dynamic analysis against anti-Frida checks. (source: wiki/sources/descriptions/thelok1s__florida-zygisk.md) Zygisk gadget injectors such as [[zygisk-frida]] load the in-process Frida agent via Magisk Zygisk into app processes during specialization for early hooking without external attach. (source: wiki/sources/descriptions/lico-n__ZygiskFrida.md) Script collections such as [[frida-scripts]] (JS/Python; editor tooling and hooking) sit in the same cheat / Frida research lane. (source: wiki/sources/descriptions/smartdone__Frida-Scripts.md) Class/function-trace and return-value-modify helpers such as [[frida-android-hook]] (iOS-oriented scripts noted) sit in that same lane. (source: wiki/sources/descriptions/noobpk__frida-android-hook.md) Stack/backtrace helpers such as [[frida-stack]] reuse unwind helpers for clearer Frida traces. (source: wiki/sources/descriptions/rednaga__frida-stack.md) Unreal explorers also script Frida dumpers in TypeScript (e.g. [[ts-ue4dumper]], with C++ offset helpers). (source: wiki/sources/descriptions/yring-me__ts-ue4dumper.md) For Unity IL2CPP dumps across a wide version range, [[frida-il2cpp-bridge]] is a common Frida-side bridge. (source: wiki/sources/descriptions/vfsfitvnm__frida-il2cpp-bridge.md) On Windows desktop, [[thats-no-pipe]] uses Frida to intercept named-pipe I/O (`NtReadFile`/`NtWriteFile` and related waits) and relay IPC to an HTTP proxy over WebSocket for protocol analysis and fuzzing. (source: wiki/sources/descriptions/synacktiv__thats_no_pipe.md) On macOS, [[frida-usb-dump]] sniffs and dumps USB traffic (Big Sur-era offsets). (source: wiki/sources/descriptions/piotrbania__frida_usb_dump.md) On iOS and macOS, [[xpc-tracer]] traces XPC IPC messages (xpcspy variant). (source: wiki/sources/descriptions/miticollo__xpc-tracer.md) On Android ARM64, [[rust-frida]] offers a Frida-like injector/agent stack (QuickJS, Java/native/stealth hooks, QBDI) that pairs with [[mkpms]] wxshadow KPM stealth (R^X page-split hook; bypass self-read integrity). (source: wiki/sources/descriptions/kkkbbb__rustFrida.md) (source: wiki/sources/descriptions/kkkbbb__mkpms.md)

## Related

[[il2cpp]] · [[nightowl]] · [[frida-il2cpp-bridge]] · [[frida-android-hook]] · [[frida-scripts]] · [[frida-stack]] · [[frida-usb-dump]] · [[xpc-tracer]] · [[fridare]] · [[florida-zygisk]] · [[zygisk-frida]] · [[rust-frida]] · [[mkpms]] · [[antifrida]] · [[frida-detection]] · [[ts-ue4dumper]] · [[thats-no-pipe]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
