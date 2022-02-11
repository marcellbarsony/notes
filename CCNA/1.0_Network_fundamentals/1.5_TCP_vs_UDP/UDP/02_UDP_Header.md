## UDP Header

The **UDP header** is 8 bytes long and consists of the following fields:

| Source port (16 bits) | Destination port (16 bits) |
| --------------------- | -------------------------- |
| Length (16 bits)      | Checksum (16 bits)         |

- **Source port** – The port number of the application on the host sending the data
- **Destination port** – The port number of the application on the host receiving the data
- **Length** – The length of the UDP header and data
- **Checksum** - Checksum of both the UDP header and the UDP data fields
