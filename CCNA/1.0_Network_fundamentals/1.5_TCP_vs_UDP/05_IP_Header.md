# IP Packet

An **IP packet** consists of a header section and a data section.
An **IP packet** has no data checksum or any other footer after the data section.

## Header

**IP header** is a prefix to an IP packet that contains information about the IP version, length of the packet, source and destination IP addresses, etc.

The **IPv4 packet header** consists of 14 fields, of which 13 are required.
The 14th field is optional (aptly named).

<img src="https://www.dropbox.com/s/ga8976h75me1d7z/ip_header.jpg?dl=1" alt="ip_header" class="inline" />

### Version

The first header field in an IP packet is the four-bit version field.
For IPv4 it is always equal to 4.

### Internet Header Length (IHL)

The IPv4 header is variable in size due to the optional 14th field.
The IHL field contains the size of the IPv4 header:
it has 4 bits that specify the number of 32-bit words in the header.

- The **minimum value** is 5:<br>
  It indicates a length of 5 x 32 bits = 160 bits = 20 bytes.

- The **maximum value** is 15:<br>
  The maximum size of a IPv4 header is 15 x 32 bits = 480 bits = 60 bytes.

### Differentiated Services Code Point (DSCP)

Originally defined as the type of service (ToS), this field specifies differentiated services (DiffServ) per RFC 2474.
Real-time data streaming makes use of the DSCP field.
An example is Voice over IP (VoIP), which is used for interactive voice services.

### Explicit Congestion Notification (ECN)

This field is defined in RFC 3168 and allows end-to-end notification of network congestion without dropping packets.
ECN is an optional feature available when both endpoints support it and effective when also supported by the underlying network.

### Total Length

This 16-bit field defines the entire packet size in bytes, including header and data.
The minimum size is 20 bytes (header without data) and the maximum is 65,535 bytes.
All hosts are required to be able to reassemble datagrams of size up to 576 bytes, but most modern hosts handle much larger packets.
Links may impose further restrictions on the packet size, in which case datagrams must be fragmented.
Fragmentation in IPv4 is performed in either the sending host or in routers.
Reassembly is performed at the receiving host.

### Identification

This field is an identification field and is primarily used for uniquely identifying the group of fragments of a single IP datagram.
Some experimental work has suggested using the ID field for other purposes, such as for adding packet-tracing information to help trace datagrams with spoofed source addresses, but RFC 6864 now prohibits any such use.

### Flags

A three-bit field follows and is used to control or identify fragments.<br>
They are (in order, from most significant to least significant):

- bit 0: Reserved; must be zero.
- bit 1: Don't Fragment (DF)
- bit 2: More Fragments (MF)

If the DF flag is set, and fragmentation is required to route the packet, then the packet is dropped.
This can be used when sending packets to a host that does not have resources to perform reassembly of fragments.
It can also be used for path MTU discovery, either automatically by the host IP software, or manually using diagnostic tools such as ping or traceroute.

For unfragmented packets, the MF flag is cleared.
For fragmented packets, all fragments except the last have the MF flag set.
The last fragment has a non-zero Fragment Offset field, differentiating it from an unfragmented packet.

### Fragment offset

This field specifies the offset of a particular fragment relative to the beginning of the original unfragmented IP datagram in units of eight-byte blocks.
The first fragment has an offset of zero.
The 13 bit field allows a maximum offset of (213 – 1) × 8 = 65,528 bytes, which, with the header length included (65,528 + 20 = 65,548 bytes), supports fragmentation of packets exceeding the maximum IP length of 65,535 bytes.

### Time to live (TTL)

An eight-bit time to live field limits a datagram's lifetime to prevent network failure in the event of a routing loop.
It is specified in seconds, but time intervals less than 1 second are rounded up to 1.
In practice, the field is used as a hop count—when the datagram arrives at a router, the router decrements the TTL field by one.
When the TTL field hits zero, the router discards the packet and typically sends an ICMP time exceeded message to the sender.
The program traceroute sends messages with adjusted TTL values and uses these ICMP time exceeded messages to identify the routers traversed by packets from the source to the destination.

### Protocol

This field defines the protocol used in the data portion of the IP datagram.
IANA maintains a list of IP protocol numbers as directed by RFC 790.

### Header checksum

The 16-bit IPv4 header checksum field is used for error-checking of the header.

When a packet arrives at a router, the router calculates the checksum of the header and compares it to the checksum field.
If the values do not match, the router discards the packet.
Errors in the data field must be handled by the encapsulated protocol.
Both UDP and TCP have separate checksums that apply to their data.
When a packet arrives at a router, the router decreases the TTL field in the header.
Consequently, the router must calculate a new header checksum.

### Source address

This field is the IPv4 address of the sender of the packet.
This address may be changed in transit by a network address translation device.

### Destination address

This field is the IPv4 address of the receiver of the packet.
As with the source address, this may be changed in transit by a network address translation device.

### Options

The options field is not often used. Packets containing some options may be considered as dangerous by some routers and be blocked.
Note that the value in the IHL field must include enough extra 32-bit words to hold all the options plus any padding needed to ensure that the header contains an integer number of 32-bit words.
If IHL is greater than 5 (i.e., it is from 6 to 15) it means that the options field is present and must be considered.
The list of options may be terminated with an EOOL (End of Options List, 0x00) option;
this is only necessary if the end of the options would not otherwise coincide with the end of the header.
The possible options that can be put in the header are as follows:

| Field         | Size (bits) | Description                                                                                                         |
| ------------- | ----------- | ------------------------------------------------------------------------------------------------------------------- |
| Copied        | 1           | Set to 1 if the options need to be copied into all fragments of a fragmented packet.                                |
| Option Class  | 2           | A general options category. 0 is for control options, and 2 is for debugging and measurement. 1 and 3 are reserved. |
| Option Number | 5           | Specifies an option                                                                                                 |
| Option Length | 8           | Indicates the size of the entire option (including this field). This field may not exist for simple options.        |
| Option Data   | Variable    | Option-specific data. This field may not exist for simple options.                                                  |

The table below shows the defined options for IPv4.
The Option Type column is derived from the Copied, Option Class, and Option Number bits as defined above.

| Option Type (dec / hex) | Option Name | Description                   |
| :---------------------: | :---------: | ----------------------------- |
|        0 / 0x00         |    EOOL     | End of Option List            |
|        1 / 0x01         |     NOP     | No Operation                  |
|        2 / 0x02         |     SEC     | Security (defunct)            |
|        7 / 0x07         |     RR      | Record Route                  |
|        10 / 0x0A        |     ZSU     | Experimental Measurement      |
|        11 / 0x0B        |    MTUP     | MTU Probe                     |
|        12 / 0x0C        |    MTUR     | MTU Reply                     |
|        15 / 0x0F        |   ENCODE    | ENCODE                        |
|        25 / 0x19        |     QS      | Quick-Start                   |
|        30 / 0x1E        |     EXP     | RFC3692-style Experiment      |
|        68 / 0x44        |     TS      | Time Stamp                    |
|        82 / 0x52        |     TR      | Traceroute                    |
|        94 / 0x5E        |     EXP     | RFC3692-style Experiment      |
|       130 / 0x82        |     SEC     | Security (RIPSO)              |
|       131 / 0x83        |     LSR     | Loose Source Route            |
|       133 / 0x85        |    E-SEC    | Extended Security (RIPSO)     |
|       134 / 0x86        |    CIPSO    | Commercial IP Security Option |
|       136 / 0x88        |     SID     | Stream ID                     |
|       137 / 0x89        |     SSR     | Strict Source Route           |
|       142 / 0x8E        |    VISA     | Experimental Access Control   |
|       144 / 0x90        |    IMITD    | IMI Traffic Descriptor        |
|       145 / 0x91        |     EIP     | Extended Internet Protocol    |
|       147 / 0x93        |   ADDEXT    | Address Extension             |
|       148 / 0x94        |   RTRALT    | Router Alert                  |
|       149 / 0x95        |     SDB     | Selective Directed Broadcast  |
|       151 / 0x97        |     DPS     | Dynamic Packet State          |
|       152 / 0x98        |     UMP     | Upstream Multicast Pkt.       |
|       158 / 0x9E        |     EXP     | RFC3692-style Experiment      |
|       205 / 0xCD        |    FINN     | Experimental Flow Control     |
|       222 / 0xDE        |     EXP     | RFC3692-style Experiment      |

## Data

the packet payload is not included in the checksum.
Its contents are interpreted based on the value of the Protocol header field.

[List of IP protocol numbers](https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers) contains a complete list of payload protocol types.

Some of th common payload protocols include:

| Protocol No. | Protocol Name                        | Abbreviation |
| ------------ | ------------------------------------ | ------------ |
| 1            | Internet Control Message Protocol    | ICMP         |
| 2            | Internet Group Management Protocol   | IGMP         |
| 6            | Transmission Control Protocol        | TCP          |
| 17           | User Datagram Protocol               | UDP          |
| 41           | IPv6 encapsulation                   | ENCAP        |
| 89           | Open Shortest Path First             | OSPF         |
| 132          | Stream Control Transmission Protocol | SCTP         |

[[Wikipedia - IPv4](https://en.wikipedia.org/wiki/IPv4)]

[[Study CCNA](https://study-ccna.com/ip-header/)]
