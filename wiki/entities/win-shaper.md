---
title: win-shaper
kind: entity
topics: [game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/WPO-Foundation__win-shaper.md
updated: 2026-08-19
confidence: medium
---

# win-shaper

Windows **traffic-shaping packet filter** for emulating real-world network conditions. A kernel driver built on **WFP** (Windows Filtering Platform) callouts pairs with command-line and GUI control apps to inject latency, limit bandwidth, apply packet loss, and manage queue sizes on inbound and outbound traffic. Intended for testing network-sensitive software and games under controlled adverse conditions — sits in the Game Testing / Packet Sniffer&Filter lane beside WFP diversion stacks such as [[divert]] and NDIS capture tools such as [[ndisapi]]. (source: wiki/sources/descriptions/WPO-Foundation__win-shaper.md)

## Links

- Repo: https://github.com/WPO-Foundation/win-shaper

## Related

[[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[divert]] · [[ndisapi]] · [[packet-sniffer]] · [[gatling]]
