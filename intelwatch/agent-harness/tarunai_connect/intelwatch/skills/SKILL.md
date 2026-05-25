---
name: >-
  tarunai-connect-intelwatch
description: >-
  Zero friction. Full context. Competitive intelligence, M&A due diligence, and OSINT directly from your terminal. Uses Node.js/npx.
---

# tarunai-connect-intelwatch

Intelwatch bridges the gap between hacker OSINT and B2B Sales/M&A data. It executes complex financial data aggregation, technology stack detection, and AI-powered due diligence in seconds.

## Installation

This CLI is installed as part of the tarunai-connect-intelwatch package:

```bash
pip install tarunai-connect-intelwatch
```

**Prerequisites:**
- Node.js >=18 must be installed and accessible via `npx`
- Run `node -v` and `npx -v` to ensure your system meets the requirements

## Usage

### Basic Commands

```bash
# Show help
tarunai-connect-intelwatch --help

# Generate a deep profile for a company
tarunai-connect-intelwatch profile kpmg.fr

# Generate a profile with AI Due Diligence
tarunai-connect-intelwatch profile kpmg.fr --ai
```

## For AI Agents

When using this CLI programmatically:

1. Provide the domain name (e.g., `doctolib.fr`)
2. Use the `--ai` flag to let Intelwatch perform due diligence automatically
3. The output is human-readable and provides a deep breakdown of the company
4. Ensure `npx` is available on the machine

## Example Scenarios

- **M&A Due Diligence:** `tarunai-connect-intelwatch profile company-name.com --ai`
- **Sales Intelligence:** `tarunai-connect-intelwatch profile target-client.com`
