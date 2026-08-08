---
title: manipulating_token
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__manipulating_token.md
updated: 2026-08-08
confidence: medium
---

# manipulating_token

Educational C/C++ samples demonstrating Windows access-token manipulation for privilege escalation and impersonation: steal, duplicate, and modify process tokens to gain elevated privileges, impersonate other users, or bypass access-control checks. Covers token theft, `SeDebugPrivilege` exploitation, and token impersonation—including obtaining a SYSTEM integrity-level process token and manipulating it for LPE. (source: wiki/sources/descriptions/gmh5225__manipulating_token.md)

Useful for security researchers studying Windows privilege escalation through token semantics, integrity levels, and impersonation—adjacent to TrustedInstaller-token launchers such as [[cmdt]] but focused on generic access-token abuse rather than TI-ACL reach.

## Links

- Repo: https://github.com/gmh5225/manipulating_token

## Related

[[cmdt]] · [[systeminformer]] · [[dk]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
