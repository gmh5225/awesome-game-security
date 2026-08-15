---
title: battleye-re
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/experienceds__battleye-re.md
updated: 2026-08-15
confidence: medium
---

# battleye-re

Independent reverse-engineering reference for BattlEye's kernel-mode anti-cheat driver **`BEDaisy.sys`** (experienceds). Educational security research only—documents driver internals rather than shipping bypass or cheat code. Covers PE section layout, dynamic resolution of dozens of kernel APIs, IOCTL dispatch on the BattlEye device, HAL table verification, anti-DMA behavior, a custom VM obfuscation region, and security-cookie derivation. Ships structured JSON findings, address lists, disassembly extracts, and hex dumps of key data sections for offline study. Primary audience: game-security and anti-cheat researchers analyzing how a modern kernel anti-cheat protects titles such as Enlisted. (source: wiki/sources/descriptions/experienceds__battleye-re.md)

Complements offensive BEDaisy samples such as [[bedaisy-bypass]] and APC instrumentation via [[goodeye]] with a defensive RE corpus focused on IOCTL/API surfaces, anti-DMA checks, and driver obfuscation—not report suppression or injection.

## Links

- Repo: https://github.com/experienceds/battleye-re

## Related

[[battleye]] · [[bedaisy-bypass]] · [[goodeye]] · [[battleye-region-walking]] · [[pubg-p2c-re]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
