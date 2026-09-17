---
title: aaoracled
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/regulad__aaoracled.md
  - wiki/sources/README-categories.md
updated: 2026-09-17
confidence: medium
---

# aaoracled

Jailbroken iOS/iPadOS research tool that exposes a headless **App Attest oracle**: mint keys and produce attestations or assertions for caller-specified App IDs. Ships as one Debian package with **OracledDCPatch** (Theos tweak hooking `devicecheckd` to forge bundle identities) and **aaoracled** (local REST daemon driving `DCAppAttestService` for key generation, attestation, signing, and deletion). Objective-C implementation with Ghidra- and Frida-assisted offset discovery. Demonstrates that App Attest App-ID binding is enforced in userspace rather than the Secure Enclave on compromised hardware—aimed at authorized researchers evaluating anti-fraud SDKs that over-rely on App Attest, with paired server-side mitigation guidance. (source: wiki/sources/descriptions/regulad__aaoracled.md)

## Links

- Repo: https://github.com/regulad/aaoracled

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[mobile-trust-boundaries]] · [[ihide]] · [[free-rasp-ios]] · [[frida]]
