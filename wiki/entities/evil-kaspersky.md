---
title: EvilKaspersky
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__EvilKaspersky.md
updated: 2026-08-13
confidence: medium
---

# EvilKaspersky

Tool (gmh5225; README `[Kaspersky]`) that **abuses Kaspersky's signed kernel-mode drivers** for unauthorized privileged operations. It leverages trusted Kaspersky driver capabilities to execute kernel code while activity appears as legitimate antivirus behavior to other security software — a security-product [[byovd]] lane distinct from hypervisor syscall redirection in [[kaspersky-hook]]. (source: wiki/sources/descriptions/gmh5225__EvilKaspersky.md)

## Links

- Repo: https://github.com/gmh5225/EvilKaspersky

## Related

[[byovd]] · [[kaspersky-hook]] · [[terminator]] · [[watchdog-killer]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
