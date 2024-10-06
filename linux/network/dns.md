# DNS

- [Arch Wiki - DNS Resolution](https://wiki.archlinux.org/title/Domain_name_resolution)
- [Arch Wiki - Openresolv](https://wiki.archlinux.org/title/Openresolv)

The glibc resolver reads `/etc/resolv.conf`.

<!-- ## Tools {{{ -->
## Tools

### NetworkManager

- [Arch Wiki - NetworkManager: Unmanaged /etc/resolv.conf](https://wiki.archlinux.org/title/NetworkManager#Unmanaged_/etc/resolv.conf)

Stop NetworkManager from modifying `/etc/resolv.conf`
```sh
# /etc/NetworkManager/conf.d/dns.conf
[main]
dns=none
```
### [Bind9](https://github.com/isc-projects/bind9)

- [Arch Wiki - BIND](https://wiki.archlinux.org/title/BIND)

### [ldns](https://github.com/NLnetLabs/ldns)
<!-- }}} -->

<!-- ## Service {{{ -->
## Service

Systemd
```sh
# Status
stemctl status systemd-resolved.service

# Start
stemctl start systemd-resolved.service

# Stop
stemctl stop systemd-resolved.service
```

Config
```sh
systemd_resolved_service = "sudo systemctl start systemd-resolved.service"
```
<!-- }}} -->

<!-- ## Cache {{{ -->
## Cache

Flush cache 

- Systemd resolved
```sh
sudo systemd-resolve --flush-caches
```

- Browsers
```md
# Firefox
about:networking#dns

# Chromium
chrome://net-internals/#dns
```
<!-- }}} -->

<!-- ## Security {{{ -->
## Security

- [DNSSEC](https://wiki.archlinux.org/title/DNSSEC)
<!-- }}} -->

<!-- ## DNS Leaks {{{ -->
## DNS Leaks

### Disable IPv6

- [Arch Wiki - IPv6: Disable_IPv6](https://wiki.archlinux.org/title/IPv6#Disable_IPv6)
- [Arch Wiki - IPv6: NetworkManager](https://wiki.archlinux.org/title/IPv6#NetworkManager)

```sh
# NetworkManager
nmcli connection modify <connection_name> ipv6.method "disabled"
```

#### ProtonVPN

- [ProtonVPN - Prevent IPv6 VPN Leaks](https://protonvpn.com/support/prevent-ipv6-vpn-leaks/)

IPv6 traffic is disabled; any potential IPv6 traffic is routed to a black hole (null route) to ensure your device cannot make connections over IPv6.

### WebRTC

- [BrowserLeaks - WebRTC](https://browserleaks.com/webrtc)

#### Firefox

To disable WebRTC in Firefox (`/* 7020: disable WebRTC (Web Real-Time Communication`)
Type `about:config` in the address bar and press Enter.
search bar, type `media.peerconnection.enabled` and to set its value to `false`.

#### Chrome

- [Chrome Store - WebRTC Network Limiter](https://chrome.google.com/webstore/detail/webrtc-network-limiter/npeicpdbkakmehahjeeohfdhnlpdklia)
<!-- }}}-->
