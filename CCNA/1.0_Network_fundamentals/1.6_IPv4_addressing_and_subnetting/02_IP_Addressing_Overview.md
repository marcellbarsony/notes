## IP Addressing Overview

IPv4 addresses are 32-bit integers which will be expressed in decimal notation. (e.g.: 192.0.2.126)

<details>
<summary>Characteristics</summary><br>

- IPv4 could be a 32-Bit IP Address.
- IPv4 could be a numeric address, and its bits are separated by a dot.
- The number of header fields is twelve and the length of the header field is twenty.
- It has Unicast, broadcast, and multicast style of addresses.
- IPv4 supports VLSM (Virtual Length Subnet Mask).
- IPv4 uses the Post Address Resolution Protocol to map to the MAC address.
- RIP may be a routing protocol supported by the routed daemon.
- Networks ought to be designed either manually or with DHCP.
- Packet fragmentation permits from routers and causing host.

[[Geeksforgeeks](https://www.geeksforgeeks.org/what-is-ipv4/)]

</details>

<details>
<summary>IPv4 Advantages</summary><br>

- IPv4 security permits encryption to keep up privacy and security.
- IPV4 network allocation is significant and presently has quite 85000 practical routers.
- It becomes easy to attach multiple devices across an outsized network while not NAT.
- This is a model of communication so provides quality service also as economical knowledge transfer.
- IPV4 addresses are redefined and permit flawless encoding.
- Routing is a lot of scalable and economical as a result of addressing is collective more effectively.
- Data communication across the network becomes a lot of specific in multicast organizations.
- Limits net growth for existing users and hinders the use of the net for brand new users.
- Internet Routing is inefficient in IPv4.
- IPv4 has high System Management prices and it’s labor-intensive, complex, slow & frequent to errors.
- Security features are nonobligatory.
- Difficult to feature support for future desires as a result of adding it on is extremely high overhead since it hinders the flexibility to attach everything over IP.

[[Geeksforgeeks](https://www.geeksforgeeks.org/what-is-ipv4/)]

</details>

## IPv4 Parts

### Network (Network ID)

The network part conjointly **identifies the category of the network** that’s assigned.

Routers maintain **routing tables** that contain network addresses: routers will look at the destination IP address of a packet and match that to a network address in their routing table.

The network part indicates the distinctive variety that’s appointed to the network.

### Host

The host part uniquely **identifies an endpoint** on a network. This part of the IPv4 address is assigned to every host.

For each host on the network, the network part is the same, however, the host half must vary.

### Subnet

This is the nonobligatory part of IPv4. Local networks that have massive numbers of hosts are divided into subnets and subnet numbers are appointed to that.

## Connectionless

IPv^4^ is a connectionless protocol, meaning there are no sessions formed when the traffic is transmitted. The transmitter simply sends data without notification to the receiver. No status information is sent back from the receiver to the transmitter. IPv4 does not have data recovery features - it relies on higher layer protocols (eg. TCP) to handle dropped, corrupted, misdirected, etc.

Each packet is treated independently from other packets - traffic may take different path based on:

- Load balancing
- Bandwidth (OSPF - Open Shortest Path First)
- Hop count (RIP - Routing Information Protocol)

## TCP is connection-oriented

TCP IP will set up a session before the transmission takes place. In TCP IP, the transmitter initiates a 3-way handshake (SYN, SYN ACK, ACK) with the receiver.
