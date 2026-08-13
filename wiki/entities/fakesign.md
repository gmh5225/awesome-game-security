---
title: FakeSign
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__FakeSign.md
updated: 2026-08-13
confidence: medium
---

# FakeSign

Tool that applies fake Authenticode signatures to PE binaries to bypass signature verification checks. Crafts certificate data structures that pass superficial validation while not being cryptographically valid — useful for evading signature-presence checks rather than full chain-of-trust validation. README category: Fake Cert. (source: wiki/sources/descriptions/gmh5225__FakeSign.md)

Contrasts with real cert synthesis via [[lazy-sign]] (Microsoft devkit binaries), signature transplantation via [[sigthief]], and in-place signed-PE patching via [[sigflip]]: here the focus is injecting structurally plausible but invalid Authenticode material onto unsigned binaries.

## Links

- Repo: https://github.com/gmh5225/FakeSign

## Related

[[lazy-sign]] · [[sigthief]] · [[sigflip]] · [[chainoffools]] · [[pesign-analyzer]] · [[pedigest]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
