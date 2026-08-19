---
title: mouse-input-injection
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/Zpes__mouse-input-injection.md
updated: 2026-08-19
confidence: medium
---

# mouse-input-injection

C++ demonstration of low-level mouse event injection through the undocumented **NtUserInjectMouseInput** win32k syscall. The repo defines custom input structures and a small interface layer for movement and click actions, offering an alternative to higher-level APIs such as `SendInput` and `mouse_event`. (source: wiki/sources/descriptions/Zpes__mouse-input-injection.md)

Useful for automation research, input-emulation tooling, and cheat-adjacent experimentation studying how aim/trigger logic reaches the Windows input stack and what anti-cheat telemetry can observe on win32k syscall paths. Complements preserved syscall reference [[ntuserinjectmouseinput-syscall]], MouClass kernel-driver research such as [[kernel-mouse]], and hardware/filter paths under [[hardware-input-injection]].

## Links

- Repo: https://github.com/Zpes/mouse-input-injection

## Related

[[ntuserinjectmouseinput-syscall]] · [[kernel-mouse]] · [[hardware-input-injection]] · [[mouseclassservicecallbacktrick]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
