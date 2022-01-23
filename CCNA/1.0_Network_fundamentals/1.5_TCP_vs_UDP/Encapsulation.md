## Encapsulation

**Encapsulation** is used to describe a process of adding headers and trailers around some data.<br>

Example with the 4-layer TCP/IP model

1. **Application layer** – The e-mail is sent from the Application layer to the Transport layer.
2. **Transport layer** – The Transport layer encapsulates the data and adds its own header with its own information (e.g., port used) and passes the data.
3. **Internet layer** – The Internet layer encapsulates the received data and adds its own header (e.g., source and destination IP addresses).
4. **Network Access layer** – The Network Access layer is the only layer that adds both a header and a trailer.
   The data is then sent through a physical network link.

| Frame header | IP header | TCP header | Data | Frame trailer |

Each packet (header + encapsulated data) defined by a particular layer has a specific name:

- **Frame** – Encapsulated data defined by the Network Access layer.
  A Frame can have both a header and a trailer.
- **Packet** – Encapsulated data defined by the network layers.
  A header contains the source and destination IP addresses.
- **Segment** – Encapsulated data as defined by the Transport layer.
  Information such as the source and destination ports or sequence and acknowledgement numbers are included in the header.

## Encapsulation in the OSI model

Just like with the **TCP/IP** layers, each OSI layer encapsulates the higher layer's data between a header (Data Link protocols also add a trailer).

### PDU

While the **TCP/IP model** uses terms like segment, packet and frame to refer to a data packet defined by a particular layer, the **OSI model** uses a different term:
**Protocol Data unit (PDU)**.

A **PDU** represent a unit of data with headers and trailers for the particular layer, as well as the encapsulated data.
**PDU**s are numbered from 1 to 7, since the **OSI model** has 7 layers.
