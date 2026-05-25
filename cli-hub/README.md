# tarunai-connect

Package manager for [TarunAI Connect](https://github.com/tharunramagiri/tarunai-connect) — a framework that auto-generates stateful CLI interfaces for GUI applications, making them agent-native.

Browse, install, and manage 40+ CLI harnesses for software like GIMP, Blender, Inkscape, LibreOffice, Audacity, OBS Studio, and more — all from your terminal.

**Web Hub**: [tarunai.dev](https://tarunai.dev)

## Install

```bash
pip install tarunai-connect
```

## Usage

```bash
# Browse all available CLIs, grouped by category
tarunai-connect list

# Filter by category (image, 3d, video, audio, office, ai, ...)
tarunai-connect list -c image

# Search by name, description, or category
tarunai-connect search "3d modeling"

# Show details for a CLI
tarunai-connect info gimp

# Install a CLI harness
tarunai-connect install gimp

# Update a CLI to the latest version
tarunai-connect update gimp

# Uninstall a CLI
tarunai-connect uninstall gimp
```

## Preview Viewer

`tarunai-connect` also includes the generic preview consumer for preview-capable
harnesses.

Use this split:

- `tarunai-connect-<software> preview ...` creates or updates preview state
- `tarunai-connect previews ...` inspects or opens that existing preview state

Canonical viewer commands:

```bash
# Inspect an existing preview bundle or live session
tarunai-connect previews inspect /path/to/bundle-or-session

# Render HTML for a bundle or live session
tarunai-connect previews html /path/to/bundle-or-session -o page.html

# Watch a live session over localhost
tarunai-connect previews watch /path/to/session --open --poll-ms 1500

# Open a bundle or live session directly in a browser
tarunai-connect previews open /path/to/bundle-or-session
```

For live sessions, `tarunai-connect previews` reads:

- `session.json` for the current head
- `trajectory.json` for the command-to-preview history
- the current bundle manifest and artifacts

This command group never renders or publishes previews by itself.

## What gets installed

Each CLI harness is a standalone Python package that wraps a real application (GIMP, Blender, etc.) with a stateful command-line interface. Every harness supports:

- **REPL mode**: `tarunai-connect-gimp` launches an interactive session
- **One-shot commands**: `tarunai-connect-gimp project create --name my-project`
- **JSON output**: `tarunai-connect-gimp --json project list` for machine-readable output
- **Undo/redo**: Stateful project management with full operation history

## For AI agents

tarunai-connect is designed to be agent-friendly. AI coding agents can:

1. `pip install tarunai-connect` to get the package manager
2. `tarunai-connect search <keyword>` or `tarunai-connect list --json` to discover tools
3. `tarunai-connect install <name>` to install what they need
4. Use `--json` output for structured data parsing
5. For preview-capable harnesses, call `tarunai-connect-<software> preview ... --json`
   first, then inspect returned bundle/session paths with `tarunai-connect previews ...`

## Available categories

3D, AI, Audio, Communication, Database, Design, DevOps, Diagrams, Game, GameDev, Generation, Graphics, Image, Music, Network, Office, OSINT, Project Management, Search, Streaming, Testing, Video, Web

## JSON output

All listing commands support `--json` for machine-readable output:

```bash
tarunai-connect list --json
tarunai-connect search blender --json
```

## Analytics

tarunai-connect sends anonymous usage events to help track adoption. The default provider is [PostHog](https://posthog.com), while the legacy Umami path remains available via `TARUNAI_CONNECT_ANALYTICS_PROVIDER=umami`. No personal data is collected.

Opt out:

```bash
export TARUNAI_CONNECT_NO_ANALYTICS=1
```

## Links

- **Web Hub**: [tarunai.dev](https://tarunai.dev)
- **Repository**: [github.com/tharunramagiri/tarunai-connect](https://github.com/tharunramagiri/tarunai-connect)
- **Live Catalog**: [tarunai.dev/catalog](https://tarunai.dev/catalog)
