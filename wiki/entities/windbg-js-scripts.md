---
title: WinDbg-JS-Scripts
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/KasperskyLab__WinDbg-JS-Scripts.md
updated: 2026-08-24
confidence: medium
---

# WinDbg-JS-Scripts

**WinDbg-JS-Scripts** (KasperskyLab) is a collection of **JavaScript scripts for WinDbg** that helps analysts examine **Windows memory dumps**. Commands cover finding exception-record candidates, walking **STL map** structures, fixing broken **noexcept** stack traces, and inspecting **x86 stacks in x64 kernel dumps**. The codebase is primarily JavaScript with supporting manifest XML files and a small Python helper for related debugging workflows. Primary audience: reverse engineers and game-security researchers who need faster low-level dump triage during anti-cheat and malware analysis. (source: wiki/sources/descriptions/KasperskyLab__WinDbg-JS-Scripts.md)

Complements other JS WinDbg automation collections such as [[windbg-scripts]] and [[windbg-cookbook]], and KasperskyLab IDA tooling such as [[hrtng]].

## Links

- Repo: https://github.com/KasperskyLab/WinDbg-JS-Scripts (README tag: JS Scripts)

## Related

[[windbg-scripts]] · [[windbg-cookbook]] · [[awesome-windbg-extensions]] · [[mcp-windbg]] · [[hrtng]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
