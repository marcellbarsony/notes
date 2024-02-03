# DNS

[DNS Resolution](https://wiki.archlinux.org/title/Domain_name_resolution)
[Openresolv](https://wiki.archlinux.org/title/Openresolv)

The glibc resolver reads `/etc/resolv.conf`.

<!-- {{{ ## Tools -->
## Tools

### [Bind9](https://github.com/isc-projects/bind9)

[Arch Wiki](https://wiki.archlinux.org/title/BIND)


### [ldns](https://github.com/NLnetLabs/ldns)

## NetworkManager

[NetworkManager - Unmanaged /etc/resolv.conf](https://wiki.archlinux.org/title/NetworkManager#Unmanaged_/etc/resolv.conf)

Stop NetworkManager from modifying `/etc/resolv.conf`
```sh
# /etc/NetworkManager/conf.d/dns.conf

[main]
dns=none
```
<!-- }}} -->

<!-- {{{ ## Service -->
## Service

Systemd
```sh
# Status
stemctl status systemd-resolved.service

# Start
stemctl start systemd-resolved.service
```

Config
```sh
systemd_resolved_service = "sudo systemctl start systemd-resolved.service"
```
<!-- }}} -->

<!-- {{{ ## Cache -->
## Cache

Flush cache (Systemd resolved)
```sh
sudo systemd-resolve --flush-caches
```

Browsers
```sh
# Firefox
about:networking#dns

# Chromium
chrome://net-internals/#dns
```
<!-- }}} -->

<!-- {{{ ## Security -->
## Security

[DNSSEC](https://wiki.archlinux.org/title/DNSSEC)
<!-- }}} -->
