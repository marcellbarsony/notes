# Port numbers

In computer networking, a **port** is a software-based virtual communication endpoint. Specific port numbers are reserved to identify specific process or service.

Port numbers are assigned in various ways, based on three ranges:

- System Ports (0-1023)
- User Ports (1024-49151)
- Dynamic and/or Private Ports (49152-65535)

The [IANA - Internet Assigned Numbers Authority](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml) is responsible for maintaining the official assignments of port numbers for specific uses.

Service names and port numbers are used to distinguish between different
services that run over transport protocols such as TCP, UDP, DCCP, and SCTP.

[Wikipedia - TCP and UDP port numbers](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)

## Ephemeral port

An **ephemeral port** is a short-lived transport protocol port for IP communications.

**Ephemeral ports** are allocated automatically from a predefined range by the IP stack software.

An **ephemeral port** (random) is typically used as the port assignment for the **client end** of a client-server communication.
A **server service will listen** on a **well-known port** number.

### Ephemeral range

RFC 6056 says that the range should be 1024-65535.

IANA and RFC 6335 suggests the range 49152-65535 for dynamic or private ports.

- Linux: 32768-60999
- BSD: 1024-5000
- Solaris OS: 32768-65538
- Windows: IANA range - since Windows 2000 a custom range can be used anywhere within 1025-65535

[Wikipedia - Ephemeral ports](https://en.wikipedia.org/wiki/Ephemeral_port)
