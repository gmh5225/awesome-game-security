---
title: logitech-cve
kind: entity
topics: [game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/ekknod__logitech-cve.md
  - wiki/sources/descriptions/BatogiX__logitech-cve.md
updated: 2026-08-31
confidence: medium
---

# logitech-cve

**logitech-cve** names multiple offensive/research projects that interact with **Logitech virtual drivers** to emulate HID input on Windows—mouse movement, clicks, wheel, keyboard, multi-key sequences, and text typing—via native device I/O control rather than standard user-mode injection APIs.

## Implementations

| Fork | Language | Focus |
|------|----------|-------|
| [ekknod/logitech-cve](https://github.com/ekknod/logitech-cve) | C/C++ | Driver development; cheat / triggerbot & aimbot input paths (source: wiki/sources/descriptions/ekknod__logitech-cve.md) |
| [BatogiX/logitech-cve](https://github.com/BatogiX/logitech-cve) | Rust | Typed library APIs over Logitech virtual driver handles; input-emulation research, automation experiments, vulnerable-driver attack-surface analysis (source: wiki/sources/descriptions/BatogiX__logitech-cve.md) |

Sits in the vendor-driver **HID input** lane catalogued under [[hardware-input-injection]]—alongside G HUB/LGS internal move APIs, multi-backend libraries such as [[ib-input-simulator]], and MouClass kernel samples such as [[kernel-mouse]]—when threat-modeling aim/trigger execution that avoids direct user-mode injection APIs.

## Related

[[hardware-input-injection]] · [[ib-input-simulator]] · [[kernel-mouse]] · [[mouseclassservicecallbacktrick]] · [[ntuserinjectmouseinput-syscall]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
