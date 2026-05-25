# Evaluation Pipeline — tarunai-connect-rekordbox

## Smoke
`pytest tarunai_connect/rekordbox/tests/`

## Manual integration (requires Rekordbox 6/7 installed)
1. `tarunai-connect-rekordbox status` → expect non-zero `track_count`
2. `tarunai-connect-rekordbox library search "Demo"` → expect default Pioneer demo tracks
3. `tarunai-connect-rekordbox playlist create eval-test` → expect `created`
4. `tarunai-connect-rekordbox playlist add eval-test --track-title "Demo Track 1"` → expect `added`
5. `tarunai-connect-rekordbox playlist clear eval-test` → expect removed > 0

## MIDI integration (requires virtual MIDI port + rekordbox open + mapping enabled)
6. `tarunai-connect-rekordbox install-mapping` → expect at least one path written
7. (manual) Enable LoopBe Internal MIDI in rekordbox prefs
8. `tarunai-connect-rekordbox deck eq --deck 1 --hi 0.5 --mid 0.5 --lo 0.5 --port LoopBe`
9. Observe in rekordbox: deck 1 EQ knobs set to noon
