---
title: Cognitor
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/kernelstub__Cognitor.md
updated: 2026-08-02
confidence: medium
---

# Cognitor

Go-based Windows kernel driver static analysis: ingest IDA or Ghidra exports to map IOCTL handlers and flag access-check gaps, ALPC issues, COM vulnerabilities, and unsafe native API usage via configurable rules. Defensive Patch Tuesday workflows compare Windows snapshots with PE/driver IOCTL semantic diff, a rule engine, lab dossiers, and SARIF/MD/JSON output for sibling-bug triage. (source: wiki/sources/descriptions/kernelstub__Cognitor.md)

Complements interactive disassembler annotation (e.g. [[ida-kmdf]]) and general PE triage via sibling [[retract]] — focused on `.sys` security review rather than live attach or broad malware triage.

## Links

- Repo: https://github.com/kernelstub/Cognitor

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[retract]] · [[ida-kmdf]] · [[kernforge]]
