# WireGuard

[Arch Wiki - WireGuard](https://wiki.archlinux.org/title/WireGuard)

<!-- {{{ ## Configuration -->
## Configuration

1. Switch to root

```sh
sudo su
```

2. Copy ProtonVPN [configuration](https://account.proton.me/u/0/vpn/WireGuard)

```sh
[root@arch] cp /home/user/Downloads/vpn/wg0.conf /etc/wireguard
[root@arch] ls -al /etc/wireguard
-rw-r--r-- 1 root root  337 Oct 23 18:00 wg0.conf
```
<!-- }}} -->

<!-- {{{ ## NetworkManager -->
## NetworkManager

Manage WireGuard VPN connection with [NetworkManager](https://wiki.archlinux.org/title/NetworkManager#Usage)

### Import profile

```sh
nmcli connection import type wireguard file /etc/wireguard/wg0.conf
```

### Enable/Disable connection

```sh
nmcli connection up wg0
nmcli connection down wg0
```

### Delete profile

```sh
nmcli connection delete wg0
nmcli device delete ipv6leakintrf0
```

### Autoconnect

Prevent autoconnect

```sh
nmcli connection modify <profile> connection.autoconnect no
```
<!-- }}} -->
