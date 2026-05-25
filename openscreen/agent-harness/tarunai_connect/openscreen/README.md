# tarunai-connect-openscreen

CLI harness for [Openscreen](https://github.com/siddharthvaddem/openscreen) — a screen recording editor.

Edit screen recordings via command line: add zoom effects, speed ramps, trim sections, crop, annotate, set backgrounds, and export polished demo videos.

## Installation

```bash
pip install git+https://github.com/tharunramagiri/tarunai-connect.git#subdirectory=openscreen/agent-harness
```

**Prerequisites:**
- Python 3.10+
- ffmpeg (for rendering/export)

## Quick Start

```bash
# Interactive REPL
tarunai-connect-openscreen

# Create project from a recording
tarunai-connect-openscreen project new -v recording.mp4 -o project.openscreen

# Add zoom on a click moment (2.5s-5s, depth 3, focus on button)
tarunai-connect-openscreen zoom add --start 2500 --end 5000 --depth 3 --focus-x 0.8 --focus-y 0.3

# Speed up idle time (10s-15s at 2x)
tarunai-connect-openscreen speed add --start 10000 --end 15000 --speed 2.0

# Export
tarunai-connect-openscreen export render demo.mp4

# JSON output for AI agents
tarunai-connect-openscreen --json project info
```

## Preview Bundles

Openscreen supports static preview bundles for review-ready editing checks.

```bash
# Capture a low-res preview bundle
tarunai-connect-openscreen --json --project project.openscreen preview capture --recipe quick

# Read the latest bundle
tarunai-connect-openscreen --json --project project.openscreen preview latest --recipe quick
```

The preview bundle contains a low-res review clip, sampled frames, and summary
metadata. Capture also appends to a stable `trajectory.json` beside the preview
recipe root.

Inspect or open the resulting bundle with:

```bash
cli-hub previews inspect /path/to/bundle
cli-hub previews html /path/to/bundle -o page.html
cli-hub previews open /path/to/bundle
```

## Command Groups

| Group | Commands |
|-------|----------|
| `project` | new, open, save, info, set-video, set |
| `zoom` | list, add, remove |
| `speed` | list, add, remove |
| `trim` | list, add, remove |
| `crop` | get, set |
| `annotation` | list, add-text, remove |
| `media` | probe, check, thumbnail |
| `export` | presets, render |
| `session` | status, undo, redo, save, list |
