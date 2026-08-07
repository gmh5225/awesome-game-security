---
title: Ghost
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/pandaadir05__ghost.md
updated: 2026-08-07
confidence: medium
---

# Ghost

Cross-platform **process injection detection** framework in Rust that scans running processes for code injection, memory tampering, and common evasion techniques used by malware and unauthorized injected code. Detects suspicious RWX memory regions, shellcode patterns, API and library hooks, process hollowing, thread anomalies, and optional YARA rule matches, mapping findings to MITRE ATT&CK techniques. Ships with a CLI and interactive terminal UI supporting continuous watch mode, baseline differencing, configurable TOML settings, and webhook alerts, plus an optional Python machine learning module for behavioral and shellcode classification. Runs on Windows, Linux, and macOS for security researchers, defenders, and game anti-cheat analysts who need live endpoint detection of injection-based threats. (source: wiki/sources/descriptions/pandaadir05__ghost.md)

Complements Windows-focused injection catalogs such as [[windows-process-injection]], kernel DLL thread injection detectors such as [[dll-thread-injection-detector]], ETW ThreatIntel consumers such as [[tietwagent]], and live PE/hook scanners such as [[pe-sieve]] / [[xmalhunter]].

## Links

- Repo: https://github.com/pandaadir05/ghost

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[windows-process-injection]] · [[dll-thread-injection-detector]] · [[tietwagent]] · [[pe-sieve]] · [[xmalhunter]] · [[hookhunter]] · [[injectors]]
