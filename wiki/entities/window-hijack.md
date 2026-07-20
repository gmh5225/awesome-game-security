---
title: window_hijack
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/thesecretclub__window_hijack.md
updated: 2026-07-20
confidence: medium
---

# window_hijack

Windows kernel driver that hijacks window handles for covert kernel↔usermode communication—dispatch control handlers, process-info getters, and NT/windowing subsystem headers for studying window-object manipulation and stealth driver channels (README: hijacking thread contexts). (source: wiki/sources/descriptions/thesecretclub__window_hijack.md)

Research sample for kernel / game-security work on Ring0↔UM paths that avoid obvious IOCTL or named-device surfaces—not a production stack.

## Links

- Repo: https://github.com/thesecretclub/window_hijack

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[boom]] · [[data-ptr-swap]] · [[evcommunication]] · [[double-callback]]
