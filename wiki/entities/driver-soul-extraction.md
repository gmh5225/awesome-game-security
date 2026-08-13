---
title: Driver-SoulExtraction
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__Driver-SoulExtraction.md
updated: 2026-08-13
confidence: medium
---

# Driver-SoulExtraction

Kernel-oriented certificate extraction toolkit that parses PE Authenticode data and returns the main signing certificate's subject and validity window — not merely whether a file is signed. (source: wiki/sources/descriptions/gmh5225__Driver-SoulExtraction.md)

The archive splits into a driver project and reusable **Lib-SoulExtraction**, embedding adapted Linux PKCS#7, ASN.1, and X.509 parsing alongside Windows-specific wrappers for kernel file access and string conversion. The core routine walks the PE signature directory, parses the PKCS#7 message, selects the likely primary certificate, and emits fields such as signer name and validity timestamps. README lane: **Extracting cert information**. Aimed at Windows kernel developers and reverse engineers who need in-kernel certificate metadata from PE files for telemetry, trust analysis, or triage tooling.

Complements usermode metadata extractors such as [[pesign-analyzer]] and low-level digest libraries such as [[pedigest]]: here the focus is **in-kernel** Authenticode certificate field extraction, not signing ([[osslsigncode]]), digest computation, or signature transplant ([[sigthief]]).

## Links

- Repo: https://github.com/gmh5225/Driver-SoulExtraction

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[pesign-analyzer]] · [[pedigest]] · [[osslsigncode]] · [[sigthief]]
