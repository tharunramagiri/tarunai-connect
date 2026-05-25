# tarunai-connect-exa

Agent-native CLI harness for [Exa](https://exa.ai) — AI-powered web search and full-text content extraction.

## HOW TO RUN

### 1. Prerequisites

- Python 3.10+
- An Exa API key — get one free at [dashboard.exa.ai/api-keys](https://dashboard.exa.ai/api-keys)

### 2. Install

```bash
pip install git+https://github.com/tharunramagiri/tarunai-connect.git#subdirectory=exa/agent-harness
```

Or from source (development):

```bash
cd exa/agent-harness
pip install -e .
```

### 3. Configure

```bash
export EXA_API_KEY="your-api-key-here"
```

### 4. Verify

```bash
tarunai-connect-exa server status
```

Expected output:
```
[OK] API key valid — Exa reachable
```

### 5. Use

**Web search:**
```bash
tarunai-connect-exa search "large language models 2024" --type deep --content highlights
```

**Fetch page contents:**
```bash
tarunai-connect-exa contents https://exa.ai --content text
```

**JSON output (for agents):**
```bash
tarunai-connect-exa --json search "AI safety papers" --num-results 3
```

**Interactive REPL:**
```bash
tarunai-connect-exa
```

## Running Tests

**Unit tests** (no API key required):
```bash
cd exa/agent-harness
pip install -e ".[dev]"
pytest tarunai_connect/exa/tests/test_core.py -v
```

**End-to-end tests** (requires `EXA_API_KEY`):
```bash
pytest tarunai_connect/exa/tests/test_full_e2e.py -v
```
