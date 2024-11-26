# DNS over HTTPS

## Installation

Install the [dns-over-https](https://archlinux.org/packages/?name=dns-over-https)
package

## Client startup

Check if any programs using port 53
```sh
$ ss -lp 'sport = :domain'
```

### Startup

Enable the `doh-client.service`
```sh
systemctl enable doh-client.service
```
