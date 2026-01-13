---
name: game-engine-resources
description: Guide for game engine development resources including engine source code, plugins, and development guides. Use this skill when researching game engines (Unreal, Unity, Godot, custom engines), engine architecture, or game development frameworks.
---

# Game Engine Development Resources

## Overview

This skill covers game engine development resources from the awesome-game-security collection, including both commercial (Unreal, Unity) and open-source engines.

## Major Engine Categories

### Unreal Engine
- Official documentation and forums
- Source code access (requires Epic Games account)
- Community guides and tutorials
- Plugin development references

### Unity Engine
- C# reference source code
- Asset store resources
- Unity-specific design patterns
- VR/AR development guides

### Open Source Engines
- **Godot**: Free and open-source, supports GDScript and C#
- **Cocos2d-x**: Cross-platform 2D game framework
- **CRYENGINE**: High-fidelity graphics engine
- **Source Engine**: Valve's game engine (various versions)

### Custom/Educational Engines
- Hazel Engine (TheCherno's educational series)
- Bevy (Rust-based data-driven engine)
- Fyrox (Rust game engine)

## Key Technical Areas

### Rendering
- Software renderers for learning
- Ray tracing implementations
- Shader development tutorials
- Post-processing effects

### Mathematics
- Linear algebra libraries (GLM, DirectXMath)
- Physics simulation (PhysX, Bullet)
- Collision detection algorithms

### Networking
- Client-server architectures
- KCP reliable UDP protocol
- Steam networking integration
- MMORPG server implementations

## Resource Categories

### Documentation & Guides
```markdown
- Learning resources and tutorials
- Architecture documentation
- Best practices and style guides
```

### Source Code
```markdown
- Complete engine implementations
- Subsystem references (renderer, physics, audio)
- Plugin and extension examples
```

### Plugins & Extensions
```markdown
- ImGui integration for debug UIs
- Scripting language bindings (Lua, .NET)
- Editor tool plugins
```

## Engine Selection Criteria

When researching engines for security analysis or development:

1. **Target Platform**: PC, mobile, console compatibility
2. **Source Access**: Open source vs proprietary
3. **Language**: C++, C#, Rust, or scripting
4. **Graphics API**: DirectX, OpenGL, Vulkan, Metal
5. **Community**: Documentation and support quality

## Security Research Focus

For game security research, understanding engine internals helps with:
- Memory layout and object structures
- Rendering pipeline hooks
- Network protocol analysis
- Anti-cheat integration points
