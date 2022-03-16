# User Datagram Protocol (UDP)

**User Datagram Protocol (UDP)** provides delivery if data between application running on hosts on a TCP/IP network on **Layer 4** of the OSI Model.

**UDP** is a connectionless, unreliable protocol:
Unlike TCP, it does not sequence the data and does not care about the order in which the data segments arrive at the destination.

**UDP** uses much less network resources than TCP

- **Applications that are tolerant of the lost data** – VoIP uses UDP because if a voice packet is lost, by the time the packet would be retransmitted, too much delay would have occurred, and the voice would be unintelligible.

- **Applications that have some application mechanism to recover lost data** – Network File System (NFS) performs recovery with application layer code, so UDP us used as transport-layer protocol.
