---
title: pedigest
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/mihaly044__pedigest.md
updated: 2026-07-30
confidence: medium
---

# pedigest

C library for computing **Authenticode digests** of PE files. Implements the Microsoft hash-exclusion algorithm that skips the PE checksum field and the certificate/security directory while hashing the rest of the image. Uses BCrypt for SHA-1, SHA-256, SHA-384, and SHA-512; parses embedded `WIN_CERTIFICATE` structures. Built for both kernel-mode (`ksecdd.lib`) and usermode (`bcrypt.lib`) signing and verification workflows. (source: wiki/sources/descriptions/mihaly044__pedigest.md)

Complements full signing stacks such as [[osslsigncode]] and [[pesign]] and signature-transplant research such as [[sigthief]]: here the focus is the low-level digest primitive AC/sign-tool and driver-trust research depends on, not packaging or cert theft.

## Links

- Repo: https://github.com/mihaly044/pedigest

## Related

[[osslsigncode]] · [[pesign]] · [[sigthief]] · [[magic-signer]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
