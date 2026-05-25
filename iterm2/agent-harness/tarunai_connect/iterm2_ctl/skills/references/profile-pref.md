# Profiles & Preferences

## Profiles
```bash
tarunai-connect-iterm2 profile list [--filter NAME]
tarunai-connect-iterm2 profile get <guid>                 # detailed settings
tarunai-connect-iterm2 profile color-presets
tarunai-connect-iterm2 profile apply-preset "Solarized Dark" [--session-id ID]
```

## Preferences
```bash
tarunai-connect-iterm2 pref list-keys                     # all valid PreferenceKey names
tarunai-connect-iterm2 pref list-keys --filter tmux       # filter by substring
tarunai-connect-iterm2 pref get OPEN_TMUX_WINDOWS_IN
tarunai-connect-iterm2 pref set OPEN_TMUX_WINDOWS_IN 2
tarunai-connect-iterm2 pref theme                         # current theme tags + is_dark bool
```

## tmux preferences (shorthand)
```bash
tarunai-connect-iterm2 pref tmux-get                      # all tmux prefs at once
tarunai-connect-iterm2 pref tmux-set open_in 2            # 0=native_windows 1=new_window 2=tabs_in_existing
tarunai-connect-iterm2 pref tmux-set auto_hide_client true
tarunai-connect-iterm2 pref tmux-set use_profile true
tarunai-connect-iterm2 pref tmux-set dashboard_limit 10
```
