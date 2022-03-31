# Open Shortest Path First (OSPF)

**Open Shortest Path First (OSPF)** is a classless routing protocol for IP networks that uses Link State Routing (LSR) algorithm and falls into the group of Interior Gateway Protocols (IGPs), operating withing a single autonomous system (AS).

**OSPF** gathers link state information from available routers and constructs a topology map of the network.
Each **OSPF** router runs SFP algorithm to calculate the best routes and adds those to the routing table.
The topology presented as a routing table to the Internet Layer for routing packets by their destination IP address.

Each **OSPF** router stores routing and topology information in three tables:

- **Neighbor table** - Stores information about **OSPF** neighbors
- **Topology table** - Stores the topology structure of a network
- **Routing table** - Stores the best routes

**OSPF** supports IPv4 and IPv6 networks and supports the CIDR addressing model and VLSM.<br>
**OSPF** uses only one parameter as the metric - the interface cost.<br>
**OSPF** reserves the multicast addresses `224.0.0.5` (IPv4) and `FF02::5` (IPv6) for all SPF/link state routers (AllSPFRouters) and `224.0.0.6` (IPv4) and `FF02::6` (IPv6) for all Designated Routers (AllDRouters).

[[Wikipedia - Open Shortest Path First](https://en.wikipedia.org/wiki/Open_Shortest_Path_First)]

## OSPF Concepts

**OSPF** is an IGP for routing IP packets withing a single routing domain (such as an AS).
**OSPF** gathers link state information from available routers and constructs a topology map of the network.
The topology map is presented as a routing table to the Internet Layer which routes packets based solely on their destination IP address.

**OSPF** detects changes (e.g. link failures) in the topology and converges on a new loop-free routing structure within seconds.
It computes the [shortest-path tree](https://en.wikipedia.org/wiki/Shortest-path_tree) for each route using a method based on Dijkstra's algorithm.
The **OSPF** routing policies for constructing a route table are governed by link metrics associated with each routing interface.
Cost factors may be: the distance of the router (round-trip time), data throughput of a link, or link availability and reliability.

**OSPF** divides the network into routing areas to simplify administration and optimize traffic and resource utilization.
Areas are identified by 32-bit numbers, expressed either simply in decimal, or octet-based dot-decimal notation.
By convention, Area 0, or `0.0.0.0` represents the core or backbone area of an **OSPF** network.

## OSPF vs. EIGRP

| Protocol  | Type of routing          | Metric                           | Manual summarization   | Load balancing                        | Administrative distance | Cisco proprietary | Multicast address    |
| --------- | ------------------------ | -------------------------------- | ---------------------- | ------------------------------------- | ----------------------- | ----------------- | -------------------- |
| **EIGRP** | Advanced distance vector | Composite of bandwidth and delay | On all routers         | Equal and unequal cost load balancing | 90                      | Yes               | 224.0.0.10           |
| **OSPF**  | Link state               | Cost                             | Only on ABRs and ASBRs | Equal cost load balancing             | 110                     | No                | 224.0.0.5, 224.0.0.6 |

[[Study CCNA - Differences between OSPF and EIGRP](https://study-ccna.com/differences-between-ospf-and-eigrp/)]<br>
