---
name: "tarunai-connect-calibre"
description: >-
  Command-line interface for Calibre - A stateful CLI harness for e-book library management, metadata editing, and format conversion wrapping the real Calibre tools (calibredb, ebook-convert, ebook-meta)...
---

# tarunai-connect-calibre

A stateful CLI harness for Calibre e-book management. Wraps the real Calibre tools (`calibredb`, `ebook-convert`, `ebook-meta`) to give AI agents and scripts a clean, structured interface for library operations, metadata editing, and format conversion.

## Installation

This CLI is installed as part of the tarunai-connect-calibre package:

```bash
pip install git+https://github.com/tharunramagiri/tarunai-connect.git#subdirectory=calibre/agent-harness
```

**Prerequisites:**
- Python 3.10+
- Calibre must be installed on your system (hard dependency)

```bash
# Debian/Ubuntu
sudo apt-get install calibre

# macOS
brew install --cask calibre

# Verify tools are in PATH
which calibredb
which ebook-convert
which ebook-meta
```


## Usage

### Basic Commands

```bash
# Show help
tarunai-connect-calibre --help

# Start interactive REPL mode
tarunai-connect-calibre

# Connect to a Calibre library
tarunai-connect-calibre library connect ~/Calibre\ Library

# Run with JSON output (for agent consumption)
tarunai-connect-calibre --json books list
```

### REPL Mode

When invoked without a subcommand, the CLI enters an interactive REPL session:

```bash
tarunai-connect-calibre
# Enter commands interactively with tab-completion and history
# Use 'help' to see available commands
# Use 'quit' or 'exit' to leave
```


## Command Groups


### Library

Library management commands.

| Command | Description |
|---------|-------------|
| `connect <path>` | Set active library path |
| `info` | Show library statistics (book count, formats, db size) |
| `check` | Verify library integrity using calibredb check_library |


### Books

Book operations (wrap `calibredb`).

| Command | Description |
|---------|-------------|
| `list` | List books with filtering and sorting |
| `search <query>` | Search using Calibre query language |
| `add <files>` | Add book files to library |
| `remove <ids>` | Remove books (move to trash or permanent delete) |
| `show <id>` | Show full metadata for a book |
| `export <ids>` | Export books to directory |
| `export-chapters <id>` | Export each chapter as separate PDF (requires EPUB format) |


### Meta

Metadata editing (wrap `calibredb set_metadata`).

| Command | Description |
|---------|-------------|
| `get <id> [field]` | Get metadata (all or specific field) |
| `set <id> <field> <value>` | Set a metadata field |
| `embed <ids>` | Embed metadata into book files |


### Formats

Format management (wrap `calibredb` + `ebook-convert`).

| Command | Description |
|---------|-------------|
| `list <id>` | List available formats for a book |
| `add <id> <file>` | Add a format to a book |
| `remove <id> <fmt>` | Remove a format from a book |
| `convert <id> <input_fmt> <output_fmt>` | Convert book format |


### Custom

Custom columns (wrap `calibredb`).

| Command | Description |
|---------|-------------|
| `list` | List all custom columns |
| `add <label> <name> <type>` | Create custom column |
| `remove <label>` | Delete custom column |
| `set <id> <label> <value>` | Set custom field value |


### Catalog

Catalog generation.

| Command | Description |
|---------|-------------|
| `catalog <output>` | Generate a catalog of the library (EPUB, CSV, or OPDS) |


## Examples


### Connect and List Books

Connect to your Calibre library and list books.

```bash
tarunai-connect-calibre library connect ~/Calibre\ Library
tarunai-connect-calibre books list
# Or with JSON output
tarunai-connect-calibre --json books list --search "author:asimov"
```


### Search and Filter

Search books using Calibre query language.

```bash
tarunai-connect-calibre books search "title:Foundation"
tarunai-connect-calibre books search "author:asimov and tags:scifi"
tarunai-connect-calibre books search "rating:>3"
```


### Metadata Editing

Set metadata fields on books.

```bash
tarunai-connect-calibre meta set 42 title "New Title"
tarunai-connect-calibre meta set 42 series "Foundation"
tarunai-connect-calibre meta set 42 series_index 1
tarunai-connect-calibre meta set 42 tags "scifi,classic"
tarunai-connect-calibre meta set 42 rating 5
```


### Format Conversion

Convert between e-book formats.

```bash
tarunai-connect-calibre formats convert 42 EPUB MOBI
tarunai-connect-calibre formats convert 42 EPUB PDF --output /tmp/book.pdf
```


### Export Chapters as PDFs

Export each chapter of an EPUB as a separate PDF file.

```bash
tarunai-connect-calibre books export-chapters 42 --to-dir ./pdfs
tarunai-connect-calibre books export-chapters 42 --to-dir ./pdfs --chapters 1-5
```


## Calibre Query Language

Used with `books search` and `books list --search`:

```
author:asimov                    # Author contains "asimov"
title:"Foundation"               # Title phrase
tags:fiction                     # Tag match
rating:>3                        # Rating greater than 3
series:"Foundation"              # Series match
pubdate:[2020-01-01,2021-12-31]  # Date range
identifiers:isbn:1234567890      # Specific identifier
has:cover                        # Has cover image
not:tags:fiction                 # Negation
author:asimov and tags:scifi     # Boolean AND
```

## Key Metadata Fields

| Field | Type | Description |
|-------|------|-------------|
| `title` | text | Book title |
| `authors` | text | Author names (&-separated) |
| `tags` | text | Comma-separated tags |
| `series` | text | Series name |
| `series_index` | float | Position in series |
| `rating` | float | Rating 1-5 |
| `publisher` | text | Publisher name |
| `pubdate` | datetime | Publication date |
| `comments` | text | Description/comments |
| `languages` | text | Language codes |
| `identifiers` | text | ISBN, ASIN, etc. (`type:value`) |

## Supported Formats

**Input:** EPUB, MOBI, AZW, AZW3, PDF, HTML, DOCX, ODT, FB2, TXT, RTF, LIT, and more

**Output (conversion):** EPUB, MOBI, AZW3, PDF, HTML, DOCX, TXT, and more

## State Management

The CLI maintains session state with:

- **Session file**: `~/.tarunai-connect-calibre/session.json`
- **Library path persistence**: Active library is saved across sessions
- **Environment override**: `CALIBRE_LIBRARY` environment variable

## Output Formats

All commands support dual output modes:

- **Human-readable** (default): Tables, colors, formatted text
- **Machine-readable** (`--json` flag): Structured JSON for agent consumption

```bash
# Human output
tarunai-connect-calibre books list

# JSON output for agents
tarunai-connect-calibre --json books list
```

## For AI Agents

When using this CLI programmatically:

1. **Always use `--json` flag** for parseable output
2. **Check return codes** - 0 for success, non-zero for errors
3. **Parse stderr** for error messages on failure
4. **Verify outputs exist** after export/conversion operations
5. **Use `--library` flag** or `CALIBRE_LIBRARY` env to specify library path
6. **Chapter export requires EPUB format** - convert first if needed

## More Information

- Full documentation: See README.md in the package
- Architecture SOP: See CALIBRE.md in the agent-harness directory
- Test coverage: See test_core.py and test_full_e2e.py in the tests directory
- Methodology: See HARNESS.md in the tarunai-connect-plugin

## Version

1.0.0