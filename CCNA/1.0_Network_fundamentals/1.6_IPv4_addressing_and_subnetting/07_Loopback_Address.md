## Loopback address

**Local Loopback Address** is used to let a system send a message to itself - without requiring a physical NIC - to make sure that TCP/IP stack is installed correctly on the machine.
(e.g., a locally installed website may be accessed from a web browser by the URL _http://localhost_ to display its home page)

[[Wikipedia - localhost](https://en.wikipedia.org/wiki/Localhost)]<br>
[[Wikipedia - loopback](https://en.wikipedia.org/wiki/Loopback)]

## Name resolution

**IPv4 network standards** reserve the entire address block `127.0.0.0/8` for loopback purposes.
Any packet sent to those addresses is looped back.
The address `127.0.0.1` is the standard address for loopback traffic.

**IPv6 network standard** assigns only a single address for loopback: `::1`

The resolution of the name _localhost_ is normally configured in the [hosts file](<https://en.wikipedia.org/wiki/Hosts_(file)>)

```cmd
127.0.0.1    localhost
::1          localhost
```

The name should be resolved locally, and should not be forwarded to remote name servers, however the name may also be resolved by DNS servers.

In the Domain Name System the name localhost is reserved as a top-level domain name, to avoid confusion with the hostname used for loopback purposes.

## Routers & Switches

CISCO Routers and switches also have loopback addresses that are not the same as the local loopback address:

A loopback interface is a logical interface that will not go down unless it is shut down manually.<br>
It typically has only one IP address but allows to configure multiple IP addresses.

```
Router(config)#interface loopback ?
  <0-2147483647>  Loopback interface number
Router(config)#interface loopback 0

%LINK-5-CHANGED: Interface Loopback0, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback0, changed state to up

Router(config-if)#ip address 2.2.2.2 255.255.255.255
Router(config-if)#
```

### OSPF

Routing protocols, such as OSPF, use the loopback to determine the the router IDs in the OSPF network.

When a routing protocol (e.g. OSPF) is enabled, it selects a router ID for itself.

```
Router(config)#router ospf 1
Router(config-router)#network 0.0.0.0 255.255.255.255 area 0
```

[[Study CCNA](https://study-ccna.com/loopback-interface-loopback-address/)]
