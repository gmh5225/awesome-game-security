---
title: vPhone Workstation
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/zqxwce__vphone-ws.md
  - wiki/sources/README-categories.md
updated: 2026-09-08
confidence: medium
---

# vPhone Workstation

Native **macOS SwiftUI** front-end for managing virtual iPhone research VMs. Wraps [[vphone-cli]] to browse, create, boot, clone, export, and delete iOS and cloudOS virtual machines built on Apple's **Virtualization.framework** and PCC research firmware. (source: wiki/sources/descriptions/zqxwce__vphone-ws.md)

**Features:** creation wizard with security variants from minimal hardening changes to jailbreak and experimental profiles; live streamed progress from underlying CLI tasks; host readiness checks for `vphone-cli` installation, research guest permissions, and AMFI bypass before VM launch.

README category: IOS Emulator. Targets security researchers, reverse engineers, and developers who need a controlled iOS sandbox for platform security and mobile application behavior analysis.

## Links

- Repo: https://github.com/zqxwce/vphone-ws

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[vphone-cli]] · [[vphone-aio]] · [[darwin-vm]] · [[research-rigor]]
