# tarunai-connect-calibre

A CLI harness for [Calibre](https://calibre-ebook.com/), the powerful e-book management application. Part of the [tarunai-connect](https://github.com/tharunramagiri/tarunai-connect) toolkit.

## What It Does

`tarunai-connect-calibre` gives AI agents and scripts a clean, structured command-line interface to Calibre's library operations, metadata editing, and format conversion — without reimplementing any of Calibre's logic. It wraps the real tools:

- **`calibredb`** — library management, metadata, import/export
- **`ebook-convert`** — format conversion (EPUB → MOBI, PDF, TXT, etc.)
- **`ebook-meta`** — standalone file metadata editing

## Requirements

### 1. Install Calibre (hard dependency)

```bash
# Debian/Ubuntu
sudo apt-get install calibre

# Fedora/RHEL
sudo dnf install calibre

# macOS
brew install --cask calibre

# Windows / other
# Download from: https://calibre-ebook.com/download
```

Verify:
```bash
which calibredb        # must be in PATH
which ebook-convert    # must be in PATH
```

### 2. Install tarunai-connect-calibre

```bash
cd agent-harness
pip install -e .
```

Verify:
```bash
which tarunai-connect-calibre
tarunai-connect-calibre --version
```

## Quick Start

```bash
# Connect to your Calibre library
tarunai-connect-calibre library connect ~/Calibre\ Library

# List all books
tarunai-connect-calibre books list

# List as JSON (for agent consumption)
tarunai-connect-calibre --json books list

# Search books
tarunai-connect-calibre books search "author:asimov"

# Show metadata for book ID 42
tarunai-connect-calibre books show 42

# Set metadata
tarunai-connect-calibre meta set 42 series "Foundation"
tarunai-connect-calibre meta set 42 series_index 1

# Convert EPUB to MOBI
tarunai-connect-calibre formats convert 42 EPUB MOBI

# Export books to directory
tarunai-connect-calibre books export 42 --to-dir ~/kindle-transfer

# Enter interactive REPL (default when no subcommand given)
tarunai-connect-calibre
```

## Command Reference

### Library Management

```bash
tarunai-connect-calibre library connect <path>   # Set active library
tarunai-connect-calibre library info             # Library statistics
tarunai-connect-calibre library check            # Verify integrity
```

### Book Operations

```bash
tarunai-connect-calibre books list [--search QUERY] [--sort FIELD] [--limit N]
tarunai-connect-calibre books search "title:Foundation"
tarunai-connect-calibre books add book.epub [book2.epub ...]
tarunai-connect-calibre books remove 42,43,44
tarunai-connect-calibre books show 42
tarunai-connect-calibre books export 42 --to-dir /path/to/dir
```

### Metadata Editing

```bash
tarunai-connect-calibre meta get 42          # All metadata
tarunai-connect-calibre meta get 42 title    # Single field
tarunai-connect-calibre meta set 42 title "New Title"
tarunai-connect-calibre meta set 42 authors "Author One & Author Two"
tarunai-connect-calibre meta set 42 tags "scifi,classic,favorite"
tarunai-connect-calibre meta set 42 rating 5
tarunai-connect-calibre meta embed 42        # Embed into book file
```

### Format Management

```bash
tarunai-connect-calibre formats list 42
tarunai-connect-calibre formats add 42 /path/to/book.mobi
tarunai-connect-calibre formats remove 42 MOBI
tarunai-connect-calibre formats convert 42 EPUB MOBI
tarunai-connect-calibre formats convert 42 EPUB PDF --output /tmp/book.pdf
```

### Custom Columns

```bash
tarunai-connect-calibre custom list
tarunai-connect-calibre custom add "#genre" "Genre" text
tarunai-connect-calibre custom add "#read_date" "Date Read" datetime
tarunai-connect-calibre custom set 42 "#genre" "Science Fiction"
tarunai-connect-calibre custom remove "#genre"
```

### Catalog Generation

```bash
tarunai-connect-calibre catalog /output/catalog.epub --title "My Library"
tarunai-connect-calibre catalog /output/catalog.csv --format csv
```

## JSON Output Mode

All commands support `--json` for machine-readable output:

```bash
tarunai-connect-calibre --json books list
tarunai-connect-calibre --json books search "author:asimov"
tarunai-connect-calibre --json meta get 42
tarunai-connect-calibre --json library info
```

## Calibre Query Language

Used with `books list --search` and `books search`:

```
author:asimov                    # Author contains "asimov"
title:"Foundation"               # Title phrase
tags:fiction                     # Tag match
rating:>3                        # Rating greater than 3
series:"Foundation"              # Series exact match
pubdate:[2020-01-01,2021-12-31]  # Date range
identifiers:isbn:9780553293357   # ISBN lookup
has:cover                        # Books with covers
not:tags:read                    # Unread books
author:asimov and tags:scifi     # Boolean AND
```

## Session State

The active library path is persisted in `~/.tarunai-connect-calibre/session.json`.
Override with the `CALIBRE_LIBRARY` environment variable.

## Running Tests

```bash
cd agent-harness

# Syntax check
python -m py_compile \
  tarunai_connect/calibre/calibre_cli.py \
  tarunai_connect/calibre/core/*.py \
  tarunai_connect/calibre/utils/*.py

# Unit and CLI smoke tests (no Calibre required)
python -m pytest tarunai_connect/calibre/tests/test_core.py -v

# Installed-command smoke tests (no Calibre required)
pip install -e .
TARUNAI_CONNECT_FORCE_INSTALLED=1 python -m pytest \
  tarunai_connect/calibre/tests/test_core.py::TestCLISubprocessSmoke -v

# Full E2E tests (Calibre required)
python -m pytest tarunai_connect/calibre/tests/test_full_e2e.py -v -s

# All tests with installed binary and real Calibre backend
TARUNAI_CONNECT_FORCE_INSTALLED=1 python -m pytest tarunai_connect/calibre/tests/ -v -s
```

### Real Backend Validation

Before running E2E validation, verify Calibre's commands are on PATH:

```bash
which calibredb
which ebook-convert
which ebook-meta
```

The E2E suite creates temporary Calibre libraries, imports generated EPUB files,
updates metadata with `calibredb`, converts EPUB files with `ebook-convert`, and
checks exported/converted artifacts for real output files. These tests require a
real Calibre installation; `test_core.py` remains the no-Calibre validation path.
