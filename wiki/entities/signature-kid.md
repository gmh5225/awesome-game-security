---
title: SignatureKid
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/dslee2022__SignatureKid.md
updated: 2026-08-16
confidence: medium
---

# SignatureKid

Header-only C++ tool that steals Authenticode digital signatures from signed PE files and copies them onto unsigned target executables, then hooks Windows registry internals so the transplanted signature appears valid to the OS. Manipulates the `WIN_CERTIFICATE` structure in the PE security directory and patches certificate trust verification at the system level. Aimed at security researchers studying code-signing bypass techniques and anti-cheat engineers evaluating signature-based trust verification robustness. (source: wiki/sources/descriptions/dslee2022__SignatureKid.md)

Extends the PE signature-transplant lane beside [[sigthief]] (user-mode `certTable` copy without registry trust patching) and [[sigflip]] (in-place signed-PE payload inject while preserving validity): here the focus is copied signatures plus system-level trust verification bypass so unsigned binaries pass OS-level Authenticode checks.

## Links

- Repo: https://github.com/dslee2022/SignatureKid

## Related

[[sigthief]] · [[sigflip]] · [[fakesign]] · [[lazy-sign]] · [[pesign-analyzer]] · [[pedigest]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
