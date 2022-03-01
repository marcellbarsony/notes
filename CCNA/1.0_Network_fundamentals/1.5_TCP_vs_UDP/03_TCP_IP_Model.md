# TCP/IP model part 1: Bits, Frames, Packets, Segments and more

| No. | OSI          | TCP/IP      |          | Examples                             | Description                                                                            |
| --- | ------------ | ----------- | -------- | ------------------------------------ | -------------------------------------------------------------------------------------- |
| 7   | Application  |             |          | HTTP, FTP, IRC, SSH, DNS             | Human-computer interaction layer, where applications access network services           |
| 6   | Presentation |             |          | SSL, TLS, SSH, IMAP, FTP, MPEG, JPEG | Ensures that data is in usable format, applies data encryption and compression         |
| 5   | Session      | Application |          | API's, Sockets, WinSock              | Maintains connections and is responsible for controlling ports and sessions            |
| 4   | Transport    | Transport   | Segments | TCP, UDP                             | Transmits data using transmission protocols (incl. TCP and UTP header)                 |
| 3   | Network      | Network     | Packets  | IP, ARP, ICMP, IPSec, IGMP           | Decides which physical path the data will take (contains src. and destination address) |
| 2   | Data Link    | Data Link   | Frames   | Ethernet, PPP, ATM, Switch, Bridge   | Defines the format of data on the network (MAC, Logical Link Control)                  |
| 1   | Physical     | Physical    | Bits     | Fiber, Wireless, Hubs, Repeaters     | Transmits raw bit stream via the hardware                                              |

[Wikipedia - Internet Protocol suite](https://en.wikipedia.org/wiki/Internet_protocol_suite)

## Bits

When **data** is sent at the **Physical layer** (Layer 1), we're sending 0s and 1s, known as **bits**.

## Frames

A **frame** is a digital **data transmission unit** in computer networking.<br> In packet switched systems, a frame is a simple container for a single network packet.

In general, the **frame** is a formatting unit resource for data that needs to be split up into recognizable pieces in order to be interpreted by a receiver.

[Wikipedia - Frame (networking)](<https://en.wikipedia.org/wiki/Frame_(networking)>)

## Packets

A **network packet** is a formatted unit of data carried by a packet-switched network.

A **packet** consists of **control information** and **user data**; the latter is also known as _payload_.<br>
**Control information** provides information for the **router** for delivering the payload (e.g. source and destination network address, error detection codes or sequencing information).

[Wikipedia - Network packet](https://en.wikipedia.org/wiki/Network_packet)

## Segments

A **network segment** is a portion of a computer network.
The nature and extent of a segment depends on the nature of the network and the device (or devices) used to interconnect end stations.

[Wikipedia - Network segment](https://en.wikipedia.org/wiki/Network_segment)

## Socket

A **socket** is the combination of

- **IP address** of a host
- **Port number** used
- **Transport protocol** used (_TCP or UDP_)
