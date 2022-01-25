## IP address

An **Internet Protocol (IP)** address is a numerical label on **layer 3** that is used to identify and locate a network interface of a computer or a network node.

IP addresses are included in the [packet header](https://en.wikipedia.org/wiki/IPv6_packet#Fixed_header) to indicate the source and the destination.

Two main functions:

- Network interface identification
- Location addressing

**IPv4** defines an IP address as a 32-bit number number in the [address space](https://en.wikipedia.org/wiki/Address_space) - _2^32^ = 4,294,967,296 possible addresses_.

**IPv4** addresses are usually represented in dot-decimal notation, consisting 4 decimal numbers, each ranging from 0 to 255, separated by dots. Each part represents a group of 8 bits (an octet).

The IP address space is managed globally by [IANA](https://www.iana.org/), and by five regional Internet registers ([RIRs](https://en.wikipedia.org/wiki/Regional_Internet_registry)) responsible in their designated territories for assignment to local Internet registries, such as ISPs and other end users.

| Format         | 1<sup>st</sup> octet | 2<sup>nd</sup> octet | 3<sup>rd</sup> octet | 4<sup>th</sup> octet |
| -------------- | -------------------: | -------------------: | -------------------: | -------------------: |
| Dotted Decimal |                  10. |                 129. |                  16. |                  123 |
| Binary         |            00001010. |            10000001. |            00010000. |             01111011 |

| Base ^ Exponent | 2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Binary          | 0   | 0   | 0   | 0   | 1   | 0   | 1   | 0   |
| Decimal         | 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |

[Wikipedia - IP address](https://en.wikipedia.org/wiki/IP_address)

## Static vs. Dynamic

Network administrators assign (statically or dynamically) an IP address to each device connected to a network.

- **Static** – Static IP address is set manually on the device.
  It is best practice to set static IP addresses on network devices, such as routers, switches and servers.

- **Dynamic** – Dynamic IP address can be automatically allocated to a device via DHCP.
  Dynamic IP addresses are best to be used on end devices.

## Public vs. Private

- **Public** – Used to route Internet traffic.
  This is given out by ISPs to their customers.

- **Private** – Used in private networks for internal traffics within the LAN.
  Private addresses are not routable on the Internet.

## Subnetworks

IP network may be divided into [subnetworks](https://en.wikipedia.org/wiki/Subnetwork) in both IPv4 and IPv6.

An IP address is recognized as consisting of two parts:

- The **network prefix** in the high-order bits
- and the **rest field**, **host-identifier**, or **interface identifier** (IPv6)

The **subnet mask** or [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation) determines how the IP address is divided into network and host parts.

The term **subnet mask** is only used for IPv4.
Both IP versions however use the CIDR concept and notation.

The IP address is followed by a slash and the number (in decimal) of bits used for the network part (routing prefix).

Example:

An IPv4 address and its subnet mask may be 192.0.2.1 and 255.255.255.0, respectively.
The CIDR notation for the IP address and the subnet is 192.0.2.1/24, because the first 24 bits of the IP address indicate the network and the subnet.
