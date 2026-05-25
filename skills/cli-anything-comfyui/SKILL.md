---
name: "tarunai-connect-comfyui"
description: >-
  Command-line interface for ComfyUI - AI image generation workflow management via ComfyUI REST API. Designed for AI agents and power users who need to queue workflows, manage models, download generated images, and monitor the generation queue without a GUI.
---

# tarunai-connect-comfyui

AI image generation workflow management via the ComfyUI REST API. Designed for AI agents and power users who need to queue workflows, manage models, download generated images, and monitor the generation queue without a GUI.

## Installation

This CLI is installed as part of the tarunai-connect-comfyui package:

```bash
pip install tarunai-connect-comfyui
```

**Prerequisites:**
- Python 3.10+
- ComfyUI must be installed and running at http://localhost:8188

## Usage

### Basic Commands

```bash
# Show help
tarunai-connect-comfyui --help

# Start interactive REPL mode
tarunai-connect-comfyui repl

# Check server stats
tarunai-connect-comfyui system stats

# Run with JSON output (for agent consumption)
tarunai-connect-comfyui --json system stats
```

### REPL Mode

Start an interactive session for exploratory use:

```bash
tarunai-connect-comfyui repl
# Enter commands interactively with tab-completion and history
```

## Command Groups

### Workflow

Workflow management commands.

| Command | Description |
|---------|-------------|
| `list` | List saved workflows |
| `load` | Load a workflow from a JSON file |
| `validate` | Validate a workflow JSON against the ComfyUI node graph |

### Queue

Generation queue management.

| Command | Description |
|---------|-------------|
| `prompt` | Queue a workflow for execution |
| `status` | Show current queue status (running and pending) |
| `clear` | Clear the generation queue |
| `history` | Show prompt execution history |
| `interrupt` | Interrupt the currently running generation |

### Models

Model discovery commands.

| Command | Description |
|---------|-------------|
| `checkpoints` | List available checkpoint models |
| `loras` | List available LoRA models |
| `vaes` | List available VAE models |
| `controlnets` | List available ControlNet models |
| `node-info` | Show detailed info for a specific node type |
| `list-nodes` | List all available node types |

### Images

Generated image management.

| Command | Description |
|---------|-------------|
| `list` | List generated images on the server |
| `download` | Download a specific generated image |
| `download-all` | Download all images from a prompt execution |

### System

Server status and information.

| Command | Description |
|---------|-------------|
| `stats` | Show ComfyUI system statistics (GPU, CPU, memory) |
| `info` | Show ComfyUI server info and extensions |

## Examples

### Check System Status

```bash
# Server stats
tarunai-connect-comfyui system stats

# Server info
tarunai-connect-comfyui system info
```

### Discover Available Models

```bash
# List checkpoints
tarunai-connect-comfyui models checkpoints

# List LoRAs
tarunai-connect-comfyui models loras

# List all node types
tarunai-connect-comfyui models list-nodes
```

### Queue and Monitor Generation

```bash
# Queue a workflow
tarunai-connect-comfyui queue prompt --workflow my_workflow.json

# Check queue status
tarunai-connect-comfyui queue status

# View execution history
tarunai-connect-comfyui --json queue history
```

### Download Generated Images

```bash
# List generated images
tarunai-connect-comfyui images list

# Download a specific image
tarunai-connect-comfyui images download --filename ComfyUI_00001_.png --output ./out.png

# Download all images from a prompt
tarunai-connect-comfyui images download-all --prompt-id <id> --output-dir ./outputs
```

## Output Formats

All commands support dual output modes:

- **Human-readable** (default): Tables, colors, formatted text
- **Machine-readable** (`--json` flag): Structured JSON for agent consumption

```bash
# Human output
tarunai-connect-comfyui system stats

# JSON output for agents
tarunai-connect-comfyui --json system stats
```

## For AI Agents

When using this CLI programmatically:

1. **Always use `--json` flag** for parseable output
2. **Check return codes** - 0 for success, non-zero for errors
3. **Parse stderr** for error messages on failure
4. **Use absolute paths** for all file operations
5. **Verify ComfyUI is running** with `system stats` before other commands

## More Information

- Full documentation: See README.md in the package
- Test coverage: See TEST.md in the package
- Methodology: See HARNESS.md in the tarunai-connect-plugin

## Version

1.0.0
