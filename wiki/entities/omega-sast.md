---
title: omega-sast
kind: entity
topics: [reverse-engineering, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Black0ffR__omega-sast.md
updated: 2026-08-30
confidence: medium
---

# omega-sast

**OMEGA-5.0** is a zero-dependency static analysis engine for JavaScript bundles, built in Node.js for security researchers inspecting minified, framework-heavy, or obfuscated production code. It runs a multi-phase pipeline combining hand-rolled AST parsing, inter-procedural taint tracking, obfuscator fingerprinting, and deobfuscation (string-array decoding, control-flow flattening recovery, optional JSFuck or AAEncode payload extraction). The tool detects XSS, injection, credential leaks, broken crypto, CSRF weaknesses, ReDoS patterns, and other client-side security issues, then emits HTML, JSON, Markdown, and SARIF reports with CI-friendly exit codes. It also generates LLM-ready taint contracts and backward slices for deeper manual review of complex bundles — including game clients and anti-cheat-related web assets where hidden logic must be recovered from heavily protected JavaScript. (source: wiki/sources/descriptions/Black0ffR__omega-sast.md)

Complements offensive obfuscation tooling such as [[javascript-obfuscator]] on the analyst side, binary-oriented SAST such as [[ida-security-scanner]], and Node.js runtime tracing via [[nodejs-tracer]] when reviewing protected client scripts.

## Links

- Repo: https://github.com/black0ffr/omega-sast

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[javascript-obfuscator]] · [[ida-security-scanner]] · [[nodejs-tracer]] · [[control-flow-flattening]]
