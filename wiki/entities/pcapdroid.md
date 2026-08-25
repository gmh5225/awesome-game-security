---
title: PCAPdroid
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/emanuele-f__PCAPdroid.md
updated: 2026-08-25
confidence: medium
---

# PCAPdroid

**PCAPdroid** is a privacy-friendly open-source Android app for tracking, analyzing, and blocking connections made by other apps on the device. It exports PCAP traffic dumps, inspects HTTP, decrypts TLS, and supports broader mobile wire-analysis workflows aimed at game-security researchers and reverse engineers studying offensive techniques in the cheat / Android Network Explorer lane. (source: wiki/sources/descriptions/emanuele-f__PCAPdroid.md)

Sits beside VPN/MITM stacks such as [[lamda]] and [[android-proxy-mcp]], and kernel/eBPF capture toolkits such as [[peetch]].

## Capabilities

| Feature | Role |
|---------|------|
| Per-app connection monitor | Track, analyze, and block outbound traffic |
| PCAP export | Offline wire analysis in standard tools |
| HTTP inspection | Plaintext protocol RE without full MITM setup |
| TLS decrypt | Inspect encrypted mobile game/API traffic |

## Links

- Repo: https://github.com/emanuele-f/PCAPdroid

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[rtl8852au-userspace]] · [[peetch]] · [[lamda]] · [[android-proxy-mcp]] · [[move-certificate]] · [[pcapplusplus]]
