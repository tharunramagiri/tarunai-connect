# tarunai-connect-zoom

CLI harness for **Zoom** — manage meetings, participants, and recordings from the command line via the Zoom REST API.

## Installation

```bash
pip install tarunai-connect-zoom
# or from source:
cd zoom/agent-harness && pip install -e .
```

## Prerequisites

1. A Zoom account (free or paid)
2. A Zoom OAuth App — create one at https://marketplace.zoom.us/develop/create
   - App type: **General App** (OAuth)
   - Redirect URL: `http://localhost:4199/callback`
   - Required scopes: `user:read:admin`, `meeting:read:admin`, `meeting:write:admin`, `recording:read:admin`

## Quick Start

```bash
# 1. Configure OAuth credentials
tarunai-connect-zoom auth setup --client-id YOUR_CLIENT_ID --client-secret YOUR_CLIENT_SECRET

# 2. Login (opens browser)
tarunai-connect-zoom auth login

# 3. Create a meeting
tarunai-connect-zoom meeting create --topic "Team Standup" --duration 30

# 4. List meetings
tarunai-connect-zoom meeting list

# 5. Interactive mode
tarunai-connect-zoom repl
```

## Commands

| Group | Commands |
|---|---|
| `auth` | `setup`, `login`, `status`, `logout` |
| `meeting` | `create`, `list`, `info`, `update`, `delete`, `join`, `start` |
| `participant` | `add`, `add-batch`, `list`, `remove`, `attended` |
| `recording` | `list`, `files`, `download`, `delete` |

## Agent Usage (JSON mode)

All commands support `--json` for machine-readable output:

```bash
tarunai-connect-zoom --json meeting list
tarunai-connect-zoom --json meeting create --topic "Sync" --duration 60 --auto-recording cloud
```
