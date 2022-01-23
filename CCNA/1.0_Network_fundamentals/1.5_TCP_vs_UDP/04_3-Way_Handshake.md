## 3-Way Handshake

Since **TCP** is a connection-oriented protocol, a connection needs to be established before two devices can communicate.
**TCP** uses a process called **3-way handshake** to negotiate the sequence and acknowledgement fields and start the session.

<img src="https://www.dropbox.com/s/cc54tpf66gsnul0/3-way_handshake.jpg?dl=1" alt="3-way_handshake" class="inline" />

The **3-way handshake** consists of three steps:

1. **SYN**: The client initiates the connection by sending the TCP SYN packet to the destination server.
   The packet contains a random sequence number which marks the beginning of the sequence numbers for data that the client will transit.

2. **SYN, ACK**: The server receives the packet and responds with its own sequence number.
   The response also includes the acknowledgement number, which is the client's sequence number incremented by 1.

3. **ACK**: The client acknowledges the response of the Server by sending the acknowledgement number, which is the server's sequence number incremented by one.

## Termination

After the data transmission process is finished, **TCP** will terminate the connection between the endpoints.

<img src="https://www.dropbox.com/s/0we0ehjmw3koi14/tcp_termination.jpg?dl=1" alt="termination" class="inline" />

1. **FIN**: The client application that wants to close the connection sends a **TCP** segment with the **FIN** (Finished) flag set to 1.

2. **ACK**: The server receives the TCP segment and acknowledges it with the **ACK** segment.

3. **FIN**: To terminate the connection, the server sends it's own TCP segment with the **FIN** flag set to 1 to the client.

4. **ACK**: The client acknowledges the server's FIN segment and closes the connection.
