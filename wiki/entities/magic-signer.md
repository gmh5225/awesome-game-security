---
title: MagicSigner
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/namazso__MagicSigner.md
updated: 2026-07-28
confidence: medium
---

# MagicSigner

Tooling to sign binaries with leaked certificates (README: Sign Leaked Cert). Requires admin privileges and can break other apps while active by invalidating certificates used by TLS/HTTPS connections. Aimed at anti-cheat engineers and defensive researchers in the sign-tools lane rather than as a production signing workflow. (source: wiki/sources/descriptions/namazso__MagicSigner.md)

Adjacent to leaked-cert / clock-rollback DSE research such as [[pastdse]], Authenticode transplant tooling such as [[sigthief]], and legitimate UEFI PE signing such as [[pesign]]: here the focus is signing with leaked cert material for AC/sign-tool study, with noted TLS side effects under admin.

## Links

- Repo: https://github.com/namazso/MagicSigner

## Related

[[pastdse]] · [[sigthief]] · [[pesign]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[hvci]]
