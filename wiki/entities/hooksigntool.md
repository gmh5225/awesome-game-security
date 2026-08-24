---
title: HookSigntool
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Jemmy1228__HookSigntool.md
updated: 2026-08-24
confidence: medium
---

# HookSigntool

C++ **Microsoft Detours** hook DLL for Windows **code-signing utilities** (Sign Leaked Cert lane): intercepts **certificate validity checks** and **timestamp-related signing APIs**, with redirection to custom timestamp endpoints and modified signing-time behavior via configuration or command-line parameters. Supports research and testing of Authenticode workflows, certificate validation logic, and timestamp handling. (source: wiki/sources/descriptions/Jemmy1228__HookSigntool.md)

Unlike [[sign-expired]] (XmlLite.dll sideload + in-process `WriteProcessMemory` patch) and [[fuck-cert-verify-time-validity]] (LordPE import hook focused on `CertVerifyTimeValidity` / optional `-fuckyear`), here Detours targets both expiry bypass and **timestamp endpoint/time control** in signing-tool processes. Contrasts with [[signtoolex]], which signs with leaked/expired certs but does **not** spoof Authenticode timestamps.

## Links

- Repo: https://github.com/Jemmy1228/HookSigntool

## Related

[[sign-expired]] · [[fuck-cert-verify-time-validity]] · [[signtoolex]] · [[magic-signer]] · [[signtoolgui]] · [[osslsigncode]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
