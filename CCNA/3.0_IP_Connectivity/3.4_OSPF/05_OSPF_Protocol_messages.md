# Protocol Messages - Link State packets

Unlike other routing protocols **OSPF** does not carry data via transport protocol (such as UDP or TCP).
Instead, **OSPF** forms IP datagrams directly, packaging them using protocol number 89 for the IP protocol field.

**OSPF** defines five different message types, for various types of communication.

- Hello
- Database description
- Link State Request
- Link State Update
- Link State Acknowledgement

## Link State Packets

### LSA - LSU - LSR

**Link-State Advertisements (LSAs)** are used by **OSPF** routers to exchange topology information.
Each **LSA** contains routing and topology information to describe a part of an **OSPF** network.
When two neighbors decide to exchange routes, they send each other a list of all **LSA**s in their respective topology database.
Each router then checks its topology database and sends a **Link State Request (LSR)** message requesting all **LSA**s not found in its topology table.
Other router responds with the **Link State Update (LSU)** that contains all **LSA**s requested by the other neighbor.
