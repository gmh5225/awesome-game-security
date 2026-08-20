---
title: ida-security-scanner
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/SymbioticSec__ida-security-scanner.md
updated: 2026-08-20
confidence: medium
---

# ida-security-scanner

IDA Pro plugin (Python) that automates vulnerability discovery on decompiled pseudocode. Runs rule-based SAST scans using opengrep/semgrep-style YAML patterns and surfaces findings in an interactive IDA UI. Optional AI-assisted explanations help triage and understand reported issues. Aimed at reverse engineers, CTF players, and security auditors who want faster binary vulnerability analysis workflows. (source: wiki/sources/descriptions/SymbioticSec__ida-security-scanner.md)

Complements IoT/firmware audit tooling such as [[firmeye]], in-IDA Yara file scanning via [[yarascan-ida]], and LLM-assisted IDA assistants such as [[wpechatgpt]] and [[idassist]] when triaging risky patterns in Hex-Rays output.

## Links

- Repo: https://github.com/SymbioticSec/ida-security-scanner

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[firmeye]] · [[yarascan-ida]] · [[wpechatgpt]] · [[idassist]] · [[list-of-ida-plugins]]
