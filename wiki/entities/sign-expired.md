---
title: sign-expired
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/mathisvickie__sign-expired.md
updated: 2026-08-05
confidence: medium
---

# sign-expired

DLL side-loading exploit for Microsoft's `signtool.exe` that hijacks `XmlLite.dll` to patch `CertVerifyTimeValidity` (`crypt32.dll`) and `GetSystemTimeAsFileTime` (`KernelBase.dll`) in-memory via `WriteProcessMemory`, zeroing return values to bypass certificate expiration checks during Authenticode signing. README: Sign Leaked Cert. (source: wiki/sources/descriptions/mathisvickie__sign-expired.md)

Contrasts with clock-rollback paths such as [[pastdse]] and admin TLS-breaking leaked-cert signers such as [[magic-signer]]: here expiry is bypassed inside the `signtool` process via sideload + API patching, without changing system time. Sibling Detours import-hook path: [[fuck-cert-verify-time-validity]]. Complements legitimate `signtool` workflow tooling such as [[signtoolgui]] and cross-platform Authenticode tooling such as [[osslsigncode]].

## Links

- Repo: https://github.com/mathisvickie/sign-expired

## Related

[[pastdse]] · [[magic-signer]] · [[fuck-cert-verify-time-validity]] · [[signtoolgui]] · [[osslsigncode]] · [[windows-dll-hijacking]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
