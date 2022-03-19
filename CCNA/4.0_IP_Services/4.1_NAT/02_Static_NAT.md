# Static NAT

**Static NAT** is a one-to-one mapping of a private IP address to a public IP address.
**Static NAT** maps network traffic from a static external IP address to an internal IP address or network.
**Static NAT** creates a static translation of real addresses to mapped addresses.
**Static NAT** provides internet connectivity to networking devices through a private LAN with an unregistered private IP address.

[[Juniper - Static NAT](https://www.juniper.net/documentation/us/en/software/junos/nat/topics/topic-map/security-nat-static.html)]

**Static NAT** defines a one-to-one mapping from one IP subnet to another IP subnet.
The mapping includes destination IP address translation in one direction and source IP address translation in the reverse direction.
From the NAT device, the original destination address is the virtual host IP address while the mapped-to address is the real host IP address.

**Static NAT** allows connections to be originated from either side of the network, but translation is limited to on-to-one or between blocks of addresses of the same size.
For each private address, a public address must be allocated.
No address pools are necessary.

**Static NAT** also supports the following types of translation:

- To map multiple IP addresses and specified ranges of ports to a same IP address and different range of ports
- To map a specific IP address and port to a different IP address and port

The port address translation (PAT) is also supported by giving static mapping between destination-port (range) and mapped-port (range).

> Note<br>
> The original destination address, along with other addresses in source and destination NAT pools, must not overlap within the same routing instance.

## Static NAT Rules

**Static NAT** rules specify two layers of match conditions:

- **Traffic Direction** — Allows to specify **from interface**, **from zone**, or **from routing-instance**.
- **Packet Information** — Can be source addresses and ports, and destination addresses and ports.

## Static NAT Configuration Overview

The main configuration tasks for **Static NAT** are as follows:

1. Configure private/public address mapping with the `ip nat inside source static <private_ip> <public_ip>` command.
2. Configure the router's inside interface using the `ip nat inside` command.
3. Configure the router's outside interface using the `ip nat outside` command.

The NAT table can be viewed with the `ip nat translations` command.
