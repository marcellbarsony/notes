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

**Link-State Advertisements (LSAs)** are used by **OSPF** routers to exchange topology information.
Each **LSA** contains routing and topology information to describe a part of an **OSPF** network.
When two neighbors decide to exchange routes, they send each other a list of all **LSA**s in their respective topology database.
Each router then checks its topology database and sends a **Link State Request (LSR)** message requesting all **LSA**s not found in its topology table.
Other router responds with the **Link State Update (LSU)** that contains all **LSA**s requested by the other neighbor.

### Link State Request (LSR)

**Link State Request** messages are used by one router to request updated information about a portion of the LSDB from another router.
The message specifies the link(s) for which the requesting device wants more current information.

### Link State Update (LSU)

**Link State Update** messages contain updated information about the state of certain link on the LSDB.
They are sent in response to a **Link State Request** message, and also broadcast or multicast by routers on a regular basis.
Their contents are used to update the information in the LSDBs of routers that receive them.

### Link state Acknowledgement (LSAck)

**Link State Acknowledgement** messages provide reliability to the link-state exchange process, by explicitly acknowledging receipt of a **Link State Update** message.
