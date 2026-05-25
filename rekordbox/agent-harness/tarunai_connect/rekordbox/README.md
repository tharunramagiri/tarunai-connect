# tarunai-connect-rekordbox

Agent-native command-line interface for Pioneer Rekordbox 6/7. Provides programmatic access to:
1. The encrypted master.db library (tracks, playlists, cues, hot cues)
2. Live deck control via virtual MIDI (play/pause, sync, crossfade, EQ, hot cues)

## Install

```bash
pip install tarunai-connect-rekordbox
# Optional Windows extras for UI automation:
pip install tarunai-connect-rekordbox[windows]
```

Requires Python 3.10+, Rekordbox 6 or 7, and (optionally) a virtual MIDI driver for live-deck control.

## Why

Pioneer ships no public REST API for playback. This harness combines `pyrekordbox` (direct SQLCipher DB access) with `mido` (virtual MIDI) into a single CLI for AI agents.

## Quick start

```bash
tarunai-connect-rekordbox status
tarunai-connect-rekordbox library count
tarunai-connect-rekordbox library search "Daft Punk"
tarunai-connect-rekordbox playlist create "MyMix"
tarunai-connect-rekordbox playlist add "MyMix" --track-title "One More Time"
tarunai-connect-rekordbox install-mapping
tarunai-connect-rekordbox deck crossfade 1 2 --secs 16
```

Playlist writes are guarded: the CLI creates a `master.db` backup before
mutation and refuses to write while Rekordbox is running unless `--force` is
provided. `--no-backup` is only accepted when Rekordbox is closed.

## License
MIT
