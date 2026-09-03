---
title: FF ACE Anti-Cheat Analysis
kind: entity
topics: [anti-cheat, mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/Lixense__ff-ace-anticheat-analysis.md
updated: 2026-09-03
confidence: medium
---

# FF ACE Anti-Cheat Analysis

**Reverse-engineering research writeup and tooling suite** documenting how **Tencent ACE (Anti-Cheat Expert)** operates inside **Free Fire** on Android **armeabi-v7a**. Analyzes the `libanogs.so` and `libanort.so` client libraries through **IDA Pro** decompilation, cataloging byte-level detection mechanisms. (source: wiki/sources/descriptions/Lixense__ff-ace-anticheat-analysis.md)

## Detection catalog

Documented client-side checks include:

- **APK hash verification** — package integrity against expected hashes
- **Certificate parsing** — signing-chain and cert-field validation
- **Inline hook scanning** — detection of modified native code paths
- **Self-integrity checksums** — native library tamper and memory-integrity probes

## Tooling

Python and JavaScript automation supports parallel IDA workflows, string decryption, detection hunting, and a searchable **SQLite** index of findings. Extensive markdown notes accompany the scripts and shell wrappers. Targets game security researchers and anti-cheat engineers who need evidence-backed insight into ACE client behavior—not cheat implementations or bypasses.

Listed in the README under **Explore AntiCheat System:ACE** as a byte-level RE post-mortem on Tencent ACE (`libanogs`/`libanort`) in Free Fire with IDA tooling and a detection catalog.

Complements other Tencent ACE mobile RE such as [[honor-of-kings-re-research]], [[pubgm1.6-deadgame]], [[dfm-android-unicorn]], and [[kpm-memreader]] on the [[mobile-anti-cheat]] concept page.

## Links

- Repo: https://github.com/Lixense/ff-ace-anticheat-analysis

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[mobile-anti-cheat]] · [[honor-of-kings-re-research]] · [[pubgm1.6-deadgame]] · [[dfm-android-unicorn]] · [[kpm-memreader]] · [[research-rigor]]
