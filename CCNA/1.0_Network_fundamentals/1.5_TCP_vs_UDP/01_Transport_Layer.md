# Transport Layer (Layer 4)

**Transport Layer** is responsible for end-to-end communication over the network and provides service to upper-layer protocols (Application layer).
Simply, it is responsible for tracking the conversations (raw data) between multiple applications that are passing through the network.

> NOTE<br>
> Transport Layer provides the logical communication between applications that runs on different hosts by simply adding a transport header on the raw data.
> The Protocol Data Unit (PDU) is now called a **Segment**.

Networking devices have limitation on the amoun of data that can be inserted in an IP packet.
Because of that, the **Transport Layer** segments (sender) and reasssemble (receiver) the data between the sender and the receiver.

The role of the Transport Layer is to ensure that the data is transmitted and delivered to the intended application.
If a different protocol is received on a specific application, the application will drop the data.

## Transport Layer Protocols - TCP & UDP

The commonly used Transport Layer protocols responsible for message delivery are **TCP** and **UDP**.

Under the TCP and UDP are port number that are used to distinguish the specific type of application.
A specific port number is attached when sending the data so that the data will be received exactly by the intended application.

The below diagram shows a segment in which the raw data is encapsulated by transport header (source and destianation port).

<img src="https://www.dropbox.com/s/tktcizp4nnqrti3/transport_header.jpg?dl=1" alt="network" class="inline" />

[[Study CCNA](https://study-ccna.com/transport-layer/)]
