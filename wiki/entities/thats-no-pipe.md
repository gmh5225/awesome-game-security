---
title: thats_no_pipe
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/synacktiv__thats_no_pipe.md
updated: 2026-07-21
confidence: medium
---

# thats_no_pipe

Synacktiv Frida-based Windows named-pipe I/O interception toolkit. Hooks `NtReadFile`, `NtWriteFile`, `NtWaitForSingleObject`, and IoQueue paths to monitor, record, and manipulate pipe traffic for protocol analysis and fuzzing; relays IPC to an HTTP proxy over WebSocket. Useful when game or AC clients speak over named pipes rather than sockets. (source: wiki/sources/descriptions/synacktiv__thats_no_pipe.md)

## Links

- Repo: https://github.com/synacktiv/thats_no_pipe (README: Frida-based Windows named pipe interceptor)

## Related

[[frida]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
