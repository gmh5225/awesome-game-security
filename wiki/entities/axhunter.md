---
title: axhunter
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/BlackSnufkin__AxHunter.md
updated: 2026-08-30
confidence: medium
---

# axhunter

**AxHunter** (BlackSnufkin) is a Rust proof-of-concept suite that exploits privileged kernel drivers from Wellbia **XIGNCODE3** anti-cheat, covering both `xhunter1.sys` and the newer `xhunter2.sys` associated with **CVE-2026-15430**. Each PoC communicates with the driver through **WriteFile**-based command frames to bypass authentication checks, obtain PPL-bypassing process handles, and read arbitrary process memory from user mode. (source: wiki/sources/descriptions/BlackSnufkin__AxHunter.md)

A shared crate performs **LSA credential extraction** by walking `lsass.exe`, recovering BCrypt 3DES keys, and decrypting LogonSessionList and WDigest entries for NT/SHA1 hashes and plaintext passwords. Additional modes can forcibly close handles in protected processes such as Windows Defender and escalate to a SYSTEM shell via `winlogon.exe`. Intended for game-security and anti-cheat researchers analyzing kernel driver weaknesses, driver exploitation, and Windows credential-theft primitives.

## Links

- Repo: https://github.com/BlackSnufkin/AxHunter

## Related

[[xign-poc-april-2026]] · [[xigncode3-blackdesert]] · [[xigncode3-bypass]] · [[xigncode3-bypass-alternative]] · [[byovd]] · [[pplkiller]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
