# Static vs. Dynamic Routing

In TCP/IP, routing can be one of two types: **Static** or **Dynamic**.

[[IBM - Static and Dynamic routing](https://www.ibm.com/docs/nl/aix/7.1?topic=routing-static-dynamic)]

### Static Routing

With **Static Routing** (non-adaptive routing), the routing table is being maintained manually by the network administrator with the `route` command.<br>
**Static Routing** does not use complex routing algorithms nd it provides more security than dynamic routing.

### Dynamic Routing

With **Dynamic Routing**, daemons update the routing table automatically using complex algorithms.<br>
Routing daemons continuously receive information broadcast by other routing daemons, and so continuously update the routing table.

### Static vs. Dynamic Comparison

| Properties               | Static Routing                                        | Dynamic Routing                                   |
| ------------------------ | ----------------------------------------------------- | ------------------------------------------------- |
| **Route updates**        | Routes are user defined                               | Routes are updated according to topology          |
| **Algorithm**            | Does not use complex routing algorithms               | Uses complex routing algorithms                   |
| **Security**             | Provides high or more security                        | Provides less security                            |
| **Scaling**              | Does not scale                                        | Does scale                                        |
| **Automation**           | Static routing is manual                              | Routing is automated                              |
| **Implementation**       | Implemented in small networks                         | Implemented in large networks                     |
| **Resources (Overhead)** | Additional resources are not required (less Overhead) | Additional resources are required (more Overhead) |
| **Failure**              | Failure of link disrupts the rerouting                | Failure of link does not interrupt the rerouting  |

[[GeeksforGeeks - Difference between Static and Dynamic Routing](https://www.geeksforgeeks.org/difference-between-static-and-dynamic-routing/)]

## Routing Daemons

TCP/IP provides two daemons for use in dynamic routing: **routed** and **gated** daemons.

**Gated daemons** support the following routing protocols simultaneously:

- **RIP** — Routing Information Protocol
- **RIPng** — Routing Information Protocol Next Generation
- **EGP** — Exterior Gateway Protocol
- **BGP** and **BGP4+** — Border Gateway Protocol and BGP4+
- **HELLO** — Defense Communications Network Local-Network Protocol
- **OSPF** — Open Shortest Path First
- **IS-IS** — Intermediate System to Intermediate System
- **ICMP** and **ICMPv6** — Internet Control Message Protocol/Router Discovery

**Routed daemon** only supports **RIP** (Routing Information protocol).

### Daemon modes

Routing daemons can operating in one of two modes, **passive** or **active**, depending upon the options used when starting the daemons.

- **Active mode** — Routing daemons both broadcast routing information periodically about their local network to gateways and hosts, and receive routing information from hosts and gateways.
- **Passive mode** — Routing daemons receive routing information from hosts and gateways, but do not attempt to keep remote gateways updated
  (they do not advertise their own routing information).

These two types of routing can be used not only for gateways, but for other hosts on a network as well.
Static routing works the same for gateways as for other hosts.
Dynamic routing daemons, however, must be run in the passive (quiet) mode when run on a host that is not a gateway.
