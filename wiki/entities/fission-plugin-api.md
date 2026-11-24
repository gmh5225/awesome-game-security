---
title: fission-plugin-api
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/fission-systems__fission-plugin-api.md
updated: 2026-11-24
confidence: medium
---

# fission-plugin-api

Experimental Rust-first headless plugin SDK and cross-tool compatibility runtime from fission-systems. Runs IDA Pro Python, Ghidra, Binary Ninja, and angr automation scripts against the Fission analysis engine (or fixture-backed development hosts) instead of those native products. A versioned JSON-lines wire protocol connects the Rust host—fixture data or the Fission CLI—to profile-specific shims; capabilities are negotiated explicitly and unsupported calls fail with errors rather than silent stubs. Function discovery can use Fission’s contract API; fixture mode supports mapped byte reads for offline development. The workspace bundles protocol crates, an SDK, Python entry points, and conformance tests for security researchers who want one headless pipeline to reuse existing RE plugin scripts. (source: wiki/sources/descriptions/fission-systems__fission-plugin-api.md)

## Links

- Repo: https://github.com/fission-systems/fission-plugin-api

## Related

[[overviews/reverse-engineering]] · [[ghidra-bridge]] · [[ghidra-headless-mcp]] · [[binary-ninja-headless-mcp]] · [[gui-plugin-template]] · [[angry-ghidra]] · [[headless-ida]] · [[mcp-reverse]]