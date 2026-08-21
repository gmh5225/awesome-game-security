---
title: DriverRiskScout
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Systemhaus-Schulz__DriverRiskScout.md
updated: 2026-08-20
confidence: medium
---

# DriverRiskScout

Read-only defensive tool for assessing Windows kernel-driver exposure and risk on endpoints. Written primarily in PowerShell with an optional Python-based central collector server, it inventories loaded, installed, and DriverStore drivers, verifies signatures, and correlates hashes against [[loldrivers]], Microsoft's vulnerable-driver blocklist ([[ms-vulnerable-driver-list]]), and curated [[byovd]] research profiles. Applies static PE analysis, YARA rules, exploitability scoring, and event-log correlation from Sysmon and Code Integrity while detecting [[hvci]], VBS, WDAC, and other protection posture. Reports export as CSV, JSON, HTML, and Wazuh NDJSON, with optional NVD CVE enrichment and Sigma rule generation. Aimed at defenders, incident responders, and game-security teams hunting BYOVD abuse and other kernel-level threats without exploiting drivers or modifying the host. (source: wiki/sources/descriptions/Systemhaus-Schulz__DriverRiskScout.md)

## Links

- Repo: https://github.com/Systemhaus-Schulz/DriverRiskScout

## Related

[[byovd]] · [[loldrivers]] · [[ms-vulnerable-driver-list]] · [[hvci]] · [[vulnerable-driver-scanner]] · [[vulnerable-driverscanner]] · [[byovdfinder]] · [[loldrivers-client]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
