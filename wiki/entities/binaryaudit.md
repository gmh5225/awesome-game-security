---
title: binaryaudit
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/QuesmaOrg__BinaryAudit.md
updated: 2026-08-21
confidence: medium
---

# binaryaudit

Open-source benchmark for evaluating AI agents on finding backdoors and other malicious modifications hidden in compiled binaries of real open-source software. Agents receive stripped executables without source code inside isolated Docker environments and may use reverse engineering tools such as [[ghidra]] and Radare2. The task suite covers artificially injected backdoors, clean negative controls, and timebomb detection across programs written in C, Go, and Rust—including lighttpd, dnsmasq, Dropbear, Sozu, and Caddy. Built around the Harbor evaluation framework with Python tooling and YAML job configs for running multi-model experiments. Primary use case: security research and reverse-engineering evaluation of AI agents on binary malware and backdoor analysis. (source: wiki/sources/descriptions/QuesmaOrg__BinaryAudit.md)

Complements MCP bridges such as [[ida-pro-mcp]], [[ghidra-mcp]], [[radare2-mcp]], and [[binary-analysis-mcps]] by providing a standardized scored benchmark rather than ad hoc tool access.

## Links

- Repo: https://github.com/QuesmaOrg/BinaryAudit [BinaryAudit — open-source Harbor benchmark for AI agents finding injected backdoors in stripped binaries (Ghidra/Radare2); lighttpd/dnsmasq/Dropbear/Sozu/Caddy]

## Related

[[overviews/reverse-engineering]] · [[ghidra]] · [[radare2-mcp]] · [[r2ai]] · [[plugin-ghidra]] · [[reai-ida]] · [[binary-analysis-mcps]] · [[awesome-mcp-servers]]
