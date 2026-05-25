# tarunai-connect-minimax

CLI harness for **MiniMax AI** — chat and text-to-speech via the MiniMax API.

## Installation

```bash
pip install git+https://github.com/tharunramagiri/tarunai-connect.git#subdirectory=minimax/agent-harness
```

For local validation from this repository:

```bash
cd minimax/agent-harness
python3 -m pip install -e .
tarunai-connect-minimax --help
```

## Prerequisites

- Python 3.10+
- MiniMax API key from [platform.minimax.io](https://platform.minimax.io)

## Quick Start

```bash
export MINIMAX_API_KEY="your-api-key"
tarunai-connect-minimax chat --prompt "Hello!"
tarunai-connect-minimax tts --text "Hello world" --output hello.mp3
```

## Usage

### Chat

```bash
# Simple chat (default model: MiniMax-M2.7)
tarunai-connect-minimax chat --prompt "Explain quantum computing"

# High-speed model
tarunai-connect-minimax chat --prompt "Quick answer please" --model MiniMax-M2.7-highspeed

# Streaming output
tarunai-connect-minimax stream --prompt "Write a haiku about AI"

# JSON output for agents
tarunai-connect-minimax --json chat --prompt "Hello"
```

### TTS

```bash
# Synthesize speech (default model: speech-2.8-hd, default voice: English_Graceful_Lady)
tarunai-connect-minimax tts --text "Hello, world!" --output hello.mp3

# Use turbo model
tarunai-connect-minimax tts --text "Fast speech" --model speech-2.8-turbo --output fast.mp3

# List available voices
tarunai-connect-minimax voices
```

### Session & Config

```bash
# Session management
tarunai-connect-minimax session status
tarunai-connect-minimax session clear

# Configuration
tarunai-connect-minimax config set api_key "your-key"
tarunai-connect-minimax config get

# Test connectivity
tarunai-connect-minimax test

# List models
tarunai-connect-minimax models
tarunai-connect-minimax models --tts
```

## Models

### Chat

| Model | Description |
|-------|-------------|
| `MiniMax-M2.7` | Peak Performance. Ultimate Value. (default) |
| `MiniMax-M2.7-highspeed` | Same performance, faster and more agile |

### TTS

| Model | Description |
|-------|-------------|
| `speech-2.8-hd` | High-definition TTS (default) |
| `speech-2.8-turbo` | Fast TTS |

## Environment Variables

| Variable | Description |
|----------|-------------|
| `MINIMAX_API_KEY` | MiniMax API key (required) |
| `MINIMAX_BASE_URL` | Override API base URL (optional) |

## Validation

No-backend and mocked API validation:

```bash
cd minimax/agent-harness
python3 -m py_compile \
  tarunai_connect/minimax/minimax_cli.py \
  tarunai_connect/minimax/core/session.py \
  tarunai_connect/minimax/utils/minimax_backend.py \
  tarunai_connect/minimax/tests/test_core.py \
  tarunai_connect/minimax/tests/test_full_e2e.py
python3 -m pytest tarunai_connect/minimax/tests/test_core.py tarunai_connect/minimax/tests/test_full_e2e.py -v
python3 -m pip install -e .
TARUNAI_CONNECT_FORCE_INSTALLED=1 python3 -m pytest \
  tarunai_connect/minimax/tests/test_full_e2e.py::TestCLISubprocessSmoke -v -s
```

Real MiniMax backend validation:

```bash
cd minimax/agent-harness
python3 -m pip install -e .
export MINIMAX_API_KEY="sk-your-real-key"
tarunai-connect-minimax --json test
tarunai-connect-minimax --json chat --prompt "Say ok only" --max-tokens 10
tarunai-connect-minimax stream --prompt "Say ok only" --max-tokens 10
tarunai-connect-minimax --json tts --text "MiniMax validation" --output /tmp/minimax-validation.mp3
test -s /tmp/minimax-validation.mp3
python3 -m pytest tarunai_connect/minimax/tests/test_full_e2e.py -v -s
```
