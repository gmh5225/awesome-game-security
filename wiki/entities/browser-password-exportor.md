---
title: Browser Password Exportor
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/BL0odz__BrowserPasswordExportor.md
updated: 2026-09-01
confidence: medium
---

# Browser Password Exportor

**BrowserPasswordExportor** (BL0odz) is a **Python utility** for decrypting and exporting saved browser passwords on Windows. It supports **Chromium-based browsers** (including Edge) and **Firefox** by parsing profile login databases, applying **DPAPI/AES** decryption, and handling **Firefox key-material** extraction. The code includes **ASN.1 parsing** and browser-specific routines to recover credentials from common login-storage formats. (source: wiki/sources/descriptions/BL0odz__BrowserPasswordExportor.md)

Primary use case is **authorized credential forensics**, red-team lab research, and understanding how browsers protect stored secrets — complementary to broader post-ex collectors such as [[pillager]], DPAPI attack-surface PoCs such as [[custom-dpapi]], and locked browser-database acquisition samples such as [[idontlikefilelocks]].

README category: Decrypt and export browser password, including Chromium, Edge and Firefox.

## Links

- Repo: https://github.com/BL0odz/BrowserPasswordExportor

## Related

[[pillager]] · [[custom-dpapi]] · [[idontlikefilelocks]] · [[qvoid-token-grabber]] · [[kvcforensic]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
