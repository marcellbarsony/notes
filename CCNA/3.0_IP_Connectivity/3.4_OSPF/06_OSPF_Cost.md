# OSPF Cost - OSPF Routing Protocol Metric

**OSPF** is a dynamic routing protocol that uses Link Stat Routing (LSR) algorithm.
**OSPF cost** is its metric - the unit used by a router to make routing decisions.

**OSPF** executes a process using an algorithm developed by Edsger Dijkstra to find the shortest route to the advertising node.
The router will then use this output as a candidate path for its routing table.
For the **OSPF** to accurately represent topology, each link of the network myst have an associated **OSPF cost**.

**OSPF** relies on costs that are inversely proportional to the bandwidth of the link.
Therefore, higher bandwidth links are preferred to lower ones.
The Cost formula is reference bandwidth divided by interface bandwidth.
The default reference bandwidth of 100 Mbps us used for **OSPF cost** calculation.

[[Study CCNA - OSPF Cost Metric](https://study-ccna.com/ospf-cost-metric/)]

## OSPF Default Interface Cost Values

Default Cost values for each interface type:

|           Interface type            | Cost |
| :---------------------------------: | ---: |
| Gigabit Ethernet Interface (1 Gbps) |    1 |
| Fast Ethernet Interface (100 Mbps)  |    1 |
|    Ethernet Interface (10 Mbps)     |   10 |
|          DS1 (1.544 Mbps)           |   64 |
|           DSL (768 Kbps)            |  133 |

Cisco routers have trhe methods to change the OSPF interface cost:

1. By directly using the interface command `ip ospf cost <1-65535>`

```
Router#conf t
Router(config)#int gi0/0/0
Router(config-if)#ip ospf cost <1-65535>
```

We can verify this by using the ‘show ip ospf interface’ command.

2. Changing the `interface bandwidth` setting (in kilobits), which changes the calculated value

```
Router#conf t
Router(config)#int gi0/0/0
Router(config-if)#bandwidth <1-10000000>
```

3. Changing the OSPF reference bandwidth setting, which changes the calculated value

```
Router#conf t
Router(config)#router ospf 1
Router(config-router)#auto-cost reference-bandwidth 100000
```

> Note<br>
> Ensure reference bandwidth is the same across all routers.
> The reference bandwidth command warns you that you need to make the same change across all your routers.
> This will allow all routers to make their calculations on the same information
