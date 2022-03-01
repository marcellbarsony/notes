# TCP

**Transmission Control Protocol (TCP)** is one of the main protocols of the [internet protocol suite](https://en.wikipedia.org/wiki/Internet_protocol_suite).<br>
**TCP** provides reliable, ordered and error-checked delivery of a stream of octets (bytes) between applications running on hosts on a TCP/IP network.

**TCP** is [connection-oriented](https://en.wikipedia.org/wiki/Connection-oriented_communication): a connection between two hosts must be established before data is sent.
The process used to establish a TCP connection is known as a **three-way handshake**.
Data transfer phase begins after the connection has been established, and terminates after the data is transmitted.

**TCP** uses sequence numbers to identify the order of the bytes sent from each computer.
The data then can be reconstructed in order at its destination.
The sender can also retransmit the data if it is lost during the transmission.

**TCP** is considered to be complicated and costly in terms of network usage, due to its characteristics.

**TCP** example vulnerabilities:

- [Denial of service](https://en.wikipedia.org/wiki/Denial-of-service_attack)
- [Connection hijacking](https://en.wikipedia.org/wiki/TCP_sequence_prediction_attack)
- TCP veto
- [TCP reset attack](https://en.wikipedia.org/wiki/TCP_reset_attack)

[[Study CCNA](https://study-ccna.com/tcp-explained/)]
