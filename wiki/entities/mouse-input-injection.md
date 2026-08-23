---
title: mouse-input-injection
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/Zpes__mouse-input-injection.md
  - wiki/sources/descriptions/M3351AN__mouse_input_injection.md
updated: 2026-08-23
confidence: medium
---

# mouse-input-injection

Low-level mouse event injection through the undocumented **NtUserInjectMouseInput** win32k syscall. Two README-listed implementations share this entity:

| Variant | Author | Packaging | Notes |
|---------|--------|-----------|-------|
| C++ PoC | Zpes | Custom input structures + movement/click interface | Alternative to `SendInput` / `mouse_event` |
| Header-only utility | M3351AN | Single include + wrapper functions | **`mouse_event`-like API** for easier migration; minimal C/C++ |

Both target automation research, input-emulation tooling, and cheat-adjacent experimentation studying how aim/trigger logic reaches the Windows input stack and what anti-cheat telemetry can observe on win32k syscall paths. (source: wiki/sources/descriptions/Zpes__mouse-input-injection.md) (source: wiki/sources/descriptions/M3351AN__mouse_input_injection.md)

Complements preserved syscall reference [[ntuserinjectmouseinput-syscall]], MouClass kernel-driver research such as [[kernel-mouse]], and hardware/filter paths under [[hardware-input-injection]].

## Links

- Zpes repo: https://github.com/Zpes/mouse-input-injection
- M3351AN repo: https://github.com/M3351AN/mouse_input_injection

## Related

[[ntuserinjectmouseinput-syscall]] · [[kernel-mouse]] · [[hardware-input-injection]] · [[mouseclassservicecallbacktrick]] · [[mousedetection]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
