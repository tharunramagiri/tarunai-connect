# tarunAI Connect-Slay-the-Spire-2

`tarunAI Connect-Slay-the-Spire-2` is a CLI harness that connects the real Steam version of *Slay the Spire 2* to a stateful command-line interface, making it agent-native.

<p align="center">
  <img src="assets/example_gif.gif" alt="tarunAI Connect-Slay-the-Spire-2 demo" width="900">
</p>

It works like this:

1. The in-game bridge mod `STS2_Bridge` runs inside the game process.
2. The mod exposes a local HTTP API at `http://localhost:15526/api/v1/singleplayer`.
3. The CLI reads state and sends actions through that API.

This project controls the real running game. It is not a headless simulator and it does not use screen automation.

## What Is Included

- `agent-harness/`
  - The CLI harness package (`tarunai_connect/slay_the_spire_ii/`), installable via `pip install -e .`.
- `agent-harness/bridge/plugin/`
  - `.NET 9` source for the bridge mod. **This mod is required** — the CLI cannot function without it.
- `agent-harness/bridge/install/`
  - Install bundle and scripts for the bridge mod.

**Important:** Unlike other tarunAI Connect harnesses that wrap standalone applications, this harness requires a custom bridge mod to be built and installed into the game. The bridge mod exposes the game's internal state via HTTP, which the CLI then consumes.

## Requirements

- A working Steam installation of *Slay the Spire 2*
- Python `>= 3.10`
- `.NET 9 SDK` (only for building the bridge mod)

The bridge build and install scripts currently auto-detect the default macOS Steam path. If your game is installed elsewhere, pass the path explicitly or override it with an environment variable.

## Installation

### 1. Install the CLI

From the repository root:

```bash
cd slay_the_spire_ii/agent-harness
pip install -e .
```

This installs the `tarunai-connect-sts2` command.

### 2. Build the bridge mod

```bash
cd slay_the_spire_ii/agent-harness/bridge/plugin
./build.sh
```

The script tries to auto-detect the game data directory and refreshes the local install bundle at:

```text
slay_the_spire_ii/agent-harness/bridge/install/bridge_plugin/
```

If auto-detection fails, set `STS2_GAME_DATA_DIR` or pass the directory directly:

```bash
STS2_GAME_DATA_DIR="/path/to/data_sts2_macos_arm64" ./build.sh
```

The target directory must contain at least:

- `sts2.dll`
- `GodotSharp.dll`
- `0Harmony.dll`

### 3. Install the bridge mod into the game

```bash
cd slay_the_spire_ii/agent-harness/bridge/install
./install_bridge.sh
```

The default target path is:

```text
~/Library/Application Support/Steam/steamapps/common/Slay the Spire 2/SlayTheSpire2.app/Contents/MacOS/mods/STS2_Bridge/
```

If your game is not installed in the default location, pass the game root explicitly:

```bash
./install_bridge.sh "/path/to/Slay the Spire 2"
```

### 4. Enable the mod in game

Launch the game and make sure `STS2_Bridge` is loaded and enabled. Once enabled, the mod listens on:

```text
http://localhost:15526/
```

### 5. Verify the setup

```bash
tarunai-connect-sts2 --help
tarunai-connect-sts2 state
```

If `tarunai-connect-sts2 state` returns JSON, the CLI and the bridge are connected correctly.

## Usage

### Shortest path

1. Build and install `STS2_Bridge`
2. Launch the real game and enable the mod
3. Run `pip install -e .` from `slay_the_spire_ii/agent-harness`
4. Run `tarunai-connect-sts2 state`

### Start from the main menu

```bash
tarunai-connect-sts2 state
tarunai-connect-sts2 continue-game
tarunai-connect-sts2 start-game --character IRONCLAD --ascension 0
tarunai-connect-sts2 abandon-game
tarunai-connect-sts2 return-to-main-menu
```

`start-game --character` currently recognizes:

- `IRONCLAD`
- `SILENT`
- `DEFECT`
- `NECROBINDER`
- `REGENT`

### Manual control during a run

```bash
tarunai-connect-sts2 state
tarunai-connect-sts2 choose-map 0
tarunai-connect-sts2 play-card 0 --target jaw_worm_0
tarunai-connect-sts2 end-turn
tarunai-connect-sts2 claim-reward 0
tarunai-connect-sts2 pick-card-reward 0
tarunai-connect-sts2 rest 0
tarunai-connect-sts2 event 0
tarunai-connect-sts2
```

Common command groups:

- State inspection: `state`, `raw-state`
- Menu actions: `continue-game`, `start-game`, `abandon-game`, `return-to-main-menu`
- Combat: `play-card`, `use-potion`, `end-turn`
- Map and rooms: `choose-map`, `event`, `advance-dialogue`, `rest`, `proceed`
- Rewards and overlays: `claim-reward`, `pick-card-reward`, `skip-card-reward`, `select-card`, `confirm-selection`, `select-relic`

For the full command surface:

```bash
tarunai-connect-sts2 --help
```

## Configuration

### CLI

- `--base-url`
  - Default: `http://localhost:15526`
- `--timeout`
  - Default: `10.0`

Example:

```bash
tarunai-connect-sts2 --base-url http://127.0.0.1:15526 --timeout 20 state
```

### Bridge build

- `STS2_GAME_DATA_DIR`
  - Use this when `slay_the_spire_ii/agent-harness/bridge/plugin/build.sh` cannot auto-detect the game data directory

## Troubleshooting

### `tarunai-connect-sts2 state` cannot connect

This usually means one of the following is still missing:

- The game is not running
- `STS2_Bridge` is not installed or not enabled
- The local API on `localhost:15526` is not up yet

### `slay_the_spire_ii/agent-harness/bridge/plugin/build.sh` cannot find the game directory

Confirm that the game is installed, then pass `STS2_GAME_DATA_DIR` explicitly:

```bash
STS2_GAME_DATA_DIR="/path/to/data_sts2_macos_arm64" ./slay_the_spire_ii/agent-harness/bridge/plugin/build.sh
```

## Related Docs

- [agent-harness/STS2.md](agent-harness/STS2.md)
- [agent-harness/bridge/plugin/README.md](agent-harness/bridge/plugin/README.md)

## Credits

This project was informed by:

- [`wuhao21/sts2-cli`](https://github.com/wuhao21/sts2-cli)
- [`Gennadiyev/STS2MCP`](https://github.com/Gennadiyev/STS2MCP)
- [`tharunramagiri/tarunai-connect`](https://github.com/tharunramagiri/tarunai-connect)
