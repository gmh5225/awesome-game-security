---
title: dwm-window-capture
kind: entity
topics: [graphics-api, anti-cheat]
sources:
  - wiki/sources/descriptions/vmguard__dwm-window-capture.md
updated: 2026-09-10
confidence: medium
---

# dwm-window-capture

Small Windows utility (vmguard) that captures the **currently focused window** using **Direct3D 11** and **Desktop Window Manager (DWM) redirection surfaces**, then saves the result as a PNG. It avoids traditional GDI **BitBlt** screen capture by obtaining GPU-backed window surfaces through **undocumented DWM exports**, copying the shared texture to a staging resource, reading pixels back to the CPU, and encoding output with the **Windows Imaging Component (WIC)**. Written in C++17 with D3D11 device creation, COM initialization, and a global hotkey (**Alt+Insert**) to snapshot the foreground window on demand. Aimed at researchers studying Windows graphics internals, screen capture techniques, and game security topics such as how protected or GPU-accelerated windows can still be captured outside standard GDI paths. (source: wiki/sources/descriptions/vmguard__dwm-window-capture.md)

README tag: `[DWM Redirect]` — Anti Cheat → Screenshot lane.

## Links

- Repo: https://github.com/vmguard/dwm-window-capture

## Related

[[screenshot]] · [[dwm-screen-shot]] · [[disablenvidiascreenshot]] · [[anti-screenshot-capture]] · [[present-hook]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]]
