## Loopback address

**Local Loopback Address** is used to let a system send a message to itself -
without requiring a physical NIC -
to make sure that TCP/IP stack is installed correctly on the machine.
(e.g., a locally installed website may be accessed from a web browser by the URL _http://localhost_ to display its home page)

[[Wikipedia - localhost](https://en.wikipedia.org/wiki/Localhost)]<br>
[[Wikipedia - loopback](https://en.wikipedia.org/wiki/Loopback)]

## Name resolution

**IPv4 network standards** reserve the entire address block `127.0.0.0/8` for loopback purposes.
Any packet sent to those addresses is looped back.
The address `127.0.0.1` is the standard address for loopback traffic.

**IPv6 network standard** assigns only a single address for loopback: `::1`

The resolution of the name _localhost_ is normally configured in the [hosts file](https://en.wikipedia.org/wiki/Hosts_(file))

```cmd
127.0.0.1    localhost
::1          localhost
```

The name should be resolved locally, and should not be forwarded to remote name servers, however the name may also be resolved by DNS servers.

In the Domain Name System the name localhost is reserved as a top-level domain name, to avoid confusion with the hostname used for loopback purposes.

## Routers & Switches

Routers and switches also have loopback addresses which are not the same as the local loopback address.
