# DNS

[DNS Resolution](https://wiki.archlinux.org/title/Domain_name_resolution)
[Openresolv](https://wiki.archlinux.org/title/Openresolv)

The glibc resolver reads `/etc/resolv.conf`.

## Tools

### [Bind9](https://github.com/isc-projects/bind9)

[Arch Wiki](https://wiki.archlinux.org/title/BIND)


### [ldns](https://github.com/NLnetLabs/ldns)

## NetworkManager

[NetworkManager - Unmanaged /etc/resolv.conf](https://wiki.archlinux.org/title/NetworkManager#Unmanaged_/etc/resolv.conf)

Stop NetworkManager from touching `/etc/resolv.conf`
```sh
/etc/NetworkManager/conf.d/dns.conf

[main]
dns=none
```

## Systemd

Service
```sh
stemctl status systemd-resolved.service
```

Config
```sh
systemd_resolved_service = "sudo systemctl start systemd-resolved.service"
```

## Flush cache

Systemd resolved
```sh
sudo systemd-resolve --flush-caches"
```

Firefox
```
about:networking#dns
```

Chromium
```
chrome://net-internals/#dns
```

## Security

[DNSSEC](https://wiki.archlinux.org/title/DNSSEC)
