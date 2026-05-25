# cli-hub-meta-skill

cli-hub (inside tarunAI Connect) is the package manager. This SKILL tells an agent how to use it.

Commands:

- `tarunai-connect list` — browse all available CLIs
- `tarunai-connect search image` — search by keyword
- `tarunai-connect search "3d modeling"` — multi-word search
- `tarunai-connect install gimp` — install a CLI
- `tarunai-connect info gimp` — show CLI details
- `tarunai-connect list --json` — machine-readable output

## Usage Pattern

1. The agent has `tarunai-connect` available (it's a pip package).
2. **Find your tool**: `tarunai-connect search <keyword>` or `tarunai-connect list -c <category>`
3. **Install**: `tarunai-connect install <name>`
4. **Use**: invoke the `entry_point` for that CLI (e.g., `tarunai-connect-gimp` for GIMP)
5. For preview-capable harnesses, call the tool's preview command first, then `tarunai-connect previews ...` to inspect or open the result

## Example

```
tarunai-connect search video
tarunai-connect install kdenlive
tarunai-connect-kdenlive --help
```

## Links

- Repository: https://github.com/tharunramagiri/tarunai-connect
