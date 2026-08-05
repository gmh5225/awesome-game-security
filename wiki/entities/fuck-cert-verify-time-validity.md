---
title: FuckCertVerifyTimeValidity
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/hzqst__FuckCertVerifyTimeValidity.md
updated: 2026-08-05
confidence: medium
---

# FuckCertVerifyTimeValidity

Microsoft **Detours** hook DLL for **Sign Leaked Cert** research: after **LordPE** adds an import on `signtool.exe`, `DSignTool`, or `CSignTool`, the module hooks `crypt32!CertVerifyTimeValidity` to always return success and optionally hooks `kernel32!GetLocalTime` so a `-fuckyear` CLI flag can supply a signing-time year (e.g. 2011) without manually rolling back system clock. Lets anti-cheat engineers sign with outdated or leaked Authenticode material for defensive sign-tool study. (source: wiki/sources/descriptions/hzqst__FuckCertVerifyTimeValidity.md)

Contrasts with [[sign-expired]] (XmlLite.dll sideload + in-process `WriteProcessMemory` patch of the same APIs) and [[magic-signer]] (admin leaked-cert signer with TLS side effects): here expiry bypass is via Detours import injection into the signing tool process.

## Links

- Repo: https://github.com/hzqst/FuckCertVerifyTimeValidity

## Related

[[sign-expired]] · [[magic-signer]] · [[pastdse]] · [[lazy-sign]] · [[signtoolgui]] · [[osslsigncode]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
