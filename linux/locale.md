# Keyboard

[Keyboard configuradion](https://wiki.archlinux.org/title/Linux_console/Keyboard_configuration)

```sh
/etc/X11/xorg.conf.d/00-keyboard.conf
```

<!-- {{{ ## Set keymap -->
## Set keymap

### View settings
```sh
localectl status
```

### List layouts
```sh
localectl list-x11-keymap-models
localectl list-x11-keymap-layouts
localectl list-x11-keymap-variants [layout]
localectl list-x11-keymap-options
```

### Set using setxkbmap
```sh
sudo localectl [--no-convert] set-x11-keymap layout [model [variant [options]]]
sudo localectl set-x11-keymap us "" colemak 
```
<!-- }}} -->
