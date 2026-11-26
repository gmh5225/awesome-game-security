---
title: VD Google
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/VD171__VD-Google.md
updated: 2026-11-26
confidence: medium
---

# VD Google

**VD Google** (VD171/VD-Google) is a rooted **Android** app and optional **Magisk / KernelSU / APatch WebUI** module that reads **Google-local** records for **RCS**, **Google Wallet**, **DroidGuard**, and **Play Integrity** without network access. Kotlin with **Jetpack Compose** and Material 3; superuser reads system-protected databases and caches; bundled **sqlite3** helper for on-device SQL. (source: wiki/sources/descriptions/VD171__VD-Google.md)

## Signals surfaced

RCS and Wallet attestation state, **Play Protect** certification, cached Play Integrity attestations with expiry, and which apps recently requested Play Integrity checks. Plain-language explanations and **JSON export** support automated device review and lab baselines.

## Privacy and root stack

Declares **no Android permissions** (including no internet). Targets **KernelSU**, **APatch**, and **Magisk** root hosts. Audience: security researchers, privacy-focused power users, and engineers studying mobile attestation and anti-abuse signals.

## Positioning

Complements live attestation probes such as [[securify]] and [[keyattestation]] with **offline cache forensics** of what Google already stored on-device. Pairs with sibling VD171 module [[vd-backup]] for evidence preservation on the same root stacks.

## Links

- Repo: https://github.com/VD171/VD-Google

## Related

[[overviews/mobile-security]] · [[mobile-trust-boundaries]] · [[vd-backup]] · [[keyattestation]] · [[securify]] · [[magisk]] · [[kernelsu]] · [[apatch]]