---
title: ttddbg
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__ttddbg.md
updated: 2026-08-07
confidence: medium
---

# ttddbg

IDA Pro plugin that replays **Time Travel Debugging (TTD)** traces recorded by WinDbg inside IDA. Loads Microsoft TTD `.run` trace files and supports forward and backward stepping through recorded execution without a live debugging session, replaying syscalls, memory operations, and register state from the capture. Aimed at reverse engineers and malware analysts who want IDA Pro's static analysis and decompilation alongside TTD's time-travel debugging workflow. (source: wiki/sources/descriptions/gmh5225__ttddbg.md)

Complements WinDbg-centric TTD capture and triage tooling such as [[mcp-windbg]] and [[windbg-decompile-ext]], and TTD-oriented anti-debug stress samples such as [[ttd-anti-debugging]].

## Links

- Repo: https://github.com/gmh5225/ttddbg

## Related

[[overviews/reverse-engineering]] · [[tenet]] · [[mcp-windbg]] · [[windbg-decompile-ext]] · [[windbg-scripts]] · [[ttd-anti-debugging]] · [[x64dbg-trace-reader]] · [[execution-trace-viewer]]
