# DHCP Operation

**DHCP** employs a connectionless service model, using UDP.<br>
It is implemented with two UDP port numbers which are the same as for the bootstrap protocol ([BOOTP](https://en.wikipedia.org/wiki/Bootstrap_Protocol)):

- UDP Port 67 is the destination port of a server
- UDP Port 68 is used by the client

### DHCP Operation — Allocating IP addresses

Depending on implementation, the DHCP Server may have three different methods of allocating IP addresses:

1. **Dynamic allocation** — An administrator reserver a range of IP addresses for DHCP, and each DHCP client is configured to request an IP address from the DHCP server during network initialization.

2. **Automatic allocation** — The DHCP server permanently assigns an IP address to a requesting client from a range defined by an administrator.
   This is similar to dynamic allocation, byt the DHCP server keeps a table of past IP address assignments, so that it can permanently assign ato a client the smae IP address that the client previously had.

3. **Manual allocation** — An administrator maps a unique identifier (Client ID or MAC address) for each client to an IP address, which is offered to the requesting client.
   Also called as Static DHCP allocation/fixed address allocation/reservation, and MAC/IP address binding.

## DHCP Operation Phases

DHCP operations fall into four phases and IP lease acknowledgement - these stages are often abbreviated as DORA for Discovery, Offer, Request, and Acknowledgement.

1. **DHCP Server Discovery** — The **DHCP Client** sends a broadcast packet to discover DHCP server on the LAN segment.

2. **DHCP IP Lease Offer** — The **DHCP Server** receives the **DHCP Discover** packet and responds with **DHCP Offer** packets, offering IP addressing information.

3. **DHCP IP Request** — The **DHCP Client** receives the **DHCP Offer** packets from multiple DHCP servers: the first **DHCP Offer** packet is accepted.
   The **DHCP Client** responds by broadcasting a **DHCP Request** packet, requesting the network parameters from the server that responded first.

4. **DHCP IP Acknowledgement** — The **DHCP Server** approves the lease with a **DHCP Acknowledgement** packet that includes the lease duration and other configuration information.

### DHCP Discovery

The DHCP Client broadcasts a **DHCPDISCOVER** message on the network subnet using the destination address 255.255.255.255 (limited broadcast) of the specific subnet broadcast address (directed broadcast).

A DHCP Client may also request its last know IP address - if the DHCP client remains connected to the same network, the DHCP server may grant the request.
Otherwise, it depends whether the server is set up as authoritative or not:

- An **authoritative server** denies the request, causing the client to issue a new request.
- A **non-authoritative server** simply ignores the request, leading to an implementation-dependent timeout for the client to expire the request and ask for a new IP address.

### DHCP Offer

When a DHCP Server receives a **DHCPDISCOVER** message from a DHCP Client, the DHCP Server reserves an IP address for the client and makes a leas offer by sending a DHCPOFFER message to the DHCP Client.

The **DHCPOFFER** message consists of:

- **Client ID** of the DHCP Client (traditionally a MAC address)
- **IP address** that the DHCP Server is offering
- **IP address** of the DHCP Server that is making the offer
- **Subnet mask**
- **Lease duration**

The DHCP Server may also take notice of the hardware-level MAC address in the underlying transport layer: according to current RFC's, the transport layer MAC address may be used if no Client ID is provided in the DHCP packet.

The DHCP Server determines the configuration based on the client's hardware address as specified in the CHADDR (Client Hardware Address) field.

### DHCP Request

In response to the DHCP Offer, the DHCP Client replies with a **DHCPREQUEST message** broadcast to the server, requesting the offered address.

The DHCP Client will produce a gratuitous ARP in order to find if there is any other host present in the network with the same IP address.
If there's no reply by other host, then there is no host with the same IP configuration in the network and the message is broadcasted to servers showing the acceptance of the received IP address.

The DHCP Client must send the _server identification_ option in the **DHCP Request** message indicating the server whose the offer the client has selected.

### DHCP Acknowledgement

When a DHCP Server receives the **DHCPREQUEST** message from the DHCP Client, the configuration process enter its final phase.
The **DHCP Acknowledgement** phase involves sending a **DHCPACK** packet to the client that includes the lease duration and any other configuration information that the client might have requested.

The protocol expects the DHCP Client to configure its network interface with the negotiated parameters.

After the DHCP Client obtains an IP address, it should probe the newly received address (e.g with ARP) to prevent address conflicts caused by overlapping address pools of DHCP servers.
If the probe fails, the computer should send a **DHCPDECLINE** broadcast to the server.

### Information

A DHCP Client may request more information than the server sent with the original **DHCPOFFER** and also request repeat data for a particular application.

### Releasing

The DHCP Client sends a request to the DHCP Server to release the DHCP information and the DHCP Client deactivates its IP address.

### Configuration Information

A DHCP Server can provide optional configuration parameters to the client: RFC 2132 describes the available DHCP options defined by IANA - DHCP and BOOTP PARAMETERS.

A DHCP Client can select, manipulate and overwrite parameters provided by a DHCP Server.
In UNIX-like operating systems this client-level refinement typically takes place according to the values in the configuration file `/etc/dhcclient.conf`.

### DHCP Message types

| Code | Name                 | Length  | RFC                     |
| ---- | -------------------- | ------- | ----------------------- |
| 1    | DHCPDISCOVER         | 1 octet | rfc2132: Section 9.6    |
| 2    | DHCPOFFER            | 1 octet | rfc2132: Section 9.6    |
| 3    | DHCPREQUEST          | 1 octet | rfc2132: Section 9.6    |
| 4    | DHCPDECLINE          | 1 octet | rfc2132: Section 9.6    |
| 5    | DHCPACK              | 1 octet | rfc2132: Section 9.6    |
| 6    | DHCPNAK              | 1 octet | rfc2132: Section 9.6    |
| 7    | DHCPRELEASE          | 1 octet | rfc2132: Section 9.6    |
| 8    | DHCPINFORM           | 1 octet | rfc2132: Section 9.6    |
| 9    | DHCPFORCERENEW       | 1 octet | rfc3203: Section 4      |
| 10   | DHCPLEASEQUERY       | 1 octet | rfc4388: Section 6.1    |
| 11   | DHCPLEASEUNASSIGNED  | 1 octet | rfc4388: Section 6.1    |
| 12   | DHCPLEASEUNKNOWN     | 1 octet | rfc4388: Section 6.1    |
| 13   | DHCPLEASEACTIVE      | 1 octet | rfc4388: Section 6.1    |
| 14   | DHCPBULKLEASEQUERY   | 1 octet | rfc6926: Section 6.2.1  |
| 15   | DHCPLEASEQUERYDONE   | 1 octet | rfc6926: Section 6.2.1  |
| 16   | DHCPACTIVELEASEQUERY | 1 octet | rfc7724: Section 5.2.1  |
| 17   | DHCPLEASEQUERYSTATUS | 1 octet | rfc7724: Section 5.2.1  |
| 18   | DHCPTLS              | 1 octet | rfc7724: Section 5.2.1  |
