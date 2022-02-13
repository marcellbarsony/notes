## 3-Way Handshake

Since **TCP** is a connection-oriented protocol, a connection needs to be established before two devices can communicate.
**TCP** uses a process called **3-way handshake** to negotiate the sequence and acknowledgement fields and start the session.

<img src="https://www.dropbox.com/s/cc54tpf66gsnul0/3-way_handshake.jpg?dl=1" alt="3-way_handshake" class="inline" />

The **3-way handshake** consists of three steps:

1. **SYN**: The client initiates the connection by sending the TCP SYN packet to the destination server.<br>
   The host initiating the session will set the SYN flag (or SYN bit) in the TCP header.
   The packet contains a random sequence number which marks the beginning of the sequence numbers for data that the client will transit.<br>

2. **SYN, ACK**: The server receives the packet and responds with its own sequence number (SEQ) to indicate the next sequence number of the next byte of data it expects to receive from the host.<br>
   The response also includes the acknowledgement number (ACK), which is the client's sequence number incremented by 1.
   This flag indicates the next portion of data the server expect to receive.<br>

3. **ACK**: The client acknowledges the response of the Server by sending the acknowledgement number, which is the server's sequence number incremented by one.

   The unset SYN flag confirms that the tree-way handshake has completed successfully.

### TCP Seq and Ack numbers

TCP is a byte-oriented sequencing protocol.<br>
**TCP Sequence Number** is a 4-byte long field in the TCP header that indicates the first byte of the outgoing segment.
The **TCP Sequence Number** field is necessary to ensure that missing or misordered packets can be detected and fixed.

The **Sequence Number field** is always set, even when there is no data in the segment.

The **TCP Sequence Number** is sent by the **TCP Client**, indicating how much data has been sent for the session (byte-order number).

The **ACK Sequence Number** is sent by the **TCP Server**, indicating that it has received cumulated data and is ready for the next segment.

<details>
<summary>Example - Diagram</summary>
<br>

For example, the sequence number for this packet is X.
The length for this packet is Y.<br>
If this packet is transferred to another side successfully, then the sequence number for the next packet is X+Y.
The sequence number is the first byte of the outgoing segment.

The picture shows a real example of TCP SEQ and ACK numbers in a TCP flow diagram.
The key variable is a the TCP segment length for each TCP segment sent in the session.

<img src="https://www.dropbox.com/s/gpfwieorwfmytx4/tcp_sequence_number.png?dl=1" alt="tcp_seq_ack_flow" class="inline" />

The client sends the first segment with SEQ=1 and the length of the segment is 669 bytes.<br>
The server responds with an ACK=670, which tells the client that the next expected segment will have a sequence number of 670.

In the next segment, the client sends SEQ=670 and the length now is 1460 bytes.<br>
In return, the server responds with ACK=2130 (670 + 1460).<br>
This cycle continues until the end of the TCP session.

</details>

<details>
<summary>Example - Wireshark</summary>
<br>

By default, **Wireshark** converts all SEQ and ACK numbers to relative numbers.
This means, that all SEQ and ACK numbers always start at 0 for the first packet seen in each conversation.

1. Client sends SEQ = 1, and the TCP segment length is 669 bytes.

<img src="https://www.dropbox.com/s/s1g64zxbyg6qljc/tcp_seq_wireshark_1.png?dl=1" alt="tcp_seq_wireshark_1" class="inline" />

2. Server responds with ACK = 670 (SEQ + Length).

<img src="https://www.dropbox.com/s/6cq1nu7eamd67vy/tcp_seq_wireshark_2.png?dl=1" alt="tcp_seq_wireshark_2" class="inline" />

3. Client sends segment with SEQ = 670 (ACK), and the segment length is 1460 bytes.

<img src="https://www.dropbox.com/s/imbc5xts2cxj1m9/tcp_seq_wireshark_3.png?dl=1" alt="tcp_seq_wireshark_3" class="inline" />

4. Server responds with ACK = 2130 (SEQ + Length).

<img src="https://www.dropbox.com/s/1p60recwrgpvjlg/tcp_seq_wireshark_4.png?dl=1" alt="tcp_seq_wireshark_4" class="inline" />

</details>

## Termination (4-way handshake)

After the data transmission process is finished, **TCP** will terminate the connection between the endpoints.

<img src="https://www.dropbox.com/s/0we0ehjmw3koi14/tcp_termination.jpg?dl=1" alt="termination" class="inline" />

1. **FIN**: The client application that wants to close the connection sends a **TCP** segment with the **FIN** (Finished) flag set to 1.

2. **ACK**: The server receives the TCP segment and acknowledges it with the **ACK** segment.

3. **FIN**: To terminate the connection, the server sends it's own TCP segment with the **FIN** flag set to 1 to the client.

4. **ACK**: The client acknowledges the server's FIN segment and closes the connection.
