# Keyboard

[Keyboard configuradion](https://wiki.archlinux.org/title/Linux_console/Keyboard_configuration)
```sh
/etc/X11/xorg.conf.d/00-keyboard.conf
```

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
sudo localectl set-x11-keymap us "" colemak_dh caps:capslock
```

```sh
 cat /etc/X11/xorg.conf.d/00-keyboard.conf
# Written by systemd-localed(8), read by systemd-localed and Xorg. It's
# probably wise not to edit this file manually. Use localectl(1) to
# update this file.
Section "InputClass"
        Identifier "system-keyboard"
        MatchIsKeyboard "on"
        Option "XkbLayout" "us"
        Option "XkbVariant" "colemak_dh"
        Option "XkbOptions" "caps:capslock"
EndSection
```
