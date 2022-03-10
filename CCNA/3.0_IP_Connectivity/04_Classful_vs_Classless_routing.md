# Classful vs. Classless Routing

| Properties                    | Classful Routing                                           | Classless Routing                                  |
| ----------------------------- | ---------------------------------------------------------- | -------------------------------------------------- |
| **VLSM Support**              | VLSM is not supported                                      | VLSM is supported                                  |
| **Subnet Mask Import**        | Does not import subnet mask                                | Imports subnet mask                                |
| **Subnet Mask Advertisement** | Does not advertise subnet mask                             | Do advertise subnet mask                           |
| **Subnet Display**            | Subnets are not displayed in other major subnet            | Subnets are displayed in other major subnet        |
| **CIDR Support**              | CIDR is not supported                                      | CIDR is supported                                  |
| **Address Dividing**          | Address is divided into three parts: Network, Subnet, Host | Address is divided into two parts: Subnet and Host |
| **Bandwidth**                 | Requires more bandwidth                                    | Requires less bandwidth                            |
| **HELLO Messages**            | HELLO messages are not used                                | HELLO messages are used                            |
| **Updates**                   | Regular or periodic updates are used                       | Change-triggered updates are used                  |
| **Fault Detection**           | Fault can be detected easily                               | Fault detection harder                             |

[[GeeksforGeeks](https://www.geeksforgeeks.org/difference-between-classful-routing-and-classless-routing/)]

## Classful Routing

- Classful Routing does not import subnet mask.
- Subnet mask is provided after the route update.
- Subnet mask is same throughout, does not vary for all devices.
- [VLSM(Variable Length Subnet Mask)](https://www.geeksforgeeks.org/introduction-of-variable-length-subnet-mask-vlsm/) is not supported.
- CIDR is not supported.

## Classless Routing

Classless Routing imports subnet mask and in this, triggered updates are used.

- Classless Routing does import subnet mask.
- HELLO messages are used for checking status.
- Subnet mask is not same throughout, it may vary for all devices.
- VLSM is supported.
- CIDR is supported.

### Classless Routing Protocols

- OSPF
- EIGRP - act as classful routing protocol (automatically summarize)
- RIP v2
- IS-IS
