## Notes

- Static vs. Dynamic protocols
- Distance vector protocols
- Link state protocols

## Abbreviations

- **IGP** – Interior Gateway Protocol
- **EGP** – Exterior Gateway Protocol
- **RIP** – Routing Information Protocol
- **IGRP** – Interior Gateway Routing Protocol
- **OSPF** – Open Shortest Path First
- **ISIS** – Intermediate System to Intermediate System
- **EIGRP** – Enhanced Interior Gateway Routing Protocol
- **BGP** – Border Gateway Protocol

## IBM - notes

Static and dynamic routing
In TCP/IP, routing can be one of two types: static or dynamic.

TCP/IP routing gateways
Gateways are a type of router. Routers connect two or more networks and provide the routing function. Some routers, for example, route at the network interface level or at the physical level. Gateways, however, route at the network level.

Gateway considerations
Take these actions before configuring your gateway.

Configuring a gateway
To configure a machine to act as a gateway, use these instructions.

Route use restrictions
Routes can be restricted so they can be used only by some users. The restrictions are based on the primary group IDs of users.

Dead gateway detection
A host can be configured to detect whether a gateway it is using is down, and can adjust its routing table accordingly.

Route cloning
Route cloning allows a host route to be created for every host that a system communicates with.

Dynamic route removal
If you are using the routed daemon, a manually deleted route is not replaced by incoming RIP information (because ioctl's are used).

Configuring the routed daemon
Follow these steps to configure the routed daemon.

Configuring the gated daemon
When configuring the gated daemon, you must decide which gateway protocols are most appropriate for your system.

Autonomous system numbers
If you use EGP or BGP, you should obtain an official autonomous system number for your gateway.

[[IBM](https://www.ibm.com/docs/en/aix/7.1?topic=protocol-tcpip-routing)]
