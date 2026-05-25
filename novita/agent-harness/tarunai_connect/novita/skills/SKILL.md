---
name: >-
  tarunai-connect-novita
description: >-
  Command-line interface for Novita AI - An OpenAI-compatible AI API client for DeepSeek, GLM, and other models.
---

# tarunai-connect-novita

A CLI harness for **Novita AI** - an OpenAI-compatible API service for AI models like DeepSeek, GLM, and others.

## Installation

This CLI is installed as part of the tarunai-connect-novita package:

```bash
pip install tarunai-connect-novita
```

**Prerequisites:**
- Python 3.10+
- Novita API key from [novita.ai](https://novita.ai)

## Usage

### Basic Commands

```bash
# Show help
tarunai-connect-novita --help

# Start interactive REPL mode
tarunai-connect-novita

# Chat with model
tarunai-connect-novita chat --prompt "What is AI?" --model deepseek/deepseek-v3.2

# Streaming chat
tarunai-connect-novita stream --prompt "Write a poem about code"

# List available models
tarunai-connect-novita models

# JSON output (for agent consumption)
tarunai-connect-novita --json chat --prompt "Hello"
```

### REPL Mode

When invoked without a subcommand, the CLI enters an interactive REPL session:

```bash
tarunai-connect-novita
# Enter commands interactively with tab-completion and history
```

## Command Groups

### Chat

Chat with AI models through the Novita API.

| Command | Description |
|---------|-------------|
| `chat` | Chat with the Novita API |
| `stream` | Stream chat completion |

### Session

Session management for chat history.

| Command | Description |
|---------|-------------|
| `status` | Show session status |
| `clear` | Clear session history |
| `history` | Show command history |

### Config

Configuration management.

| Command | Description |
|---------|-------------|
| `set` | Set a configuration value |
| `get` | Get a configuration value (or show all) |
| `delete` | Delete a configuration value |
| `path` | Show the config file path |

### Utility

| Command | Description |
|---------|-------------|
| `test` | Test API connectivity |
| `models` | List available models |

## Examples

### Configure API Key

```bash
# Set API key via config file (recommended)
tarunai-connect-novita config set api_key "sk-xxx"

# Or use environment variable
export NOVITA_API_KEY="sk-xxx"
```

### Chat with DeepSeek

```bash
# Simple chat
tarunai-connect-novita chat --prompt "Explain quantum computing" --model deepseek/deepseek-v3.2

# Streaming chat
tarunai-connect-novita stream --prompt "Write a Python function to calculate factorial"
```

### Test Connectivity

```bash
# Verify API key and connectivity
tarunai-connect-novita test --model deepseek/deepseek-v3.2

# List all available models
tarunai-connect-novita models
```

## Default Models

The Novita API supports multiple model providers:

| Model ID | Provider | Description |
|----------|----------|-------------|
| `deepseek/deepseek-v3.2` | DeepSeek | DeepSeek V3.2 model (default) |
| `zai-org/glm-5` | Zhipu AI | GLM-5 model |
| `minimax/minimax-m2.5` | MiniMax | MiniMax M2.5 model |

## Output Formats

All commands support dual output modes:

- **Human-readable** (default): Tables, colors, formatted text
- **Machine-readable** (`--json` flag): Structured JSON for agent consumption

```bash
# Human output
tarunai-connect-novita chat --prompt "Hello"

# JSON output for agents
tarunai-connect-novita --json chat --prompt "Hello"
```

## For AI Agents

When using this CLI programmatically:

1. **Always use `--json` flag** for parseable output
2. **Check return codes** - 0 for success, non-zero for errors
3. **Parse stderr** for error messages on failure
4. **Use absolute paths** for all file operations
5. **Verify outputs exist** after export operations

## More Information

- Full documentation: See README.md in the package
- Test coverage: See TEST.md in the package
- Methodology: See HARNESS.md in the tarunai-connect-plugin

## Version

1.0.0
