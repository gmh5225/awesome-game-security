---
title: fnv-speedhack (lightview)
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/lightview__fnv-speedhack.md
updated: 2026-11-06
confidence: medium
---

# fnv-speedhack (lightview)

**Fallout: New Vegas** 单机速度控制：DLL 内用 **MinHook** 钩住进程内的计时 API（如 `QueryPerformanceCounter`、`GetTickCount` / `GetTickCount64`、`timeGetTime`），按倍率缩放流逝时间，行为上接近 **Cheat Engine** 的 speedhack，且不依赖对可执行文件打补丁或追逐游戏内内存地址。可构建为 **NVSE** 插件或放在游戏目录侧的 **dinput8** 代理 DLL；README 还提到 **Proton** 覆盖用法与可选 **Decky Loader** 插件（Steam Deck 上通过 hidraw 读背键并以 INI 文件 IPC 驱动）。配置支持键盘热键、预设循环、可选 **XInput** 组合键、蜂鸣与日志。 (source: wiki/sources/descriptions/lightview__fnv-speedhack.md)

仅适用于授权环境；线上或条款禁止的场景不适用。

## Links

- Repo: https://github.com/lightview/fnv-speedhack

## Related

[[cheat-engine]] · [[speedhack]] · [[speed-hack]] · [[ce-speed-hack]] · [[uptime-faker]] · [[overviews/game-hacking]]
