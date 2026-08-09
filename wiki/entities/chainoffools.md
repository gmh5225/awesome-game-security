---
title: ChainOfFools
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__chainoffools.md
updated: 2026-08-09
confidence: medium
---

# ChainOfFools

Python PoC for **CVE-2020-0601** (Windows **CryptoAPI** ECC certificate spoofing — **CurveBall** / **ChainOfFools**). Uses `gen-key.py` plus OpenSSL to craft a rogue P-384 private key whose public point matches a trusted root CA, then mint a spoofed intermediate CA and leaf certificates that unpatched Windows validates as legitimate. README categories: **CVE** and **Fake Cert**. gmh5225 fork of [kudelskisecurity/chainoffools](https://github.com/kudelskisecurity/chainoffools). (source: wiki/sources/descriptions/gmh5225__chainoffools.md)

Contrasts with leaked-cert signers such as [[magic-signer]] and fake-cert devkit tooling such as [[lazy-sign]]: here the attack forges elliptic-curve parameters so a new private key reproduces an existing trusted root public key, rather than transplanting signatures ([[sigthief]]) or signing with leaked material.

## Links

- Repo: https://github.com/gmh5225/chainoffools
- Upstream: https://github.com/kudelskisecurity/chainoffools
- Advisory context: CVE-2020-0601 (Windows CryptoAPI spoofing)

## Related

[[magic-signer]] · [[lazy-sign]] · [[sigthief]] · [[sign-expired]] · [[pastdse]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
