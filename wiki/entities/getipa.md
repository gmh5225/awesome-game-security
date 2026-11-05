---
title: getIPA
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/RansomWhisker__getIPA.md
updated: 2026-11-05
confidence: medium
---

# getIPA

**getIPA** (RansomWhisker/getIPA) is a **Python 3 CLI** that SSHes into a **jailbroken iPhone**, lists installed App Store apps, and packages a selected bundle as a ready-to-use **IPA** in one workflow. The host side uses only the **standard library** plus the system **OpenSSH** client; optional **bagbak** (Node.js) with **Frida** on device can produce **decrypted** Mach-O instead of FairPlay-encrypted copies pulled from disk. (source: wiki/sources/descriptions/RansomWhisker__getIPA.md)

## Catalog lane

Cheat / IOS App Packaging — jailbroken iOS IPA acquisition and metadata reporting before static RE or client-protection study on owned hardware. (source: wiki/sources/descriptions/RansomWhisker__getIPA.md)

## Mechanism

1. **Connect** — SSH session to the jailbroken device; interactive app picker or scripted flags.
2. **Select** — recent user apps sorted; system bundles filtered out.
3. **Package** — bundle staged and repacked as IPA on the host (encrypted copy path, or bagbak/Frida decrypt path when enabled).
4. **Report** — optional app report: permissions, entitlements, ATS, URL schemes, embedded frameworks, encryption status (extracted or local IPAs).

Remote paths and archive data are handled defensively—path validation, safe tar extraction, sanitized filenames—because the phone is treated as **untrusted input**. Audience: security researchers and reverse engineers authorized to analyze iOS apps, including mobile game client protections. (source: wiki/sources/descriptions/RansomWhisker__getIPA.md)

## Positioning

SSH-first, stdlib-heavy workflow beside Frida-centric [[frida-ios-dump]] and deprecated Node [[bagbak]] in the same jailbroken IPA lane; complements [[copyapp]] agent evidence/rebuild tooling and static follow-on (IDA/Ghidra, [[ida-ios-helper]]).

## Links

- Repo: https://github.com/RansomWhisker/getIPA

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[frida]] · [[bagbak]] · [[frida-ios-dump]] · [[copyapp]] · [[ida-ios-helper]]
