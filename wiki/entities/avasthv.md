---
title: AvastHV
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__AvastHV.md
updated: 2026-08-14
confidence: medium
---

# AvastHV

Research project (gmh5225; README `[Avast]`) that **documents or exploits Avast antivirus's hypervisor component** for kernel-level operations. It demonstrates using Avast's signed hypervisor driver to gain elevated privileges or execute arbitrary code in hypervisor context, leveraging Avast's trusted driver status to bypass DSE and anti-cheat protections — a security-product [[byovd]] lane focused on **AV hypervisor components** rather than standard kernel IOCTL abuse. (source: wiki/sources/descriptions/gmh5225__AvastHV.md)

## Links

- Repo: https://github.com/gmh5225/AvastHV

## Related

[[byovd]] · [[hvci]] · [[kaspersky-hook]] · [[evil-kaspersky]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
