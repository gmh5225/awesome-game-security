---
title: nvidiaCapture
kind: entity
topics: [graphics-api, anti-cheat]
sources:
  - wiki/sources/descriptions/TheCruZ__nvidiaCapture.md
updated: 2026-09-10
confidence: medium
---

# nvidiaCapture

Windows proof-of-concept (TheCruZ) that captures the **real on-screen image** by reading the NVIDIA GPU **scanout buffer** through the undocumented **`NvAPI_D3D11_WksReadScanout`** function. Unlike conventional capture APIs such as **BitBlt**, **DXGI OutputDuplication**, or **PrintWindow**, this path operates **below user-mode graphics hooks** that cheat software uses to hide overlays and return sanitized screenshots. Written in C++ with **Direct3D 11**, **DXGI**, and **NVAPI**; saves the captured framebuffer to a **PNG** and reports NVAPI errors when capture is blocked or unsupported. Intended for anti-cheat and game security researchers studying screenshot-evasion techniques on NVIDIA hardware running **Windows 10 or later**. (source: wiki/sources/descriptions/TheCruZ__nvidiaCapture.md)

README tag: `[NVIDIA Scanout]` — Anti Cheat → Screenshot lane.

## Links

- Repo: https://github.com/TheCruZ/nvidiaCapture

## Related

[[disablenvidiascreenshot]] · [[dwm-window-capture]] · [[screenshot]] · [[screencapture]] · [[anti-screenshot-capture]] · [[present-hook]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]]
