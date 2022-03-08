# Routed vs. Routing protocols

| Routed protocol | Routing protocol       |
| --------------- | ---------------------- |
| IP              | RIP, IGRP, OSPF, EIGRP |
| IPX             | RIP, NLSP, EIGRP       |
| Appletalk       | RMTP, AURP, EIGRP      |

### Routed Protocol

A **Routed Protocol** is a network protocol that is used to send the user data from one network to another network.<br>
**Routed Protocol** carries user traffic such as e-mails, file transfers, web traffic etc.

**Routed Protocols** use an addressing system (e.g IPv4, IPv6) which can address a particular network (Network part) and a host inside that network (Host part).

**Routed Protocols** are routed by **Routing Protocols** to gather routing information for networks.

### Routing protocol

**Routing Protocols** are used between routers (and Layer 3 devices) to dynamically advertise and learn routing information across the network, and store the information into a **Routing Table**.
**Routing Protocols** running in different routers exchange updates between each other do determine the most efficient route using routing algorithms.
