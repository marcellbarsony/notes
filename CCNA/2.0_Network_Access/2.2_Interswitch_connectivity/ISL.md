## Inter-Switch Link (ISL)

**Inter-Switch Link (ISL)** is a Cisco proprietary encapsulation protocol that maintains VLAN information in Ethernet frames as traffic flows between switches and routers.
**ISL** functions at the data-link layer (Layer 2) of the OSI model.

With **ISL**, an Ethernet frame is encapsulated with a header that transports VLAN IDs between switches and routers.
With **IEEE 802.1Q** the tag is internal, which is a great advantage as tagged frames can be sent over standard Ethernet links.

**ISL** does add overhead to the frame as a 26-byte header containing a 10-bit VLAN ID.
In addition, a 4-byte CRC is appended to the end of each time.

A VLAN ID is added only if the frame is forwarded out a port configured as a trunk link.
If the frame is to be forwarded out a port configured as an access link, the ISL encapsulation is removed.

The size of an Ethernet encapsulated **ISL frame** can be expected to start from 94 bytes and increase up to 1548 bytes because of the overhead (additional fields) the protocol creates via encapsulation.
**ISL** adds a 26-byte header (containing a 15-bit VLAN identifier) and a 4-byte CRC trailer to the frame.

Original frame:

| Destination MAC | Source MAC | Length/Type | Data | FCS |

ISL frame:

| **ISL Header** | Destination MAC | Source MAC | Length/Type | Data | FCS | **ISL FCS** |

[Wikipedia - ISL](https://en.wikipedia.org/wiki/Cisco_Inter-Switch_Link)
