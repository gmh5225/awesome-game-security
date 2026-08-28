---
title: showstopper
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/CheckPointSW__showstopper.md
updated: 2026-08-28
confidence: medium
---

# showstopper

Windows **anti-debug exploration tool** from CheckPoint Software for testing debugger resilience against real anti-debug techniques. Implements a large collection of checks and tricks drawn from malware samples and published research, and exposes relevant function addresses for hands-on experimentation. Researchers attach debuggers and compare behavior across tools, plugins, and mitigation strategies on modern Windows versions. Aimed at reverse engineers, malware analysts, and tool developers validating anti-anti-debug capabilities. (source: wiki/sources/descriptions/CheckPointSW__showstopper.md)

Complements technique catalogs such as [[al-khaser]] and [[antidbg-hackovert]], bypass-practice harnesses such as [[gh-anti-debug-bypass-practice-tool]], and hide/bypass tooling studied in RE workflows ([[scyllahide]], [[titanhide]], [[makin]]).

## Links

- Repo: https://github.com/CheckPointSW/showstopper

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[al-khaser]] · [[antidbg-hackovert]] · [[gh-anti-debug-bypass-practice-tool]] · [[anti-debugging]] · [[makin]] · [[scyllahide]]
