---
title: NeacSafe-Analysis
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__NeacSafe-Analysis.md
updated: 2026-08-11
confidence: medium
---

# NeacSafe-Analysis

User-mode **NeacSafe** communication probe plus saved analysis notes (gmh5225) for reverse engineering NetEase's anti-cheat client–driver IPC. The C++ sample defines a 0x28-byte `NeacSafeConnectContext`, connects to `\NeacSafePort` via `FilterConnectCommunicationPort`, and sends encoded request buffers to query data through the minifilter communication channel. The archive also preserves a Pediy forum writeup on NeacSafe interface analysis, so the repo reproduces the port protocol alongside the original article material. (source: wiki/sources/descriptions/gmh5225__NeacSafe-Analysis.md)

Mainly useful for studying NeacSafe command-message buffer encoding, filter-manager communication ports, and user-mode access to a minifilter-backed AC driver — complementary to broader regional AC RE such as [[starrail-ace-b]] (Tencent ACE) and static XIGNCODE corpora like [[xigncode-dump]] / [[xigncode3-blackdesert]].

## Links

- Repo: https://github.com/gmh5225/NeacSafe-Analysis

## Related

[[starrail-ace-b]] · [[xigncode-dump]] · [[xigncode3-blackdesert]] · [[kernel-callbacks]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
