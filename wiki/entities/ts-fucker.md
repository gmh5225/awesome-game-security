---
title: TS-Fucker
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__TS-Fucker.md
updated: 2026-08-14
confidence: medium
---

# TS-Fucker

Proof-of-concept utility that toggles Windows **TestSigning** mode at runtime by abusing the Dell **`dbutil_2_3.sys`** vulnerable driver for kernel read/write access. It live-patches security-relevant system state to change the machine's test-signing flag **without a reboot**, downloads symbol files for the current Windows build to locate required kernel fields, and expects the vulnerable driver to already be loaded. The repo is a focused research sample—not a generic BYOVD toolkit—demonstrating how a kernel memory primitive can alter trust state on a running system. Mainly useful for Windows kernel researchers studying runtime test-signing manipulation, symbol-assisted offset discovery, and the practical impact of **`dbutil_2_3.sys`**. Shares the same driver backend and kernel R/W IOCTL lane as canonical LPE PoC [[cve-2021-21551]]. (source: wiki/sources/descriptions/gmh5225__TS-Fucker.md)

## Links

- Repo: https://github.com/gmh5225/TS-Fucker

## Related

[[byovd]] · [[cve-2021-21551]] · [[dse-hook]] · [[loldrivers]] · [[kdu]] · [[telemetry-sourcerer]] · [[overviews/windows-kernel]]
