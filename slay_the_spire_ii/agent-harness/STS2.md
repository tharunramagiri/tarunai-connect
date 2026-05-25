# Slay the Spire 2: Project-Specific Analysis & SOP

## Architecture Summary

Slay the Spire 2 is a real-time roguelike deckbuilder running as a native
Steam game. Unlike other tarunAI Connect harnesses that wrap desktop applications
via subprocess, this harness communicates with a live game process through an
in-game bridge mod (`STS2_Bridge`) that exposes a local HTTP API.

```
┌────────────────────────────────────────────┐
│          Slay the Spire 2 (Steam)          │
│  ┌──────────┐  ┌──────────┐  ┌─────────┐  │
│  │  Combat   │  │   Map    │  │  Menu   │  │
│  └─────┬────┘  └────┬─────┘  └────┬────┘  │
│        │             │             │        │
│  ┌─────┴─────────────┴─────────────┴─────┐ │
│  │         STS2_Bridge (.NET mod)        │ │
│  │  Reads game state, executes actions   │ │
│  └──────────────────┬────────────────────┘ │
│                     │                       │
│         http://localhost:15526              │
└─────────────────────┼──────────────────────┘
                      │
        ┌─────────────┴────────────────┐
        │      tarunai-connect-sts2       │
        │  state · play-card · rest …  │
        └──────────────────────────────┘
```

## CLI Strategy: HTTP Bridge + Normalized State

The CLI communicates with the bridge mod over HTTP at
`localhost:15526/api/v1/singleplayer`. It reads normalized JSON state and
sends action commands back through the same endpoint.

### Core Domains

| Domain | Module | Key Operations |
|--------|--------|----------------|
| State | `state_adapter.py` | Normalize raw bridge JSON into decision-based state |
| Actions | `action_adapter.py` | Build typed action payloads for every game command |
| Backend | `sts2_backend.py` | HTTP client wrapping GET/POST to the bridge API |
| Types | `types.py` | `JsonDict` type alias, `PlannedAction` dataclass |

### Decision States

The bridge normalizes all game screens into one of 15 decision types:

`menu` · `combat_play` · `hand_select` · `map_select` · `game_over` ·
`combat_rewards` · `card_reward` · `event_choice` · `rest_site` · `shop` ·
`card_select` · `relic_select` · `treasure` · `overlay` · `unknown`

### Characters

`IRONCLAD` · `SILENT` · `DEFECT` · `NECROBINDER` · `REGENT`

## Backend: Low Translation Gap

The bridge mod has direct access to the game's internal state and action API.
The CLI translates cleanly to HTTP calls. The only requirement is that the
game must be running with the `STS2_Bridge` mod enabled and listening on
`localhost:15526`.
