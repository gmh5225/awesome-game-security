---
title: cheat-agent
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/heaven-hm__cheat-agent.md
  - wiki/sources/README-categories.md
updated: 2026-10-15
confidence: medium
---

# cheat-agent

**cheat-agent** (heaven-hm/cheat-agent) is a cross-platform autonomous reverse-engineering stack for authorized offline single-player games and controlled test processes. A native C/C++20 engine handles process attach, multi-pass memory scanning, AOB pattern matching, and pointer-chain resolution; a Rust workspace orchestrates sessions, SQLite storage, and trainer code generation. A five-stage closed-loop verifier discovers candidates, confirms in-game effects, restarts the target to survive ASLR, emits standalone C++, Rust, or Cheat Engine table artifacts, and re-runs the trainer to prove persistence. (source: wiki/sources/descriptions/heaven-hm__cheat-agent.md)

## Closed-loop verifier

1. Discover candidate addresses or pointer chains from multi-pass scans and AOB matches
2. Confirm observable in-game behavior changes
3. Restart the target to validate stability under ASLR
4. Emit standalone trainer artifacts (C++, Rust, or Cheat Engine table)
5. Re-run the generated trainer to prove persistence

(source: wiki/sources/descriptions/heaven-hm__cheat-agent.md)

## Integration modes

- **MCP server:** stdio Model Context Protocol host for Codex, Claude Code, and other MCP clients
- **Standalone CLI:** drives OpenAI, Anthropic, OpenRouter, or local Ollama models toward explicit RE goals

Targets educators, game-security researchers, and QA teams who need reproducible, toolchain-native trainer workflows rather than interactive-only editors. Sits beside MCP orchestrators such as [[skid-factory]], verification-gated hosts such as [[reverify]], and cross-platform pipelines such as [[n0xis]] in the **Cheat → RE Tools** lane.

## Links

- Repo: https://github.com/heaven-hm/cheat-agent

## Related

[[research-rigor]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[skid-factory]] · [[reverify]] · [[n0xis]] · [[pymemory-editor]] · [[cheat-engine]]
