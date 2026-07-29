---
title: osslsigncode
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/mtrojnar__osslsigncode.md
updated: 2026-07-29
confidence: medium
---

# osslsigncode

Cross-platform Authenticode signing tool built on OpenSSL and cURL. Signs and timestamps PE (EXE/SYS/DLL), CAB, CAT, MSI, APPX, and PowerShell/JS script files without requiring Windows or Microsoft `signtool`. Supports PKCS#12/PFX certificates, PKCS#11 hardware tokens (e.g. SoftHSM), RFC 3161 timestamping, page-hash computation, nested signatures, and catalog-file creation. (source: wiki/sources/descriptions/mtrojnar__osslsigncode.md)

Complements Linux UEFI PE-COFF signing via [[pesign]] and offensive Authenticode transplant tooling such as [[sigthief]]: here the focus is legitimate cross-platform signing for drivers, installers, and scripts in AC/sign-tool and kernel-trust research, not signature theft or CI bypass.

## Links

- Repo: https://github.com/mtrojnar/osslsigncode

## Related

[[pesign]] · [[sigthief]] · [[magic-signer]] · [[pastdse]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
