---
title: LolDriverScan
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/FourCoreLabs__LolDriverScan.md
updated: 2026-08-25
confidence: medium
---

# LolDriverScan

Go-based scanner that detects known vulnerable drivers on a Windows host. Pulls vulnerable-driver intelligence from a public driver threat feed and compares it against local driver hashes and metadata. Supports verbose reporting and JSON export for automation or integration into security workflows, and is designed to run without elevated privileges. Aimed at defensive security auditing—system hardening and anti-cheat environment checks—rather than offensive BYOVD exploitation. (source: wiki/sources/descriptions/FourCoreLabs__LolDriverScan.md)

## Links

- Repo: https://github.com/FourCoreLabs/LolDriverScan

## Related

[[loldrivers]] · [[loldrivers-client]] · [[driver-risk-scout]] · [[vulnerable-driver-scanner]] · [[hvci-loldrivers-check]] · [[byovd]] · [[ms-vulnerable-driver-list]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
