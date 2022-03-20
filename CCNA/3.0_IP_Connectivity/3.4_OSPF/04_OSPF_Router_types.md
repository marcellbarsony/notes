# Router Types

The router type is an attribute of an OSPF process.
A given physical router may have one or more OSPF processes.
For example, a router that is connected to more than one area, and which receives routes from a BGP process connected to another AS, is both an area border router and an autonomous system boundary router.

Each router has an identifier, customarily written in the dotted-decimal format (e.g., 1.2.3.4) of an IP address.
This identifier must be established in every OSPF instance. If not explicitly configured, the highest logical IP address will be duplicated as the router identifier.
However, since the router identifier is not an IP address, it does not have to be a part of any routable subnet in the network, and often isn't to avoid confusion.

**OSPF** defines the following overlapping categories of routers

## Internal Router (IR)

An **Internal Router** has all its interfaces belonging to the same area.

## Area Border Router (ABR)

An **Area Border Router** is a router that connects one or more areas to the main backbone network.
It is considered a member of all areas it is connected to.
An **Area Border Router** keeps multiple instances of the link-state database in memory, one for each area to which that router is connected.

## Backbone Router (BR)

A **Backbone Router** has an interface to the backbone area.
**Backbone Routers** may also be area routers, but do not have to be.

## Autonomous System Boundary Router (ASBR)

An **Autonomous System Boundary Router** is a router that is connected by using more than one routing protocol and that exchanges routing information with routers autonomous systems.
**ASBR**s typically also run an exterior routing protocol (e.g. BGP), or use static router, or both.
An **ASBR** is used to distribute routes received from other, external ASs throughout its own AS.
An **ASBR** creates External LSAs for external addresses and floods them to all areas via ABR.
Routers in other areas use ABRs as next hops to access external addresses.
Then ABRs forward packets to the **ASBR** that announces the external addresses.
