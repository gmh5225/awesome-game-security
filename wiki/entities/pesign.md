---
title: pesign
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/rhboot__pesign.md
updated: 2026-07-24
confidence: medium
---

# pesign

Linux C tooling for signing and verifying UEFI Secure Boot PE-COFF binaries in Authenticode / PKCS#7 form. Generates, embeds, removes, and validates signatures on EFI bootloaders and kernel images, with certificate management via NSS databases. Aimed at Linux distribution maintainers and engineers who run Secure Boot signing infrastructure rather than at offensive bypass research. (source: wiki/sources/descriptions/rhboot__pesign.md)

Complements offensive Authenticode transplant tooling such as [[sigthief]] and early-boot Secure Boot / DSE research such as [[bootbypass]]: here the focus is legitimate firmware-compatible PE signing, not signature theft or CI bypass.

## Links

- Repo: https://github.com/rhboot/pesign

## Related

[[sigthief]] · [[bootbypass]] · [[pastdse]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[hvci]]
