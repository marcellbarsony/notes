# IP Classes

A **classful network** is a [network addressing](https://en.wikipedia.org/wiki/Network_address) architecture used in the Internet from 1981 until the introduction of **[CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing "Classless Inter-Domain Routing")** in 1993.

**IPv4** address classes are replaced with [CIDR](https://study-ccna.com/cidr-classless-inter-domain-routing/).<br>
**IPv6** does not use address classes.

## Classes

| Class   | Traffic   | Leading bits |         Number of networks |       Addresses per network |       Total addresses in class | Start address | End address     | Default subnet mask | CIDR notation |
| ------- | --------- | ------------ | -------------------------: | --------------------------: | -----------------------------: | ------------- | --------------- | ------------------- | ------------- |
| Class A | Unicast   | 0            |        128 (2<sup>2</sup>) | 16,777,216 (2<sup>24</sup>) | 2,147,483,648 (2<sup>31</sup>) | 0.0.0.0       | 127.255.255.255 | 255.0.0.0           | /8            |
| Class B | Unicast   | 10           |    16,384 (2<sup>14</sup>) |     65,536 (2<sup>16</sup>) | 1,073,741,824 (2<sup>30</sup>) | 128.0.0.0     | 191.255.255.255 | 255.255.0.0         | /16           |
| Class C | Unicast   | 110          | 2,097,152 (2<sup>21</sup>) |         256 (2<sup>8</sup>) |   536,870,912 (2<sup>29</sup>) | 192.0.0.0     | 223.255.255.255 | 255.255.255.0       | /24           |
| Class D | Multicast | 1110         |                not defined |                 not defined |   268,435,456 (2<sup>28</sup>) | 224.0.0.0     | 239.255.255.255 | not defined         | not defined   |
| Class E | Reserved  | 1111         |                not defined |                 not defined |   268,435,456 (2<sup>28</sup>) | 224.0.0.0     | 255.255.255.255 | not defined         | not defined   |

**Classes A**, **B**, and **C** provide **unicast** addresses for networks of three different network sizes.<br>
**Class D** is for **multicast** networking and the **class E** address range is **reserved** for future or experimental purposes.

## Bit-wise representation

- _n_ indicates a bit used for the **network ID**.
- _H_ indicates a bit used for the **host ID**.
- _X_ indicates a bit without a specified purpose.

### Class A

```cmd
  0.  0.  0.  0 = 00000000.00000000.00000000.00000000
127.255.255.255 = 01111111.11111111.11111111.11111111
                  0nnnnnnn.HHHHHHHH.HHHHHHHH.HHHHHHHH
```

### Class B

```cmd
128.  0.  0.  0 = 10000000.00000000.00000000.00000000
191.255.255.255 = 10111111.11111111.11111111.11111111
                  10nnnnnn.nnnnnnnn.HHHHHHHH.HHHHHHHH
```

### Class C

```cmd
192.  0.  0.  0 = 11000000.00000000.00000000.00000000
223.255.255.255 = 11011111.11111111.11111111.11111111
                  110nnnnn.nnnnnnnn.nnnnnnnn.HHHHHHHH
```

### Class D

```cmd
224.  0.  0.  0 = 11100000.00000000.00000000.00000000
239.255.255.255 = 11101111.11111111.11111111.11111111
                  1110XXXX.XXXXXXXX.XXXXXXXX.XXXXXXXX
```

### Class E

```cmd
240.  0.  0.  0 = 11110000.00000000.00000000.00000000
255.255.255.255 = 11111111.11111111.11111111.11111111
                  1111XXXX.XXXXXXXX.XXXXXXXX.XXXXXXXX
```

The number of addresses usable for addressing specific hosts in each network is always 2<sup>N</sup> - 2, where N is the number of rest field bits, and the subtraction of 2 adjusts for the use of the all-bits-zero host value to represent the network address and the all-bits-one host value for use as a broadcast address.
Thus, for a Class C address with 8 bits available in the host field, the maximum number of hosts is 254.

Today, IP addresses are associated with a subnet mask.
This was not required in a classful network because the mask was implied by the address itself;
any network device would inspect the first few bits of the IP address to determine the class of the address and thus its netmask.

The blocks numerically at the start and end of classes A, B and C were originally reserved for special addressing or future features, i.e., 0.0.0.0/8 and 127.0.0.0/8 are reserved in former class A;
128.0.0.0/16 and 191.255.0.0/16 were reserved in former class B but are now available for assignment;
192.0.0.0/24 and 223.255.255.0/24 are reserved in former class C.

Class D is reserved for multicast and cannot be used for regular unicast traffic.
Class E is reserved and cannot be used on the public Internet.

## Special Addresses

Although reserved, special addresses are still part of the address group.

[[Wikipedia - List of assigned /8 IPv4 address blocks](https://en.wikipedia.org/wiki/List_of_assigned_/8_IPv4_address_blocks)]

### Class A

- **Default network**: 0.1.1.1 through 0.255.255.255

- **[Loopback addresses](https://en.wikipedia.org/wiki/Localhost)**: 127.0.0.1 through 127.255.255.255

### Class D

- **OSPF [Multicast address](https://en.wikipedia.org/wiki/Multicast_address)**: 224.0.0.5 and 224.0.0.6

### Class E

- **IPv4 [Broadcast address](https://en.wikipedia.org/wiki/Broadcast_address)**: 255.255.255.255
