---
title: SignToolEx
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/hackerhouse-opensource__SignToolEx.md
updated: 2026-08-06
confidence: medium
---

# SignToolEx

Sign Leaked Cert tooling that enables Authenticode code-signing with expired or leaked certificates for anti-cheat / sign-tools defensive research. Unlike some sibling tools, it does **not** support spoofing Authenticode timestamps — expiry bypass is limited to signing-time certificate validity checks, not backdating the signature timestamp itself. (source: wiki/sources/descriptions/hackerhouse-opensource__SignToolEx.md)

Sits alongside [[sign-expired]] (XmlLite.dll sideload + in-process API patch), [[fuck-cert-verify-time-validity]] (Detours import hook on `CertVerifyTimeValidity`), and [[magic-signer]] (admin leaked-cert signer with TLS side effects): here the focus is leaked/expired cert signing without timestamp forgery. Complements legitimate `signtool` workflow tooling such as [[signtoolgui]] and cross-platform Authenticode tooling such as [[osslsigncode]].

## Links

- Repo: https://github.com/hackerhouse-opensource/SignToolEx

## Related

[[sign-expired]] · [[fuck-cert-verify-time-validity]] · [[magic-signer]] · [[pastdse]] · [[signtoolgui]] · [[osslsigncode]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
