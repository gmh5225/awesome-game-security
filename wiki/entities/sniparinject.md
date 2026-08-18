---
title: SniParInject
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/airvzxf__sniparinject.md
updated: 2026-08-18
confidence: medium
---

# SniParInject

Python toolkit (**Sn**iffer, **Par**ser, **Inject**) that captures live network traffic with Scapy on a chosen interface, filters by server IP and port, and maps protocol opcodes to readable fields through YAML rules—without changing source code. Struct definitions can declare binary fields (integers, shorts, character sequences) with hex or formatted output for both host and node traffic. Packet injection is planned but not yet complete. Aimed at game-security researchers and reverse engineers who need to inspect and decode live game protocol traffic; demonstrated with Mana Plus. (source: wiki/sources/descriptions/airvzxf__sniparinject.md)

Distinct from wire-level craft/inject CLI tooling such as [[inject]] and C/C++ decryptor loggers such as [[packet-sniffer]]; SniParInject focuses on declarative YAML-driven decode of game opcodes over Scapy capture.

## Links

- Repo: https://github.com/airvzxf/sniparinject

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[packet-sniffer]] · [[inject]] · [[pcapplusplus]] · [[peetch]]
