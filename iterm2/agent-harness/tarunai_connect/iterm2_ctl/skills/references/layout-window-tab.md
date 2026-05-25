# Windows & Tabs

## Windows
```bash
tarunai-connect-iterm2 window list
tarunai-connect-iterm2 window create [--profile NAME] [--command CMD]
tarunai-connect-iterm2 window close [WINDOW_ID]           # positional arg, NOT --window-id; uses context if omitted
tarunai-connect-iterm2 window activate [WINDOW_ID]
tarunai-connect-iterm2 window set-title "My Window"
tarunai-connect-iterm2 window frame                       # get position/size
tarunai-connect-iterm2 window set-frame --x 0 --y 0 --width 1200 --height 800
tarunai-connect-iterm2 window fullscreen on|off|toggle|status
```

## Tabs
```bash
tarunai-connect-iterm2 tab list [--window-id ID]
tarunai-connect-iterm2 tab create [--window-id ID] [--profile NAME]
tarunai-connect-iterm2 tab close [TAB_ID]
tarunai-connect-iterm2 tab activate [TAB_ID]
tarunai-connect-iterm2 tab info [TAB_ID]
tarunai-connect-iterm2 tab select-pane right              # focus adjacent split pane
tarunai-connect-iterm2 tab select-pane left|above|below [--tab-id ID]
```
