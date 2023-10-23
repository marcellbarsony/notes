# WireGuard

[Arch Wiki](https://wiki.archlinux.org/title/WireGuard)

1. Switch to root

```sh
sudo su
```

2. Copy [ProtonVPN](https://proton.me) configuration

```sh
[root@arch] cp /home/user/Downloads/vpn/wg0.conf /etc/wireguard
[root@arch] ls -al /etc/wireguard
-rw-r--r-- 1 root root  337 Oct 23 18:00 wg0.conf
```

## NetworkManager

### Import profile

```sh
nmcli connection import type wireguard file /etc/wireguard/wg0.conf
```

### Delete profile

```sh
nmcli connection delete wg0
```

### Enable/Disable connection

```sh
nmcli connection up wg0
nmcli connection down wg0
```
