---
name: >-
  tarunai-connect-libreoffice
description: >-
  Command-line interface for Libreoffice - A stateful command-line interface for document editing, producing real ODF files (ZIP archives with ...
---

# tarunai-connect-libreoffice

A stateful command-line interface for document editing, producing real ODF files (ZIP archives with XML). Designed for AI agents and power users who need to create and manipulate Writer, Calc, and Impress documents without a GUI or LibreOffice installation.

## Installation

This CLI is installed as part of the tarunai-connect-libreoffice package:

```bash
pip install tarunai-connect-libreoffice
```

**Prerequisites:**
- Python 3.10+
- libreoffice must be installed on your system


## Usage

### Basic Commands

```bash
# Show help
tarunai-connect-libreoffice --help

# Start interactive REPL mode
tarunai-connect-libreoffice

# Create a new project
tarunai-connect-libreoffice project new -o project.json

# Run with JSON output (for agent consumption)
tarunai-connect-libreoffice --json project info -p project.json
```

### REPL Mode

When invoked without a subcommand, the CLI enters an interactive REPL session:

```bash
tarunai-connect-libreoffice
# Enter commands interactively with tab-completion and history
```


## Command Groups


### Document

Document management commands.

| Command | Description |
|---------|-------------|
| `new` | Create a new document |
| `open` | Open project JSON, or import an existing Office/ODF file |
| `import` | Import an existing Office/ODF file to project JSON |
| `import-formats` | List supported import formats |
| `save` | Save the current document |
| `info` | Show document information |
| `profiles` | List available page profiles |
| `json` | Print raw project JSON |


### Writer

Writer (word processor) commands.

| Command | Description |
|---------|-------------|
| `add-paragraph` | Add a paragraph to the document |
| `add-heading` | Add a heading to the document |
| `add-list` | Add a list to the document |
| `add-table` | Add a table to the document |
| `add-page-break` | Add a page break |
| `remove` | Remove a content item by index |
| `list` | List all content items |
| `set-text` | Set the text of a content item |


### Calc

Calc (spreadsheet) commands.

| Command | Description |
|---------|-------------|
| `add-sheet` | Add a new sheet |
| `remove-sheet` | Remove a sheet by index |
| `rename-sheet` | Rename a sheet |
| `set-cell` | Set a cell value |
| `get-cell` | Get a cell value |
| `list-sheets` | List all sheets |


### Impress

Impress (presentation) commands.

| Command | Description |
|---------|-------------|
| `add-slide` | Add a slide to the presentation |
| `remove-slide` | Remove a slide by index |
| `set-content` | Update a slide's title and/or content |
| `list-slides` | List all slides |
| `add-element` | Add an element to a slide |


### Style Group

Style management commands.

| Command | Description |
|---------|-------------|
| `create` | Create a new style |
| `modify` | Modify an existing style |
| `list` | List all styles |
| `apply` | Apply a style to a content item (Writer only) |
| `remove` | Remove a style |


### Export Group

Export/render commands.

| Command | Description |
|---------|-------------|
| `presets` | List export presets |
| `preset-info` | Show preset details |
| `render` | Export the document to a file |


### Session

Session management commands.

| Command | Description |
|---------|-------------|
| `status` | Show session status |
| `undo` | Undo the last operation |
| `redo` | Redo the last undone operation |
| `history` | Show undo history |




## Examples


### Create a New Project

Create a new libreoffice project file.

```bash
tarunai-connect-libreoffice project new -o myproject.json
# Or with JSON output for programmatic use
tarunai-connect-libreoffice --json project new -o myproject.json
```


### Interactive REPL Session

Start an interactive session with undo/redo support.

```bash
tarunai-connect-libreoffice
# Enter commands interactively
# Use 'help' to see available commands
# Use 'undo' and 'redo' for history navigation
```


### Export Project

Export the project to a final output format.

```bash
tarunai-connect-libreoffice --project myproject.json export render output.pdf --overwrite
```


## State Management

The CLI maintains session state with:

- **Undo/Redo**: Up to 50 levels of history
- **Project persistence**: Save/load project state as JSON
- **Existing file import**: Convert ODF/DOCX/XLSX/PPTX and related formats into editable project JSON
- **Session tracking**: Track modifications and changes

## Output Formats

All commands support dual output modes:

- **Human-readable** (default): Tables, colors, formatted text
- **Machine-readable** (`--json` flag): Structured JSON for agent consumption

```bash
# Human output
tarunai-connect-libreoffice project info -p project.json

# JSON output for agents
tarunai-connect-libreoffice --json project info -p project.json
```

## For AI Agents

When using this CLI programmatically:

1. **Always use `--json` flag** for parseable output
2. **Check return codes** - 0 for success, non-zero for errors
3. **Parse stderr** for error messages on failure
4. **Use absolute paths** for all file operations
5. **Import existing Office files to JSON first** with `document import input.docx -o work.json`
6. **Verify outputs exist** after export operations

## More Information

- Full documentation: See README.md in the package
- Test coverage: See TEST.md in the package
- Methodology: See HARNESS.md in the tarunai-connect-plugin

## Version

1.0.0
