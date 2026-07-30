---
title: SDCM
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/microsoft__SDCM.md
updated: 2026-07-30
confidence: medium
---

# SDCM

**Surface Dev Center Manager** — Microsoft CLI that automates Partner Center (Hardware Dev Center) workflows over REST APIs. Supports programmatic creation of Attestation/WHQL product submissions, download of Microsoft-signed driver packages, and management of shipping labels for Windows Update driver distribution. (source: wiki/sources/descriptions/microsoft__SDCM.md)

Useful for game-security and driver researchers studying the **legitimate** WHQL/Attestation signing path—how vendors get Microsoft-trusted kernel drivers onto Windows Update—contrasted with BYOVD abuse of unrelated signed vulnerable drivers ([[byovd]]) or leaked-cert signing tooling ([[magic-signer]], [[pastdse]]).

Complements low-level Authenticode digest work ([[pedigest]]) and cross-platform sign tooling ([[osslsigncode]], [[pesign]]) on the driver-trust / sign-tools lane.

## Links

- Repo: https://github.com/microsoft/SDCM

## Related

[[pedigest]] · [[osslsigncode]] · [[pesign]] · [[byovd]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
