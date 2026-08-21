---
title: StealingSignatures
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/Sentient111__StealingSignatures.md
updated: 2026-08-21
confidence: medium
---

# StealingSignatures

Small C++ utility that copies Authenticode certificate data from one PE file onto another executable. Parses PE headers to locate and duplicate the security-directory `WIN_CERTIFICATE` blob. The output carries transplanted certificate metadata but does **not** produce a cryptographically valid trusted signature—useful for testing verifier behavior, tampering detection, and trust-pipeline edge cases in Windows security research. (source: wiki/sources/descriptions/Sentient111__StealingSignatures.md)

Sits in the PE signature-transplant lane beside [[sigthief]] (user-mode `certTable` copy for weak CA/presence checks) and [[signature-kid]] (copy plus registry-hook trust patching): here the focus is explicit PE security-directory duplication without claiming OS-level trust bypass.

## Links

- Repo: https://github.com/Sentient111/StealingSignatures

## Related

[[sigthief]] · [[unsign]] · [[signature-kid]] · [[sigflip]] · [[pesign-analyzer]] · [[pedigest]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
