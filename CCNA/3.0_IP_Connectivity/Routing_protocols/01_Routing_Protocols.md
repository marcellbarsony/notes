# Main Routing Protocols

## Five types of routes

| Route               | Description                                                                                                                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **host route**      | Defines a gateway that can forward packets to a specific host on another network                                                                                                                                  |
| **network route**   | Defines a gateway that can forward packets to any of the hosts on a specific network                                                                                                                              |
| **default route**   | Defines a gateway to use when a host or network route to a destination is not otherwise defined                                                                                                                   |
| **loopback route**  | Default route for all packets sent to local network addresses. The loopback route IP is always 127.0.0.1.                                                                                                         |
| **broadcast route** | Default route for all broadcast packets. Two broadcast routes are automatically assigned to each subnet on which the network has an IP (one to the subnet address and one to the broadcast address of the subnet) |

[[IBM - TCP/IP Routing](https://www.ibm.com/docs/en/aix/7.1?topic=protocol-tcpip-routing)]
