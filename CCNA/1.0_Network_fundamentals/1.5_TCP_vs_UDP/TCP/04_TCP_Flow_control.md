## TCP Flow Control

**TCP Flow Control** uses a system of buffers and variables to determine how quickly data can be transmitted.<br>
The underlying concept is that a receiving end system is able to notify the sending end system that its application is unable to keep up with the transmission rate.
TCP's flow control mechanisms leverage the dynamics of these buffers to create a **speed matching service**.

The throughput of a TCP communication is limited by two windows:

- Receive window
- [Congestion window (CWND)](https://en.wikipedia.org/wiki/TCP_congestion_control#Congestion_window)

[[Alpharithms - TCP flow control](https://www.alpharithms.com/tcp-flow-control-515714)]
[IBM - TCP flow control](https://www.ibm.com/docs/en/tsm/7.1.0?topic=tuning-tcp-flow-control-sliding-window)
[[Wikipedia - Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)]

## Sliding window

TCP uses a **sliding window** for flow control.

The **window size** is the amount of data that can be managed.<br>
The **window size** might need to be adjusted if the receive buffer receives more data that it can communicate.

**TCP sliding window** determines the number of unacknowledged bytes, x, that one system can send to another.<br>
Two factors determine the value of x:

- **Sending system**: size of the send buffer
- **Receiving system**: size and available space in the receive buffer<br>

[[Wikipedia - TCP window scale option](https://en.wikipedia.org/wiki/TCP_window_scale_option)]

### Sending system buffer

The **sending system** cannot send more bytes that space that is available in he receive buffer on the receiving system.<br>
TCP on the sending system must wait to send more data until all bytes in the current send buffer are acknowledged by TCP on the receiving system.

TCP’s Flow Control is maintained by a variable, on the sender side, called the **receive window**.<br>
This value tracks the amount of space lef in the buffer on the receiver side after the existing data is accounted for.

The formula for calculating the receive window is:

```
rwnd = receiveBuffer - (lastByteReceived - LastByteRead)
```

<img src="https://www.dropbox.com/s/w0wokinx3g3xy47/receive_window.jpg?dl=1" alt="receive_window" class="inline" />

The `receive window` variable is constantly updated and reported to the sending system via the window segment of the TCP header.

If the receive buffer is full, the receiver sends a `receiveWindow = 0` notice to the sender;<br>
This created a problem once the the receiver's application has consumed the remaining buffer data; there's nothing left to send back to the initial sender in therms of ACKS's.
This would effectively transition the sender to an indefinite state of waiting.

To get around this issue, TCP makes explicit consideration by asking the sender to continue to send a single bit of data to the receiver.
This minimizes strain on the network while also maintaining a constant check on the status of the receiving buffer.

### Receiving system buffer

On the receiving system, TCP stores received data in a **receive buffer**.<br>
If data placed into the buffer has been deemed valid and in-sequence by TCP's reliable data transfer services (RDT), then TCP acknowledges receipt of the data, and advertises a new receive window to the sending system.

If the **receive buffer is full**, the receiving system advertises a receive window size of zero (`receiveWindow = 0`), and the sending system must wait to send more data.
After the receiving application retrieves data from the receive buffer, the receiving system can then advertise a receive window size that is equal to the amount of data that was read.

The **available space in the receive buffer** depends on how quickly the receiving application can read data from the buffer.

When the receiving application reads data as fast as the sending system can send it, the receive window stays at or near the size of the receive buffer.
The result is that data flow smoothly across the network.

## Network Congestion

**[Network congestion](https://en.wikipedia.org/wiki/Network_congestion)** in data networking and queueing theory is the reduced [quality of service](https://en.wikipedia.org/wiki/Quality_of_service) that occurs when a network node or link is carrying more data then it can handle.
Typical effects include: queuing, packet loss or the blocking of new connections.

Networks use **congestion control** and **congestion avoidance** techniques to try to avoid collapse.

**Congestion control** modulates traffic entry into a telecommunication network in order to avoid congestive collapse resulting from oversubscription.
This is typically accomplished by reducing the rate of packets.
Whereas **congestion control** prevents senders from overwhelming the network, **flow control** prevents the sender from overwhelming the receiver.

**Congestive collapse** is the condition in which congestion prevents or limits useful communication.<br>
**Congestion collapse** generally occurs at choke point in the network, where incoming traffic exceeds outgoing bandwidth.
Connection point between a LAN and a WAN are common choke points.
When a network is in this condition, it settles into a stable state where traffic demand is high but little useful throughput is available, during which packet delay and loss occur, and quality of service is extremely poor.

**Congestion window (CWD)** is one of the factors that determines the number of bytes that can be sent out at any time.
The **congestion window** is maintained by the sender and its purpose is to prevent the _network link_ between the sender and the receiver from being overloaded.
The **congestion window** is calculated by estimating how much congestion there is on the link.

### TCP congestion policy

TCP uses a **congestion policy** and a **congestion window** to avoid congestion.

- **Slow Start**: Initially, set to a low value and incremented exponentially to the threshold.
- **Congestion Avoidance**: After reaching the threshold increment is by 1.
- **Congestion Detection**: Sender goes back to Slow Start phase or Congestion Avoidance phase.

Congestion Avoidance

**[Weighted Random Early Detection (WRED)](https://en.wikipedia.org/wiki/Weighted_random_early_detection)** is a queueing discipling for a [network scheduler](https://en.wikipedia.org/wiki/Network_scheduler) suited for [congestion avoidance](https://en.wikipedia.org/wiki/Network_congestion_avoidance).
It is an extension to [random early detection (RED)](https://en.wikipedia.org/wiki/Random_early_detection) where a single queue may have several different sets of queue thresholds.
Each threshold set is associated to a particular [traffic class](https://en.wikipedia.org/wiki/Traffic_shaping#Traffic_classification).

On CISCO switches, **WRED** is restricted to TCP/IP traffic.
Only this kind of traffic indicates congestion to the sender to enable a reduction of the transmission rate.

### Quality of Service

**Quality of Service (QoS)** is the description or measurement of the overall performance of a service, such as a telephony, computer network or a cloud computing service.

In computer networking and packet-switched telecommunications network, **quality of service** refers to traffic prioritization and resource reservation control mechanisms.

**Quality of service** consists of the measurement of:

- [Packet loss](https://en.wikipedia.org/wiki/Packet_loss)
- [Bit rate](https://en.wikipedia.org/wiki/Bit_rate)
- [Throughput](https://en.wikipedia.org/wiki/Throughput)
- [Transmission delay](https://en.wikipedia.org/wiki/Transmission_delay)
- [Availability](https://en.wikipedia.org/wiki/Availability)
- [Jitter](https://en.wikipedia.org/wiki/Jitter)
- etc.
