---
title: vmem-decrypt
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/heeeyaaaa__vmem-decrypt.md
updated: 2026-08-05
confidence: medium
---

# vmem-decrypt

Pure-Python tooling to decrypt VMware vTPM-encrypted `.vmem`, `.vmsn`, `.vmss`, and `.nvram` artifacts using the VM password. Uses encobj AES-256-CBC; `vmem_flatten.py` produces a Volatility 3-ready memory image. Supports Win11 partial VM encryption. Decrypted `.vmsn`, `.vmss`, and `.nvram` outputs are directly usable without flattening. Aimed at anti-cheat engineers and defensive researchers in the Information System & Forensics lane. (source: wiki/sources/descriptions/heeeyaaaa__vmem-decrypt.md)

Upstream to offline RAM analysis via [[volatility3]] when VMware snapshots are vTPM-protected; complements in-place VM credential extractors such as [[vmkatz]] on unencrypted VM artifacts.

## Links

- Repo: https://github.com/heeeyaaaa/vmem-decrypt

## Related

[[volatility3]] · [[volatility]] · [[vmkatz]] · [[kvcforensic]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
