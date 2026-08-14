---
title: lenovo-exec
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__lenovo_exec.md
updated: 2026-08-08
confidence: medium
---

# lenovo-exec

Exploit for a Lenovo kernel driver vulnerability in **`LenovoDiagnosticsDriver.sys`**: abuses the signed driver's insecure IOCTL interface to execute custom code in kernel mode, demonstrating a [[byovd]] chain from user-mode to arbitrary kernel code execution. Aimed at BYOVD researchers studying Lenovo driver vulnerabilities. (source: wiki/sources/descriptions/gmh5225__lenovo_exec.md)

Sibling gmh5225 projects on the same OEM driver include [[lenovo-mapper]] (manual unsigned driver map via memory-access IOCTLs), [[cve-2022-3699]] (CVE-2022-3699 PoC; IOCTL validation → arbitrary kernel memory access / LPE), and other Lenovo OEM research such as [[lenovo-cve-2025-8061]] (`LnvMSRIO.sys` LPE) and [[phantomkiller]] (`BootRepair.sys` process kill).

## Links

- Repo: https://github.com/gmh5225/lenovo_exec

## Related

[[byovd]] · [[lenovo-mapper]] · [[cve-2022-3699]] · [[lenovo-cve-2025-8061]] · [[phantomkiller]] · [[pdfwkrnl-exploit]] · [[vdk]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
