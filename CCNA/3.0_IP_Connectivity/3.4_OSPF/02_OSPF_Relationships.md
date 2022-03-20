# OSPF Relationships

**OSPF** establishes and maintains neighbor relationships for exchanging routing updates with other routers.
The neighbor relationship table is called **Adjacent Database**.
Two **OSPF** routers are neighbors if they are members of the same subnet and share the same Area ID, Subnet mask, Timers and Authentication.
**OSPF** routers do not exchange any routing information - they are only exchanging HELLO packets.

**OSPF Adjacencies** are formed between selected neighbors and this allow them to exchange routing information.
Two routers must be neighbors first, and only then they can become adjacent.
Two routers become adjacent if at least one of them is designated router (or backup designated router - on multiaccess-type networks), or they are interconnected by a point-to-point network type.

### OSPF Operation modes

**OSPF** can have different operation modes on the following setups on an interface/network:

- **Broadcast** (default) — Each router advertises itself by periodically multicasting hello packets, and the use of designated routers.
- **Non-broadcast multi-access** — with the use of designated routers.
  May need static configuration.
  Packets are sent as unicast.
- **Point-to-multipoint**, where OSPF treats neighbors as point-to-point links.
  No designated router is elected.
  Using multicast.
  Separate hello packets are sent to each neighbor.
- **Point-to-point** — Each router advertises itself by periodically multicasting hello packets.
  No designated router is elected.
  The interface can be IP unnumbered (without assigning a unique IP address to it).
- **Virtual links** — The packets are sent as unicast.
  Can only be configured on a non-backbone area (but not stub-area).
  Endpoints need to be ABR, the virtual links behave as unnumbered point-to-point connections.
  The cost of an intra-area path between the two routers is added to the link.
- **Virtual link over Generic Routing Encapsulation (GRE)** — Since OSPF does not support virtual links for other areas then the backbone.
  A workaround is to use GRE over backbone area.
  Note if the same IP or router ID is used the link creates two equal-cost routes to the destination.
- **Sham link** — A link that connects sites that belong to the same OSPF area and share an OSPF backdoor link via MPLS VPN backbone.

### OSPF Adjacency states

Each **OSPF** router within a network communicates with other neighboring routers on each connecting interface to establish the states of all adjacencies.
Before establishing a neighbor relationship, **OSPF** routers need to go through several state changes.

1. **Down** - The initial state of a conversation when no information has been exchanged and retained between routers with the HELLO Protocol.
2. **Attempt** - Similar to **Down** state, except that a router is in the process of efforts to establish a conversation with another router.
3. **Init state** – A router has received a HELLO message from the other OSFP router.
4. **2-way state** – Established bidirectional communication: this state precedes the establishment of adjacency - this is the lowest state of a router that may be considered as a Designated Router.
5. **Exstart state** – First step of adjacency of two routers: beginning of the LSDB exchange.
6. **Exchange state** – Routers are able to change OSPF routing protocol packets: DBD (Database Descriptor) packets are exchanged.
   Routers will use this information (LSA headers) to see what LSAs need to be exchanged.
7. **Loading state** – One neighbor sends LSRs (Link State Requests) for every network it doesn’t know about.
   The other neighbor replies with the LSUs (Link State Updates) which contain information about requested networks.
   After all the requested information have been received, other neighbor goes through the same process
8. **Full state** – Both routers have the synchronized database and are fully adjacent with each other.
