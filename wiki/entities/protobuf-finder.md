---
title: protobuf-finder
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Accenture__protobuf-finder.md
updated: 2026-09-03
confidence: medium
---

# protobuf-finder

**Accenture/protobuf-finder** — **IDA Pro** plugin (Python / IDAPython) that reconstructs original **Protocol Buffer** schema information from compiled binaries. Uses the Google protobuf runtime with IDA APIs to decode embedded descriptors and display recovered `.proto` definitions. Integrates into the disassembler workflow via a dedicated search action and custom result views for easier inspection. Targets reverse engineers recovering network or serialization formats during game security and binary analysis when schemas are not published. (source: wiki/sources/descriptions/Accenture__protobuf-finder.md)

Complements published Steam/Valve schema dumps such as [[protobufs]], wire-capture tooling such as [[packet-sniffer]], and title-specific in-IDA packet helpers such as [[spirit-ida-plugin]].

## Links

- Repo: https://github.com/Accenture/protobuf-finder (README tag: [Protobuf])

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[protobufs]] · [[packet-sniffer]] · [[spirit-ida-plugin]]
