---
title: idarem
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/xsslize__idarem.md
updated: 2026-07-18
confidence: medium
---

# idarem

IDA Pro plugin that serves a live IDA database to a browser on another device. An IDAPython/Flask server inside IDA exposes REST and Server-Sent Events for functions, disassembly, graphs, Hex-Rays pseudocode, cross-references, strings, imports, and related views; a React/TypeScript client renders them remotely. Supports live follow of IDA’s current address/window, optional drive-back navigation into IDA, and optional write-back for renames/comments when explicitly enabled. Token-authenticated; intended over tunnels such as Tailscale, Cloudflare Tunnel, or ngrok—lightweight remote IDB browsing without RDP, VNC, or copying the database. (source: wiki/sources/descriptions/xsslize__idarem.md)

Not a disassembler or decompiler itself—remote UI over a running IDA session.

## Links

- Repo: https://github.com/xsslize/idarem

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[symbridge]] · [[xrefsext]] · [[idadeflat]]
