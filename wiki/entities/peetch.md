---
title: peetch
kind: entity
topics: [game-hacking, mobile-security]
sources:
  - wiki/sources/descriptions/quarkslab__peetch.md
updated: 2026-07-25
confidence: medium
---

# peetch

Quarkslab eBPF toolkit for process-aware network traffic capture and TLS inspection: `dump` sniffs packets with PID/process attribution; `tls` extracts OpenSSL keys/master secrets; `proxy` intercepts and decrypts TLS. Outputs PCAPng for Scapy; targets OpenSSL, IPv4, TLS 1.2. Aimed at game-security researchers and REs in the cheat / Android kernel-explorer lane. (source: wiki/sources/descriptions/quarkslab__peetch.md)

Sits beside packet-capture stacks such as [[pcapplusplus]] and HTTP/HTTPS capture MCP such as [[android-proxy-mcp]].

## Links

- Repo: https://github.com/quarkslab/peetch

## Related

[[overviews/game-hacking]] · [[overviews/mobile-security]] · [[pcapplusplus]] · [[android-proxy-mcp]] · [[ndisapi]]
