---
title: xCam-Enhanced
kind: entity
topics: [mobile-security, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Klassiqblintz__xCam-Enhanced.md
updated: 2026-11-20
confidence: medium
---

# xCam-Enhanced

Universal Android **LibXposed** module that injects pre-recorded video or still images into live camera previews, still capture, and in-app video recording across third-party apps. Hooks **Camera1**, **Camera2**, **ImageReader**, **MediaRecorder**, **WebRTC**, and related media paths; uses **MediaCodec** surface transcoding plus YUV or JPEG synthesis so preview and recorded output stay aligned on Android 9–16. Kotlin/Java on LibXposed; targets rooted **LSPosed**-style loaders or non-root **LSPatch** patching. Pipeline telemetry, rotation/mirroring, synchronized virtual audio, and optional device or location spoof helpers support anti-fraud, anti-cheat, and identity-verification research on camera and device-integrity signals. (source: wiki/sources/descriptions/Klassiqblintz__xCam-Enhanced.md)

Contrasts with Magisk/Zygisk **ArtHook** virtual camera [[android-virtualcam-manager]] (Camera1-only, no LSPosed) and no-root inject sandboxes such as [[android-virtual-inject]].

## Links

- Repo: https://github.com/Klassiqblintz/xCam-Enhanced

## Related

[[android-virtualcam-manager]] · [[android-virtual-inject]] · [[lsposed-universal-template]] · [[xposed-module-kit]] · [[mobile-anti-cheat]] · [[overviews/mobile-security]] · [[overviews/anti-cheat]]