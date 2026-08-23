---
title: TrustMeBro
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/KriyosArcane__TrustMeBro.md
updated: 2026-08-23
confidence: medium
---

# TrustMeBro

Authenticode signature manipulation toolkit for authorized red-team operations and Windows security research. Ships Python and C++ implementations for stealing and cloning PE signatures, embedding payloads in PKCS#7 certificate data, and hijacking Subject Interface Package (SIP) providers across 19 file types. Key techniques include WinVerifyTrust FinalPolicy bypass, Smart App Control evasion on Windows 11, SIP execution-surface implants for lateral movement (SIPExec), and analyst-triggered persistence via CryptDllFormatObject handlers (FormatGhost). Bundles YARA and Sigma detection rules, SigStash payload extraction tooling, and remote registry orchestration via Impacket. Intended for authorized offensive security testing, trust-control research, and understanding how adversaries subvert Windows code-signing enforcement. (source: wiki/sources/descriptions/KriyosArcane__TrustMeBro.md)

Extends the PE signature-transplant lane ([[sigthief]], [[stealing-signatures]], [[signature-kid]]) with SIP-level provider hijacking, PKCS#7 steganography, and verification-chain bypass—not just copying `WIN_CERTIFICATE` blobs. Complements signature stripping ([[unsign]]) and in-place signed patching ([[sigflip]]) on the Authenticode manipulation spectrum.

## Links

- Repo: https://github.com/KriyosArcane/TrustMeBro

## Related

[[sigthief]] · [[stealing-signatures]] · [[signature-kid]] · [[sigflip]] · [[unsign]] · [[pesign-analyzer]] · [[pedigest]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
