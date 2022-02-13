## TCP Protocol Operation

**TCP operation** may be divided into three phases:

**Connection establishment** is a multi-step handshake process that establishes a connection before entering the **data transfer** phase.
After data transfer is completed, the **connection termination** closes the connection and releases all allocated resources.

A TCP connection is managed by an operating system through a resource that represents the local end-point for communications, the [Internet socket](https://en.wikipedia.org/wiki/Network_socket). During the lifetime of a TCP connection, the local end-point undergoes a series of state changes.

| State        | Endpoint         | Description                                                                                                                                                                     |
| ------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LISTEN       | Server           | Waiting for a connection request from any remote TCP end-point.                                                                                                                 |
| SYN-SENT     | Client           | Waiting for a matching connection request after having sent a connection request.                                                                                               |
| SYN-RECEIVED | Server           | Waiting for a confirming connection request acknowledgment after having both received and sent a connection request.                                                            |
| ESTABLISHED  | Server & client  | An open connection, data received can be delivered to the user. The normal state for the data transfer phase of the connection.                                                 |
| FIN-WAIT-1   | Server & client  | Waiting for a connection termination request from the remote TCP, or an acknowledgment of the connection termination request previously sent.                                   |
| FIN-WAIT-2   | Server & client  | Waiting for a connection termination request from the remote TCP.                                                                                                               |
| CLOSE-WAIT   | Server & client  | Waiting for a connection termination request from the local user.                                                                                                               |
| CLOSING      | Server & client  | Waiting for a connection termination request acknowledgment from the remote TCP.                                                                                                |
| LAST-ACK     | Server & client  | Waiting for an acknowledgment of the connection termination request previously sent to the remote TCP (which includes an acknowledgment of its connection termination request). |
| TIME-WAIT    | Server or client | Waiting for enough time to pass to be sure the remote TCP received the acknowledgment of its connection termination request.[e]                                                 |
| CLOSED       | Server & client  | No connection state at all.                                                                                                                                                     |
