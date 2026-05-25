# tarunai-connect-browser — Browser Automation CLI

A command-line interface for browser automation using [DOMShell](https://github.com/apireno/DOMShell)'s MCP server. Maps Chrome's Accessibility Tree to a virtual filesystem for agent-native browser automation.

## Features

- **Filesystem-first navigation**: Use `ls`, `cd`, `cat` to explore web pages
- **Search**: `grep` for text patterns in the accessibility tree
- **Actions**: `click`, `type` to interact with elements
- **JSON output**: `--json` flag for machine-readable output
- **Interactive REPL**: Stateful session with command history
- **Daemon mode**: Optional persistent connection for faster interactive use

## Installation

### Prerequisites

1. **Node.js and npx** (required for DOMShell MCP server):
   ```bash
   # Install Node.js from https://nodejs.org/
   node --version
   npx --version
   ```

2. **Chrome/Chromium** with DOMShell extension:
   - Install DOMShell from [Chrome Web Store](https://chromewebstore.google.com/detail/domshell-%E2%80%94-browser-filesy/okcliheamhmijccjknkkplploacoidnp)
   - Ensure Chrome is running before using the CLI

3. **Python 3.10+**:
   ```bash
   python --version
   ```

### Install CLI

```bash
cd browser/agent-harness
pip install -e .
```

Verify installation:
```bash
tarunai-connect-browser --help
```

## Usage

### One-Shot Commands

```bash
# Open a page
tarunai-connect-browser page open https://example.com

# List elements at root
tarunai-connect-browser fs ls /

# Navigate into a section
tarunai-connect-browser fs cd /main

# List elements in current directory
tarunai-connect-browser fs ls

# Read element content
tarunai-connect-browser fs cat /main/button[0]

# Search for text
tarunai-connect-browser fs grep "Login"

# Click an element
tarunai-connect-browser act click /main/button[0]

# Type into an input
tarunai-connect-browser act type /main/input[0] "Hello, World!"

# Get page info
tarunai-connect-browser page info

# Navigate back/forward
tarunai-connect-browser page back
tarunai-connect-browser page forward
```

**Note:** One-shot commands each start with a fresh session (no URL or working directory). For stateful workflows (like `cd` followed by `ls` without a path), use the REPL instead.

### JSON Output

```bash
# Get machine-readable output
tarunai-connect-browser --json fs ls /

# Returns:
{
  "path": "/",
  "entries": [
    {
      "name": "main",
      "role": "landmark",
      "path": "/main"
    }
  ]
}
```

### Daemon Mode (Persistent Connection)

For faster interactive use, start daemon mode within a REPL session:

```bash
# Start REPL with daemon mode
tarunai-connect-browser --daemon

# Or start daemon within REPL
session daemon-start

# Run commands (uses persistent connection)
fs ls /
fs cd /main

# Stop daemon when done
session daemon-stop
```

**Note:** Daemon mode only works within a single running process (REPL or `--daemon` flag). State does not persist across separate CLI invocations.

### Interactive REPL

Run without arguments to enter interactive mode:

```bash
tarunai-connect-browser
```

REPL commands:
- `page open <url>` — Open a URL
- `fs ls [path]` — List elements
- `fs cd <path>` — Change directory
- `fs cat [path]` — Read element
- `fs grep <pattern>` — Search for text
- `fs pwd` — Print working directory
- `act click <path>` — Click element
- `act type <path> <text>` — Type text
- `session status` — Show session state
- `help` — Show commands
- `quit` — Exit REPL

## Command Groups

### `page` — Page Navigation
- `open <url>` — Navigate to URL
- `reload` — Reload current page
- `back` — Navigate back in history
- `forward` — Navigate forward in history
- `info` — Show current page info

### `fs` — Filesystem Commands
- `ls [path]` — List elements at path
- `cd <path>` — Change directory
- `cat [path]` — Read element content
- `grep <pattern> [path]` — Search for text
- `pwd` — Print working directory

### `act` — Action Commands
- `click <path>` — Click an element
- `type <path> <text>` — Type text into input

### `session` — Session Management
- `status` — Show session status
- `daemon-start` — Start persistent daemon mode
- `daemon-stop` — Stop daemon mode

## Path Syntax

DOMShell uses a filesystem-like path syntax for the Accessibility Tree:

```
/                           — Root (page)
/main                       — Main landmark
/main/div[0]                — First div in main
/main/div[0]/button[2]      — Third button in first div
```

Array indices are 0-based. Use relative paths with `..` to go up.

## Examples

### Basic Navigation
```bash
# Open a page
tarunai-connect-browser page open https://example.com

# Explore structure
tarunai-connect-browser fs ls /
tarunai-connect-browser fs cd /main
tarunai-connect-browser fs ls

# Go back to root
tarunai-connect-browser fs cd /
```

### Search and Click
```bash
# Open page and search for login button
tarunai-connect-browser page open https://example.com/login
tarunai-connect-browser fs grep "Login"

# Click the login button (adjust path as needed)
tarunai-connect-browser act click /main/button[0]
```

### Form Fill
```bash
# Type into form fields
tarunai-connect-browser act type /main/input[0] "user@example.com"
tarunai-connect-browser act type /main/input[1] "password123"

# Click submit
tarunai-connect-browser act click /main/button[0]
```

## Testing

Run tests:

```bash
# Unit tests (no Chrome required)
pytest tarunai_connect/browser/tests/test_core.py -v

# E2E tests (requires Chrome + DOMShell)
pytest tarunai_connect/browser/tests/test_full_e2e.py -v
```

## Troubleshooting

### "npx not found"
Install Node.js from https://nodejs.org/

### "DOMShell not found"
Run: `npx @apireno/domshell --version` (first run downloads the package)

### "DOMShell MCP call failed"
- Ensure Chrome is running
- Install DOMShell extension from Chrome Web Store
- Check that DOMShell is enabled in Chrome

### Commands hang on first use
First `npx` call downloads DOMShell package (10-50 MB). Subsequent calls are faster. Use `--daemon` mode for persistent connection.

## Architecture

This CLI follows the [tarunAI Connect harness methodology](https://github.com/tharunramagiri/tarunai-connect/tree/main/tarunai-connect-plugin/HARNESS.md):

- **Backend**: DOMShell MCP server via stdio transport
- **State**: Page state (URL, working directory, navigation history)
- **Pattern**: Filesystem-first commands map to Accessibility Tree

## Links

- [DOMShell GitHub](https://github.com/apireno/DOMShell)
- [tarunAI Connect](https://github.com/tharunramagiri/tarunai-connect)
- [Issue #90](https://github.com/tharunramagiri/tarunai-connect/issues/90)

## License

Apache License 2.0 — See [tarunAI Connect](https://github.com/tharunramagiri/tarunai-connect) for details.
