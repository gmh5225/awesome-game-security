---
title: Keybuster
kind: entity
topics: [mobile-security, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/shakevsky__keybuster.md
updated: 2026-07-22
confidence: medium
---

# Keybuster

Samsung TrustZone Keymaster attack research client that exploits vulnerabilities in the S-Keymaster trusted application to extract hardware-protected cryptographic keys from Samsung Galaxy devices via the TEE interface. Sends unfiltered requests through `libkeymaster_helper`; USENIX Security'22 supplemental; PoC for CVE-2021-25444 / CVE-2021-25490. (source: wiki/sources/descriptions/shakevsky__keybuster.md)

Complements defensive HW attestation samples such as [[keyattestation]]: shows how Keymaster TA bugs can undermine the trust assumptions behind hardware-backed keys used in mobile integrity / anti-cheat attestation designs. Related TrustZone attack-surface study: [[cve-2021-1961]] (Qualcomm QSEECOM / Widevine).

## Links

- Repo: https://github.com/shakevsky/keybuster
- CVEs: CVE-2021-25444, CVE-2021-25490

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[keyattestation]] · [[cve-2021-1961]] · [[android-vuln]] · [[magiskdetector]]
