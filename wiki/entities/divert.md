---
title: Divert (WinDivert)
kind: entity
topics: [game-hacking, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/basil00__Divert.md
updated: 2026-08-18
confidence: medium
---

# Divert (WinDivert)

Windows packet capture and diversion library. User-mode applications intercept, modify, drop, or inject network packets in real time via a kernel driver that hooks the Windows network stack through **WFP** (Windows Filtering Platform), with layer-based filtering by IP address, port, protocol, and packet direction. The C library supports both passive sniffing and active manipulation—aimed at network security developers building firewalls, NAT, packet analyzers, and tunneling tools on Windows. In game-security work it sits in the Cheat → **Packet Divert** lane for protocol RE and traffic manipulation beside NDIS capture stacks such as [[ndisapi]] and [[npcap]]. (source: wiki/sources/descriptions/basil00__Divert.md)

## Links

- Repo: https://github.com/basil00/Divert

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[ndisapi]] · [[npcap]] · [[packet-sniffer]] · [[inject]]
