---
name: >-
  tarunai-connect-obsidian
description: >-
  Command-line interface for Obsidian — Knowledge management and note-taking via Obsidian Local REST API. Designed for AI agents and power users who need to manage notes, search the vault, and execute commands without the GUI.
---

# tarunai-connect-obsidian

Knowledge management and note-taking via the Obsidian Local REST API. Designed for AI agents and power users who need to manage notes, search the vault, and execute commands without the GUI.

## Installation

This CLI is installed as part of the tarunai-connect-obsidian package:

```bash
pip install tarunai-connect-obsidian
```

**Prerequisites:**
- Python 3.10+
- Obsidian must be installed and running with the [Local REST API plugin](https://github.com/coddingtonbear/obsidian-local-rest-api) enabled


## Usage

### Basic Commands

```bash
# Show help
tarunai-connect-obsidian --help

# Start interactive REPL mode
tarunai-connect-obsidian

# List vault files
tarunai-connect-obsidian vault list

# Run with JSON output (for agent consumption)
tarunai-connect-obsidian --json vault list
```

### REPL Mode

When invoked without a subcommand, the CLI enters an interactive REPL session:

```bash
tarunai-connect-obsidian
# Enter commands interactively with tab-completion and history
```


## Command Groups


### Vault

Vault file management commands.

| Command | Description |
|---------|-------------|
| `list` | List files in the vault or a subdirectory |
| `read` | Read the content of a note |
| `create` | Create a new note |
| `update` | Overwrite an existing note |
| `delete` | Delete a note from the vault |
| `append` | Append content to an existing note |


### Search

Vault search commands.

| Command | Description |
|---------|-------------|
| `query` | Search using Obsidian query syntax |
| `simple` | Plain text search across the vault |


### Note

Active note commands.

| Command | Description |
|---------|-------------|
| `active` | Get the currently active note in Obsidian |
| `open` | Open a note in the Obsidian editor |


### Command

Obsidian command palette commands.

| Command | Description |
|---------|-------------|
| `list` | List all available Obsidian commands |
| `execute` | Execute a command by its ID |


### Server

Server status and info commands.

| Command | Description |
|---------|-------------|
| `status` | Check if the Obsidian Local REST API is running |


### Session

Session state commands.

| Command | Description |
|---------|-------------|
| `status` | Show current session state |



## Examples


### List and Read Notes

```bash
# List all vault files
tarunai-connect-obsidian vault list

# List files in a subdirectory
tarunai-connect-obsidian vault list "Daily Notes"

# Read a note
tarunai-connect-obsidian vault read "Projects/my-project.md"
```


### Create and Update Notes

```bash
# Create a new note
tarunai-connect-obsidian vault create "Projects/new-project.md" --content "# New Project"

# Update (overwrite) a note
tarunai-connect-obsidian vault update "Projects/new-project.md" --content "# Updated Content"

# Append to a note
tarunai-connect-obsidian vault append "Projects/new-project.md" --content "\n## New Section"
```


### Search

```bash
# Plain text search (GET /search/simple/)
tarunai-connect-obsidian search simple "meeting notes"

# Dataview DQL query — default --type dql, sent as
# application/vnd.olrapi.dataview.dql+txt
tarunai-connect-obsidian search query 'TABLE file.link FROM "Projects"'

# JsonLogic query — application/vnd.olrapi.jsonlogic+json
tarunai-connect-obsidian search query --type jsonlogic \
  '{"==":[{"var":"frontmatter.status"},"active"]}'
```


### Commands

```bash
# List available commands
tarunai-connect-obsidian command list

# Execute a command by ID
tarunai-connect-obsidian command execute "editor:toggle-bold"
```


### Interactive REPL Session

Start an interactive session for exploratory use.

```bash
tarunai-connect-obsidian
# Enter commands interactively
# Use 'help' to see available commands
```


### API Key Configuration

```bash
# Via flag
tarunai-connect-obsidian --api-key YOUR_KEY vault list

# Via environment variable (recommended for agents)
export OBSIDIAN_API_KEY=YOUR_KEY
tarunai-connect-obsidian vault list
```


## State Management

The CLI maintains lightweight session state:

- **API key**: Configurable via `--api-key` or `OBSIDIAN_API_KEY` environment variable
- **Host URL**: Defaults to `https://localhost:27124`; configurable via `--host`

## Output Formats

All commands support dual output modes:

- **Human-readable** (default): Tables, colors, formatted text
- **Machine-readable** (`--json` flag): Structured JSON for agent consumption

```bash
# Human output
tarunai-connect-obsidian vault list

# JSON output for agents
tarunai-connect-obsidian --json vault list
```

## For AI Agents

When using this CLI programmatically:

1. **Always use `--json` flag** for parseable output
2. **Check return codes** - 0 for success, non-zero for errors
3. **Parse stderr** for error messages on failure
4. **Set `OBSIDIAN_API_KEY`** environment variable to avoid passing `--api-key` on every call
5. **Verify Obsidian is running** with `server status` before other commands

## More Information

- Full documentation: See README.md in the package
- Test coverage: See TEST.md in the package
- Methodology: See HARNESS.md in the tarunai-connect-plugin

## Version

1.1.0
