---
title: Android-VirtualCam-Manager
kind: entity
topics: [mobile-security, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/smithluke874__Android-VirtualCam-Manager.md
updated: 2026-08-01
confidence: medium
---

# Android-VirtualCam-Manager

Rooted Android **virtual camera** system that replaces live camera feeds with pre-recorded video. Combines a **Magisk/Zygisk** module with a Kotlin Jetpack Compose controller app (control files, media import) and native C++ **ArtHook** hooks on Camera1 APIs (`setPreviewTexture`, `startPreview`, `PreviewCallback`) for surface rendering and NV21 frame injection—no LSPosed/Xposed required. (source: wiki/sources/descriptions/smithluke874__Android-VirtualCam-Manager.md)

Frame delivery follows the classic `android_virtual_cam` pattern: **MediaPlayer** for preview surfaces and **MediaCodec** decoding `virtual.mp4` into NV21 buffers for callback-based apps. Multi-ABI Zygisk builds, process gating with hook-status telemetry, and one-tap enable/import via root shell.

Research focus: camera spoofing, anti-cheat camera checks, and liveness/identity-verification bypass on Android. Contrasts with Xposed GPS spoof modules such as [[locusmimic]] and no-root inject paths such as [[android-virtual-inject]].

## Links

- Repo: https://github.com/smithluke874/Android-VirtualCam-Manager

## Related

[[magisk]] · [[zygisk]] · [[locusmimic]] · [[android-virtual-inject]] · [[mobile-anti-cheat]] · [[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
