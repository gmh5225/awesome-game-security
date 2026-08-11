---
title: Hardware Input Injection
kind: concept
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/skills/game-hacking.md
  - wiki/sources/descriptions/gmh5225__Overwatch2-colorbot-Cheats.md
updated: 2026-08-11
confidence: medium
---

# Hardware Input Injection

Input paths that emit **protocol-conformant HID reports** (USB keyboard/mouse) or driver-filtered events instead of direct `SendInput` / `mouse_event` calls. Common in AI visual cheat pipelines where aim logic runs off-box or aims to reduce user-mode injection telemetry. Individual reports may look ordinary; **descriptors, timing, topology, firmware, and gameplay behavior** can still be observable. (source: wiki/sources/skills/game-hacking.md)

## Device classes

| Class | Mechanism | Trade-offs |
|-------|-----------|------------|
| KMBox Net/B Pro | TCP/UDP or serial → USB HID | Dual-PC friendly; Net uses MAC/index/CMD framing (verify per firmware) |
| Arduino / Teensy | Serial commands → ATmega32U4 HID | Low cost; custom firmware |
| Logitech driver abuse | Inject into G HUB/LGS; internal move APIs | No extra hardware; version-patched |
| interception.sys | Filter driver inject | Known signature; widely flagged |
| KVM middleman | Hardware between mouse and host | Complex setup; limited host software |

KMBox Net example command families (firmware-dependent): connect, `mouse_move`, interpolated `mouse_automove`, Bézier `mouse_beizer`, button/wheel events; encrypted `enc_*` variants resist passive packet sniffing.

## Illustrative detection-surface ordering

Not a universal stealth ranking—measure per title and AC generation:

1. Dedicated HID hardware — fewer software artifacts; device/behavior signals remain
2. KVM middleman — limited host footprint if timing/descriptors match
3. Vendor-driver abuse — process/module/version artifacts
4. Known filter drivers — driver identity and load path
5. User-mode injection APIs — direct syscall/API telemetry

Defensive pairing: [[ai-aimbot-detection]] (hardware enumeration, input micro-signatures, server replay). Offensive smoothing samples: [[human-mouse-movement]], [[pine]]. End-to-end colorbot + Arduino Leonardo serial HID samples such as [[overwatch2-colorbot-cheats]] (Python screen purple-outline detection → aim deltas → 115200-baud serial → chunked `Mouse.move()`; cheat / game:overwatch2) illustrate the Arduino/Teensy class in a zero-memory visual pipeline. (source: wiki/sources/descriptions/gmh5225__Overwatch2-colorbot-Cheats.md)

## Related

[[kernel-mouse]] · [[ai-aimbot-detection]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
