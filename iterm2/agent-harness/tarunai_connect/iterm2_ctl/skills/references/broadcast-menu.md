# Broadcast & Menu

## Broadcast — sync keystrokes across panes simultaneously
```bash
tarunai-connect-iterm2 broadcast list
tarunai-connect-iterm2 broadcast add <s1> <s2>            # group into one domain
tarunai-connect-iterm2 broadcast set "s1,s2" "s3,s4"     # set all domains at once
tarunai-connect-iterm2 broadcast all-panes [--window-id ID]
tarunai-connect-iterm2 broadcast clear                    # stop all broadcasting
```

Pattern — run the same command on all panes at once:
```bash
tarunai-connect-iterm2 broadcast all-panes
tarunai-connect-iterm2 session send "export ENV=staging"
tarunai-connect-iterm2 broadcast clear
```

## Menu — invoke iTerm2 menu items programmatically
```bash
tarunai-connect-iterm2 menu list-common
tarunai-connect-iterm2 menu select "Shell/Split Vertically with Current Profile"
tarunai-connect-iterm2 menu select "Shell/New Window"
tarunai-connect-iterm2 menu state "View/Enter Full Screen"   # checked + enabled?
```
