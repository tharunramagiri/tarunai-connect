---
name: "tarunai-connect-krita"
description: "CLI harness for Krita digital painting — manage projects, layers, filters, and export via command line. Use when automating Krita workflows, batch processing images, or operating Krita without a GUI."
---

# tarunai-connect-krita

CLI harness for **Krita**, the professional open-source digital painting application.

## Prerequisites

- **Krita** installed on the system
- **Python 3.10+**

Install the CLI:
```bash
cd krita/agent-harness && pip install -e .
```

## Command Reference

### Project Management
```bash
tarunai-connect-krita project new -n "My Art" -w 2048 -h 2048 -o project.json
tarunai-connect-krita project open project.json
tarunai-connect-krita --project project.json project save
tarunai-connect-krita --project project.json project info
```

### Layer Management
```bash
tarunai-connect-krita -p project.json layer add "Sketch" -t paintlayer
tarunai-connect-krita -p project.json layer add "Colors" --opacity 200
tarunai-connect-krita -p project.json layer add "Group" -t grouplayer
tarunai-connect-krita -p project.json layer remove "Sketch"
tarunai-connect-krita -p project.json layer list
tarunai-connect-krita -p project.json layer set "Colors" opacity 180
tarunai-connect-krita -p project.json layer set "Colors" visible false
tarunai-connect-krita -p project.json layer set "Colors" blending_mode multiply
```

Layer types: `paintlayer`, `grouplayer`, `vectorlayer`, `filterlayer`, `filllayer`, `clonelayer`, `filelayer`

### Filters
```bash
tarunai-connect-krita -p project.json filter apply blur -l "Background"
tarunai-connect-krita -p project.json filter apply sharpen
tarunai-connect-krita -p project.json filter apply levels -c '{"shadows": 10, "highlights": 240}'
tarunai-connect-krita filter list
```

Available: blur, sharpen, desaturate, levels, curves, brightness-contrast, hue-saturation, color-balance, unsharp-mask, posterize, threshold

### Canvas Operations
```bash
tarunai-connect-krita -p project.json canvas resize -w 4096 -h 4096
tarunai-connect-krita -p project.json canvas resize --resolution 600
tarunai-connect-krita -p project.json canvas info
```

### Export
```bash
tarunai-connect-krita -p project.json export render output.png -p png --overwrite
tarunai-connect-krita -p project.json export render output.jpg -p jpeg
tarunai-connect-krita -p project.json export render output.psd -p psd
tarunai-connect-krita -p project.json export animation ./frames/ -p png
tarunai-connect-krita export presets
tarunai-connect-krita export formats
```

Presets: png, png-web, jpeg, jpeg-web, jpeg-low, tiff, tiff-lzw, psd, pdf, svg, webp, gif, bmp

### Session (Undo/Redo)
```bash
tarunai-connect-krita session undo
tarunai-connect-krita session redo
tarunai-connect-krita session history
```

### Status
```bash
tarunai-connect-krita status
```

## Agent Usage (JSON Mode)

All commands support `--json` for machine-readable output:

```bash
tarunai-connect-krita --json -p project.json project info
tarunai-connect-krita --json -p project.json layer list
tarunai-connect-krita --json status
```

## Example Workflow

```bash
# 1. Create project
tarunai-connect-krita --json project new -n "Illustration" -w 3000 -h 4000 -o art.json

# 2. Set up layer stack
tarunai-connect-krita --json -p art.json layer add "Background" -t paintlayer
tarunai-connect-krita --json -p art.json layer add "Sketch" -t paintlayer --opacity 180
tarunai-connect-krita --json -p art.json layer add "Inking" -t paintlayer
tarunai-connect-krita --json -p art.json layer add "Colors" -t paintlayer
tarunai-connect-krita --json -p art.json layer add "Effects" -t paintlayer --opacity 128

# 3. Apply effects
tarunai-connect-krita --json -p art.json filter apply blur -l "Background"

# 4. Export
tarunai-connect-krita --json -p art.json export render final.png -p png --overwrite
```
