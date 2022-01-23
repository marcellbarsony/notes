## Private IP Address

A **private network** is a computer network that uses a private address space of IP addresses.
These addresses are used for LANs in residential, office, and enterprise environments.

Private network addresses are not allocated to any specific organization.<br>
Private address spaces were originally defined in [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918) to assist in delaying IPv4 address exhaustion.

IP packets originating from or addresses to a private IP address **cannot be routed through the public internet**.
The private IP address has to be NATted to a public IP address.

[[Wikipedia - Private Network](https://en.wikipedia.org/wiki/Private_network)]

## RFC

A **Request for Comments (RFC)** is a publication series from the [Internet Engineering Task Force (IETF)](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force)
to set the principal technical development guidelines and standards for the Internet.

## Private IPv4 addresses

The IANA has reserved the following IPv4 address ranges for private networks

| RFC 1918 name | IP address range              | Number of addresses | Largest CIDR block (subnet mask) | Host ID size | Mask bits | Classful description            |
| ------------- | ----------------------------- | ------------------: | -------------------------------: | ------------ | --------- | ------------------------------- |
| 24-bit block  | 10.0.0.0    – 10.255.255.255  |          16 777 216 |           10.0.0.0/8 (255.0.0.0) | 24 bits      | 8 bits    | single class A network          |
| 20-bit block  | 172.16.0.0  – 172.31.255.255  |           1 048 576 |      172.16.0.0/12 (255.240.0.0) | 20 bits      | 12 bits   | 16 contiguous class B networks  |
| 16-bit block  | 192.168.0.0 – 192.168.255.255 |              65 536 |     192.168.0.0/16 (255.255.0.0) | 16 bits      | 16 bits   | 256 contiguous class C networks |

## RFC 1149

[IP over Avian Carriers](https://en.wikipedia.org/wiki/IP_over_Avian_Carriers) is a proposal to carry Internet Protocol traffic by birds such as homing pigeons.
**IP over Avian Carriers** was initially described in **RFC 1149** issued by the IETF, written by D. Waitzman, and released on April 1, 1990.

[[IETF - RFC 1149](https://datatracker.ietf.org/doc/html/rfc1149)]
