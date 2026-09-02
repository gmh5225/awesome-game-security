---
title: PSFree-Enhanced
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/ArabPixel__PSFree-Enhanced.md
updated: 2026-09-02
confidence: medium
---

# PSFree-Enhanced

**WebKit-based exploit-chain host** for jailbreaking **PlayStation 4** consoles through the system browser. Combines userland exploits (**PSFree**, **Bad Hoist**, **CSSFontFace**) with kernel privilege-escalation techniques (**Lapse**, **NetCtrl**, Sleirsgoevy's 6.7x exploit) across firmware **6.00–11.02**. (source: wiki/sources/descriptions/ArabPixel__PSFree-Enhanced.md)

Implemented mainly in **JavaScript** (ES modules; Babel for older firmwares), with supporting **C** kernel patches, HTML/CSS UI, and **Python** tooling for cache manifests. After a successful jailbreak it can load **HEN** or **GoldHEN** payloads, accept payloads on port **9020**, and optionally host or scan for devices when served locally. Targets console security researchers, reverse engineers, and users who need multi-firmware PS4 jailbreak hosting and payload delivery.

Consolidated exploit host—not a single standalone WebKit bug PoC. Sits beside [[cssfontface-exploit]] and other PlayStation browser jailbreak chains; post-jailbreak static RE tooling includes [[ida-ps4-helper]] and [[ghidra-orbis]].

## Links

- Repo: https://github.com/ArabPixel/PSFree-Enhanced

## Related

[[cssfontface-exploit]] · [[bd-un-jb]] · [[ida-ps4-helper]] · [[ghidra-orbis]] · [[ps5-linux-loader]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
