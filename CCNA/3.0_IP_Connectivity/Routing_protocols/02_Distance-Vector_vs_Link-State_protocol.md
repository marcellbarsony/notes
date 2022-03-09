# Distance Vector vs. Link State Protocol

| Properties                     | Distance Vector Routing                                             | Link State Routing                                    |
| ------------------------------ | ------------------------------------------------------------------- | ----------------------------------------------------- |
| **Bandwidth requirement**      | Less - Local sharing, Small packets, No flooding                    | More - Flooding, Large link state packets             |
| **Knowledge**                  | Local Knowledge - Updates table based on information from neighbors | Global Knowledge - Has knowledge about entire network |
| **Algorithm**                  | Bellman-Ford                                                        | Dijkstra's                                            |
| **Traffic**                    | Less traffic                                                        | More traffic                                          |
| **Convergence**                | Converges slowly - Good news spread fast, Bad news spread slowly    | Converges faster                                      |
| **Count to Infinity problem**  | Yes                                                                 | No                                                    |
| **Persistent looping problem** | Yes                                                                 | No, Transient Loops only                              |
| **Practical implementation**   | RIP and GRIP                                                        | OSPF and IS-IS                                        |

[[GeeksforGeeks - Difference between Distance vector routing and Link State routing](https://www.geeksforgeeks.org/difference-between-distance-vector-routing-and-link-state-routing/)]

## Distance-Vector Protocol

A **Distance-Vector Routing Protocol** in data network determines the best route for data packets based on distance.<br>
**Distance-Vector Routing Protocol** measure the distance by the number of routers a packet has to pass.
Some **Distance-Vector Routing Protocols** take into account network latency and other factors that influence traffic on a given route.

The term **Distance Vector** refers to the fact that the protocol manipulates vectors (arrays) of distances to other nodes in the network.

**Distance-Vector Routing Protocols** use the [Bellman-Ford algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) to calculate the best route.
Another way of calculating the best route across a network is based on link cost.

[[Wikipedia - Distance-vector routing protocol](https://en.wikipedia.org/wiki/Distance-vector_routing_protocol)]

### Distance-Vector Algorithm

1. A router transmits its distance vector to each of its neighbors in a routing packet.
2. Each router receives and saves the most recently received distance vector from each of its neighbors.
3. A router recalculates its distance vector when:
   - It receives a distance vector from a neighbor containing different information than before.
   - It discovers that a link to a neighbor has gone down.

[[GeeksforGeeks - Distance Vector Routing (DVR) Protocol](https://www.geeksforgeeks.org/distance-vector-routing-dvr-protocol/)]

### Bellman-Ford Algorithm Basics

The [Bellman–Ford algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph.
It is slower than Dijkstra's algorithm for the same problem, but more versatile, as it is capable of handling graphs in which some of the edge weights are negative numbers.

Each router maintains a **Distance Vector table** containing the distance between itself and all possible destination nodes.
Distances, based on a chosen metric, are computed using information from the neighbors’ distance vectors.

```
Information kept by DV router -
  - Each router has an ID
  - Associated with each link connected to a router,
    there is a link cost (static or dynamic).
  - Intermediate hops

Distance Vector Table Initialization -
  - Distance to itself = 0
  - Distance to ALL other routers = infinity number.
```

## Link-State Protocol

The basic concept of **Link-State Routing Protocol** is that every node constructs a map of the connectivity to the network, in the form of a graph, showing which nodes are connected to which other nodes.<br>
Each node then independently calculates the next best logical path from it to every possible destination in the network.
Each collection of best paths will then form each node's routing table.

In a **Link-State Protocol** the only information passed between nodes is connectivity related.
**Link-State algorithms** are sometimes characterized informally as each router "telling the world about its neighbors".

[[Wikipedia - Link-State Protocol](https://en.wikipedia.org/wiki/Link-state_routing_protocol)]
