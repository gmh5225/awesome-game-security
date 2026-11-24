---
title: SecurityAnalyzer
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/jumpeip__SecurityAnalyzer.md
updated: 2026-11-24
confidence: medium
---

# SecurityAnalyzer

**SecurityAnalyzer** (jumpeip/SecurityAnalyzer) is a **Ghidra extension** (Java, Gradle) for **defensive binary triage**: vulnerability patterns, malware behavior, cryptography, and obfuscation recovery. **P-code–based analyzers** flag dangerous API usage, format-string and integer-overflow patterns, anti-debug and process-injection indicators, crypto constant signatures, XOR loops, entropy windows, and stack-string recovery. Findings land as in-listing **bookmarks and comments**, a dockable results panel, and **Markdown / JSON / vulnerability writeup** exports. A companion **headless script** supports batch scans. Suited to malware analysis, security research, and documentation around reverse engineering and binary hardening—not exploit development. (source: wiki/sources/descriptions/jumpeip__SecurityAnalyzer.md)

## Positioning

README category: **Ghidra extension** for P-code vulnerability and malware triage with crypto/obfuscation recovery and report export. Complements angr-heavy Ghidra audit tools such as [[vulnhunter4ghidra]] (source–sink taint, CWE tags) and [[ghidra-obfuscation-detection]] (heuristic obfuscation triage) by staying **in-process on P-code** without an external symbolic engine—closer to interactive annotation workflows like [[better-string-analyzer]].

## Links

- Repo: https://github.com/jumpeip/SecurityAnalyzer

## Related

[[overviews/reverse-engineering]] · [[ghidra]] · [[vulnhunter4ghidra]] · [[ghidra-obfuscation-detection]] · [[better-string-analyzer]] · [[angry-ghidra]]