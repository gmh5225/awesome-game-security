---
title: peekaboo
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/cocomelonc__peekaboo.md
updated: 2026-08-17
confidence: medium
---

# peekaboo

Modular **malware-behavior emulator** for safely reproducing threat scenarios—command-and-control communication, persistence, and lateral movement—without destructive payloads. Combines Python tooling (CLI, TUI, Flask dashboard, offline LLM worker pipeline) with portable C/C++ modules for injection, encryption, persistence, and data exfiltration, and can auto-generate obfuscated payloads using API hashing and string encryption. The dashboard integrates MITRE ATT&CK research, Malpedia threat intelligence, an APT campaign pipeline with Sigma rule coverage, YARA rule generation, and VirusTotal scanning for detection validation. Targets security researchers, red/blue teamers, and detection engineers who need predictable, reproducible threat artifacts for operator training, purple-team exercises, and defensive rule development. (source: wiki/sources/descriptions/cocomelonc__peekaboo.md)

Not to be confused with the unrelated `peekaboo` stealth memory-access module inside [[ovo]] (Android ARM64 kernel driver).

Complements sibling cocomelonc shellcode tooling [[tabby]], Windows payload build frameworks such as [[scfw]] and [[shellcode-factory]], static packer triage via [[packpeek]], YARA authoring via [[hyara]], and AC evaluation harnesses such as [[anti-cheat-testing-framework]].

## Links

- Repo: https://github.com/cocomelonc/peekaboo

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[tabby]] · [[scfw]] · [[shellcode-factory]] · [[packpeek]] · [[hyara]] · [[xmalhunter]] · [[anti-cheat-testing-framework]]
