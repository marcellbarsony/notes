# EIGRP - Enhanced Interior Gateway Routing Protocol

**Enhanced Interior Gateway Routing Protocol (EIGRP)** is an advanced dynamic distance-vector routing protocol that is used for automating routing decisions and configuration between any two Layer 3 devices.<br>
**EIGRP** is considered to be an advanced distance vector protocol, although some materials erroneously state that **EIGRP** is a hybrid routing protocol, a combination of distance vector and link state.
**EIGRP** was designed by **Cisco Systems** as a proprietary protocol, available only on Cisco routers.

**EIGRP** is used on a router to share routes with other routers within the same autonomous system.
Unlike other well known routing protocols, such as RIP, **EIGRP** only sends incremental updates, reducing the workload on the router and the amount of data that needs to be transmitted.

[[Wikipedia - EIGRP](https://en.wikipedia.org/wiki/Enhanced_Interior_Gateway_Routing_Protocol)]<br>
[[Cisco - EIGRP](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/16406-eigrp-toc.html)]

## Theory of Operation

Some of the many advantages of **EIGRP** are:

- Very low usage of network resources during normal operation;<br>
  Only hello packets are transmitted on a stable network.

- When a change occurs, only routing table changes are propagated, not the entire routing table;<br>
  This reduces the load the routing protocol itself places on the network.

- Rapid convergence times for changes in the network topology<br>
  (in some situations convergence can be almost instantaneous).

EIGRP is an enhanced distance vector protocol, relying on the Diffused Update Algorithm (DUAL) to calculate the shortest path to a destination within a network.

## Configuration

Example of setting up **EIGRP** for a private network.<br>
The _0.0.15.255_ wildcard indicates a subnetwork with a maximum of 4094 hosts - it is the [bitwise complement](https://en.wikipedia.org/wiki/Bitwise_operation#NOT) of the subnet mask 255.255.240.0.
The `no auto-summary` command prevents automatic [route summarization](https://en.wikipedia.org/wiki/Supernetwork) on classful boundaries, which would otherwise result in routing loops in discontiguous networks.

```
Router# configure terminal
 Router(config)# router eigrp 1
 Router (config-router)# network 10.201.96.0 0.0.15.255
 Router (config-router)# no auto-summary
```

## Administrative Distances

| EIGRP routes    | AD values |
| --------------- | :-------: |
| Summary Routes  |     5     |
| Internal Routes |    90     |
| External routes |    170    |
