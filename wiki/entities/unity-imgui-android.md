---
title: Unity-ImGUI-Android
kind: entity
topics: [mobile-security, game-engine, game-hacking, graphics-api, reverse-engineering]
sources:
  - wiki/sources/descriptions/Octowolve__Unity-ImGUI-Android.md
updated: 2026-08-22
confidence: medium
---

# Unity-ImGUI-Android

**Android Unity native template** for rendering a Dear **ImGui** menu through hooked graphics and input paths (Octowolve). Uses **C++** with **[[dobby]]** hooks to intercept **`eglSwapBuffers`** and Unity input injection so overlays plus touch or key handling run inside the game process. Includes a tutorial for finding **`nativeInjectEvent`** signatures in **`libunity`** with IDA and SigMaker. Targets **mod-menu prototyping** and **mobile game reverse-engineering** research. README tag: `[Imgui For Unity]`. (source: wiki/sources/descriptions/Octowolve__Unity-ImGUI-Android.md)

Complements other Android Unity ImGui scaffolds ([[imgui-unity-android]], [[imgui-unity]], [[polarimgui]], [[android-mod-menu-imgui]]) and NDK Unity cheat templates ([[cheat-unity-games]]) when the goal is an in-process GLES + Unity input hook workflow with signature-finding guidance for `libunity` rather than external overlays ([[external-imgui-android]]) or Frida-only workflows.

## Links

- Repo: https://github.com/Octowolve/Unity-ImGUI-Android

## Related

[[dobby]] · [[imgui-unity-android]] · [[imgui-unity]] · [[polarimgui]] · [[android-mod-menu-imgui]] · [[cheat-unity-games]] · [[present-hook]] · [[il2cpp]] · [[overviews/mobile-security]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]]
