---
title: Driver Vuln Analyzer
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/CyberSecurityUP__DriverVuln-Analyzer-IDA-Plugin.md
updated: 2026-08-26
confidence: medium
---

# Driver Vuln Analyzer

**Driver Vuln Analyzer** (CyberSecurityUP) is a Python IDAPython plugin for static triage of potentially vulnerable Windows kernel drivers inside IDA Pro. It automatically extracts IOCTL values, decodes `CTL_CODE` fields, highlights risky `METHOD_NEITHER` usage, and flags sensitive kernel API patterns. Findings can be exported as consolidated JSON for downstream analysis pipelines. Primary users are reverse engineers and vulnerability researchers assessing driver attack surface. (source: wiki/sources/descriptions/CyberSecurityUP__DriverVuln-Analyzer-IDA-Plugin.md)

Complements interactive driver annotation via [[driver-buddy-reloaded]] and batch export-based review via [[cognitor]] — focused on in-IDA vulnerability heuristics rather than live IRP tracing or fuzzing prep.

## Links

- Repo: https://github.com/CyberSecurityUP/DriverVuln-Analyzer-IDA-Plugin

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[driver-buddy-reloaded]] · [[cognitor]] · [[ioctl-helper]] · [[ida-kmdf]] · [[cfb]] · [[drvtrace]]
