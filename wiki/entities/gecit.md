---
title: gecit
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/boratanrikulu__gecit.md
updated: 2026-08-17
confidence: medium
---

# gecit

Cross-platform transparent proxy and network interception tool written in Go for network security testing. On Linux it uses eBPF `sock_ops` for traffic redirection; on macOS and Windows it routes through a TUN-based proxy with DNS manipulation. DPI bypass research features include fake TLS ClientHello desync and built-in DNS-over-HTTPS. (source: wiki/sources/descriptions/boratanrikulu__gecit.md)

Sits beside packet-capture stacks such as [[peetch]] and [[pcapdroid]], NDIS filter APIs such as [[ndisapi]], and parse/craft libraries such as [[pcapplusplus]].

## Platform notes

| Platform | Mechanism |
|----------|-----------|
| Linux | eBPF `sock_ops` traffic redirect |
| macOS / Windows | TUN proxy + DNS manipulation |
| All | Fake TLS ClientHello desync; built-in DoH |

## Links

- Repo: https://github.com/boratanrikulu/gecit

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[peetch]] · [[pcapdroid]] · [[ndisapi]] · [[pcapplusplus]] · [[npcap]]
