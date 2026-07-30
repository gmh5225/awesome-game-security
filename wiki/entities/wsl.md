---
title: WSL
kind: entity
topics: [windows-kernel, overview]
sources:
  - wiki/sources/descriptions/microsoft__WSL.md
updated: 2026-07-30
confidence: medium
---

# WSL

Official Microsoft **Windows Subsystem for Linux** open-source stack — the Windows-side userspace and VM infrastructure for running unmodified Linux ELF binaries on Windows. Components include `wsl.exe` / `wslconfig.exe` front-ends, the **Lxss Manager** service, **Plan 9 / DrvFS** filesystem integration, the **GNS** networking stack, **init/systemd** orchestration, and the lightweight utility-VM plumbing that hosts the Linux guest. Distinct from the separate [[wsl2-linux-kernel]] tree (guest kernel image) and community kernel references such as [[windows-subsystem-linux]]. Useful for Windows-subsystem researchers auditing host↔guest boundaries, networking, and filesystem bridging in the README **WSL** lane. (source: wiki/sources/descriptions/microsoft__WSL.md)

## Links

- Repo: https://github.com/microsoft/WSL

## Related

[[wsl2-linux-kernel]] · [[windows-subsystem-linux]] · [[overviews/windows-kernel]] · [[conbeerlib]] · [[winvisor]] · [[kace]]
