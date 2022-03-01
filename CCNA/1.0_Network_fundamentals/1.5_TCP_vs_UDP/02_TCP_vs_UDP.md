# TCP vs UDP - Differences

| X                       | TCP                                                                           | UDP                                                                                         |
| ----------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **OSI Layer**           | Transport layer (Layer 4)                                                     | Transport layer (Layer 4)                                                                   |
| **Reliability**         | Reliable                                                                      | Unreliable / Best effort                                                                    |
| **Connection type**     | Connection-oriented                                                           | Connectionless                                                                              |
| **Handshake technique** | Three-way handshake (SYN, ACK, SYN-ACK)                                       | No handshake                                                                                |
| **Transfer method**     | Data is read as a byte stream; messages are transmitted to segment boundaries | UDP packets with defined boundaries; sent individually and checked for integrity on arrival |
| **Retransmission**      | Retransmission of lost packets is possible                                    | No retransmission of lost packets                                                           |
| **Broadcasting**        | No - Does not support broadcasting                                            | Yes - Does support broadcasting                                                             |
| **Stream type**         | Byte stream                                                                   | Message stream                                                                              |
| **Error checking**      | Extensive error checking and acknowledgement of data                          | Basic error checking mechanism using checksums                                              |
| **Sequencing**          | Yes - Packets arrive in order at the receiver                                 | No                                                                                          |
| **Speed**               | Slower than UDP                                                               | Faster than TCP                                                                             |
| **Overhead**            | Low but higher than UDP                                                       | Very low                                                                                    |
| **Header length**       | 20-60 bytes variable length header                                            | 8 bytes fixed-length header                                                                 |
| **Application**         | HTTP, E-mail, FTP                                                             | Voice streaming, Video streaming                                                            |

### Connection

**TCP** is connection-oriented, while **UDP** is not.

### Reliability

**TCP** implements reliability as every successfully transmitted segment is acknowledged.

**UDP** does not implement reliability; it relies on higher layer protocols to implement reliability if required.

### Flow control

**TCP** uses end-to-end flow control to avoid sending data too quickly:<br>
If sender send data faster than receiver can handle, receiver drop data and require retransmission - retransmission is wasting time and network resources
Most flow control mechanisms try to maximize transfer rate while minimizing the requirements to retransmit.

**TCP** uses a **sliding window** to control the flow of the data.<br>
Windowing allows the receiving device to advertise how much data it's able to to receive before transmitting an ACK to the sending device.<br>
In each TCP segment, the receiver will specify in the receive window field the amount of additional receive data in bytes that it is willing to buffer for the connection.

**UDP** does not implement flow control; it relies on higher layer protocols to implement such solution.

## TCP vs UDP - Similarities

### Session multiplexing

**TCP** and **UDP** allow for **session multiplexing**.

**Session multiplexing** is when a single host with a single IP address is able to communicate with multiple servers (or multiple devices) and have mutiple session iccur simultaneously.

A session is created when a source host needs to send data or information to a destination host.
Replies are often received but not mandatory.
The session is created and controlled within the network application, which contains the functionality of OSI layers 5 through 7.

[[Session multiplexing - Wikipedia](https://en.wikipedia.org/wiki/Session_multiplexing)]
