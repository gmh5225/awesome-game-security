---
title: FilterTap
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/weak1337__FilterTap.md
updated: 2026-09-29
confidence: medium
---

# FilterTap

Lightweight **Windows Filtering Platform (WFP)** kernel driver that passively captures network metadata at the **Ethernet frame layer**. Written in C++ with the Windows Driver Kit, it registers inbound and outbound WFP callout filters to extract the local NIC MAC and IP, the gateway MAC, and plaintext DNS query hostnames from passing traffic. Once local and gateway identifiers are collected, the driver logs them via kernel debug output and can optionally observe DNS lookups as a side effect of L2 inspection. Serves as a proof-of-concept for how anti-cheat systems such as **Easy Anti-Cheat** obtain hardware identifiers by reading frames directly in kernel space, bypassing user-mode MAC spoofing APIs — aimed at game security researchers and reverse engineers studying anti-cheat network fingerprinting and WFP-based telemetry. (source: wiki/sources/descriptions/weak1337__FilterTap.md)

## Links

- Repo: https://github.com/weak1337/FilterTap

## Related

[[easy-anti-cheat]] · [[hwid-spoofing]] · [[network-environment-evidence]] · [[divert]] · [[win-shaper]] · [[360wfp-exploit]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
