---
title: DeepZero
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/416rehman__DeepZero.md
updated: 2026-09-04
confidence: medium
---

# DeepZero

**DeepZero** (416rehman) is an automated vulnerability-research framework for Windows kernel drivers. It parses and decompiles driver binaries at scale, then uses AI agents to analyze potentially exploitable IOCTL handlers and related attack surface. Primary users are kernel security researchers, BYOVD/LOLDriver analysts, and reverse engineers who need pipeline-scale driver triage beyond one-off IDA sessions. (source: wiki/sources/descriptions/416rehman__DeepZero.md)

Complements static in-IDA triage via [[driver-vuln-analyzer-ida-plugin]] and export-based batch review via [[cognitor]] — focused on automated parse/decompile pipelines and agent-driven IOCTL vulnerability analysis rather than interactive annotation alone.

## Links

- Repo: https://github.com/416rehman/DeepZero

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[driver-vuln-analyzer-ida-plugin]] · [[cognitor]] · [[ioctl-helper]] · [[cfb]] · [[byovd]] · [[kernforge]]
