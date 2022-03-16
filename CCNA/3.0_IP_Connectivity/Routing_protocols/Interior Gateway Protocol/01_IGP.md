# Interior Gateway Protocols (IGP)

**Interior Gateway Protocol** is a routing protocol used to exchange routing table information **between gateways** (routers) **within** an autonomous system.

**Interior Gateway Protocols** can be divided int two categories: [distance-vector routing protocols](https://en.wikipedia.org/wiki/Distance-vector_routing_protocol) and [link-state routing protocols](https://en.wikipedia.org/wiki/Link-state_routing_protocol).

### IGP Protocols

- **OSPF** — The Open Shortest Path First protocol is commonly used by network routers to dynamically identify the fastest and shortest available routes for sending packets to their destination.

- **RIP** — The Routing Information Protocol uses "hop count" to find the shortest path from one network to another.
  Hop count is number of routers a packet must pass through on the way.

- **EIGRP** —

- **IS-IS** —

[[Wikipedia - IGP](https://en.wikipedia.org/wiki/Interior_gateway_protocol)]

The following table lists the differences between the three most popular interior routing protocols:

| Feature                            | RIP                                            | EIGRP               | OSPF            |
| ---------------------------------- | ---------------------------------------------- | ------------------- | --------------- |
| **Type**                           | Distance vector                                | Hybrid              | Distance vector |
| **Metric**                         | Hop count                                      | Bandwidth and delay | Cost            |
| **Speed of convergence**           | Slow                                           | Fast                | Fast            |
| **Routing**                        | Classful (RIPv1), Classless(RIPv2)             | Classless           | Classless       |
| **Updates**                        | Periodical broadcast (RIPv1), Multicast(RIPv2) | Multicast           | Multicast       |
| **Manual summarization**           | No (RIPv1), Yes (RIPv2)                        | Yes                 | Yes             |
| **Supported on non-Cisco routers** | Yes                                            | No                  | Yes             |
| **Configuration complexity**       | Easy                                           | Medium              | Hard            |

[[Study CCNA - Comparing internal routing protocols (IGPs)](https://study-ccna.com/comparing-internal-routing-protocols-igps/)]
