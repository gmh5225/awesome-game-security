---
title: delete-self-poc
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/LloydLabs__delete-self-poc.md
updated: 2026-08-23
confidence: medium
---

# delete-self-poc

C **proof of concept** demonstrating how a **running or locked executable can delete itself from disk** on Windows. The technique renames the file's primary data stream, then sets file disposition flags through **`SetFileInformationByHandle`** APIs—exercising handle sequencing, deletion semantics, and practical edge cases around locked-file removal. Primary use case: low-level Windows internals research relevant to anti-forensics, secure cleanup, and defensive detection engineering. (source: wiki/sources/descriptions/LloydLabs__delete-self-poc.md)

Complements broader Windows anti-forensics utilities such as [[forensia]] and NTFS artifact manipulation tooling such as [[antfs]] on the evidence-obscuration side, opposite recovery and triage collectors like [[file-recovery-tool]] and [[dfirtriage]].

## Links

- Repo: https://github.com/LloydLabs/delete-self-poc (README: A way to delete a locked file, or current running executable, on disk)

## Related

[[forensia]] · [[anti-forensics]] · [[antfs]] · [[file-recovery-tool]] · [[dfirtriage]] · [[shellcode-plain-sight]] · [[wsb-detect]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
