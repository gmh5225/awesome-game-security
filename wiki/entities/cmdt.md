---
title: CmdT
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/wesmar__CmdT.md
updated: 2026-07-19
confidence: medium
---

# CmdT

Compact Windows utility that launches processes under a TrustedInstaller service token so they can access TrustedInstaller-ACL–protected resources without taking ownership. Dual-mode GUI and CLI binaries written entirely in hand-coded native x86/x64 assembly (no C runtime or third-party deps; ~40 KiB / ~30 KiB). (source: wiki/sources/descriptions/wesmar__CmdT.md)

Key capabilities: duplicate the TrustedInstaller process token, enable a large privilege set, UAC self-elevation, Explorer context-menu install, CLI I/O redirection relay, optional MRU history, plus related system-maintenance helpers (Sticky Keys IFEO, Defender exclusions). Aimed at admin, forensics, and reverse-engineering workflows where SYSTEM alone is not enough to modify protected OS components. (source: wiki/sources/descriptions/wesmar__CmdT.md)

## Links

- Repo: https://github.com/wesmar/CmdT

## Related

[[systeminformer]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
