# tarunai-connect-musescore

CLI wrapper for **MuseScore 4** — the first music notation tool in the [tarunAI Connect](https://github.com/tharunramagiri/tarunai-connect) ecosystem.

## Features

- **Transpose** scores by key, interval, or diatonically
- **Export** to PDF, PNG, SVG, MP3, FLAC, WAV, MIDI, MusicXML, Braille
- **Extract parts** from multi-instrument scores
- **Manage instruments** — list, add, remove, reorder
- **Analyze scores** — metadata, diff, statistics
- **Interactive REPL** with undo/redo session management

## Requirements

- Python >= 3.10
- [MuseScore 4](https://musescore.org/en/download) installed
- macOS, Linux, or Windows

## Install

```bash
pip install -e .
```

## Quick Start

```bash
# Interactive REPL
tarunai-connect-musescore

# One-shot commands with JSON output
tarunai-connect-musescore --json project info -i score.mscz
tarunai-connect-musescore --json transpose by-key -i score.mscz -o out.mscz --target-key "C major"
tarunai-connect-musescore --json export pdf -i score.mscz -o score.pdf
tarunai-connect-musescore --json parts list -i score.mscz
```

## Command Groups

| Group | Commands | Description |
|-------|----------|-------------|
| `project` | open, info, save | Score file management |
| `transpose` | by-key, by-interval, diatonic | Transposition |
| `parts` | list, extract, generate | Part extraction |
| `export` | pdf, png, svg, mp3, flac, wav, midi, musicxml, braille, batch | Rendering |
| `instruments` | list, add, remove, reorder | Instrument management |
| `media` | probe, diff, stats | Score analysis |
| `session` | status, undo, redo, history | Session management |
