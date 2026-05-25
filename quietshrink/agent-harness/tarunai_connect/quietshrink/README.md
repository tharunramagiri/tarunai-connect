# tarunai-connect-quietshrink

Agent-native CLI harness for [quietshrink](https://github.com/achiya-automation/quietshrink).

See [QUIETSHRINK.md](../../QUIETSHRINK.md) at the harness root for full documentation.

## Quick reference

```bash
tarunai-connect-quietshrink compress <input> [output]   # Compress a video
tarunai-connect-quietshrink probe <input>               # Inspect a file
tarunai-connect-quietshrink presets                     # List quality presets
tarunai-connect-quietshrink doctor                      # Verify environment
```

All commands accept `--json` for structured output.

## Quality presets

| Preset | q | Reduction | SSIM | Use case |
|--------|---|-----------|------|----------|
| tiny | 50 | ~90% | ~0.95 | chat / email |
| balanced | 55 | ~88% | ~0.99 | docs / sharing |
| transparent (default) | 60 | ~87% | ~0.99+ | visually lossless |
| pristine | 70 | ~84% | ~0.997 | archival |

## See also

- Skill file for agents: [skills/SKILL.md](skills/SKILL.md)
- Standalone CLI: <https://github.com/achiya-automation/quietshrink>
